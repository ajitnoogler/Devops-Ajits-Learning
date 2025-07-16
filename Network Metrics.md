
#### 📶 Networking Metrics Comparison

| 🧪 Metric       | 📘 Definition                                                                 | 📏 Unit              | 🎯 What It Affects                            | 🛠️ Tools to Measure              |
|----------------|--------------------------------------------------------------------------------|----------------------|-----------------------------------------------|----------------------------------|
| **Speed**       | Maximum rate at which data can be transmitted over a network interface        | Mbps / Gbps          | Physical/network device capability            | ethtool, NIC specs               |
| **Bandwidth**   | Maximum capacity of a network link                                            | Mbps / Gbps          | Theoretical upper limit of throughput         | iperf, speedtest-cli             |
| **Throughput**  | Actual data successfully transmitted per second                               | Mbps / Gbps          | Real-world performance                        | iperf, SNMP, Wireshark           |
| **Latency**     | Time taken for a packet to travel from source to destination and back (RTT)  | ms (milliseconds)    | App responsiveness (VoIP, gaming, APIs)       | ping, traceroute, mtr            |
| **Delay**       | Time between sending a packet and its arrival at the destination (one-way)   | ms (milliseconds)    | Real-time communication, streaming            | OWAMP, traceroute, packet capture|
| **Jitter**      | Variation in packet delay (inconsistent latency)                              | ms                   | Call/video quality (VoIP, video meetings)     | ping, VoIP test tools            |
| **Packet Loss** | % of packets lost during transmission                                         | %                    | VoIP, retransmissions, video buffering        | iperf, ping, smokeping           |

```

---
```
#### ✅ Example Use Cases

| Scenario                  | Key Metrics to Watch         |
| ------------------------- | ---------------------------- |
| Video Conferencing (Zoom) | Latency, Jitter, Packet Loss |
| File Transfers (FTP/SCP)  | Throughput, Packet Loss      |
| Cloud Gaming              | Latency, Jitter, Bandwidth   |
| VoIP Calling              | Jitter, Packet Loss, Latency |
| Speed Troubleshooting     | Bandwidth vs Throughput      |

```
---

