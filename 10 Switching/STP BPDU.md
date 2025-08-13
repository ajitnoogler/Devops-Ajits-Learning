
#### 📦 BPDU (Bridge Protocol Data Unit) – Contents Explained
BPDUs are the control messages exchanged by switches in an STP-enabled network to maintain the spanning tree and prevent loops.

#### There are two main types of BPDUs:

Configuration BPDU – used for STP elections (sent by Root and forwarded by others)

Topology Change Notification (TCN) BPDU – signals a topology change


#### 🧱 Fields in a Configuration BPDU

| **Field**            | **Size (Bytes)** | **Description**                                                   |
| -------------------- | ---------------- | ----------------------------------------------------------------- |
| **Protocol ID**      | 2                | Always `0x0000` for IEEE 802.1D                                   |
| **Protocol Version** | 1                | `0x00` for STP, `0x02` for RSTP                                   |
| **BPDU Type**        | 1                | `0x00` for Configuration BPDU, `0x80` for TCN BPDU                |
| **Flags**            | 1                | Includes topology change (TC) and proposal/ack flags in RSTP      |
| **Root Bridge ID**   | 8                | Priority + MAC address of Root Bridge                             |
| **Root Path Cost**   | 4                | Cumulative cost to reach Root from sender                         |
| **Sender Bridge ID** | 8                | Priority + MAC address of the transmitting bridge                 |
| **Port ID**          | 2                | Identifies the port on the sender bridge (Priority + Port Number) |
| **Message Age**      | 2                | Time since Root sent the original BPDU                            |
| **Max Age**          | 2                | Time before BPDU info is considered stale (default 20 sec)        |
| **Hello Time**       | 2                | Interval between BPDUs sent by Root (default 2 sec)               |
| **Forward Delay**    | 2                | Time in Listening and Learning states (default 15 sec each)       |

---

#### 🧪 Sample Breakdown of a BPDU

BPDU Type           : 0x00 (Configuration BPDU)
Root ID             : 32768 / 00:11:22:33:44:55
Root Path Cost      : 4
Sender Bridge ID    : 32768 / 00:11:22:33:44:66
Port ID             : 0x8002
Hello Time          : 2 sec
Max Age             : 20 sec
Forward Delay       : 15 sec
Flags               : 0x00

---

#### 📢 TCN BPDU (Topology Change Notification)

``` bash

| **Field**        | **Size** | **Description**   |
| ---------------- | -------- | ----------------- |
| Protocol ID      | 2        | Always `0x0000`   |
| Protocol Version | 1        | `0x00`            |
| BPDU Type        | 1        | `0x80` (TCN BPDU) |

```
---

#### 🔢 BPDU Types with Hex Codes

| **BPDU Type**                    | **Hex Code** | **Used In**                  | **Purpose**                                                            |
| -------------------------------- | ------------ | ---------------------------- | ---------------------------------------------------------------------- |
| **Configuration BPDU**           | `0x00`       | STP (802.1D)                 | Standard STP BPDU used for Root Bridge election, topology info         |
| **Topology Change Notification** | `0x80`       | STP (802.1D)                 | Sent by a switch when it detects a topology change                     |
| **RSTP/MSTP BPDU (Rapid BPDU)**  | `0x02`       | RSTP (802.1w), MSTP (802.1s) | Used by Rapid STP and MSTP, combines config and TCN into a single BPDU |

#### 🧾 BPDU Types with Hex Codes

| **BPDU Type Name**              | **Hex Code** | **Function**                                |
|---------------------------------|--------------|---------------------------------------------|
| Configuration BPDU              | `0x00`       | Root election, timers                       |
| Topology Change Notification    | `0x80`       | Topology change alert                       |
| RSTP/MSTP BPDU                  | `0x02`       | Fast convergence & multiple trees           |


---

####  🧩 BPDU Packet Format Diagram

```bash
+--------------------+----------------------+
| Protocol ID (2B)   | 0x0000               |
+--------------------+----------------------+
| Version ID (1B)    | 0x00 (STP)           |
+--------------------+----------------------+
| BPDU Type (1B)     | 0x00 (Config BPDU)   |
+--------------------+----------------------+
| Flags (1B)         | TC, Proposal, etc.   |
+--------------------+----------------------+
| Root Bridge ID     | 8B (Priority + MAC)  |
+--------------------+----------------------+
| Root Path Cost     | 4B                   |
+--------------------+----------------------+
| Sender Bridge ID   | 8B (Priority + MAC)  |
+--------------------+----------------------+
| Port ID            | 2B (Priority + Port) |
+--------------------+----------------------+
| Message Age        | 2B                   |
+--------------------+----------------------+
| Max Age            | 2B                   |
+--------------------+----------------------+
| Hello Time         | 2B                   |
+--------------------+----------------------+
| Forward Delay      | 2B                   |
+--------------------+----------------------+
```

#### 📸 🟦 Wireshark Sample: Configuration BPDU

```bash
Frame 1: 60 bytes on wire
Ethernet II
    Destination: 01:80:c2:00:00:00 (STP Multicast)
    Source:      00:11:22:33:44:55
    Type: 0x0026 (STP)
Spanning-Tree Protocol (BPDU)
    Protocol Identifier: 0x0000
    Protocol Version:    0 (IEEE 802.1D)
    BPDU Type:           0x00 (Configuration)
    Flags:               0x00
    Root Identifier:     Priority: 32768 / MAC: 00:11:22:33:44:55
    Root Path Cost:      0
    Bridge Identifier:   Priority: 32768 / MAC: 00:11:22:33:44:55
    Port Identifier:     0x8001
    Message Age:         0
    Max Age:             20
    Hello Time:          2
    Forward Delay:       15
```

---
