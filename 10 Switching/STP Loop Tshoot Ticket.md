
### 🧰 STP Troubleshooting Playbook for TAC/NOC Teams

This playbook is designed for use by TAC (Technical Assistance Center) and NOC (Network Operations Center) teams to systematically troubleshoot Spanning Tree Protocol (STP) issues in enterprise networks.

---

### 🔍 STP Loop Detection & Isolation (Runbook with Examples)

### 🧠 Goal:

Identify the switch and specific port causing **L2 loop**, **excessive broadcast**, **MAC flapping**, or **STP reconvergence** in a 5-switch environment (Switches A, B, C, D, E).

---

#### 🔧 Step 1: Check Symptoms from Core Switch (Switch A)

**Command:**

```bash
SwitchA# show process cpu | include CPU
SwitchA# show interfaces | include input rate|output rate
```

**Sample Output:**

```
CPU utilization for five seconds: 98%/85%; one minute: 91%; five minutes: 87%
GigabitEthernet1/0/1: input rate 3000000 bits/sec, 5000 packets/sec
```

✅ CPU spike and high packet input → likely broadcast storm.

**Next:**

```bash
SwitchA# show logging | include STP|MACFLAP|LOOP
```

**Sample Output:**

```
%STP-2-LOOPGUARD_BLOCK: Loop guard blocking port Gi1/0/24 on VLAN0001.
%SW_MATM-4-MACFLAP_NOTIF: Host 0011.2233.4455 flapping between Gi1/0/23 and Gi1/0/24
```

---

#### 🧪 Step 2: Check STP Topology

**Command:**

```bash
SwitchA# show spanning-tree vlan 1
```

**Sample Output:**

```
Root ID    Priority    4096
           Address     0012.aaaa.bbbb
Bridge ID  Priority    32769
           Address     0023.bbbb.cccc
Gi1/0/24   Root FWD
Gi1/0/23   Designated FWD
```

✅ Observe roles. Unexpected "forwarding" on multiple redundant uplinks = red flag.

---

#### 🗺 Step 3: Monitor MAC Address Flapping

**Command:**

```bash
SwitchA# show mac address-table | include 0011.2233.4455
```

**Sample Output:**

```
0011.2233.4455 DYNAMIC Gi1/0/23
0011.2233.4455 DYNAMIC Gi1/0/24
```

✅ Flap detected on two ports. Track where they connect next.

---

#### 📊 Step 4: Find High Broadcast Interfaces

**Command:**

```bash
SwitchA# show interfaces counters errors
```

**Sample Output:**

```
Port        Broadcast    Multicast
Gi1/0/23    4294967295   0
Gi1/0/24    4294961000   0
```

✅ Massive broadcast count. Suspect loop from connected switch.

---

#### ♻️ Step 5: Topology Change Counter

**Command:**

```bash
SwitchA# show spanning-tree vlan 1 detail | include ieee|occurred
```

**Sample Output:**

```
Number of topology changes 2410 last change occurred 00:00:21 ago
```

✅ Frequent changes = loop or flapping

---

#### 🔌 Step 6: Trace the Source

**Top-Down Method:**

1. Switch A: Gi1/0/23 connects to Switch B
2. Switch B: Check interface stats and MAC flaps
3. Repeat till you reach:

   * Access switch
   * Port with massive MAC learning

**MAC Flood Check:**

```bash
SwitchC# show mac address-table dynamic | include Gi0/1
```

**Output:**

```
Hundreds of MACs learned on Gi0/1 → unmanaged switch, rogue AP, or loop
```

---

#### 🛡️ Step 7: Isolate the Port

**Command:**

```bash
SwitchC# configure terminal
SwitchC(config)# interface Gi0/1
SwitchC(config-if)# shutdown
```

**Observe:**

* CPU usage drops
* Broadcast count returns to normal
* Logs stop flapping

---

#### ✅ Step 8: Prevent Future Occurrences

**BPDU Guard & PortFast:**

```bash
interface range Gi1/0/1 - 48
 spanning-tree portfast
 spanning-tree bpduguard enable
```

**STP Root Priority:**

```bash
spanning-tree vlan 1 priority 4096
```

**Storm Control:**

```bash
interface range Gi1/0/1 - 48
 storm-control broadcast level 1.00 0.10
```

**Loop Guard / UDLD:**

```bash
spanning-tree guard loop
udld enable
```

---

#### 📂 Sample Tools for Monitoring & Alerts

#### 1. Cisco EEM Script

```tcl
event manager applet MAC_FLAP_DETECT
 event syslog pattern "MACFLAP_NOTIF"
 action 1.0 syslog msg "MAC FLAPPING DETECTED"
 action 2.0 cli command "enable"
 action 3.0 cli command "show mac address-table"
 action 4.0 cli command "show log | include MACFLAP"
```

#### 2. Enable SNMP Traps

```bash
snmp-server enable traps spanning-tree
snmp-server enable traps mac-notify
snmp-server host <syslog-server-ip> version 2c public
```

#### 3. NetFlow/sFlow

```bash
ip flow-export destination 10.10.10.1 9996
ip flow-export version 9
```

Use with: **ElastiFlow**, **ntopng**, **sFlow-RT**

#### 4. Syslog Correlation in ELK/Splunk

```sql
(stp OR macflap) AND source:SWITCH-A
```

---

#### 📈 Flowchart Summary (Text Format)

```
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
|  show cpu, interfaces      |
+-------------+--------------+
              |
              v
+----------------------------+
|  Step 2: Check STP Status  |
|  show spanning-tree vlan X |
+-------------+--------------+
              |
              v
+----------------+     +--------------------------+
| MAC Flap       |     | High Broadcast Interface |
| show mac       |     | show int counters        |
+-------+--------+     +-----------+--------------+
        |                          |
        v                          v
+------------------------+   +------------------------+
| Isolate Flap Interface |<->| Trace Downstream Path  |
+-----------+------------+   +------------+-----------+
            |                          |
            v                          v
  +--------------------------+  +-------------------------+
  | Disconnect suspect port  |  | CPU drop confirms loop  |
  +--------------------------+  +-------------------------+
            |
            v
  +--------------------------+
  | Apply Prevention:        |
  | - BPDU Guard             |
  | - Root Priority          |
  | - Storm Control          |
  +--------------------------+
```
---
