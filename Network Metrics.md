
#### 📶 Networking Metrics Comparison

| 🧪 Metric       | 📘 Definition                                                                 | 📏 Unit              | 🎯 What It Affects                            | 🛠️ Tools to Measure              |
|----------------|--------------------------------------------------------------------------------|----------------------|-----------------------------------------------|----------------------------------|
| **Speed**       | How fast data can move over a link/interface                                 | Mbps / Gbps          | Device-to-device communication                | ethtool, NIC specs               |
| **Bandwidth**   | Maximum capacity of a link (what it can carry)                               | Mbps / Gbps          | Potential throughput, max possible transfer   | iperf, speedtest-cli             |
| **Throughput**  | Actual data successfully transferred per second                              | Mbps / Gbps          | Real performance experienced by users         | iperf, SNMP, Wireshark           |
| **Latency**     | Time it takes for a packet to travel from source to destination (RTT)        | ms (milliseconds)    | App responsiveness (VoIP, gaming, DB queries) | ping, traceroute, mtr            |
| **Jitter**      | Variation in latency between packets (delay inconsistency)                   | ms                   | Audio/video quality (VoIP, Zoom, Teams)       | ping, VoIP QoS test tools        |
| **Packet Loss** | Percentage of packets that fail to reach destination                         | %                    | Streaming, voice, retransmissions             | ping, iperf, smokeping           |
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

