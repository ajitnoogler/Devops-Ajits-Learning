
#### 🧰 STP Troubleshooting Playbook for TAC/NOC Teams

This playbook is designed for use by TAC (Technical Assistance Center) and NOC (Network Operations Center) teams to systematically troubleshoot Spanning Tree Protocol (STP) issues in enterprise networks.

---

#### 🎯 Common STP Symptoms & Impact

| Symptom                              | Possible Impact                               |
| ------------------------------------ | --------------------------------------------- |
| Intermittent network outages         | STP flaps, convergence issues                 |
| Broadcast storms or CPU spikes       | Layer 2 loop, failure to block redundant link |
| Ports err-disabled due to BPDU Guard | Unexpected BPDUs on PortFast ports            |
| Duplicate frames / MAC flapping      | Loops or improper STP states                  |
| High topology change counter         | Frequent reconvergence or instability         |

---

#### 🧭 Step-by-Step Troubleshooting Workflow

#### ✅ 1. **Initial Assessment**

* Collect impact scope: VLAN, location, devices
* Ask: Was there a recent config change?
* Check change logs / Syslog / SNMP alerts

#### 🧪 2. **Verify STP State and Root Bridge**

```bash
show spanning-tree vlan <X>
```

* Identify:

  * Who is the Root Bridge?
  * Which ports are Root/Designated/Blocked?
  * Are unexpected switches becoming root?

#### 🔍 3. **Look for Topology Changes**

```bash
show spanning-tree vlan <X> detail
```

* Look for "Number of topology changes"
* If increasing rapidly → flap or loop likely

#### 🔗 4. **Check Interface Role & State**

```bash
show spanning-tree interface <int> detail
```

* Is a port stuck in learning/listening?
* Is a designated port incorrectly blocking?

#### 🚨 5. **Err-Disabled or Blocked Ports**

```bash
show interfaces status err-disabled
show spanning-tree inconsistentports
```

* BPDU Guard? Inconsistency? Misconfigured trunks?

#### 🔥 6. **MAC Address Instability (Flaps)**

```bash
show mac address-table dynamic | include <MAC>
```

```bash
show logging | include MACFLAP
```

* Rapid MAC movement = loop

#### 🧠 7. **Check for Loops via Broadcast/CPU Symptoms**

```bash
show process cpu | include CPU
show platform hardware capacity forwarding
```

* Look for high CPU, dropped frames, unusual traffic patterns

#### ⚠️ 8. **BPDU Problems**

```bash
show spanning-tree vlan <X>
show cdp neighbors
```

* Are BPDUs being received on the correct ports?
* Are access ports receiving BPDUs? (possible loop)

---

#### 🧯 Common Root Causes

| Root Cause                         | Description                                 |
| ---------------------------------- | ------------------------------------------- |
| No STP Root priority configured    | Unexpected switch becomes Root Bridge       |
| Access port connected to switch/AP | Loop via unmanaged device                   |
| BPDU Guard triggered               | BPDU received on PortFast port              |
| Misconfigured EtherChannel         | Inconsistent config causes STP loop or drop |
| Broken cable / unidirectional link | One-way BPDU loss, loop isn't detected      |
| VLAN misalignment in trunks        | STP not active for affected VLAN            |

---

#### 🛠️ Recovery Actions

* Identify & disable the loop port

  ```bash
  shutdown interface <int>
  ```
* Change STP priority to control root

  ```bash
  spanning-tree vlan <X> priority 4096
  ```
* Enable BPDU Guard + Root Guard where needed
* Migrate to RSTP/MSTP if using legacy 802.1D

---

#### 📊 Proactive Hardening Checklist

| Recommendation                    | Purpose                                  | Configuration Example                                       | Verification Command                        |
| --------------------------------- | ---------------------------------------- | ----------------------------------------------------------- | ------------------------------------------- |
| **STP Root Priority Enforcement** | Ensures predictable root bridge          | `spanning-tree vlan <ID> priority 4096`                     | `show spanning-tree vlan <ID>`              |
| **BPDU Guard on edge ports**      | Prevents rogue loops                     | `spanning-tree bpduguard enable` on access interfaces       | `show running-config interface <int>`       |
| **Root Guard on access uplinks**  | Prevents upstream switches becoming root | `spanning-tree guard root` on distribution-to-access links  | `show spanning-tree interface <int> detail` |
| **PortFast only on edge ports**   | Avoids loop risk on switch interconnects | `spanning-tree portfast` on end-user ports only             | `show spanning-tree interface <int> detail` |
| **Use RSTP or MSTP**              | Faster convergence, better scalability   | `spanning-tree mode rapid-pvst` or `spanning-tree mode mst` | `show spanning-tree summary`                |


---

#### 📁 Documentation

* [x] Network topology diagram (L2 map)
* [x] Root Bridge list (per VLAN)
* [x] STP timers and version per switch
* [x] Policy for BPDU Guard / PortFast

---

#### 🧠 TAC/NOC Tip

> "Most STP issues start from the access layer. Always suspect unmanaged switches, rogue APs, or end-user loops first."

---
