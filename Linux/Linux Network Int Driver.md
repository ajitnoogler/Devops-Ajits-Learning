
### Scenario Summary

### ✅ Scenario Summary

- **Instance Type:** OCI Bare Metal  
- **NIC 1 (Cisco):** Routes to On-Prem (via DRG/FastConnect)  
- **NIC 2 (Broadcom):** Routes to Internet (IGW)  
- **Problem:** Intermittent packet drops on Cisco NIC only  
- **Impact:** On-prem connectivity affected (latency, retries)  
- **Suspicion:** Fleet-wide issue tied to Cisco NIC driver  

### Check Which Driver is in Use: 

$ ethtool -i ens33
driver: e1000
version: 6.8.0-51-generic
firmware-version: 
expansion-rom-version: 
bus-info: 0000:02:01.0
supports-statistics: yes
supports-test: yes
supports-eeprom-access: yes
supports-register-dump: yes
supports-priv-flags: no
leo@leo-Ansi:~$ 

### Check if Nics has Packet Drop:
$ ip -s link show
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 00:0c:29:89:20:c7 brd ff:ff:ff:ff:ff:ff
    RX:  bytes packets errors dropped  missed   mcast           
    1003428915  668640      0       0       0       0 
    TX:  bytes packets errors dropped carrier collsns           
       3276773   49145      0       0       0       0 
    altname enp2s1
    
$ netstat -i 
Kernel Interface table
Iface      MTU    RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
ens33     1500   668213      0      0 0         48830      0      0      0 BMRU
ens37     1500       81      0      0 0           107      0      0      0 BMRU
lo       65536      413      0      0 0           413      0      0      0 LRU


### Correlate with OS Kernel Logs

$ sudo dmesg | grep -i 'fail\|drop\|timeout\|nic\|cisco\|tx\|rx'
$ journalctl -k | grep -i <cisco_nic>

Look for:

NIC driver resets
Queue starvation
DMA or offload errors
PCIe link errors

### Monitor Real-Time Drops with Watch
$ watch -n 2 'ethtool -S ens33 | grep -i drop' 

Every 2.0s: ethtool -S ens33 | grep -i drop              leo-Ansi: Thu Jul 10 18:34:45 2025

     tx_dropped: 0
     dropped_smbus: 0

### Check:

rx_dropped
tx_dropped
rx_no_buffer
rx_errors
Use sar -n DEV 1 5 or iftop for more live tracking.

### Check Interface-Specific Routing
ip route get <on-prem-ip>


### Check OCI Console for Fleet-Wide Warning

In OCI Console:

Go to: Compute → Instances → Problematic Bare Metal Instance

Check "Console History" or "Work Requests"

Look for Known issues flagged with hardware or driver on Cisco NIC

### Final Steps & Escalation

| Action                                   | Purpose                                      |
| ---------------------------------------- | -------------------------------------------- |
| Save all logs and `ethtool -S`           | For TAC or Oracle support                    |
| Test with latest driver/firmware         | If allowed                                   |
| Open SR with Oracle + Cisco TAC          | Share: dmesg, driver info, packet loss stats |
| Mitigation: Move traffic to Broadcom NIC | Temporary workaround                         |

# Recommended Logs to Collect:

| Log / Output          | Command                     |                        |
| --------------------- | --------------------------- | ---------------------- |
| NIC stats             | `ip -s link`, `ethtool -S`  |                        |
| Driver/firmware       | `ethtool -i <nic>`          |                        |
| Kernel logs           | `dmesg`, `journalctl -k`    |                        |
| Routing               | `ip route get <on-prem IP>` |                        |
| OCI Metrics/Flow Logs | Console or CLI              |                        |
| PCIe info             | \`lspci -nnk                | grep -A3 -i Ethernet\` |


### Run Continuous Ping Test to On-Prem:
$ ping <on-prem-IP> -i 0.2 -s 1400 -D

### TAC Support Tip
When filing Cisco TAC case:

Mention "ENIC driver"

Attach logs (or output)

Include test results across multiple instances

Ask for firmware/driver compatibility matrix

