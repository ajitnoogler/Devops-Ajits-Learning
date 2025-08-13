
#### Step-by-Step STP Loop Detection & Isolation

Here is a step-by-step detailed guide to identify the looping port or broadcast source in a multi-switch 
(e.g., 5-switch) datacenter or enterprise environment where Spanning Tree Protocol (STP) is active or partially misconfigured.

---

#### 🧠 Goal:

Identify the switch and specific port causing **L2 loop**, **excessive broadcast**, **MAC flapping**, or **STP reconvergence** in a 5-switch environment (A, B, C, D, E).

---

#### 🛠️ Step-by-Step STP Loop Detection & Isolation

#### 🔍 Step 1: **Check Symptoms from Core Switch (Switch A)**

```bash
show process cpu | include CPU
show interfaces | include input rate|output rate
```

* Look for:

  * CPU spikes on control plane
  * Very high broadcast/multicast input/output rate

```bash
show logging | include STP|MACFLAP|LOOP
```

* Look for MAC flaps or STP topology changes

---

#### 🧪 Step 2: **Check STP Topology**

```bash
show spanning-tree vlan <X>
```

Do this **on each switch** (A, B, C, D, E) and observe:

* Who is the **Root Bridge**
* Port roles: Root, Designated, Blocked
* Ports that are **unexpectedly not blocking**

**Red Flag**: If two uplink ports are both forwarding but should not → possible loop!

---

#### 🧭 Step 3: **Monitor MAC Address Flapping**

```bash
show mac address-table | include <flapping MAC>
```

OR

```bash
show logging | include MACFLAP
```

* If the same MAC appears **on two different ports repeatedly**, that port pair is likely involved in a loop.

**TIP**: Run this on core and distribution switches.

---

#### 📈 Step 4: **Find Interfaces with Excessive Broadcasts**

```bash
show interfaces counters errors
```

Look for ports with high numbers in:

* **Broadcast** or **multicast input/output**
* **Storm-control drops** (if enabled)

---

#### 🔄 Step 5: **Check Topology Change Counter**

```bash
show spanning-tree detail | include ieee|occurr|from|to
```

Look for:

* Ports with **frequent topology changes**
* Identify **which switch** is generating them

---

#### 🔌 Step 6: **Manually Trace the Broadcast Source**

#### Option A: **Start from Core (Top-Down)**

1. Log into Core Switch A
2. Find interface with highest broadcast
3. Trace connected switch (e.g., Switch B)
4. On Switch B, repeat and check downstream interface

Continue till you find:

* End host or unmanaged switch causing excessive traffic

#### Option B: **Use MAC Table Flood**

```bash
show mac address-table dynamic | include <Interface>
```

Look for:

* Many MACs learned on an **access port** (abnormal)
* Likely: rogue switch, looped cable, or AP in bridge mode

---

#### 🧱 Step 7: **Physically or Logically Isolate Suspect Ports**

Once you've identified candidate ports:

```bash
interface <int>
shutdown
```

* Observe if:

  * CPU drops
  * Broadcast rate drops
  * MAC flaps stop

---

#### ✅ Step 8: **Prevent Future Occurrences**

* Enable **BPDU Guard** on all edge (access) ports:

  ```bash
  spanning-tree portfast
  spanning-tree bpduguard enable
  ```
* Set **Root Bridge Priority**:

  ```bash
  spanning-tree vlan <ID> priority 4096
  ```
* Enable **storm-control** on access interfaces:

  ```bash
  storm-control broadcast level 1.00 0.10
  ```
* Use **UDLD/Loop Guard** on fiber or redundant links.

---

#### 🧠 Pro Tips

* **Most loops originate in the access layer**, not the core.
* Loops may come from:

  * End-user plugging both ends of cable into wall/switch
  * Misconfigured AP in bridge mode
  * Unmanaged switch behind IP phone or printer

---

## 📁 Optional: Scripted Tools

If you have automation tools or telemetry:

* **Cisco EEM Scripts** or **SNMP Traps**
* **NetFlow/sFlow** to trace broadcast flood origin
* **Syslog correlation** for STP/macflap events

---

#### 📊 Text-Based Flowchart for STP Loop/Broadcast Storm Troubleshooting

                                +----------------------------+
                                |  Symptoms:                 |
                                |  - High CPU                |
                                |  - Broadcast storm         |
                                |  - MAC flapping            |
                                +-------------+--------------+
                                              |
                                              v
                                +----------------------------+
                                |  Step 1: Start at Core     |
                                |  Run:                      |
                                |  show cpu, interfaces      |
                                +-------------+--------------+
                                              |
                                              v
                                +----------------------------+
                                |  Step 2: Check STP Status  |
                                |  show spanning-tree vlan X |
                                |  Identify root, roles, TCN |
                                +-------------+--------------+
                                              |
                                              v
                     +------------------------+------------------------+
                     |                                                 |
                     v                                                 v
    +-----------------------------+                +--------------------------------+
    | MAC Flap Detection          |                | High Broadcast Interface       |
    | show mac | include FLAP     |                | show interfaces counters       |
    +-----------+-----------------+                +---------------+----------------+
                |                                                  |
                v                                                  v
    +-----------------------------+                    +------------------------------+
    | Isolate Flapping Interface  |<------------------->| Track Downstream Interface   |
    | shutdown <interface>        |                    | Check connected switch       |
    +-----------------------------+                    +--------------+---------------+
                                                                      |
                                                                      v
                                                      +------------------------------+
                                                      | Suspected End-Host or Port   |
                                                      | Disconnect & Verify CPU drop |
                                                      +--------------+---------------+
                                                                      |
                                                                      v
                                                      +------------------------------+
                                                      |  Step 3: Apply Prevention    |
                                                      |  - BPDU Guard                |
                                                      |  - PortFast on edge          |
                                                      |  - Storm-control             |
                                                      +------------------------------+
---

---

#### 🤖 Scripted Tools and Automation for Detection

---
### 1. **Cisco EEM Script to Detect MAC Flapping**

```tcl
event manager applet MAC_FLAP_DETECT
 event syslog pattern "MACFLAP_NOTIF"
 action 1.0 syslog msg "MAC FLAPPING DETECTED"
 action 2.0 cli command "enable"
 action 3.0 cli command "show mac address-table | include dynamic"
 action 4.0 cli command "show log | include MACFLAP"
 action 5.0 mail server 10.10.10.10 to netops@datacenter.local from router@core
```

---

#### 2. **Enable SNMP Traps for STP/MAC Events**

```bash
snmp-server enable traps spanning-tree
snmp-server enable traps mac-notify
snmp-server host <syslog-server-ip> version 2c public
```

Use this with a tool like **LibreNMS**, **SolarWinds**, or **NetBox + SNMP** to trigger alerts.

---

#### 3. **NetFlow/sFlow to Trace Source of Broadcast Storm**

✅ Export flow data to NMS:

```bash
ip flow-export destination 10.10.10.1 9996
ip flow-export version 9
```

✅ Use tools like:

* **ntopng**
* **ElastiFlow (ElasticStack-based)**
* **sFlow-RT**

→ Filter by:

* L2 Broadcast (MAC: `FF:FF:FF:FF:FF:FF`)
* Per-interface packet rates

---

#### 4. **Syslog Correlation for STP & MACFLAP**

Use **Graylog**, **ELK**, or **Splunk** to correlate:

* `MACFLAP_NOTIF`
* `Topology change notification`
* `STP BPDU Guard triggered`
* `Interface err-disabled`

Example Graylog query:

```sql
(stp OR macflap) AND source:SWITCH-A
```
---
