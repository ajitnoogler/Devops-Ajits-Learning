# VMware vSphere Troubleshooting Runbook

## Table of Contents

\begin{enumerate}
\item ESXi and vCenter Log Files
\item Log Analysis Commands and Techniques
\item Snapshot Troubleshooting
\item vSphere HA (High Availability) Troubleshooting
\item DRS (Distributed Resource Scheduler) Troubleshooting
\item vMotion Troubleshooting
\item Common Troubleshooting Commands
\end{enumerate}

---

## 1. ESXi and vCenter Log Files

### 1.1 ESXi Host Log Files

**Primary ESXi Log Location:** `/var/log/`

\begin{table}
\begin{tabular}{|l|l|p{8cm}|}
\hline
\textbf{Log File} & \textbf{Location} & \textbf{Purpose} \\
\hline
vmkernel.log & /var/log/vmkernel.log & Core VMkernel operations, storage, networking, device drivers, resource allocation \\
\hline
hostd.log & /var/log/hostd.log & Host management service, VM operations, power on/off, API calls \\
\hline
vpxa.log & /var/log/vpxa.log & vCenter agent communication, vCenter connectivity issues \\
\hline
fdm.log & /var/log/fdm.log & HA (Fault Domain Manager) operations, master/slave elections \\
\hline
shell.log & /var/log/shell.log & ESXi Shell activity, CLI commands executed \\
\hline
syslog.log & /var/log/syslog.log & General system messages, hardware events \\
\hline
vobd.log & /var/log/vobd.log & VMware ESXi Observation service, hardware health \\
\hline
storageRM.log & /var/log/storageRM.log & Storage resource management, SIOC operations \\
\hline
vmkwarning.log & /var/log/vmkwarning.log & VMkernel warnings and errors \\
\hline
vmksummary.log & /var/log/vmksummary.log & Uptime and availability statistics \\
\hline
\end{tabular}
\caption{ESXi Critical Log Files}
\end{table}

### 1.2 Virtual Machine Log Files

**VM Log Location:** `/vmfs/volumes/<datastore>/<VM_name>/`

\begin{table}
\begin{tabular}{|l|p{10cm}|}
\hline
\textbf{File} & \textbf{Purpose} \\
\hline
vmware.log & Current VM operations, errors, warnings \\
\hline
vmware-*.log & Archived VM logs (vmware-1.log, vmware-2.log, etc.) \\
\hline
vmx.log & VM configuration changes \\
\hline
*.vmdk & Virtual disk descriptor files \\
\hline
*.vmx & VM configuration file \\
\hline
*.vmsd & Snapshot metadata and state \\
\hline
*.vmsn & Snapshot state files (memory dump) \\
\hline
\end{tabular}
\caption{Virtual Machine Files}
\end{table}

### 1.3 vCenter Server Appliance (VCSA) Log Files

**Primary vCenter Log Location:** `/var/log/vmware/`

\begin{table}
\begin{tabular}{|l|l|p{7cm}|}
\hline
\textbf{Log File} & \textbf{Location} & \textbf{Purpose} \\
\hline
vpxd.log & /var/log/vmware/vpxd/ & vCenter Server daemon, all vCenter operations \\
\hline
vws.log & /var/log/vmware/vws/ & Web Services, vSphere Client connections \\
\hline
eam.log & /var/log/vmware/eam/ & ESX Agent Manager \\
\hline
cm.log & /var/log/vmware/cm/ & Certificate Manager \\
\hline
vcha.log & /var/log/vmware/vcha/ & vCenter High Availability \\
\hline
cloudvm.log & /var/log/vmware/cloudvm/ & VMware Cloud services \\
\hline
sps.log & /var/log/vmware/sps/ & Storage Policy Service \\
\hline
\end{tabular}
\caption{vCenter Server Log Files}
\end{table}

---

## 2. Log Analysis Commands and Techniques

### 2.1 Essential Linux Commands for Log Analysis

**Viewing Logs:**

# Tail last 100 lines of a log file
tail -100 /var/log/vmkernel.log

# Follow log in real-time
tail -f /var/log/hostd.log

# View specific lines
head -50 /var/log/vpxa.log

# View entire log with paging
less /var/log/fdm.log

# View specific time range
cat /var/log/vmkernel.log | grep "2025-11-20"

**Searching with grep:**

# Search for errors
grep -i error /var/log/vmkernel.log

# Search for warnings
grep -i warning /var/log/hostd.log

# Search with case-insensitive
grep -i "snapshot" /var/log/vmkernel.log

# Search multiple patterns
grep -E "error|fail|timeout" /var/log/hostd.log

# Search with context (3 lines before and after)
grep -A 3 -B 3 "vmotion" /var/log/vpxa.log

# Count occurrences
grep -c "error" /var/log/vmkernel.log

# Search recursively in directory
grep -r "snapshot" /var/log/

# Exclude lines
grep -v "info" /var/log/hostd.log | grep error

**Advanced Log Filtering:**

# Find all errors in last hour
find /var/log -name "*.log" -mmin -60 -exec grep -i error {} \;

# Search for specific VM by name
grep "VM_NAME" /var/log/hostd.log

# Filter by timestamp
awk '/2025-11-20T14:00:00/,/2025-11-20T15:00:00/' /var/log/vmkernel.log

# Extract specific fields
awk '{print $1, $2, $5}' /var/log/vmkernel.log

# Count error types
grep error /var/log/vmkernel.log | sort | uniq -c | sort -nr

# Filter logs by severity
sed -n '/error\|critical/Ip' /var/log/hostd.log

**Using vim-cmd for VM Information:**

# List all VMs and their IDs
vim-cmd vmsvc/getallvms

# Get VM power state
vim-cmd vmsvc/power.getstate <VMID>

# Get VM snapshot info
vim-cmd vmsvc/snapshot.get <VMID>

# Get VM detailed information
vim-cmd vmsvc/get.summary <VMID>

# Reload VM configuration
vim-cmd vmsvc/reload <VMID>

### 2.2 PowerCLI Log Collection Commands

# Connect to vCenter
Connect-VIServer -Server vcenter.domain.com

# Get ESXi host logs
Get-VMHost esxi01.domain.com | Get-Log

# Get specific log file
Get-VMHost esxi01.domain.com | Get-Log -Key vmkernel

# Export logs to file
Get-VMHost esxi01.domain.com | Get-Log -Key hostd | 
    Select -ExpandProperty Entries | Out-File hostd.txt

# Get logs from all hosts in cluster
Get-Cluster "Production" | Get-VMHost | Get-Log -Key vpxa

# Get VM logs
Get-VM "TestVM" | Get-Log

# Filter log entries
Get-VMHost esxi01.domain.com | Get-Log -Key vmkernel | 
    Select -ExpandProperty Entries | Where {$_ -match "error"}

### 2.3 ESXi Command-Line Log Analysis

**Using esxcli:**

# View system logs
esxcli system syslog config get

# Configure remote syslog
esxcli system syslog config set --loghost='syslog.domain.com:514'

# View log marks
esxcli system syslog mark

# System log statistics
esxcli system log stats get

**Using localcli:**

# Similar to esxcli but for local host only
localcli system syslog config get

### 2.4 Log Bundle Collection

**vCenter Support Bundle:**

# From VCSA Shell
vc-support -w /tmp/

# From vCenter GUI: Administration > System > Support Bundle

**ESXi Support Bundle:**

# Generate support bundle
vm-support

# Generate with specific parameters
vm-support -x -d 1440 -w /tmp/

# From vSphere Client: Host > Monitor > Logs > Generate Support Bundle

---

## 3. Snapshot Troubleshooting

### 3.1 Understanding Snapshot Chain

VMware snapshots create a delta disk hierarchy:

\begin{itemize}
\item Base VMDK: Original virtual disk
\item Delta disks: *-000001.vmdk, *-000002.vmdk (snapshot changes)
\item .vmsd file: Snapshot metadata database
\item .vmsn file: Snapshot memory state
\end{itemize}

### 3.2 Common Snapshot Issues

\begin{table}
\begin{tabular}{|p{5cm}|p{9cm}|}
\hline
\textbf{Issue} & \textbf{Symptoms} \\
\hline
Snapshot consolidation needed & Warning alarm, snapshot delta disks not committed \\
\hline
Unable to delete snapshot & Snapshot deletion fails with timeout or I/O error \\
\hline
Invalid snapshot configuration & Broken snapshot chain, missing descriptor files \\
\hline
Snapshot disk space issues & Datastore full, snapshots consuming excessive space \\
\hline
Performance degradation & Slow VM performance due to deep snapshot chains \\
\hline
\end{tabular}
\caption{Common Snapshot Problems}
\end{table}

### 3.3 Snapshot Troubleshooting Commands

**Check Snapshot Status:**

# List VM snapshots
vim-cmd vmsvc/get.snapshot <VMID>

# Get all VMs
vim-cmd vmsvc/getallvms

# Check for orphaned snapshots
find /vmfs/volumes -name "*-delta.vmdk" -o -name "*-[0-9][0-9][0-9][0-9][0-9][0-9].vmdk"

# List snapshot files for specific VM
ls -lh /vmfs/volumes/<datastore>/<VM_name>/*-0000*.vmdk

# Check snapshot size
du -sh /vmfs/volumes/<datastore>/<VM_name>/*.vmdk

**Delete Snapshots:**

# Remove all snapshots via CLI
vim-cmd vmsvc/snapshot.removeall <VMID>

# Remove specific snapshot
vim-cmd vmsvc/snapshot.remove <VMID> <snapshot_id>

**Manual Consolidation:**

# Power off VM
vim-cmd vmsvc/power.off <VMID>

# Navigate to VM directory
cd /vmfs/volumes/<datastore>/<VM_name>/

# Check vmdk chain
cat VM_NAME.vmdk | grep -i parent

# Example output analysis
# If VM.vmdk points to VM-000001.vmdk
# And VM-000001.vmdk points to VM-000002.vmdk
# This indicates snapshot chain

# Clone VMDK (consolidate manually)
vmkfstools -i VM-000002.vmdk VM-consolidated.vmdk

# Update VMX to point to new disk
vi VM_NAME.vmx
# Change scsi0:0.fileName = "VM-000002.vmdk"
# To: scsi0:0.fileName = "VM-consolidated.vmdk"

# Reload VM
vim-cmd vmsvc/reload <VMID>

### 3.4 Snapshot Descriptor File Issues

**Fix Broken .vmsd File:**

# Navigate to VM directory
cd /vmfs/volumes/<datastore>/<VM_name>/

# Backup current vmsd file
cp VM_NAME.vmsd VM_NAME.vmsd.backup

# Remove vmsd file
rm VM_NAME.vmsd

# Reload VM (creates new vmsd)
vim-cmd vmsvc/reload <VMID>

# Attempt snapshot deletion
vim-cmd vmsvc/snapshot.removeall <VMID>

**Analyze Snapshot Metadata:**

# View vmsd content
cat VM_NAME.vmsd

# Check for CID (Content ID) mismatch
cat VM_NAME.vmdk | grep CID
cat VM_NAME-000001.vmdk | grep CID

# CID values should form parent-child relationship
# parentCID in child should match CID in parent

### 3.5 Snapshot Log Analysis

**Key Log Files for Snapshots:**

# Check vmkernel.log for snapshot operations
grep -i snapshot /var/log/vmkernel.log

# Check hostd.log for snapshot API calls
grep -i snapshot /var/log/hostd.log | tail -100

# VM-specific snapshot logs
grep -i snapshot /vmfs/volumes/<datastore>/<VM_name>/vmware.log

# Common error patterns to search
grep -E "snapshot.*fail|snapshot.*error|consolidate.*fail" /var/log/hostd.log

**Interpreting Snapshot Errors:**

\begin{table}
\begin{tabular}{|p{6cm}|p{8cm}|}
\hline
\textbf{Error Message} & \textbf{Resolution} \\
\hline
"detected an invalid snapshot configuration" & Corrupt vmsd file - remove and reload VM \\
\hline
"not enough space on the file system" & Free up datastore space or expand datastore \\
\hline
"unable to access file" & Check permissions, locks, or APD/PDL conditions \\
\hline
"snapshot disk consolidation failed" & Manual consolidation or clone VM \\
\hline
"timeout waiting for snapshot operation" & Long-running I/O or storage latency issues \\
\hline
\end{tabular}
\caption{Snapshot Error Messages}
\end{table}

### 3.6 Best Practices for Snapshot Management

\begin{itemize}
\item Limit snapshot chain depth to maximum 3-4 snapshots
\item Do not keep snapshots for more than 72 hours
\item Monitor snapshot size - alert when exceeds 25\% of base disk
\item Always consolidate snapshots after backup operations
\item Avoid snapshots on VMs with high transaction databases
\item Power off VM if manual consolidation required
\item Create snapshot alarms in vCenter (Configuration $\rightarrow$ Alarm Definitions)
\end{itemize}

---

## 4. vSphere HA (High Availability) Troubleshooting

### 4.1 HA Architecture Overview

**Master/Slave Model:**

\begin{itemize}
\item \textbf{Master Host:} Elected via UDP communication, monitors slave hosts and VMs
\item \textbf{Slave Hosts:} Send heartbeats to master, can become master if needed
\item \textbf{FDM Agent:} Fault Domain Manager runs on each host
\item \textbf{Heartbeat Mechanisms:}
  \begin{itemize}
  \item Network Heartbeat: Management network between master and slaves
  \item Datastore Heartbeat: VMFS datastores for isolation detection
  \end{itemize}
\end{itemize}

### 4.2 HA Log Files

**Primary HA Log:** `/var/log/fdm.log`

# View HA logs
tail -f /var/log/fdm.log

# Search for master election
grep -i "election" /var/log/fdm.log

# Check HA state
grep -i "state" /var/log/fdm.log | tail -50

# Find master host
grep -i "master" /var/log/fdm.log | tail -20

# Check heartbeat issues
grep -i "heartbeat" /var/log/fdm.log

**HA Configuration Files:**

# HA configuration directory
ls -lh /etc/opt/vmware/fdm/

# FDM configuration
cat /etc/opt/vmware/fdm/fdm.cfg

# Cluster configuration
ls /etc/vmware/hostd/config/fdm/

### 4.3 Common HA Issues

\begin{table}
\begin{tabular}{|p{5cm}|p{9cm}|}
\hline
\textbf{Issue} & \textbf{Description} \\
\hline
Master cannot be elected & Insufficient number of hosts, network partition \\
\hline
Host isolation detected & Network heartbeat lost but datastore heartbeat present \\
\hline
VM restart fails & Insufficient resources, admission control policy \\
\hline
HA configuration failed & DNS issues, firewall blocking, SSL certificate problems \\
\hline
False host failures & Network instability, heartbeat timeout misconfiguration \\
\hline
\end{tabular}
\caption{Common HA Problems}
\end{table}

### 4.4 HA Troubleshooting Commands

**Check HA Status:**

# Verify HA agent is running
/etc/init.d/fdm status

# Restart HA agent (if needed)
/etc/init.d/fdm restart

# Get cluster information
vim-cmd hostsvc/hostsummary | grep cluster

# Check HA runtime status
esxcli system version get

**FDM Status Commands:**

# Check FDM service
/etc/init.d/fdm status

# FDM configuration
cat /etc/opt/vmware/fdm/fdm.cfg

# List protected VMs
cat /etc/opt/vmware/fdm/protected_vms

**Network Heartbeat Validation:**

# Test connectivity to master (from slave)
vmkping -I vmk0 <master_IP>

# Check management network interface
esxcli network ip interface list

# Verify firewall rules
esxcli network firewall ruleset list | grep fdm

# Enable HA firewall rule if disabled
esxcli network firewall ruleset set -e true -r fdm

**Datastore Heartbeat Validation:**

# List heartbeat datastores
ls -lh /vmfs/volumes/ | grep heartbeat

# Check datastore accessibility
esxcli storage filesystem list

# View storage paths
esxcli storage core path list

### 4.5 HA Master Election Process

**Determine Current Master:**

# From any host in cluster, check fdm.log
grep "is master" /var/log/fdm.log | tail -5

# Master log entry will show
# "LocalNode changed to Master"

# From slaves, log shows
# "Master elected: <Master_IP>"

**Force Master Election:**

# Disable HA on cluster (from vCenter)
# Re-enable HA on cluster

# Or restart FDM on all hosts
/etc/init.d/fdm restart

**Configure Master Election Priority (Advanced):**

Edit `/etc/opt/vmware/fdm/fdm.cfg` and add:

masterElectionPriority=<number>

Higher number = higher priority. Restart FDM after change.

### 4.6 HA Log Analysis Examples

**Successful HA Protection:**

# Look for these patterns in fdm.log
grep "Protecting" /var/log/fdm.log

# Example log entries:
# "Protecting VM <VM_NAME>"
# "HA protection enabled for VM"
# "VM successfully failed over to host"

**Host Isolation Response:**

# Check isolation events
grep -i "isolation" /var/log/fdm.log

# Typical log sequence:
# "Network isolation detected"
# "Datastore heartbeat present - not isolated"
# Or "No datastore heartbeat - host isolated"

**VM Restart Attempts:**

# Search for restart operations
grep -i "restart" /var/log/fdm.log | grep VM_NAME

# Log patterns:
# "Attempting to restart VM"
# "VM restart successful on host"
# "VM restart failed - insufficient resources"

### 4.7 HA Advanced Configuration Parameters

\begin{table}
\begin{tabular}{|p{5cm}|p{9cm}|}
\hline
\textbf{Parameter} & \textbf{Description} \\
\hline
das.isolationaddress[0-9] & IP addresses for isolation validation \\
\hline
das.usedefaultisolationaddress & Use default gateway for isolation check (true/false) \\
\hline
das.heartbeatDsPerHost & Number of datastore heartbeats per host (default: 2) \\
\hline
das.failuredetectiontime & Time in ms before declaring host failed (default: 15000) \\
\hline
das.config.fdm.reportfailoverfailed & Report VM failover failures (true/false) \\
\hline
\end{tabular}
\caption{HA Advanced Configuration}
\end{table}

**Configure Advanced Settings:**

From vSphere Client:
1. Cluster $\rightarrow$ Configure $\rightarrow$ vSphere HA $\rightarrow$ Edit
2. Advanced Options section
3. Add key-value pairs

---

## 5. DRS (Distributed Resource Scheduler) Troubleshooting

### 5.1 DRS Overview

**DRS Functions:**

\begin{itemize}
\item Initial VM placement when powered on
\item Load balancing through vMotion
\item Resource pool enforcement
\item Affinity and anti-affinity rules
\item VM-Host affinity rules
\end{itemize}

**DRS Automation Levels:**

\begin{enumerate}
\item Manual: Recommendations only
\item Partially Automated: Auto placement, manual migration
\item Fully Automated: Auto placement and migration
\end{enumerate}

### 5.2 DRS Log Files

**Primary DRS Logs:**

# vCenter side (VCSA)
/var/log/vmware/vpxd/vpxd.log    # Main vCenter log
/var/log/vmware/vpxd/vpxd-profiler.log  # DRS performance

# ESXi side
/var/log/hostd.log    # Host daemon includes DRS operations
/var/log/vpxa.log     # vCenter agent on ESXi

### 5.3 DRS Troubleshooting Commands

**Check DRS Status via PowerCLI:**

# Connect to vCenter
Connect-VIServer vcenter.domain.com

# Get cluster DRS configuration
Get-Cluster "Production" | Select Name, DrsEnabled, DrsAutomationLevel

# Get DRS recommendations
Get-Cluster "Production" | Get-DrsRecommendation

# Apply DRS recommendations
Get-Cluster "Production" | Get-DrsRecommendation | Apply-DrsRecommendation

# Get DRS rules
Get-Cluster "Production" | Get-DrsRule

# Check VM DRS settings
Get-VM "TestVM" | Select Name, DrsAutomationLevel

# Get DRS cluster group
Get-Cluster "Production" | Get-DrsClusterGroup

**Check DRS from vSphere Client:**

1. Navigate to Cluster $\rightarrow$ Monitor $\rightarrow$ vSphere DRS
2. Review DRS Faults and Recommendations tabs
3. Check DRS History for past actions

### 5.4 Common DRS Issues

\begin{table}
\begin{tabular}{|p{5cm}|p{9cm}|}
\hline
\textbf{Issue} & \textbf{Cause/Resolution} \\
\hline
DRS not generating recommendations & Cluster imbalance below threshold, check migration threshold setting \\
\hline
DRS recommendations not applied & Manual mode, VM automation level set to disabled \\
\hline
vMotion prerequisites not met & Networking, CPU compatibility, shared storage issues \\
\hline
Affinity rules violated & Conflicting rules, insufficient resources on target hosts \\
\hline
DRS showing cluster invalid & Host disconnected, EVC mode mismatch, configuration error \\
\hline
\end{tabular}
\caption{Common DRS Problems}
\end{table}

### 5.5 DRS Log Analysis

**Search for DRS Operations:**

# From vCenter VCSA shell
grep -i "drs" /var/log/vmware/vpxd/vpxd.log | tail -100

# Look for DRS invocations
grep "InvokeDrs" /var/log/vmware/vpxd/vpxd.log

# Check for DRS errors
grep -E "drs.*error|drs.*fail" /var/log/vmware/vpxd/vpxd.log

# DRS recommendation generation
grep "drs.*recommendation" /var/log/vmware/vpxd/vpxd.log

# From ESXi host
grep -i "relocate\|migrate" /var/log/vpxa.log

**Analyze DRS Decisions:**

# DRS invocation patterns in vpxd.log
# "ClusterComputeResource::InvokeDrs"
# "DRS generated N recommendations"
# "Applying recommendation: migrate VM_NAME to host"

# Check migration threshold
grep "migration threshold" /var/log/vmware/vpxd/vpxd.log

### 5.6 DRS Affinity Rules Troubleshooting

**List and Verify Rules:**

# Get all DRS rules
Get-Cluster "Production" | Get-DrsRule | 
    Select Name, Type, Enabled, @{N="VMs";E={$_.VMIds}}

# Check VM-to-VM affinity rules
Get-Cluster "Production" | Get-DrsRule -Type VMAntiAffinity

# Check VM-to-Host affinity rules
Get-Cluster "Production" | Get-DrsVMHostRule

**Identify Rule Conflicts:**

# From vpxd.log, search for rule violations
grep -i "rule.*violat\|constraint.*violat" /var/log/vmware/vpxd/vpxd.log

# Example patterns:
# "Cannot satisfy VM-Host affinity rule"
# "Anti-affinity rule prevents placement"

### 5.7 DRS Advanced Configuration

**DRS Settings to Check:**

\begin{itemize}
\item \textbf{Migration Threshold:} Conservative (5) to Aggressive (1)
\item \textbf{Predictive DRS:} Uses vRealize Operations metrics
\item \textbf{VM Distribution:} Even distribution setting
\item \textbf{CPU Over-Commitment:} Ratio limit
\item \textbf{Memory Over-Commitment:} Ratio limit
\end{itemize}

**Advanced DRS Options:**

# Set DRS automation level
Set-Cluster -Cluster "Production" -DrsAutomationLevel FullyAutomated

# Set migration threshold
Set-Cluster -Cluster "Production" -DrsMode FullyAutomated -DrsAggressiveness 3

# Disable DRS for specific VM
Get-VM "DatabaseVM" | Set-VMResourceConfiguration -DrsAutomationLevel Disabled

---

## 6. vMotion Troubleshooting

### 6.1 vMotion Prerequisites

**Requirements for Successful vMotion:**

\begin{itemize}
\item Shared storage accessible to source and destination hosts
\item Gigabit or faster network for vMotion
\item Compatible CPU families or EVC enabled
\item Same virtual switch names on source and destination
\item vMotion enabled on VMkernel interfaces
\item Proper licensing (vMotion feature)
\item No incompatible devices (local ISO, physical RDM in physical mode)
\end{itemize}

### 6.2 vMotion Log Files

**Key Log Locations:**

# ESXi Source Host
/var/log/hostd.log          # Main host daemon log
/var/log/vmkernel.log       # VMkernel operations
/var/log/vpxa.log           # vCenter agent

# ESXi Destination Host
/var/log/hostd.log
/var/log/vmkernel.log

# VM-specific log
/vmfs/volumes/<datastore>/<VM>/vmware.log

# vCenter Server (VCSA)
/var/log/vmware/vpxd/vpxd.log

### 6.3 Common vMotion Failures

\begin{table}
\begin{tabular}{|p{5cm}|p{9cm}|}
\hline
\textbf{Error} & \textbf{Cause/Resolution} \\
\hline
Timeout at 10\% or 14\% & Network connectivity issues, MTU mismatch, firewall blocking \\
\hline
Timeout at 20\% & Memory pre-copy phase timeout, high memory change rate \\
\hline
Timeout at 88\% & Final switchover timeout, storage latency \\
\hline
"Failed to receive migration" & Network configuration mismatch, VHV enable/disable mismatch \\
\hline
CPU compatibility check failed & EVC not enabled or incompatible CPU features \\
\hline
Network adapter error & Virtual switch or port group name mismatch \\
\hline
\end{tabular}
\caption{Common vMotion Errors}
\end{table}

### 6.4 vMotion Troubleshooting Commands

**Validate vMotion Configuration:**

# Check vMotion VMkernel interface
esxcli network ip interface list

# Verify vMotion enabled on interface
esxcfg-vmknic -l | grep -i vmotion

# Test vMotion network connectivity
vmkping -I vmk1 <destination_host_vmotion_ip>

# Test with large packets (MTU validation)
vmkping -s 8972 -d -I vmk1 <destination_host_vmotion_ip>

# Check virtual switch configuration
esxcfg-vswitch -l

# Verify firewall rules
esxcli network firewall ruleset list | grep -i vmotion
esxcli network firewall ruleset set -e true -r vMotion

**CPU Compatibility Check:**

# Check EVC mode
vim-cmd hostsvc/hostsummary | grep -i evc

# View CPU features
grep -i vmx /proc/cpuinfo

# From vCenter PowerCLI
Get-Cluster | Select Name, EVCMode

**Storage Validation:**

# List datastores
esxcli storage filesystem list

# Check datastore accessibility
esxcli storage core path list

# Verify VMFS mount
df -h | grep vmfs

### 6.5 vMotion Log Analysis

**Search for vMotion Operations:**

# From source ESXi host
grep -i "vmotion\|relocate\|migrate" /var/log/hostd.log | tail -100

# Look for specific VM migration
grep "VM_NAME" /var/log/hostd.log | grep -i migrate

# Check vmkernel logs
grep -i "migrate" /var/log/vmkernel.log | tail -50

# VM-specific vMotion logs
grep -i "vmotion\|migrate" /vmfs/volumes/<datastore>/<VM>/vmware.log

**Find vMotion Operation ID:**

# From vCenter vpxd.log
grep "relocate" /var/log/vmware/vpxd/vpxd-*.log | grep BEGIN

# Output shows Operation ID (opID)
# Example: opID=jzlgfw8g-11824-auto-94h-h5:70003561

# Use Operation ID to trace entire migration
grep "jzlgfw8g-11824" /var/log/vmware/vpxd/vpxd-*.log

**Interpret vMotion Failure Messages:**

# Network timeout errors
grep "timeout.*network" /var/log/hostd.log

# Example patterns:
# "failed to connect to remote host"
# "timeout waiting for data"
# "network unreachable"

# Storage errors
grep -E "storage.*fail|disk.*error" /var/log/hostd.log

# Memory migration errors
grep -E "memory.*fail|precopy.*timeout" /var/log/vmkernel.log

### 6.6 Advanced vMotion Troubleshooting

**Analyze vMotion Hang at Specific Percentage:**

**10% Hang:**
# Network connectivity/authentication issue
grep "authentication\|connect" /var/log/hostd.log | tail -20

# Check SSH connectivity between hosts
ssh root@<destination_host>

**14% Hang:**
# Resource allocation issue
grep "resource.*fail\|admission.*fail" /var/log/hostd.log

**20% Hang:**
# Memory pre-copy timeout
grep "memory.*dirty\|precopy" /var/log/vmkernel.log

# VM has high memory change rate
# Solution: Shutdown and cold migrate, or stun during switchover

**88% Hang:**
# Final switchover/cutover timeout
grep "switchover\|cutover" /var/log/vmkernel.log

# Storage latency during final sync
# Check storage performance
esxtop
# Press 'd' for disk view, check DAVG/cmd

**Detailed vMotion Tracing:**

# Enable verbose vMotion logging (ESXi)
esxcli system settings advanced set -o /Migrate/Enabled -i 1

# Set log level
esxcli system syslog config logger set --id=vmkernel --level=debug

# Attempt vMotion

# Review detailed logs
tail -f /var/log/vmkernel.log | grep -i migrate

# Disable verbose logging after troubleshooting
esxcli system settings advanced set -o /Migrate/Enabled -i 0
esxcli system syslog config logger set --id=vmkernel --level=info

**Network Packet Capture during vMotion:**

# Capture on vMotion VMkernel
pktcap-uw --vmk vmk1 --outfile /tmp/vmotion.pcap

# Attempt vMotion in another session

# Stop capture (Ctrl+C)

# Download pcap file for analysis
scp /tmp/vmotion.pcap user@workstation:/path/

### 6.7 vMotion Best Practices

\begin{itemize}
\item Use dedicated 10GbE or faster network for vMotion
\item Enable Jumbo Frames (MTU 9000) on vMotion network
\item Configure multiple vMotion VMkernel adapters for bandwidth aggregation
\item Enable EVC mode on cluster for maximum mobility
\item Use vMotion encryption when migrating sensitive workloads
\item Monitor vMotion performance using vCenter performance charts
\item Keep VMs with high memory change rate on same host or migrate during maintenance
\item Ensure consistent virtual switch naming across all hosts
\end{itemize}

---

## 7. Common Troubleshooting Commands Reference

### 7.1 VM Management Commands

# List all VMs
vim-cmd vmsvc/getallvms

# Power operations
vim-cmd vmsvc/power.on <VMID>
vim-cmd vmsvc/power.off <VMID>
vim-cmd vmsvc/power.shutdown <VMID>
vim-cmd vmsvc/power.reboot <VMID>
vim-cmd vmsvc/power.reset <VMID>

# VM information
vim-cmd vmsvc/get.summary <VMID>
vim-cmd vmsvc/get.config <VMID>
vim-cmd vmsvc/get.runtime <VMID>
vim-cmd vmsvc/get.networks <VMID>

# Snapshot operations
vim-cmd vmsvc/snapshot.create <VMID> "snapshot_name" "description"
vim-cmd vmsvc/snapshot.get <VMID>
vim-cmd vmsvc/snapshot.removeall <VMID>

# Register/Unregister VM
vim-cmd solo/registervm /vmfs/volumes/<datastore>/VM/VM.vmx
vim-cmd vmsvc/unregister <VMID>

# Reload VM configuration
vim-cmd vmsvc/reload <VMID>

### 7.2 Storage Commands

# List datastores
esxcli storage filesystem list

# Datastore browser
ls -lh /vmfs/volumes/

# Check VMFS volume
vmkfstools -P /vmfs/volumes/<datastore_name>

# Storage paths
esxcli storage core path list

# Storage adapters
esxcli storage core adapter list

# Device information
esxcli storage core device list

# Rescan storage
esxcli storage core adapter rescan --all

# VAAI status
esxcli storage core device vaai status get

### 7.3 Network Commands

# List VMkernel interfaces
esxcli network ip interface list
esxcfg-vmknic -l

# Virtual switches
esxcli network vswitch standard list
esxcfg-vswitch -l

# Port groups
esxcli network vswitch standard portgroup list

# Network connectivity test
vmkping -I vmk0 <IP_address>
vmkping -s 8972 -d -I vmk0 <IP_address>  # Jumbo frames test

# Firewall rules
esxcli network firewall ruleset list
esxcli network firewall ruleset set -e true -r <ruleset_name>

# TCP/IP stack
esxcli network ip connection list

### 7.4 System Information Commands

# ESXi version
vmware -vl
esxcli system version get

# System uptime
esxcli system stats uptime get

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

# System logs
tail -f /var/log/syslog.log
tail -f /var/log/vmkernel.log

### 7.5 Performance Monitoring Commands

# Real-time performance (esxtop)
esxtop

# esxtop in batch mode
esxtop -b -d 5 -n 12 > /tmp/esxtop.csv

# CPU statistics
esxcli vm process list
esxtop -c  # CPU view

# Memory statistics
esxtop -m  # Memory view

# Disk statistics
esxtop -d  # Disk view

# Network statistics
esxtop -n  # Network view

# VM resource usage
vsish -e cat /vm/<vmid>/mem/memoryUse

### 7.6 Cluster and Resource Management

# Cluster information via PowerCLI
Get-Cluster | Select Name, HAEnabled, DrsEnabled

# Host information
Get-VMHost | Select Name, ConnectionState, PowerState

# Resource pools
Get-ResourcePool | Select Name, CpuLimitMhz, MemLimitGB

# Move VM to resource pool
Move-VM -VM "VM_NAME" -Destination (Get-ResourcePool "PoolName")

# DRS recommendations
Get-Cluster | Get-DrsRecommendation | Apply-DrsRecommendation

# HA status
Get-Cluster | Select Name, HAEnabled, HAAdmissionControlEnabled

### 7.7 Backup and Recovery Commands

# Backup ESXi configuration
vim-cmd hostsvc/firmware/backup_config

# Export VM configuration
vim-cmd vmsvc/get.config <VMID> > /tmp/vm_config.txt

# Clone VMDK
vmkfstools -i source.vmdk destination.vmdk

# Clone with thin provisioning
vmkfstools -i source.vmdk -d thin destination.vmdk

# Extend VMDK
vmkfstools -X <new_size> VM.vmdk

### 7.8 Certificate and Security Commands

# View certificates
openssl x509 -in /etc/vmware/ssl/rui.crt -text -noout

# Certificate fingerprint
openssl x509 -in /etc/vmware/ssl/rui.crt -fingerprint -sha1 -noout

# Lockdown mode status
vim-cmd hostsvc/hostsummary | grep -i lockdown

# User list
esxcli system account list

# Password policy
esxcli system account policy get

---

## 8. Troubleshooting Workflow Summary

### 8.1 General Troubleshooting Approach

\begin{enumerate}
\item \textbf{Identify the Problem:}
  \begin{itemize}
  \item Collect symptoms and error messages
  \item Determine scope (single VM, host, cluster, vCenter)
  \item Note when issue started and any recent changes
  \end{itemize}

\item \textbf{Gather Information:}
  \begin{itemize}
  \item Review relevant log files
  \item Check vCenter events and alarms
  \item Review performance metrics
  \item Collect support bundles if needed
  \end{itemize}

\item \textbf{Analyze Data:}
  \begin{itemize}
  \item Search logs for error patterns
  \item Correlate timestamps across multiple logs
  \item Compare working vs non-working configurations
  \item Identify commonalities in affected objects
  \end{itemize}

\item \textbf{Implement Solution:}
  \begin{itemize}
  \item Test in isolated environment if possible
  \item Take backups before making changes
  \item Document changes made
  \item Monitor results after implementation
  \end{itemize}

\item \textbf{Verify Resolution:}
  \begin{itemize}
  \item Confirm issue is resolved
  \item Test related functionality
  \item Update documentation
  \item Schedule follow-up monitoring
  \end{itemize}
\end{enumerate}

### 8.2 Log Analysis Best Practices

\begin{itemize}
\item Always check timestamps - correlate events across multiple logs
\item Start with most recent entries and work backwards
\item Use grep with context flags (-A, -B, -C) for surrounding information
\item Save filtered output to files for detailed analysis
\item Create baseline logs from healthy systems for comparison
\item Enable debug logging only when needed and disable after troubleshooting
\item Collect logs before and after issue occurrence
\item Use log bundle collection for complex issues requiring vendor support
\end{itemize}

### 8.3 When to Engage VMware Support

Contact VMware/Broadcom Support when:

\begin{itemize}
\item Issue impacts production and cannot be resolved within SLA
\item Core vSphere services crash repeatedly
\item Data loss or corruption suspected
\item Hardware compatibility issues
\item Software bugs suspected (unexpected behavior)
\item Need assistance interpreting complex logs
\item Cluster-wide failures affecting business operations
\item Security incidents requiring vendor guidance
\end{itemize}

---

## 9. Quick Reference - Critical Commands

\begin{table}
\begin{tabular}{|p{7cm}|p{7cm}|}
\hline
\textbf{Task} & \textbf{Command} \\
\hline
View recent errors in vmkernel & grep -i error /var/log/vmkernel.log | tail -50 \\
\hline
Check all VM snapshots & vim-cmd vmsvc/get.snapshot <VMID> \\
\hline
Monitor HA events & tail -f /var/log/fdm.log \\
\hline
Test vMotion connectivity & vmkping -I vmk1 <dest\_IP> \\
\hline
List VMs with power state & vim-cmd vmsvc/getallvms \\
\hline
Check storage paths & esxcli storage core path list \\
\hline
Generate support bundle & vm-support \\
\hline
Restart management agents & /etc/init.d/hostd restart \\
\hline
View DRS recommendations & Get-DrsRecommendation (PowerCLI) \\
\hline
Check cluster HA status & Get-Cluster | Select HAEnabled \\
\hline
\end{tabular}
\caption{Quick Reference Commands}
\end{table}

---

## 10. Additional Resources

**VMware Knowledge Base:**
- https://knowledge.broadcom.com (Broadcom/VMware KB)
- Search for specific error messages and KB articles

**Log File References:**
- VMware vSphere 8.0 Troubleshooting Guide
- ESXi Configuration Guide
- vCenter Server Administration Guide

**Community Resources:**
- VMware Technology Network (VMTN) Communities
- Reddit r/vmware
- Yellow-Bricks.com (Duncan Epping's blog)

**Monitoring Tools:**
- vRealize Operations Manager
- vRealize Log Insight
- Grafana with telegraf for ESXi monitoring
- NAKIVO Backup & Replication with monitoring

**Training and Certification:**
- VMware vSphere: Troubleshooting Workshop
- VCAP-DCV Deploy certification
- vExpert community resources

---

## Document Version History

- Version 1.0 - November 20, 2025 - Initial creation
- Comprehensive troubleshooting guide covering snapshots, HA, DRS, and vMotion
- Includes detailed log analysis and command reference