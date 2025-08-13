STP (Spanning Tree Protocol) and how it works:

---

#### 🌐 What is STP?

**STP (Spanning Tree Protocol)** is a **Layer 2 protocol** defined in **IEEE 802.1D** that **prevents loops** in Ethernet networks with redundant paths.

#### 🧠 Why do we need STP?

In a switched network, **loops can cause broadcast storms**, MAC table instability, and multiple frame copies — essentially bringing the network down.

So STP ensures there is **only one active path** between two network devices by **blocking redundant paths**.

---

#### ⚙️ How STP Works (Step-by-Step)

STP builds a **logical loop-free tree topology** (called a *spanning tree*) from the physical network. Here's how:

### 1. **Bridge ID (BID)**

Each switch (called a *bridge*) has a **Bridge ID**:

```
Bridge ID = Bridge Priority (default 32768) + MAC address
```

#### 2. **Root Bridge Election**

* STP elects one switch as the **Root Bridge** (lowest BID wins).
* All path calculations are made with respect to this root bridge.

---

#### 3. **Path Cost Calculation**

* STP calculates the **lowest-cost path** from each switch to the Root Bridge.
* Interface speeds define **path cost** (e.g., 100 Mbps = 19, 1 Gbps = 4).

---

#### 4. **Port Roles**

Each switch assigns **roles** to its ports:

| Port Role                | Description                                                                       |
| ------------------------ | --------------------------------------------------------------------------------- |
| **Root Port (RP)**       | The best port on a non-root switch to reach the root bridge. Only one per switch. |
| **Designated Port (DP)** | Best port on a segment to reach the root. One per segment.                        |
| **Blocked Port**         | Redundant port put into blocking state to prevent loops.                          |

---

#### 5. **Port States**

STP transitions ports through 5 states:

1. **Blocking** – No frame forwarding. Listens for BPDUs.
2. **Listening** – Prepares to participate in STP. No forwarding.
3. **Learning** – Starts building MAC table. No forwarding.
4. **Forwarding** – Active and forwarding frames.
5. **Disabled** – Administratively down.

🕒 STP takes about **30-50 seconds** to converge (move ports from blocking to forwarding).

---

#### 📡 What are BPDUs?

**Bridge Protocol Data Units (BPDUs)** are STP control messages used for:

* Root Bridge election
* Path cost calculations
* Maintaining STP topology

---

## 🔁 Example Scenario

```text
Switch1 <--> Switch2
   |           |
Switch3 -------+
```

* Redundant path exists.
* STP blocks one of the redundant links (say, Switch3 ↔ Switch2).
* If the active link fails, STP unblocks the backup link, restoring connectivity.

---

#### 🌱 STP Versions

| Protocol | IEEE Standard | Features                         |
| -------- | ------------- | -------------------------------- |
| **STP**  | 802.1D        | Original; 30–50s convergence     |
| **RSTP** | 802.1w        | Rapid STP; \~6s convergence      |
| **MSTP** | 802.1s        | Multiple STP instances for VLANs |

---

#### ✅ Summary

* **STP prevents loops** in Layer 2 networks.
* **Elects a root bridge** and disables redundant paths using port roles.
* Works by sending **BPDUs** between switches.
* Modern networks use **RSTP or MSTP** for faster convergence and VLAN awareness.

---
#### How STP works with **Root Bridge**, **Root Port**, **Designated Port**, and **Blocked Port** roles:

```
                          +---------------------+
                          |     Switch A        |
                          |   (Root Bridge)     |
                          |  BID: Lowest Value  |
                          +----------+----------+
                                     |
                             Root Port (RP)
                                     |
                    +----------------+----------------+
                    |                                 |
         Designated Port (DP)              Designated Port (DP)
              +---------+                      +---------+
              | Switch B|                      | Switch C|
              +----+----+                      +----+----+
                   |                                |
                   |                                |
                   |                                |
                   |                                |
               Gi0/1|                                |Gi0/1
                   |                                |
                   |                                |
             +-----v--------------------------------v-----+
             |                Switch D                   |
             |            (Non-Root Bridge)              |
             +-------------------------------------------+
                         |                       |
                         |                       |
             Gi0/2 (Blocked Port)        Gi0/3 (Forwarding Port)
                  ❌                        ✅

```

---

#### 🔎 Port Role Summary

| Switch     | Interface | Connects To       | STP Role       | State       |
|------------|-----------|-------------------|----------------|-------------|
| Switch A   | Gi0/x     | B & C             | Root Bridge    | Forwarding  |
| Switch B   | Gi0/1     | Switch D Gi0/2    | Designated     | Forwarding  |
| Switch C   | Gi0/1     | Switch D Gi0/3    | Designated     | Forwarding  |
| Switch D   | Gi0/3     | Switch C Gi0/1    | Root Port      | Forwarding  |
| Switch D   | Gi0/2     | Switch B Gi0/1    | Alternate Port | Blocked ❌   |

---

## ✅ Notes

- STP selects **one active forwarding path** toward the Root Bridge.
- **Switch D** receives BPDUs on both links and chooses the **lowest-cost** path as Root Port.
- The **other path is blocked** by STP to prevent Layer 2 loops.
- If the forwarding link fails, STP will **recalculate** and **unblock** the alternate.


---

#### 🔑 Legend:

* **\[Switch A]**: Root Bridge (elected based on lowest Bridge ID)
* **Root Port (RP)**: Best path from non-root switch to the Root Bridge
* **Designated Port (DP)**: Best path **to** the network segment
* **Blocked Port**: Redundant path blocked to prevent loops

---

#### 🔁 What Happens Here:

1. **Switch A** becomes the **Root Bridge**.
2. Every other switch calculates the shortest path **to the Root Bridge**.
3. **Only one path** per segment is **active** (Designated Port).
4. **Redundant paths** (like Switch B ↔ Switch D ↔ Switch C) are **blocked**.
5. If an active link fails, STP re-evaluates and **unblocks a backup port**.

---

#### Enhanced text-based STP diagram with interface names to make it more practical:

---

#### 🖧 STP Topology with Interface Names:

```
                       +--------------------------+
                       |  Switch A (Root Bridge)  |
                       |  BID: 32768.aaaa         |
                       +-----------+--------------+
                                   |
                             Gi0/1 (DP) ✅
                                   |
                                   |
                +-----------------+------------------+
                |                                    |
     Gi0/2 (RP) ✅                          Gi0/2 (RP) ✅
         +--------+                      +----------+--------+
         | Switch B|                      |   Switch C       |
         | BID: bbbb|                     |   BID: cccc      |
         +----+----+                      +----------+-------+
              |                                   |
     Gi0/1 (DP) ✅                         Gi0/1 (DP) ✅
              |                                   |
              |                                   |
              |                                   |
         +----v-----------------------------------v----+
         |                  Switch D                  |
         |                BID: dddd                   |
         +-------------------+-------------------------+
                         Gi0/3 ❌          Gi0/4 ✅
                       (Blocked)         (Forwarding)
                            |                  |
                    +-------v------+     +-----v------+
                    |  Loopback    |     |  Loopback  |
                    +--------------+     +------------+


```

---


---

## 🔍 Port Role Summary

| Switch     | Interface | Connects To       | Role           | State       |
|------------|-----------|-------------------|----------------|-------------|
| Switch A   | Gi0/1     | B & C             | Designated     | Forwarding ✅ |
| Switch B   | Gi0/2     | A                 | Root Port      | Forwarding ✅ |
| Switch B   | Gi0/1     | D Gi0/3           | Designated     | Forwarding ✅ |
| Switch C   | Gi0/2     | A                 | Root Port      | Forwarding ✅ |
| Switch C   | Gi0/1     | D Gi0/4           | Designated     | Forwarding ✅ |
| Switch D   | Gi0/3     | B                 | Alternate       | Blocked ❌   |
| Switch D   | Gi0/4     | C                 | Root Port       | Forwarding ✅ |

---

## 💡 Notes

- **Switch A** is the Root Bridge.
- **Switch D** receives BPDUs on both uplinks (from B and C).
- STP chooses **Gi0/4** as the **Root Port** (lower path cost).
- **Gi0/3** becomes an **Alternate Port** and is **Blocked** ❌ to prevent loops.


---

#### 💡 Use in a Lab (Example for GNS3 or Packet Tracer)

You can simulate this using 4 switches:

* Configure `spanning-tree vlan 10` on all.
* Lower the bridge priority on Switch A:

  ```bash
  SwitchA(config)# spanning-tree vlan 10 priority 4096
  ```
* Connect the interfaces as shown.
* Verify roles with:

  ```bash
  Switch# show spanning-tree vlan 10
  ```

---

#### Sample Configuration 

#### Following is a basic STP lab for VLAN 10 using 4 switches (Switch A to D). Switch A is manually set as the Root Bridge.


---

#### ⚙️ Switch Configuration

#### 🔹 Switch A (Root Bridge)

```bash
hostname SwitchA
spanning-tree vlan 10 priority 4096

interface GigabitEthernet0/1
 switchport mode trunk

interface GigabitEthernet0/2
 switchport mode trunk
```
---
#### 🔹 Switch B

```bash
hostname SwitchB

interface GigabitEthernet0/1
 switchport mode trunk

interface GigabitEthernet0/2
 switchport mode trunk
```

#### Switch C

```bash
hostname SwitchC

interface GigabitEthernet0/1
 switchport mode trunk

interface GigabitEthernet0/2
 switchport mode trunk
 
```

### Switch D

```bash
hostname SwitchD

interface GigabitEthernet0/1
 switchport mode trunk
interface GigabitEthernet0/2
 switchport mode trunk
interface GigabitEthernet0/3
 switchport mode trunk
interface GigabitEthernet0/4
 switchport mode trunk

```

#### Verification Commands

```bash
# On all switches
show spanning-tree vlan 10
show spanning-tree interface status
```

#### Optional Enhancements

- Enable PortFast + BPDU Guard on access ports:

```bash
interface range Gi0/x - y
 spanning-tree portfast
 spanning-tree bpduguard enable
```
---

#### ✅ Expected Behavior

- Switch A is the Root Bridge.

- Switches B & C have Root Ports toward A.

- Switch D connects to both B and C, so one of the uplinks will be blocked to prevent loops.

- STP maintains loop-free topology with automatic failover.
