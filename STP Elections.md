
Here’s a complete breakdown of the **Spanning Tree Protocol (STP) election process**, covering all the key steps and components involved in selecting the Root Bridge, Root Ports, Designated Ports, and blocking redundant links to prevent loops.

---

## 🔁 **STP Election Process Overview**

STP operates at **Layer 2** of the OSI model and is used to prevent **Layer 2 loops** in Ethernet networks with redundant paths.

### 🔧 Key Components

| Element             | Description                                                                 |
| ------------------- | --------------------------------------------------------------------------- |
| **Bridge ID (BID)** | 8-byte field: 2-byte Bridge Priority + 6-byte MAC address                   |
| **BPDU**            | Bridge Protocol Data Unit used to exchange STP information between switches |
| **Root Bridge**     | Central switch elected by the lowest Bridge ID                              |
| **Root Port (RP)**  | Port with the best path to Root Bridge (one per non-root switch)            |
| **Designated Port** | Port forwarding for each segment, elected per link                          |
| **Blocked Port**    | Any port not elected RP or DP; used to break loops                          |

---

### ⚙️ **Step-by-Step STP Election Process**

#### 🔹 Step 1: **Root Bridge Election**

* All switches assume themselves as Root initially and send BPDUs with their own BID.
* Switch with **lowest Bridge ID** becomes the Root Bridge.

📘 **Bridge ID = Priority (default 32768) + MAC address**

* If priorities are the same, the lowest MAC address wins.

**🧪 Example:**

* SW1: 32768:00-14-AA-11-11-11
* SW2: 32768:00-14-AA-11-11-22
* ➤ SW1 becomes Root Bridge

---

#### 🔹 Step 2: **Root Port Election (on Non-Root Switches)**

* Each non-root switch selects **one Root Port**: the port with the **lowest cumulative path cost** to reach the Root Bridge.
* Cost is based on bandwidth:

| Bandwidth | Cost |
| --------- | ---- |
| 10 Mbps   | 100  |
| 100 Mbps  | 19   |
| 1 Gbps    | 4    |
| 10 Gbps   | 2    |

✅ If multiple equal-cost paths:

1. Lower Sending BID wins
2. Lower Sending Port ID wins

---

#### 🔹 Step 3: **Designated Port Election**

* On each LAN segment, a **Designated Port** is elected to forward traffic **towards** the Root.
* Designated Port is on the switch with:

  1. **Lowest Path Cost** to Root
  2. **If tie**, lowest BID
  3. **If tie**, lowest Port ID

✅ The DP is **forwarding**, while other ports on the segment are **blocking**.

---

#### 🔹 Step 4: **Port States**

Each port transitions through the following states:

1. **Blocking** – Receives BPDUs only
2. **Listening** – Processes BPDUs, no data forwarding
3. **Learning** – Builds MAC table, still not forwarding
4. **Forwarding** – Forwards traffic
5. **Disabled** – Admin shut or failure

🕒 **STP Convergence Delay (default timers):**

* Listening: 15 sec
* Learning: 15 sec
* Total: \~30 seconds to converge

---

#### 🔹 Step 5: **Loop Prevention**

* Only one **Root Port** and one **Designated Port** per segment are in forwarding state.
* All others are put in **blocking** to eliminate Layer 2 loops.

---

#### 🖼️ Election Process Flow Summary

```text
[Start] → All Switches send BPDUs →
↓
Compare Bridge IDs → Elect Root Bridge →
↓
Non-root Switches calculate Root Port (Lowest Path Cost) →
↓
Per Segment: Elect Designated Port (Lowest Cost to Root) →
↓
Remaining Ports are Blocked
```

---

#### ✅ Sample Output (Debugging Commands)

On Cisco:

```bash
Switch# show spanning-tree
```

Sample Output:

```bash
Root ID    : 32768 (Priority) + 0014.AA11.1111 (MAC)
Root Port  : Gi0/1
Cost       : 4
Designated : Gi0/2
Blocked    : Gi0/3
```

---

#### 🔄 STP Types and Variants

| Type              | Description                              |
| ----------------- | ---------------------------------------- |
| **STP (802.1D)**  | Original version with slow convergence   |
| **RSTP (802.1w)** | Rapid STP with faster convergence (\~1s) |
| **MSTP (802.1s)** | Multiple STP instances per VLAN group    |
| **PVST+**         | Cisco proprietary; 1 instance per VLAN   |
| **Rapid PVST+**   | Cisco’s rapid version of PVST            |

---

Would you like this converted into a **network diagram**, **flowchart**, or **cheat sheet PDF** for quick revision or interview prep?
