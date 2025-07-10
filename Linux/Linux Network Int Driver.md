
### Scenario Summary

### ✅ Scenario Summary

- **Instance Type:** OCI Bare Metal  
- **NIC 1 (Cisco):** Routes to On-Prem (via DRG/FastConnect)  
- **NIC 2 (Broadcom):** Routes to Internet (IGW)  
- **Problem:** Intermittent packet drops on Cisco NIC only  
- **Impact:** On-prem connectivity affected (latency, retries)  
- **Suspicion:** Fleet-wide issue tied to Cisco NIC driver  

## 🖧 Linux NIC Troubleshooting Cheat Sheet

---

### ✅ Check Which Driver is in Use

```bash
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
```

---

### 📉 Check if NICs Have Packet Drop

```bash
$ ip -s link show
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 00:0c:29:89:20:c7 brd ff:ff:ff:ff:ff:ff
    RX:  bytes packets errors dropped  missed   mcast           
    1003428915  668640      0       0       0       0 
    TX:  bytes packets errors dropped carrier collsns           
       3276773   49145      0       0       0       0 
    altname enp2s1
```

---

### 📊 Network Interface Stats (Drop/Error Summary)

```bash
$ netstat -i 
Kernel Interface table
Iface      MTU    RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
ens33     1500   668213      0      0 0         48830      0      0      0 BMRU
ens37     1500       81      0      0 0           107      0      0      0 BMRU
lo       65536      413      0      0 0           413      0      0      0 LRU
```

---

### 🧠 Notes

- `ethtool -i <iface>` → Shows NIC driver and features.
- `ip -s link show` → Displays NIC-level RX/TX stats including **packet drops**.
- `netstat -i` → Summarized view of all interfaces with errors/drops.

---

### Correlate with OS Kernel Logs
```bash

$ sudo dmesg | grep -i 'fail\|drop\|timeout\|nic\|cisco\|tx\|rx'

[   24.012345] enic 0000:3b:00.0 ens3: firmware version 3.2.115.0
[   25.126789] enic 0000:3b:00.0 ens3: TX timeout - resetting interface
[   25.127001] enic 0000:3b:00.0 ens3: TX ring stalled, resetting NIC
[   25.129334] enic 0000:3b:00.0 ens3: Reset complete
[   26.421553] enic 0000:3b:00.0 ens3: Link down
[   26.522201] enic 0000:3b:00.0 ens3: Link up
[   50.553229] enic 0000:3b:00.0 ens3: RX descriptor error: dropped packet
[   50.553811] enic 0000:3b:00.0 ens3: Hardware RX buffer allocation failed
[  120.789001] enic 0000:3b:00.0 ens3: Multiple TX failures detected
[  121.001256] enic 0000:3b:00.0 ens3: Firmware did not respond in time
[  121.004721] enic 0000:3b:00.0 ens3: PCIe correctable error detected
```

```bash
$ journalctl -k | grep -i <cisco_nic>

Jul 10 11:24:05 oci-bm kernel: enic 0000:3b:00.0 ens3: TX timeout - resetting interface
Jul 10 11:24:05 oci-bm kernel: enic 0000:3b:00.0 ens3: TX ring stalled, resetting NIC
Jul 10 11:24:05 oci-bm kernel: enic 0000:3b:00.0 ens3: Reset complete
Jul 10 11:25:45 oci-bm kernel: enic 0000:3b:00.0 ens3: Link down
Jul 10 11:25:46 oci-bm kernel: enic 0000:3b:00.0 ens3: Link up
Jul 10 11:28:12 oci-bm kernel: enic 0000:3b:00.0 ens3: RX descriptor error: dropped packet
Jul 10 11:28:12 oci-bm kernel: enic 0000:3b:00.0 ens3: Hardware RX buffer allocation failed
Jul 10 11:30:00 oci-bm kernel: enic 0000:3b:00.0 ens3: Firmware did not respond in time
Jul 10 11:30:01 oci-bm kernel: enic 0000:3b:00.0 ens3: PCIe correctable error detected

```

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

Mention "ENIC driver" // ethtool -i ens33

Attach logs (or output) // dmesg and journalctl logs

Include test results across multiple instances

Ask for firmware/driver compatibility matrix

