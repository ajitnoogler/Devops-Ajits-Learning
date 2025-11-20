This runbook covers common troubleshooting scenarios, step-by-step procedures, and detailed log analysis guidance for ESXi hosts, vCenter Server, virtual machines, clusters, networking, and storage. 

It is designed for IT administrators and engineers to quickly diagnose and resolve issues in a VMware environment.

***

# VMware vSphere Troubleshooting Runbook

This runbook provides structured troubleshooting procedures for common VMware vSphere issues. Each section includes actionable steps, key log files to analyze, and recommended commands for log analysis.

***

## Table of Contents

- [General Troubleshooting Methodology](#general-troubleshooting-methodology)
- [ESXi Host Issues](#esxi-host-issues)
- [Virtual Machine Issues](#virtual-machine-issues)
- [vCenter Server Issues](#vcenter-server-issues)
- [Cluster Issues](#cluster-issues)
- [Networking Issues](#networking-issues)
- [Storage Issues](#storage-issues)
- [Log Analysis Guide](#log-analysis-guide)
- [Exporting Support Bundles](#exporting-support-bundles)

***

## General Troubleshooting Methodology

A structured approach to troubleshooting ensures faster resolution and minimizes downtime.

### Steps to Follow

1. **Identify the Problem:** Gather symptoms, error messages, and affected components.
2. **Isolate the Scope:** Determine if the issue is host-wide, VM-specific, or cluster-wide.
3. **Check Logs:** Analyze relevant log files for error patterns and timestamps.
4. **Reproduce the Issue:** If possible, reproduce the issue to confirm the root cause.
5. **Apply Remediation:** Implement fixes based on log analysis and VMware best practices.
6. **Verify Resolution:** Confirm the issue is resolved and monitor for recurrence.
7. **Document:** Record the problem, root cause, and solution in a knowledge base.

***

## ESXi Host Issues

### Symptoms

- Host disconnected in vCenter
- Host unresponsive
- High CPU/memory usage
- Host fails to boot

### Troubleshooting Steps

1. **Check Host Status:**  
   - Use vSphere Client or ESXi Host Client to verify host status.
   - Check for alarms and events in vCenter.

2. **Review Key Logs:**  
   - `/var/log/vmkernel.log` – Kernel-level errors, hardware issues.
   - `/var/log/hostd.log` – Host management service errors.
   - `/var/log/vpxa.log` – vCenter agent communication errors.

3. **Commands for Analysis:**  
   ```bash
   tail -f /var/log/vmkernel.log | grep -i error
   tail -f /var/log/hostd.log | grep -i error
   tail -f /var/log/vpxa.log | grep -i error
   ```

4. **Check Resource Usage:**  
   - Use `esxtop` to monitor CPU, memory, and storage usage.
   - Press `c` for CPU, `m` for memory, and `d` for disk.

5. **Restart Management Agents:**  
   - In ESXi Shell:  
     ```bash
     /etc/init.d/hostd restart
     /etc/init.d/vpxa restart
     ```

***

## Virtual Machine Issues

### Symptoms

- VM fails to power on
- VM unresponsive
- VM performance degradation
- Snapshot creation failure

### Troubleshooting Steps

1. **Check VM Status:**  
   - Use vSphere Client to verify VM state and alarms.

2. **Review VM Logs:**  
   - `/vmfs/volumes/datastore_name/vm_name/vmware.log` – VM-specific events.

3. **Commands for Analysis:**  
   ```bash
   tail -f /vmfs/volumes/datastore_name/vm_name/vmware.log | grep -i error
   ```

4. **Check Host Resources:**  
   - Use `esxtop` to ensure host has sufficient resources.

5. **Power Cycle VM:**  
   - Try powering off and on the VM.

6. **Snapshot Issues:**  
   - Check for locked files or insufficient datastore space.

***

## vCenter Server Issues

### Symptoms

- vCenter service not starting
- vCenter unresponsive
- vCenter database errors

### Troubleshooting Steps

1. **Check vCenter Status:**  
   - Use vSphere Client or vCenter Server Appliance Management Interface.

2. **Review Key Logs:**  
   - `/var/log/vmware/vpxd/vpxd.log` – vCenter service errors.
   - `/var/log/vmware/vpostgres/postgresql-xx.log` – Database errors.

3. **Commands for Analysis:**  
   ```bash
   tail -f /var/log/vmware/vpxd/vpxd.log | grep -i error
   tail -f /var/log/vmware/vpostgres/postgresql-xx.log | grep -i error
   ```

4. **Restart vCenter Services:**  
   - In vCenter Server Appliance:  
     ```bash
     service-control --stop --all
     service-control --start --all
     ```

***

## Cluster Issues

### Symptoms

- Cluster partitioning
- HA failover issues
- DRS recommendations not applied

### Troubleshooting Steps

1. **Check Cluster Status:**  
   - Use vSphere Client to verify cluster health.

2. **Review Key Logs:**  
   - `/var/log/fdm.log` – HA cluster events.
   - `/var/log/vmkernel.log` – Cluster-related errors.

3. **Commands for Analysis:**  
   ```bash
   tail -f /var/log/fdm.log | grep -i error
   tail -f /var/log/vmkernel.log | grep -i error
   ```

4. **Check Network Connectivity:**  
   - Ensure heartbeat datastores are accessible.

***

## Networking Issues

### Symptoms

- VM network connectivity issues
- vMotion failures
- Network performance degradation

### Troubleshooting Steps

1. **Check Network Configuration:**  
   - Use vSphere Client to verify network settings.

2. **Review Key Logs:**  
   - `/var/log/vmkernel.log` – Network errors.
   - `/var/log/vobd.log` – Storage and network events.

3. **Commands for Analysis:**  
   ```bash
   tail -f /var/log/vmkernel.log | grep -i error
   esxcfg-vmknic -l
   esxtop
   ```

4. **Test Connectivity:**  
   - Use `ping` and `traceroute` from ESXi Shell.

***

## Storage Issues

### Symptoms

- Datastore inaccessible
- Storage performance degradation
- Disk I/O errors

### Troubleshooting Steps

1. **Check Datastore Status:**  
   - Use vSphere Client to verify datastore health.

2. **Review Key Logs:**  
   - `/var/log/vmkernel.log` – Storage errors.
   - `/var/log/vobd.log` – Storage subsystem errors.

3. **Commands for Analysis:**  
   ```bash
   tail -f /var/log/vmkernel.log | grep -i error
   tail -f /var/log/vobd.log | grep -i error
   ```

4. **Check Storage Path:**  
   - Use `esxcli storage vmfs extent list` to verify storage paths.

***

## Log Analysis Guide

### Key Log Files

| Log File                  | Purpose                                      | Location                                      |
|---------------------------|----------------------------------------------|-----------------------------------------------|
| vmkernel.log              | Kernel-level errors, hardware issues         | /var/log/vmkernel.log                         |
| hostd.log                 | Host management service errors               | /var/log/hostd.log                            |
| vpxa.log                  | vCenter agent communication errors           | /var/log/vpxa.log                             |
| vpxd.log                  | vCenter service errors                       | /var/log/vmware/vpxd/vpxd.log                 |
| vmware.log                | VM-specific events                           | /vmfs/volumes/datastore_name/vm_name/vmware.log |
| fdm.log                   | HA cluster events                            | /var/log/fdm.log                              |
| vobd.log                  | Storage and network events                   | /var/log/vobd.log                             |

### Log Analysis Commands

- **Filter for Errors:**  
  ```bash
  cat /var/log/vmkernel.log | grep -i error
  ```
- **Extract IP Addresses:**  
  ```bash
  cat /var/log/hostd.log | grep -E -o '([0-9]{1,3}\\.){3}[0-9]{1,3}'
  ```
- **Monitor Real-Time Logs:**  
  ```bash
  tail -f /var/log/vmkernel.log
  ```

***

## Exporting Support Bundles

### Steps to Export Logs

1. **vSphere Client:**  
   - Right-click ESXi host → Export System Logs → Select logs → Export.

2. **ESXi Shell:**  
   ```bash
   /usr/bin/vm-support
   ```

3. **vCenter Server Appliance:**  
   - Use vCenter Server Appliance Management Interface to download logs.

***

- This runbook provides a structured approach to troubleshooting VMware vSphere environments. 
- Regular log analysis and proactive monitoring are essential for maintaining stability and reliability. 
- Always document solutions and update the knowledge base for future reference.
