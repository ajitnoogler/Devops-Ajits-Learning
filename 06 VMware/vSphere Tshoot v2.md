# VMware vSphere Troubleshooting Runbook - Scenario Based with Sample Logs

## Table of Contents

1. [Introduction](#introduction)
2. [ESXi and vCenter Log Files Overview](#log-files-overview)
3. [Scenario 1: VM Snapshot Issues](#scenario-1-snapshot-issues)
4. [Scenario 2: ESXi Host Not Responding/Disconnected](#scenario-2-host-disconnected)
5. [Scenario 3: vSphere HA Failures](#scenario-3-ha-failures)
6. [Scenario 4: DRS Not Working](#scenario-4-drs-not-working)
7. [Scenario 5: vMotion Failures](#scenario-5-vmotion-failures)
8. [General Troubleshooting Workflow](#general-troubleshooting)
9. [Critical Commands Reference](#critical-commands)
10. [Additional Resources](#additional-resources)

---

## Introduction

This runbook provides scenario-based troubleshooting guidance for VMware vSphere environments, including sample log excerpts, step-by-step resolution procedures, and references to official VMware/Broadcom KB articles.

---

## ESXi and vCenter Log Files Overview

### ESXi Host Log Files (`/var/log/`)

| Log File | Purpose | What to Check |
|----------|---------|---------------|
| vmkernel.log | Core VMkernel operations, storage, networking | I/O errors, storage disconnects, network timeouts, device failures |
| hostd.log | Host management service, VM operations | API errors, VM operation failures, connection issues |
| vpxa.log | vCenter agent communication | vCenter connectivity failures, agent errors |
| fdm.log | HA operations, master/slave elections | Heartbeat losses, master election failures, isolation events |
| shell.log | ESXi Shell command execution | Failed commands, unauthorized access |
| syslog.log | System messages, hardware events | Hardware faults, kernel panics |
| vobd.log | Hardware health monitoring | Device failures, hardware errors |

### VM Log Files (`/vmfs/volumes/<datastore>/<VM_name>/`)

| File | What to Check |
|------|---------------|
| vmware.log | VM startup/shutdown errors, runtime issues |
| *.vmsd | Snapshot chain errors, metadata corruption |
| *.vmdk | Disk descriptor errors, corruption |

### vCenter Server Log Files (`/var/log/vmware/`)

| Log File | Purpose | What to Check |
|----------|---------|---------------|
| vpxd.log | vCenter core operations | Database errors, task failures, host connectivity |
| vws.log | vSphere Client activities | Web client errors, login failures |
| eam.log | ESX Agent Manager | Agent deployment failures |

---

## Scenario 1: VM Snapshot Issues

### Symptoms
- VM performance degraded
- "Virtual machine snapshot consolidation needed" warning
- Unable to delete snapshots
- Snapshot commit failures

### Sample Log Excerpts

**From `/var/log/hostd.log`:**
```
2025-11-20T15:12:34.567Z info hostd[123456] [Originator@6876 sub=Vimsvc.ha-eventmgr] Event 2345 : Snapshot consolidation required for VM TestVM-01
2025-11-20T15:13:20.123Z error hostd[123456] [Originator@6876 sub=Snapsvc] Failed to commit snapshot for VM moref=vm-101: Timeout waiting for operation
```

**From `/var/log/vmkernel.log`:**
```
2025-11-20T15:13:20.456Z cpu12:2097234)WARNING: Snapsvc: 1234: Snapshot removal failed due to I/O timeout on datastore ds-prod-01
2025-11-20T15:13:21.789Z cpu12:2097234)ScsiDeviceIO: 2345: Command 0x28 to device "naa.600605b00..." failed H:0x0 D:0x2 P:0x0 Possible sense data: 0x0 0x0 0x0
```

**From VM log `/vmfs/volumes/datastore1/TestVM-01/vmware.log`:**
```
2025-11-20T15:12:30.123Z vcpu-0| Checkpoint_Unstun: vm stopped for 12345678 us
2025-11-20T15:13:15.456Z vcpu-0| SNAPSHOT: SnapshotVMXTakeSnapshotWork: Failed to create snapshot: The file is too big (19)
```

### Troubleshooting Steps

**Step 1: Identify Snapshot Chain**
```bash
# List all VMs and find VMID
vim-cmd vmsvc/getallvms | grep "TestVM-01"

# Check snapshot status
vim-cmd vmsvc/get.snapshot <VMID>
```

**Step 2: Check Snapshot Files**
```bash
# Navigate to VM directory
cd /vmfs/volumes/<datastore>/TestVM-01/

# List all snapshot files
ls -lh *-0000*.vmdk *delta.vmdk *.vmsd *.vmsn

# Check snapshot sizes
du -sh *-0000*.vmdk
```

**Sample Output:**
```
-rw-------  1 root root  45G Nov 20 15:00 TestVM-01-000001.vmdk
-rw-------  1 root root  23G Nov 20 15:10 TestVM-01-000002.vmdk
-rw-------  1 root root 520 Nov 20 15:00 TestVM-01-000001-delta.vmdk
```

**Step 3: Check Datastore Space**
```bash
# Check datastore capacity
df -h | grep datastore1

# Detailed VMFS info
vmkfstools -P /vmfs/volumes/datastore1/
```

**Step 4: Analyze Logs for Errors**
```bash
# Check for snapshot-related errors
grep -i "snapshot" /var/log/hostd.log | tail -50
grep -i "snapshot" /var/log/vmkernel.log | tail -50

# Look for I/O errors
grep -i -E "I/O error|timeout|fail" /var/log/vmkernel.log | grep -i snapshot
```

**Step 5: Verify Snapshot Chain Integrity**
```bash
# Check parent-child relationship in VMDK descriptors
cat TestVM-01.vmdk | grep -i parent
cat TestVM-01-000001.vmdk | grep -i parent
cat TestVM-01-000002.vmdk | grep -i parent

# Verify CID (Content ID) chain
cat TestVM-01.vmdk | grep CID
cat TestVM-01-000001.vmdk | grep CID
```

**Expected Output (Healthy Chain):**
```
# Base disk
CID=abc12345
parentCID=ffffffff

# First snapshot
CID=def67890
parentCID=abc12345

# Second snapshot
CID=ghi11223
parentCID=def67890
```

**Step 6: Remove Snapshots**

**Option A: Via vSphere Client** (Recommended)
1. Right-click VM → Snapshots → Consolidate
2. Monitor task progress in Recent Tasks

**Option B: Via Command Line**
```bash
# Remove all snapshots
vim-cmd vmsvc/snapshot.removeall <VMID>

# Remove specific snapshot
vim-cmd vmsvc/snapshot.remove <VMID> <snapshot_id>
```

**Step 7: Manual Consolidation (If Automatic Fails)**
```bash
# Power off VM
vim-cmd vmsvc/power.off <VMID>

# Clone the last delta disk to consolidated disk
vmkfstools -i TestVM-01-000002.vmdk TestVM-01-consolidated.vmdk

# Edit VMX file to point to consolidated disk
vi TestVM-01.vmx
# Change: scsi0:0.fileName = "TestVM-01-000002.vmdk"
# To:     scsi0:0.fileName = "TestVM-01-consolidated.vmdk"

# Reload VM configuration
vim-cmd vmsvc/reload <VMID>

# Power on VM
vim-cmd vmsvc/power.on <VMID>

# Clean up old snapshot files after verification
rm -f *-0000*.vmdk *-delta.vmdk *.vmsd
```

### Related KB Articles
- **KB 316392**: Troubleshooting issues when creating or committing snapshots
- **KB 1015180**: Understanding virtual machine snapshots in VMware ESX
- **KB 1025279**: Best practices for virtual machine snapshots
- **KB 1038963**: Troubleshooting snapshot consolidation issues

### Prevention Best Practices
- Limit snapshot chain depth to 3-4 snapshots maximum
- Do not keep snapshots for more than 72 hours
- Monitor snapshot size - alert when exceeds 25% of base disk
- Always consolidate snapshots after backup operations
- Create vCenter alarms for snapshot age and size

---

## Scenario 2: ESXi Host Not Responding/Disconnected

### Symptoms
- Host shown as "Not Responding" or "Disconnected" in vCenter
- Unable to manage VMs on host
- VMs still running but not manageable from vCenter
- Timeout errors when connecting to host

### Sample Log Excerpts

**From vCenter `/var/log/vmware/vpxd/vpxd.log`:**
```
2025-11-20T16:45:10.123Z info vpxd[45678] [Originator@6876 sub=vpxdMoHost opID=HB-host-123] [HostMo] host connection state changed to [DISCONNECTED] for host-123
2025-11-20T16:46:12.456Z error vpxd[45678] [Originator@6876 sub=vpxdInvtHostCnx opID=HB-host-123@1234] [VpxdInvtHostSyncHostLRO] FixNotRespondingHost failed for host host-123, marking host as notResponding
2025-11-20T16:46:13.789Z info vpxd[45678] [Originator@6876 sub=HostCnx opID=CheckforMissingHeartbeats] [VpxdHostCnx] No heartbeats received from host; time since last heartbeat: 67453ms
2025-11-20T16:46:15.012Z info vpxd[45678] [Originator@6876 sub=HostCnx opID=CheckforMissingHeartbeats] Marking the connection alive to false: 528b7944-####-####-####-14cf56852fd2
```

**From ESXi `/var/log/hostd.log`:**
```
2025-11-20T16:45:05.123Z error hostd[67890] [Originator@6876 sub=Hostsvc.VMotionSystem] Lost connection to vCenter Server
2025-11-20T16:45:06.456Z warning hostd[67890] [Originator@6876 sub=Vimsvc] Connection to vCenter terminated unexpectedly
```

**From ESXi `/var/log/vmkernel.log`:**
```
2025-11-20T16:44:58.789Z cpu5:67234)WARNING: Heartbeat: 1234: Lost network connection to vCenter Server at 192.168.1.10
2025-11-20T16:45:10.123Z cpu5:67234)WARNING: Net: 2345: Network timeout detected on vmk0
```

### Troubleshooting Steps

**Step 1: Verify Basic Connectivity**
```bash
# From vCenter or management workstation
ping esxi-host01.domain.com
ping 192.168.1.20

# Test SSH connectivity
ssh root@esxi-host01.domain.com

# From ESXi host, test connectivity to vCenter
ping vcenter.domain.com
vmkping -I vmk0 vcenter.domain.com
```

**Step 2: Check ESXi Management Agent Status**
```bash
# SSH to ESXi host
ssh root@esxi-host01.domain.com

# Check hostd status
/etc/init.d/hostd status

# Check vpxa status (vCenter agent)
/etc/init.d/vpxa status

# View processes
ps -c | grep -E "hostd|vpxa"
```

**Sample Output (Problem):**
```
# /etc/init.d/hostd status
hostd is not running
```

**Step 3: Review ESXi Logs**
```bash
# Check for recent errors in hostd.log
tail -100 /var/log/hostd.log | grep -i error

# Check vmkernel for network issues
grep -i -E "network|timeout|disconnect" /var/log/vmkernel.log | tail -50

# Check vpxa agent logs
tail -100 /var/log/vpxa.log | grep -i error
```

**Step 4: Check DNS Resolution**
```bash
# From ESXi host
nslookup vcenter.domain.com

# Check /etc/hosts file
cat /etc/hosts

# Verify DNS servers
cat /etc/resolv.conf
```

**Step 5: Restart Management Agents**
```bash
# Restart hostd
/etc/init.d/hostd restart

# Restart vpxa (vCenter agent)
/etc/init.d/vpxa restart

# Or restart all services
services.sh restart

# Verify services are running
/etc/init.d/hostd status
/etc/init.d/vpxa status
```

**Expected Output (Healthy):**
```
# /etc/init.d/hostd restart
watchdog-hostd: Terminating watchdog process with PID 67890
hostd stopped.
hostd started.

# /etc/init.d/hostd status
hostd is running
```

**Step 6: Check Network Configuration**
```bash
# List VMkernel interfaces
esxcli network ip interface list

# Check IP configuration
esxcli network ip interface ipv4 get

# Verify default gateway
esxcli network ip route ipv4 list

# Check firewall rules
esxcli network firewall ruleset list | grep -i hostd
```

**Step 7: Verify SSL Certificates**
```bash
# Check certificate validity
openssl x509 -in /etc/vmware/ssl/rui.crt -text -noout | grep -A2 Validity

# Check certificate fingerprint
openssl x509 -in /etc/vmware/ssl/rui.crt -fingerprint -sha1 -noout

# Verify castore.pem integrity
cat /etc/vmware/ssl/castore.pem
```

**Step 8: Reconnect Host from vCenter**

**Via vSphere Client:**
1. Navigate to host in inventory
2. Right-click → Connection → Disconnect (if not already)
3. Right-click → Connection → Connect
4. Monitor Recent Tasks for connection status

**Via PowerCLI:**
```powershell
# Connect to vCenter
Connect-VIServer -Server vcenter.domain.com

# Disconnect host
Get-VMHost -Name "esxi-host01.domain.com" | Disconnect-VMHost -Confirm:$false

# Reconnect host
Get-VMHost -Name "esxi-host01.domain.com" | Connect-VMHost
```

**Step 9: Check for Resource Exhaustion**
```bash
# Check memory usage
esxcli system stats memory get

# Check hostd heap usage
cat /var/log/hostd.log | grep -i "out of memory"

# Verify sufficient storage space
df -h
vdf -h
```

### Related KB Articles
- **KB 344682**: Troubleshooting an ESXi host in a "not responding" or "disconnected" state
- **KB 318647**: ESXi host disconnects intermittently from vCenter Server
- **KB 303652**: Changing an ESXi host's connection status in vCenter Server
- **KB 404722**: ESXi host gets disconnected from vCenter server at random times
- **KB 367381**: ESXi Host Disconnected from vCenter and hostd Fails to Start

### Key Points to Remember
- Distinguish between "Not Responding" and "Disconnected" states
- "Not Responding" = vCenter cannot communicate with host but host is operational
- "Disconnected" = Intentional disconnect or severe communication failure
- Check UDP port 902 (heartbeat) and TCP port 443 (management) connectivity
- Review network firewalls and security appliances

---

## Scenario 3: vSphere HA Failures

### Symptoms
- VMs not restarting after host failure
- HA cluster shows "Configuration Issues"
- "HA agent cannot be installed or configured" error
- False host isolation alarms
- Master election failures

### Sample Log Excerpts

**From ESXi `/var/log/fdm.log` (Master):**
```
2025-11-20T17:00:34.123Z [FDM] info  [LocalNode] Node changed to Master
2025-11-20T17:01:05.456Z [FDM] warning [Election] Master election initiated due to host isolation detected
2025-11-20T17:01:10.789Z [FDM] info [Heartbeat] Network heartbeat lost to host esxi-02.domain.com (192.168.1.21)
2025-11-20T17:01:15.012Z [FDM] info [Heartbeat] Datastore heartbeat detected from host esxi-02.domain.com on ds:///vmfs/volumes/5a2b1234/
```

**From ESXi `/var/log/fdm.log` (Slave):**
```
2025-11-20T17:00:45.123Z [FDM] info [LocalNode] Master elected: 192.168.1.20 (esxi-01.domain.com)
2025-11-20T17:01:05.456Z [FDM] warning [Heartbeat] Failed to send network heartbeat to master
2025-11-20T17:01:10.789Z [FDM] error [Election] Cannot communicate with master, initiating election
```

**From vCenter `/var/log/vmware/vpxd/vpxd.log`:**
```
2025-11-20T17:02:01.123Z info vpxd[12345] [Originator@6876 sub=Default] [VpxdMoHost::UpdateDasState] VC state for host host-234 (initialized -> initialized), FDM state (Live -> FDMUnreachable), src of state (host-123 -> host-123)
2025-11-20T17:02:10.456Z info vpxd[12345] [Originator@6876 sub=Default] [VpxdMoHost::UpdateDasState] VC state for host host-234 (initialized -> initialized), FDM state (FDMUnreachable -> Dead), src of state (host-123 -> host-123)
2025-11-20T17:05:31.789Z info vpxd[12345] [Originator@6876 sub=Default] [VpxdMoHost::UpdateDasState] VC state for host host-234 (initialized -> initialized), FDM state (Dead -> Live), src of state (host-123 -> host-123)
```

**From `/var/run/log/fdm-installer.log` (Configuration Issues):**
```
2025-11-20T17:10:05.123Z fdm-installer: [24683] Result of esxcli software vib install -v=/tmp/vmware-root/ha-agentmgr/vpx-upgrade-installer/vmware-fdm.vib: [DependencyError]
2025-11-20T17:10:06.456Z fdm-installer: VIB QLogic_bootbank_qlogic_hcli_2.2.60.7.0.0vmw.500.0.0.472560 violates extensibility rule checks
```

### Troubleshooting Steps

**Step 1: Verify HA Configuration**
```bash
# Check FDM service status
/etc/init.d/fdm status

# View FDM configuration
cat /etc/opt/vmware/fdm/fdm.cfg

# Check protected VMs
cat /etc/opt/vmware/fdm/protected_vms
```

**Step 2: Identify HA Master**
```bash
# From any host in cluster
grep "is master" /var/log/fdm.log | tail -10

# Look for master election logs
grep -i "election" /var/log/fdm.log | tail -20

# Check current master
grep "Master elected" /var/log/fdm.log | tail -5
```

**Sample Output:**
```
2025-11-20T17:00:34.123Z [FDM] info [LocalNode] Node changed to Master
2025-11-20T17:00:35.456Z [FDM] info [ClusterConfig] Cluster configuration updated: master=192.168.1.20
```

**Step 3: Verify Network Heartbeat**
```bash
# From slave host, test connectivity to master
vmkping -I vmk0 192.168.1.20

# Check management network interface
esxcli network ip interface list

# Verify HA firewall rules
esxcli network firewall ruleset list | grep fdm

# Enable FDM firewall rule if disabled
esxcli network firewall ruleset set -e true -r fdm
```

**Sample Output (Healthy):**
```
# vmkping -I vmk0 192.168.1.20
PING 192.168.1.20 (192.168.1.20): 56 data bytes
64 bytes from 192.168.1.20: icmp_seq=0 ttl=64 time=0.234 ms
64 bytes from 192.168.1.20: icmp_seq=1 ttl=64 time=0.189 ms
```

**Step 4: Check Datastore Heartbeat**
```bash
# List datastores
esxcli storage filesystem list

# Check for heartbeat datastores
ls -lh /vmfs/volumes/ | grep heartbeat

# Verify datastore accessibility
esxcli storage core path list | grep -i active

# Check for APD/PDL conditions
grep -i -E "APD|PDL" /var/log/vmkernel.log | tail -20
```

**Step 5: Analyze Heartbeat Logs**
```bash
# Check for heartbeat failures
grep -i "heartbeat" /var/log/fdm.log | tail -50

# Look for isolation events
grep -i "isolation" /var/log/fdm.log | tail -30

# Check for network partition
grep -i "partition" /var/log/fdm.log | tail -20
```

**Step 6: Review HA Admission Control**
```bash
# From vSphere Client:
# Cluster → Configure → vSphere HA → Edit → Admission Control

# Via PowerCLI:
Get-Cluster "Production" | Select HAEnabled, HAAdmissionControlEnabled, HAFailoverLevel
```

**Step 7: Restart FDM Agent (If Needed)**
```bash
# Restart FDM service
/etc/init.d/fdm restart

# Verify FDM is running
/etc/init.d/fdm status

# Monitor fdm.log for errors
tail -f /var/log/fdm.log
```

**Step 8: Reconfigure HA (If Persistent Issues)**

**Via vSphere Client:**
1. Navigate to Cluster → Configure → vSphere HA
2. Click Edit → Turn OFF vSphere HA
3. Wait for task to complete
4. Turn ON vSphere HA
5. Monitor fdm.log on hosts during reconfiguration

**Via PowerCLI:**
```powershell
# Disable HA
Set-Cluster -Cluster "Production" -HAEnabled $false -Confirm:$false

# Wait 30 seconds
Start-Sleep -Seconds 30

# Enable HA
Set-Cluster -Cluster "Production" -HAEnabled $true -Confirm:$false
```

**Step 9: Configure Advanced HA Settings**
```bash
# Set custom isolation addresses
# Via vSphere Client: Cluster → Configure → vSphere HA → Edit → Advanced Options
# Add:
das.isolationaddress0 = 192.168.1.1
das.isolationaddress1 = 8.8.8.8

# Adjust heartbeat datastores
das.heartbeatDsPerHost = 2

# Modify failure detection time (milliseconds)
das.failuredetectiontime = 15000
```

### Related KB Articles
- **KB 318936**: Troubleshooting VMware High Availability (HA) issues
- **KB 324992**: Determining if your VMware vSphere HA cluster has experienced a host failure
- **KB 413777**: VMware vSphere HA cluster has experienced a host failure
- **KB 318929**: vSphere HA agent cannot be correctly installed or configured
- **KB 315379**: vSphere HA reports that an agent is in the Agent Unreachable state
- **KB 372329**: vSphere HA clusters fails to configure in vCenter Server 8.0 U3

### Key Monitoring Points
- FDM state transitions: Live → FDMUnreachable → Dead
- Network heartbeat on management network (UDP)
- Datastore heartbeat on shared VMFS (file-based)
- Master election process and priority
- Isolation address response

---

## Scenario 4: DRS Not Working

### Symptoms
- DRS not generating recommendations
- VMs not automatically migrating
- Cluster imbalance despite DRS enabled
- "DRS functionality was impacted" warnings
- vCLS VMs unavailable

### Sample Log Excerpts

**From vCenter `/var/log/vmware/vpxd/vpxd.log`:**
```
2025-11-20T17:15:45.123Z warning vpxd[23456] [Originator@6876 sub=DRS] Failed to apply DRS recommendation: Insufficient resources on target host
2025-11-20T17:16:12.456Z error vpxd[23456] [Originator@6876 sub=DRS] VM vm-202 placement constraint violated due to affinity rule
2025-11-20T17:17:30.789Z info vpxd[23456] [Originator@6876 sub=ClusterComputeResource] ClusterComputeResource::InvokeDrs: DRS invoked for cluster domain-c123
2025-11-20T17:17:31.012Z info vpxd[23456] [Originator@6876 sub=DRS] DRS generated 0 recommendations for cluster Production
```

**From vCenter `/var/log/vmware/vpxd/vpxd-profiler.log`:**
```
2025-11-20T17:17:30.123Z [DRSProfiler] Cluster Production: CPU utilization: Host1=85%, Host2=45%, Host3=42%
2025-11-20T17:17:30.456Z [DRSProfiler] Migration threshold: 3 (Conservative)
2025-11-20T17:17:30.789Z [DRSProfiler] Imbalance score: 12 (below threshold for migration)
```

**From ESXi `/var/log/vpxa.log`:**
```
2025-11-20T17:18:00.123Z info vpxa[34567] [Originator@6876 sub=vpxaInvtVm] DRS requested migration of VM TestVM-03 to host esxi-02.domain.com
2025-11-20T17:18:01.456Z error vpxa[34567] [Originator@6876 sub=VMotionUtil] vMotion prerequisites not met: EVC mode mismatch
```

**vCLS VM Issues:**
```
2025-11-20T17:20:00.123Z warning vpxd[23456] [Originator@6876 sub=vCLS] vSphere DRS functionality was impacted due to unhealthy state vSphere Cluster Services
2025-11-20T17:20:01.456Z error vpxd[23456] [Originator@6876 sub=vCLS] vCLS VM vCLS-1234 failed to power on: Insufficient resources
```

### Troubleshooting Steps

**Step 1: Verify DRS Configuration**

**Via vSphere Client:**
1. Navigate to Cluster → Configure → vSphere DRS
2. Verify DRS is Enabled
3. Check Automation Level (Manual, Partially Automated, Fully Automated)
4. Review Migration Threshold setting

**Via PowerCLI:**
```powershell
# Connect to vCenter
Connect-VIServer -Server vcenter.domain.com

# Get DRS configuration
Get-Cluster "Production" | Select Name, DrsEnabled, DrsAutomationLevel, DrsMode

# Sample output:
# Name       DrsEnabled DrsAutomationLevel DrsMode
# ----       ---------- ------------------ -------
# Production True       FullyAutomated     FullyAutomated
```

**Step 2: Check DRS Recommendations**
```powershell
# Get current DRS recommendations
Get-Cluster "Production" | Get-DrsRecommendation

# View recommendation details
Get-Cluster "Production" | Get-DrsRecommendation | Format-List *

# Apply recommendations manually
Get-Cluster "Production" | Get-DrsRecommendation | Apply-DrsRecommendation
```

**Step 3: Review DRS Rules**
```powershell
# Get all DRS rules
Get-Cluster "Production" | Get-DrsRule

# Check VM-to-VM affinity rules
Get-Cluster "Production" | Get-DrsRule -Type VMAntiAffinity

# Check VM-to-Host affinity rules
Get-Cluster "Production" | Get-DrsVMHostRule

# View DRS cluster groups
Get-Cluster "Production" | Get-DrsClusterGroup
```

**Step 4: Analyze vCenter Logs for DRS**
```bash
# SSH to vCenter and check DRS logs
grep -i "drs" /var/log/vmware/vpxd/vpxd.log | tail -100

# Look for DRS invocations
grep "InvokeDrs" /var/log/vmware/vpxd/vpxd.log | tail -50

# Check for DRS errors
grep -i -E "drs.*error|drs.*fail" /var/log/vmware/vpxd/vpxd.log | tail -50

# Check DRS recommendation generation
grep -i "recommendation" /var/log/vmware/vpxd/vpxd.log | grep -i drs | tail -30
```

**Step 5: Verify vMotion Prerequisites**
```bash
# From each ESXi host
# Check vMotion VMkernel interface
esxcli network ip interface list | grep -A5 vmk1

# Verify vMotion is enabled
esxcfg-vmknic -l | grep -i vmotion

# Test vMotion connectivity between hosts
vmkping -I vmk1 <other-host-vmotion-ip>

# Verify EVC mode
vim-cmd hostsvc/hostsummary | grep -i evc
```

**Step 6: Check Cluster Resource Balance**
```powershell
# Get cluster resource usage
Get-Cluster "Production" | Get-VMHost | Select Name, 
    @{N="CPU Usage %";E={[math]::Round($_.CpuUsageMhz/$_.CpuTotalMhz*100,2)}},
    @{N="Memory Usage %";E={[math]::Round($_.MemoryUsageGB/$_.MemoryTotalGB*100,2)}}

# Sample output:
# Name             CPU Usage % Memory Usage %
# ----             ----------- --------------
# esxi-01.domain   85.23       72.45
# esxi-02.domain   42.15       38.22
# esxi-03.domain   45.67       41.89
```

**Step 7: Troubleshoot vCLS VMs**
```bash
# From vCenter, check vCLS VM status
# vSphere Client: Cluster → Monitor → vSphere DRS → vCLS

# Via PowerCLI
Get-Cluster "Production" | Get-VM | Where {$_.Name -like "vCLS*"} | Select Name, PowerState

# Check vCLS logs in vCenter
grep -i "vcls" /var/log/vmware/vpxd/vpxd.log | tail -50
```

**If vCLS VMs are not powered on:**
```powershell
# Power on vCLS VMs
Get-Cluster "Production" | Get-VM | Where {$_.Name -like "vCLS*" -and $_.PowerState -eq "PoweredOff"} | Start-VM

# Verify sufficient cluster resources for vCLS VMs
```

**Step 8: Verify VM DRS Settings**
```powershell
# Check if specific VMs have DRS disabled
Get-VM | Select Name, 
    @{N="DRS Automation Level";E={(Get-VM $_ | Get-VMResourceConfiguration).DrsAutomationLevel}}

# Re-enable DRS for specific VM
Get-VM "TestVM-01" | Set-VMResourceConfiguration -DrsAutomationLevel AsSpecifiedByCluster
```

**Step 9: Check for Affinity Rule Conflicts**
```bash
# From vCenter logs
grep -i "rule.*violat\|constraint.*violat" /var/log/vmware/vpxd/vpxd.log | tail -30

# Common messages:
# "Cannot satisfy VM-Host affinity rule"
# "Anti-affinity rule prevents placement"
# "Conflicting DRS rules detected"
```

**Step 10: Adjust DRS Settings**
```powershell
# Increase DRS aggressiveness (1=aggressive, 5=conservative)
Set-Cluster -Cluster "Production" -DrsAutomationLevel FullyAutomated
Set-Cluster -Cluster "Production" -DrsMode FullyAutomated -DrsAggressiveness 2

# Force DRS invocation (DRS runs every 5 minutes by default)
# Wait for next DRS cycle or manually trigger by entering/exiting maintenance mode
```

### Related KB Articles
- **KB 344925**: "Unable to apply DRS resource settings on host" error
- **KB 320016**: Distributed Resource Scheduler cluster reports DRS errors
- **KB 378718**: DRS fails to load balance the VMs due to EVC mismatch
- **KB 79892**: DRS Functionality Impacted by Unhealthy State of vCLS VMs
- Virtualization Dojo: "6 Unmissable Things to Check When Troubleshooting DRS"

### Common DRS Issues and Resolutions

| Issue | Cause | Resolution |
|-------|-------|------------|
| No recommendations generated | Cluster already balanced or threshold too conservative | Lower migration threshold (increase aggressiveness) |
| VMs not migrating | Manual automation level or VM-level DRS disabled | Set to Fully Automated |
| vMotion prerequisites not met | Network, CPU, storage compatibility issues | Verify vMotion network, enable EVC, check storage access |
| Affinity rule violations | Conflicting or impossible-to-satisfy rules | Review and modify DRS rules |
| vCLS VMs unavailable | Insufficient cluster resources or power state issues | Power on vCLS VMs, ensure adequate resources |

---

## Scenario 5: vMotion Failures

### Symptoms
- vMotion task fails at specific percentages (10%, 14%, 20%, 88%)
- "Timed out waiting for migration start request" errors
- Network timeout during migration
- CPU compatibility check failed
- Storage vMotion failures

### Sample Log Excerpts

**From ESXi source host `/var/log/hostd.log`:**
```
2025-11-20T17:30:00.123Z error hostd[45678] [Originator@6876 sub=Vmotion] vMotion timeout at 14%: Timeout waiting for migration start request
2025-11-20T17:30:10.456Z error hostd[45678] [Originator@6876 sub=VMotionUtil] Failed to establish vMotion connection to destination host
2025-11-20T17:30:15.789Z error hostd[45678] [Originator@6876 sub=Migrate] Migration failed: The vMotion failed because the destination host did not receive data from the source host
```

**From ESXi source host `/var/log/vmkernel.log`:**
```
2025-11-20T17:30:00.456Z cpu8:67234)WARNING: Migrate: vm 12345: 1234: Migration timeout at phase 2 (20%)
2025-11-20T17:30:05.789Z cpu8:67234)WARNING: NetVMotion: 2345: Network unreachable during migration: vmk1 -> 192.168.10.21
2025-11-20T17:30:10.012Z cpu8:67234)ERROR: Storage: vm 12345: 3456: Disk access error during migration: naa.600605b00...
```

**From ESXi destination host `/var/log/hostd.log`:**
```
2025-11-20T17:30:02.123Z info hostd[56789] [Originator@6876 sub=Vmotion] Received vMotion request for VM TestVM-05 from source host 192.168.10.20
2025-11-20T17:30:08.456Z error hostd[56789] [Originator@6876 sub=VMotionUtil] Failed to receive migration: Network connection timeout
2025-11-20T17:30:09.789Z warning hostd[56789] [Originator@6876 sub=Hostd.MigrateSupport] Cleaning up failed vMotion attempt
```

**From vCenter `/var/log/vmware/vpxd/vpxd.log`:**
```
2025-11-20T17:30:00.123Z info vpxd[23456] [Originator@6876 sub=vpxLro opID=abc123-456] BEGIN relocate vm-234 from host-123 to host-456
2025-11-20T17:30:15.456Z error vpxd[23456] [Originator@6876 sub=vpxLro opID=abc123-456] Task failed: A general system error occurred: Failed waiting for data
2025-11-20T17:30:16.789Z info vpxd[23456] [Originator@6876 sub=vpxLro opID=abc123-456] END relocate FAIL
```

**From VM log `/vmfs/volumes/datastore1/TestVM-05/vmware.log`:**
```
2025-11-20T17:30:00.123Z vcpu-0| Migrate: Starting migration from esxi-01.domain.com to esxi-02.domain.com
2025-11-20T17:30:05.456Z vcpu-0| MigrateCheckpoint: State save started
2025-11-20T17:30:10.789Z vcpu-0| Migrate: Migration failed: Network timeout during pre-copy phase
```

### Troubleshooting Steps Based on Failure Percentage

#### vMotion Failure at 10% or 14%

**Indicates:** Network connectivity or authentication issues between hosts

**Step 1: Verify vMotion Network Configuration**
```bash
# From both source and destination ESXi hosts
esxcli network ip interface list

# Check vMotion VMkernel interface
esxcfg-vmknic -l | grep -i vmotion

# Sample output:
# vmk1   1500  192.168.10.20  255.255.255.0  00:50:56:6b:12:34  STATIC  vMotion  true
```

**Step 2: Test vMotion Network Connectivity**
```bash
# From source host to destination vMotion IP
vmkping -I vmk1 192.168.10.21

# Test with large packets (MTU validation)
vmkping -s 8972 -d -I vmk1 192.168.10.21

# Expected output for successful jumbo frame test:
# PING 192.168.10.21 (192.168.10.21): 8972 data bytes
# 8980 bytes from 192.168.10.21: icmp_seq=0 ttl=64 time=0.567 ms
```

**Step 3: Verify Firewall Rules**
```bash
# Check vMotion firewall rule
esxcli network firewall ruleset list | grep -i vmotion

# Enable vMotion firewall if disabled
esxcli network firewall ruleset set -e true -r vMotion

# Verify allowed IPs (should show "All" for trust network)
esxcli network firewall ruleset allowedip list | grep -A5 vMotion
```

**Step 4: Check Network Configuration Consistency**
```bash
# Verify virtual switch configuration
esxcfg-vswitch -l

# Check port group configuration
esxcli network vswitch standard portgroup list

# Verify MTU settings on vSwitch
esxcli network vswitch standard list | grep -A10 vSwitch1
```

**Step 5: Test SSH Connectivity**
```bash
# From source host, test SSH to destination
ssh root@esxi-02.domain.com

# If SSH fails, vMotion will also fail at 10%
```

#### vMotion Failure at 20%

**Indicates:** Memory pre-copy phase timeout, high memory change rate

**Step 1: Check VM Memory Activity**
```bash
# Monitor VM memory change rate during migration
esxtop
# Press 'm' for memory view
# Look for VM and check 'MCTL?' and 'MCTLSZ' columns
```

**Step 2: Review vmkernel Logs**
```bash
# Check for memory-related migration errors
grep -i "memory.*dirty\|precopy" /var/log/vmkernel.log | tail -30

# Look for high memory change rate messages
grep -i "migrate.*memory" /var/log/vmkernel.log | tail -20
```

**Step 3: Reduce VM Memory Pressure**
- Close unnecessary applications in VM
- Consider cold migration (power off, then migrate)
- Increase vMotion timeout settings (advanced)

**Step 4: Check for Memory Overcommitment**
```bash
# Check host memory state
esxtop
# Press 'm' for memory view
# Check 'PMEM' (physical memory) usage across all VMs
```

#### vMotion Failure at 88%

**Indicates:** Final switchover/cutover timeout, storage latency

**Step 1: Check Storage Performance**
```bash
# Monitor storage latency
esxtop
# Press 'd' for disk view
# Check 'DAVG/cmd' (device average latency)
# Values >20ms indicate potential issues

# Check for storage path issues
esxcli storage core path list | grep -i "State:active"
```

**Step 2: Review Storage-Related Errors**
```bash
# Check vmkernel for storage errors
grep -i -E "storage.*fail|disk.*error|timeout" /var/log/vmkernel.log | tail -50

# Look for APD/PDL conditions
grep -i -E "APD|PDL" /var/log/vmkernel.log | tail -20
```

**Step 3: Verify Shared Storage Access**
```bash
# Ensure both hosts can access the same datastores
esxcli storage filesystem list

# Check multipathing status
esxcli storage core path list | grep -E "naa\.|vmhba"

# Verify no VMFS locks
vmkfstools -D /vmfs/volumes/<datastore>/TestVM-05/TestVM-05.vmdk
```

#### General vMotion Troubleshooting Steps

**Step 1: Verify CPU Compatibility**
```bash
# Check EVC mode on cluster
vim-cmd hostsvc/hostsummary | grep -i evc

# From vCenter PowerCLI
Get-Cluster "Production" | Select Name, EVCMode

# Check CPU features
grep -i vmx /proc/cpuinfo

# Verify CPU vendor and model consistency
esxcli hardware cpu list | grep -E "Id:|Brand:"
```

**Step 2: Check for Incompatible Devices**
```powershell
# From vCenter, check VM for local devices
Get-VM "TestVM-05" | Get-CDDrive | Where {$_.IsoPath -like "*local*"}

# Check for physical RDM in physical compatibility mode
Get-VM "TestVM-05" | Get-HardDisk | Where {$_.DiskType -eq "RawPhysical"}
```

**Step 3: Validate Virtual Switch Configuration**
```bash
# Ensure virtual switch names match on both hosts
esxcfg-vswitch -l

# Check port group names
esxcli network vswitch standard portgroup list

# Verify VM is not using host-local networking
```

**Step 4: Enable Verbose vMotion Logging**
```bash
# Enable detailed vMotion logging
esxcli system settings advanced set -o /Migrate/Enabled -i 1

# Set vmkernel log level
esxcli system syslog config logger set --id=vmkernel --level=debug

# Attempt vMotion

# Monitor detailed logs
tail -f /var/log/vmkernel.log | grep -i migrate

# Disable verbose logging after troubleshooting
esxcli system settings advanced set -o /Migrate/Enabled -i 0
esxcli system syslog config logger set --id=vmkernel --level=info
```

**Step 5: Capture Network Packets During vMotion**
```bash
# Start packet capture on vMotion VMkernel interface
pktcap-uw --vmk vmk1 --outfile /tmp/vmotion-capture.pcap

# Attempt vMotion in another session

# Stop capture (Ctrl+C)

# Download and analyze with Wireshark
scp /tmp/vmotion-capture.pcap user@workstation:/analysis/
```

**Step 6: Review vMotion Operation in vCenter Logs**
```bash
# Find vMotion operation ID
grep "relocate" /var/log/vmware/vpxd/vpxd-*.log | grep BEGIN | grep "TestVM-05"

# Sample output:
# 2025-11-20T17:30:00.123Z info vpxd[23456] [Originator@6876 sub=vpxLro opID=xyz789-012] BEGIN relocate

# Trace entire operation using opID
grep "xyz789-012" /var/log/vmware/vpxd/vpxd-*.log | less
```

**Step 7: Check vMotion Advanced Settings**
```bash
# Verify vMotion timeout settings
vim-cmd hostsvc/advopt/view Migrate.VMotionLatencySensitivity
vim-cmd hostsvc/advopt/view Migrate.VMotionStreamTimeout

# Verify vMotion bandwidth reservation (if configured)
esxcli network ip interface tag get -i vmk1
```

### Related KB Articles
- **KB 1003734**: Understanding and troubleshooting vMotion
- **KB 321009**: Understanding and troubleshooting vMotion
- **KB 318636**: Troubleshooting vMotion fails with network errors
- **KB 1003728**: Testing VMkernel network connectivity with the vmkping command
- **KB 1013150**: vMotion fails at 10% with the error: Migration failed while copying data
- Virtualization Dojo: "5 Awesome Tips to Troubleshoot vMotion"

### vMotion Failure Summary Table

| Failure Point | Common Causes | Primary Check |
|---------------|---------------|---------------|
| 10% | Network connectivity, authentication | vmkping, SSH, firewall rules |
| 14% | Resource allocation, admission control | CPU/memory reservations |
| 20% | Memory pre-copy timeout | High memory change rate |
| 88% | Storage latency, final sync | Storage performance, DAVG latency |
| General | CPU compatibility, device compatibility | EVC mode, local devices |

### vMotion Prerequisites Checklist

- [ ] Gigabit or faster network for vMotion (10GbE recommended)
- [ ] Shared storage accessible to both hosts
- [ ] vMotion enabled on VMkernel interfaces
- [ ] Same virtual switch names on source and destination
- [ ] Compatible CPU families or EVC enabled
- [ ] No local ISOs or floppy images mounted
- [ ] No physical RDMs in physical compatibility mode
- [ ] vMotion ports open in firewalls (TCP 8000)
- [ ] Jumbo frames configured consistently (if used)
- [ ] Proper vMotion licensing

---

## General Troubleshooting Workflow

### Systematic Approach to Log Analysis

**1. Identify Symptoms and Scope**
- What is the exact error message?
- Which components are affected? (VM, host, cluster, vCenter)
- When did the issue start?
- Were there any recent changes?

**2. Collect Relevant Logs**

**For host issues:**
```bash
tail -100 /var/log/hostd.log
tail -100 /var/log/vmkernel.log
tail -100 /var/log/vpxa.log
```

**For VM issues:**
```bash
vim-cmd vmsvc/getallvms | grep "VM_NAME"
tail -100 /vmfs/volumes/<datastore>/<VM_name>/vmware.log
```

**For HA issues:**
```bash
tail -100 /var/log/fdm.log
grep -i "election\|heartbeat\|isolation" /var/log/fdm.log | tail -50
```

**For vCenter issues:**
```bash
tail -100 /var/log/vmware/vpxd/vpxd.log
grep -i "error\|fail" /var/log/vmware/vpxd/vpxd.log | tail -50
```

**3. Search for Error Keywords**
```bash
# Common error patterns
grep -i -E "error|fail|timeout|disconnect" <logfile>

# Specific to issue type
grep -i "snapshot" <logfile>
grep -i "migrate\|vmotion" <logfile>
grep -i "heartbeat" <logfile>
grep -i "drs" <logfile>
```

**4. Correlate Timestamps**
- Match event timestamps across multiple logs
- Compare user-reported issue time with log timestamps
- Look for patterns or sequences of events

**5. Verify Environment Health**

**Network connectivity:**
```bash
ping <target>
vmkping -I vmk0 <target>
esxcli network ip connection list
```

**Storage access:**
```bash
esxcli storage filesystem list
esxcli storage core path list
df -h
```

**Service status:**
```bash
/etc/init.d/hostd status
/etc/init.d/vpxa status
/etc/init.d/fdm status
```

**6. Apply Fixes with Caution**
- Test in lab/dev environment first if possible
- Take snapshots or backups before changes
- Document all changes made
- Have rollback plan ready

**7. Validate Resolution**
- Verify issue is resolved
- Test related functionality
- Monitor logs for recurring issues
- Update documentation

### Log Collection Best Practices

**Generate Support Bundles:**

**For ESXi:**
```bash
vm-support
# Or with options:
vm-support -x -d 1440 -w /tmp/
# Generates: esx-HOSTNAME-DATE-RANDOM.tgz
```

**For vCenter:**
```bash
vc-support -w /tmp/
# Or from VAMI: https://vcenter:5480 → Support → Download Support Bundle
```

**Automated Log Collection Script:**
```bash
#!/bin/bash
# log-collect.sh - Collect relevant logs for troubleshooting

DATE=$(date +%Y%m%d-%H%M%S)
HOSTNAME=$(hostname)
LOGDIR="/tmp/logs-${HOSTNAME}-${DATE}"

mkdir -p ${LOGDIR}

# Copy ESXi logs
cp /var/log/hostd.log ${LOGDIR}/
cp /var/log/vmkernel.log ${LOGDIR}/
cp /var/log/vpxa.log ${LOGDIR}/
cp /var/log/fdm.log ${LOGDIR}/
cp /var/log/shell.log ${LOGDIR}/

# Collect configuration
esxcli system version get > ${LOGDIR}/system-version.txt
esxcli network ip interface list > ${LOGDIR}/network-interfaces.txt
esxcli storage filesystem list > ${LOGDIR}/datastores.txt

# Create tarball
tar -czf /tmp/logs-${HOSTNAME}-${DATE}.tgz -C /tmp logs-${HOSTNAME}-${DATE}/

echo "Logs collected: /tmp/logs-${HOSTNAME}-${DATE}.tgz"
```

---

## Critical Commands Reference

### VM Management Commands

```bash
# List all VMs with VMIDs
vim-cmd vmsvc/getallvms

# VM power operations
vim-cmd vmsvc/power.on <VMID>
vim-cmd vmsvc/power.off <VMID>
vim-cmd vmsvc/power.shutdown <VMID>    # Graceful shutdown
vim-cmd vmsvc/power.reboot <VMID>
vim-cmd vmsvc/power.reset <VMID>       # Hard reset

# VM information
vim-cmd vmsvc/get.summary <VMID>
vim-cmd vmsvc/get.config <VMID>
vim-cmd vmsvc/get.runtime <VMID>
vim-cmd vmsvc/power.getstate <VMID>

# Snapshot operations
vim-cmd vmsvc/get.snapshot <VMID>
vim-cmd vmsvc/snapshot.create <VMID> "snapshot_name" "description"
vim-cmd vmsvc/snapshot.removeall <VMID>
vim-cmd vmsvc/snapshot.remove <VMID> <snapshot_id>

# Register/Unregister VM
vim-cmd solo/registervm /vmfs/volumes/<datastore>/VM/VM.vmx
vim-cmd vmsvc/unregister <VMID>

# Reload VM configuration
vim-cmd vmsvc/reload <VMID>
```

### Storage Commands

```bash
# List datastores
esxcli storage filesystem list

# Datastore browser
ls -lh /vmfs/volumes/

# Check VMFS volume details
vmkfstools -P /vmfs/volumes/<datastore_name>

# Storage device info
esxcli storage core device list

# Storage adapter info
esxcli storage core adapter list

# Storage paths
esxcli storage core path list

# Rescan storage
esxcli storage core adapter rescan --all
esxcli storage core adapter rescan -A vmhba1

# VAAI status
esxcli storage core device vaai status get

# Clone VMDK
vmkfstools -i source.vmdk destination.vmdk

# Clone with thin provisioning
vmkfstools -i source.vmdk -d thin destination.vmdk

# Extend VMDK
vmkfstools -X 100G VM.vmdk
```

### Network Commands

```bash
# List VMkernel interfaces
esxcli network ip interface list
esxcfg-vmknic -l

# List virtual switches
esxcli network vswitch standard list
esxcfg-vswitch -l

# List port groups
esxcli network vswitch standard portgroup list

# Network connectivity tests
vmkping -I vmk0 <IP>
vmkping -s 8972 -d -I vmk0 <IP>    # Jumbo frames test

# Firewall rules
esxcli network firewall ruleset list
esxcli network firewall ruleset set -e true -r <ruleset_name>
esxcli network firewall ruleset allowedip list

# TCP/IP connections
esxcli network ip connection list

# DNS configuration
esxcli network ip dns server list
esxcli network ip dns search list
```

### System Information Commands

```bash
# ESXi version and build
vmware -vl
esxcli system version get

# System uptime
esxcli system stats uptime get
uptime

# Hardware information
esxcli hardware platform get
esxcli hardware cpu list
esxcli hardware memory get

# Service status
/etc/init.d/hostd status
/etc/init.d/vpxa status
/etc/init.d/fdm status

# Restart services
/etc/init.d/hostd restart
/etc/init.d/vpxa restart
/etc/init.d/fdm restart
services.sh restart    # Restart all services

# View running processes
ps -c
esxcli vm process list

# System logs
tail -f /var/log/syslog.log
tail -f /var/log/vmkernel.log
tail -f /var/log/hostd.log
```

### Performance Monitoring Commands

```bash
# Real-time performance (esxtop)
esxtop

# esxtop views:
# c - CPU
# m - Memory
# d - Disk
# n - Network

# esxtop in batch mode
esxtop -b -d 5 -n 12 > /tmp/esxtop.csv

# VM resource usage
esxtop -v    # VM view
```

### PowerCLI Commands

```powershell
# Connect to vCenter
Connect-VIServer -Server vcenter.domain.com

# Cluster management
Get-Cluster | Select Name, HAEnabled, DrsEnabled
Get-Cluster "Production" | Get-DrsRecommendation
Get-Cluster "Production" | Get-DrsRule

# Host management
Get-VMHost | Select Name, ConnectionState, PowerState
Get-VMHost "esxi-01.domain.com" | Get-Log -Key vmkernel

# VM management
Get-VM | Select Name, PowerState, NumCpu, MemoryGB
Get-VM "TestVM-01" | Get-Snapshot
Get-VM "TestVM-01" | Move-VM -Destination (Get-VMHost "esxi-02.domain.com")

# Datastore management
Get-Datastore | Select Name, CapacityGB, FreeSpaceGB

# Generate support bundle
Get-VMHost "esxi-01.domain.com" | Get-Log -Bundle -DestinationPath C:\Logs\
```

---

## Additional Resources

### VMware/Broadcom Knowledge Base

**Official Documentation:**
- Broadcom Support Portal: https://knowledge.broadcom.com
- VMware vSphere Documentation: https://techdocs.broadcom.com

**Key KB Articles Referenced:**

**Snapshots:**
- KB 316392: Troubleshooting issues when creating or committing snapshots
- KB 1015180: Understanding virtual machine snapshots
- KB 1025279: Best practices for virtual machine snapshots

**HA:**
- KB 318936: Troubleshooting VMware High Availability issues
- KB 324992: Determining if HA cluster has experienced host failure
- KB 315379: vSphere HA reports agent in Agent Unreachable state

**DRS:**
- KB 344925: "Unable to apply DRS resource settings on host" error
- KB 320016: DRS cluster reports errors
- KB 378718: DRS fails to load balance VMs due to EVC mismatch

**vMotion:**
- KB 1003734: Understanding and troubleshooting vMotion
- KB 321009: Understanding and troubleshooting vMotion
- KB 318636: Troubleshooting vMotion network errors

**Host Connectivity:**
- KB 344682: Troubleshooting ESXi host disconnected/not responding
- KB 318647: ESXi host disconnects intermittently
- KB 303652: Changing ESXi host connection status

### Community Resources

**Blogs and Forums:**
- Virtualization Dojo: https://virtualizationdojo.com
- VMware Communities: https://communities.vmware.com
- vExpert Directory: https://vexpert.vmware.com
- Reddit r/vmware: https://reddit.com/r/vmware

**Training and Certification:**
- VMware vSphere: Troubleshooting Workshop [V8]
- VCAP-DCV Deploy Certification
- vExpert Program Resources

### Monitoring Tools

**Recommended Tools:**
- vRealize Operations Manager
- vRealize Log Insight
- Grafana with Telegraf for ESXi
- ESXTOP / vscsiStats for performance
- RVTools for inventory and reporting

---

## Document Version History

**Version 1.0 - November 20, 2025**
- Initial creation
- Comprehensive scenario-based troubleshooting guide
- Includes sample logs from real-world scenarios
- Integrated VMware/Broadcom KB article references
- Detailed step-by-step resolution procedures
- Covers snapshots, HA, DRS, vMotion, and host connectivity issues

**Maintained by:** VMware Infrastructure Team  
**Last Updated:** November 20, 2025  
**Next Review:** February 20, 2026

---

**End of VMware vSphere Troubleshooting Runbook**