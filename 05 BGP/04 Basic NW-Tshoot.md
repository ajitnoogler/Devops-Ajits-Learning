

<img width="957" height="247" alt="image" src="https://github.com/user-attachments/assets/9a7ac4f4-6e87-49e8-8918-72b689496de8" />

<img width="1451" height="782" alt="image" src="https://github.com/user-attachments/assets/ac2997d8-50aa-4940-80f4-1848b4a8201c" />

<img width="1242" height="690" alt="image" src="https://github.com/user-attachments/assets/1dc15240-c2f2-4e14-a67b-1c7844cc2d28" />

<img width="1476" height="633" alt="image" src="https://github.com/user-attachments/assets/18a97e68-86b6-4681-922e-b42fd21eec16" />

<img width="1486" height="648" alt="image" src="https://github.com/user-attachments/assets/3eeee986-8809-4cd2-831e-f6be5091ff03" />

<img width="1495" height="783" alt="image" src="https://github.com/user-attachments/assets/6420e074-bf1e-470d-9281-a0135c8a0d35" />

<img width="1413" height="676" alt="image" src="https://github.com/user-attachments/assets/4d75f334-5ddd-4fee-80dd-ee27e35c49bc" />

<img width="1442" height="706" alt="image" src="https://github.com/user-attachments/assets/1bf062de-40d0-45dd-81c9-8eb4653be382" />

<img width="1452" height="727" alt="image" src="https://github.com/user-attachments/assets/a96356ed-da83-47d1-94f0-462c36286050" />

<img width="621" height="348" alt="image" src="https://github.com/user-attachments/assets/e96f4746-bf11-4f22-b7e6-1d9575a740b3" />

<img width="1461" height="672" alt="image" src="https://github.com/user-attachments/assets/91f0890f-9ca8-451f-963d-5887af8dbe7f" />

<img width="1462" height="631" alt="image" src="https://github.com/user-attachments/assets/4bf40ca2-eaf6-4b23-9d90-5e8f8b2d1881" />

<img width="1481" height="773" alt="image" src="https://github.com/user-attachments/assets/bcb562b8-fe94-4afb-81ab-703dbb87eb2a" />

<img width="1472" height="693" alt="image" src="https://github.com/user-attachments/assets/76aac431-fb3f-4f4e-a02c-a8f74e2b4877" />

<img width="1461" height="726" alt="image" src="https://github.com/user-attachments/assets/5b72a50b-3ff2-41de-9ced-488a40eebad6" />

<img width="1427" height="702" alt="image" src="https://github.com/user-attachments/assets/91ab53f3-88cb-406d-be11-9cec3990e49f" />

<img width="1451" height="668" alt="image" src="https://github.com/user-attachments/assets/1f5abb38-b22b-49a8-ac15-7dd214195de2" />


#### # 🚦 Network Throughput Troubleshooting Guide

**Definition:**  
Throughput is the actual rate of successful data transfer over a network path, typically measured in Mbps or Gbps. Poor throughput can result in slow downloads, app lag, backup failures, or degraded user experience.

---

## 🛠️ Common Causes of Throughput Issues

1. **High Latency or Jitter**
2. **Packet Loss**
3. **Congestion or Bufferbloat**
4. **Mismatched MTU or TCP MSS**
5. **QoS Misconfigurations**
6. **Interface Errors or Duplex Mismatch**
7. **Firewall or IPS/IDS Bottlenecks**
8. **TCP Window Size/Scaling Limitations**
9. **Encryption Overhead (IPSec/SSL VPN)**
10. **Rate Limiting, Policing, or Shaping**

---

## 🔍 Step-by-Step Troubleshooting Workflow

### 1. **Verify the Problem**
- Use tools like `iperf3`, `speedtest-cli`, `netperf`, or file copy benchmarks.
- Is it **point-to-point**, **user-specific**, **application-specific**, or **global**?

---

### 2. **Check Basic Connectivity**
```bash
ping <destination>         # Check basic reachability
traceroute <destination>   # Identify network path

---

#### 3. Measure Throughput with iperf3

# On Server:
iperf3 -s

# On Client:
iperf3 -c <server-IP> -t 10
iperf3 -c <server-IP> -P 4      # Test with 4 parallel streams

#### 📟 Sample Output with Visible Packet Loss:

```bash
iperf3 -c 192.168.100.1 -u -b 100M -t 10 -l 1470

Connecting to host 192.168.100.1, port 5201
[  5] local 192.168.1.10 port 59748 connected to 192.168.100.1 port 5201
[ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
[  5]   0.00-1.00   sec  11.9 MBytes  99.8 Mbits/sec  2.325 ms  525/8700 (6.0%)
[  5]   1.00-2.00   sec  11.7 MBytes  98.0 Mbits/sec  1.870 ms  420/8600 (4.8%)
[  5]   2.00-3.00   sec  11.5 MBytes  96.5 Mbits/sec  1.634 ms  278/8500 (3.3%)
[  5]   3.00-4.00   sec  11.6 MBytes  97.3 Mbits/sec  1.520 ms  172/8600 (2.0%)
[  5]   4.00-5.00   sec  11.8 MBytes  99.1 Mbits/sec  1.479 ms  86/8700  (0.9%)
[  5]   5.00-6.00   sec  11.9 MBytes  99.9 Mbits/sec  1.388 ms  30/8700  (0.3%)
[  5]   6.00-7.00   sec  11.9 MBytes  99.9 Mbits/sec  1.324 ms  12/8700  (0.1%)
[  5]   7.00-8.00   sec  11.9 MBytes  99.9 Mbits/sec  1.310 ms  5/8700   (0.05%)
[  5]   8.00-9.00   sec  11.9 MBytes  99.9 Mbits/sec  1.265 ms  3/8700   (0.03%)
[  5]   9.00-10.00  sec  11.9 MBytes  99.9 Mbits/sec  1.240 ms  2/8700   (0.02%)
- - - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
[  5]   0.00-10.00  sec  118 MBytes   99.1 Mbits/sec  1.59 ms   1533/86900 (1.8%)

iperf Done.
```

#### 🧠 Interpretation

| Metric                   | Value                      | Meaning                                                |
| ------------------------ | -------------------------- | ------------------------------------------------------ |
| **Lost/Total**           | `1533/86900 (1.8%)`        | 1.8% packet loss over 10 seconds                       |
| **Jitter**               | `1.59 ms average`          | Relatively stable, good for VoIP/UDP despite some loss |
| **Early intervals loss** | Up to 6% in first 1 second | Initial congestion or buffer adaptation                |
| **Later intervals**      | Drops decline to <0.05%    | Network stabilizes, buffer tuning kicks in             |

---

#### 4. Check for Packet Loss, Latency, and Jitter
```bash

$ mtr -rwzbc100 8.8.8.8
Start: 2025-07-10T22:20:01+0530
HOST: test-host.local       Loss%   Snt   Last   Avg  Best  Wrst StDev
  1.|-- 192.168.1.1          0.0%    100   0.6    0.7   0.5   1.2   0.2
  2.|-- 10.1.1.1             2.0%    100   2.1    2.3   1.9   3.6   0.3
  3.|-- 172.16.20.1          0.0%    100   4.2    4.4   3.9   5.3   0.3
  4.|-- 100.72.0.1           5.0%    100  11.6   12.3  11.0  14.7   0.8
  5.|-- 8.8.8.8              0.0%    100  18.9   19.4  18.3  20.6   0.6

| Option  | Meaning                                                                |
| ------- | ---------------------------------------------------------------------- |
| `-r`    | Report mode: runs test, outputs a summary, and exits (non-interactive) |
| `-w`    | Wide output: includes full IP/hostname without truncation              |
| `-z`    | Show latency/jitter columns (Avg, Best, Worst, StdDev)                 |
| `-b`    | Show both hostnames and IP addresses                                   |
| `-c100` | Send **100 packets** to each hop (higher = more accurate stats)        |


ping -s 1400 <destination>      # Check for fragmentation or MTU issues

$ ping -s 1400 -M do 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 1400(1428) bytes of data.
From 192.168.1.1 icmp_seq=1 Frag needed and DF set (mtu = 1400)
From 192.168.1.1 icmp_seq=2 Frag needed and DF set (mtu = 1400)
From 192.168.1.1 icmp_seq=3 Frag needed and DF set (mtu = 1400)
From 192.168.1.1 icmp_seq=4 Frag needed and DF set (mtu = 1400)

--- 8.8.8.8 ping statistics ---
4 packets transmitted, 0 received, +4 errors, 100% packet loss, time 3063ms

| Part      | Meaning                                                                 |
| --------- | ----------------------------------------------------------------------- |
| `ping`    | Sends ICMP Echo Requests to test connectivity and packet delivery.      |
| `-s 1400` | Set the **payload size** of the packet to 1400 bytes (without headers). |
| `-M do`   | **"Do not fragment"** the packet (set DF bit in IP header).             |
| `8.8.8.8` | The **destination IP address** (Google DNS in this case).               |

```
---

#### 5. Validate Interface & Duplex Settings

ethtool <interface>             # Linux
show interfaces status          # Cisco
show interfaces <int>          # Errors, drops, CRC, collisions

#### 6. Check MTU, MSS, and Fragmentation
Path MTU Discovery (PMTUD) may fail if ICMP is blocked. | Check TCP MSS Clamping on firewalls or VPN:
ping -M do -s 1472 <destination>   # Test MTU (for 1500 MTU with 28B ICMP overhead)


#### 7. Analyze with Packet Capture

Use tcpdump, Wireshark, or SPAN to inspect:

    Window size scaling

    Zero-window or retransmissions

    Duplicate ACKs or slow ACKs

    Application Layer slowdowns (HTTP, SMB)

tcpdump -i eth0 port 5201 -w throughput-test.pcap

#### 8. Firewall, IPS, or VPN Bottleneck

    Check if traffic is being inspected, decrypted, or rate-limited.

    Disable DPI temporarily or bypass inspection rules.

    Inspect CPU usage or session limits on firewalls.

#### 9. QoS, Shaping, and Policing

    Use show policy-map interface (Cisco) or tc qdisc (Linux).

    Check if bandwidth limits are enforced by:

        Class-based shaping

        Policing

        Fair-queue buffers (WRED)

#### 10. Check End-System Constraints

    TCP congestion window limits

    Antivirus or host firewall interference

    Disk I/O (especially during backup or large file transfers)

---

#### 🧪 Tools Summary

| Tool        | Purpose                              |
| ----------- | ------------------------------------ |
| `iperf3`    | Raw TCP/UDP throughput test          |
| `mtr`       | Latency & loss across hops           |
| `tcpdump`   | Packet capture                       |
| `ethtool`   | NIC diagnostics                      |
| `iftop`     | Live interface usage (Linux)         |
| `nload`     | Graphical interface throughput       |
| `netstat`   | TCP stats, retransmits, state checks |
| `Wireshark` | Deep packet analysis                 |

---

🧯 Real-World Tips

    For VPN throughput issues, check MSS, CPU usage on endpoints, and whether encryption offload is supported.

    In cloud environments, ensure instance types and virtual NICs support expected throughput (AWS ENA, OCI VF NIC).

    On WAN links, use WAN Optimization or TCP acceleration techniques (e.g., Riverbed, SD-WAN).
