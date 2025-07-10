
# 🔄 ITIL: Problem Management vs Incident Management

Understanding the difference between **Incident Management** and **Problem Management** is essential for maintaining high service availability and long-term stability in IT operations.

---

## 🚨 What is Incident Management?

**Goal:**  
Restore **normal service operations as quickly as possible** and minimize business impact.

**Definition:**  
An **incident** is an unplanned interruption or degradation in the quality of an IT service.

**Examples:**
- A website is down
- A user can't access email
- Network slowness or printer not working

#### Key Activities:
- Incident detection and logging
- Initial diagnosis and categorization
- Escalation (if needed)
- Resolution and recovery
- Communication with users

**Focus:** **Fix fast** – often with a workaround

**Owner:** **Incident Manager**

---

#### 🧠 What is Problem Management?

**Goal:**  
Identify and eliminate the **root cause** of incidents and prevent recurrence.

**Definition:**  
A **problem** is the **underlying cause** of one or more incidents.

**Examples:**
- A failing disk causes repeated outages
- A misconfigured firewall rule causes intermittent network drops
- A memory leak in an application causes frequent crashes

### Key Activities:
- Problem detection (from recurring incidents, trend analysis)
- Root Cause Analysis (RCA)
- Workaround identification
- Change Request (if fix requires)
- Knowledge base documentation

**Focus:** **Fix forever** – resolve root cause

**Owner:** **Problem Manager**

---

#### 🔁 Comparison Table: Incident vs Problem Management

| Aspect                 | Incident Management                       | Problem Management                          |
|------------------------|--------------------------------------------|----------------------------------------------|
| **Objective**          | Restore service ASAP                       | Identify and eliminate root cause            |
| **Trigger**            | User reports an issue                      | Triggered by multiple/repeated incidents     |
| **Time Sensitivity**   | High – immediate business impact           | Medium/Low – long-term focus                 |
| **Approach**           | Reactive (resolve symptoms)                | Proactive & reactive (resolve root causes)   |
| **Output**             | Incident ticket resolution                 | Root cause analysis, known error record      |
| **Tools Used**         | ITSM portal, incident queues               | RCA tools, error logs, trend analytics       |
| **Responsible Role**   | Incident Manager / Support teams           | Problem Manager / Engineering                |
| **Resolution Type**    | Workaround or quick fix                    | Permanent fix or change implementation       |

---

#### 🔄 Real-world Example

#### Incident:
> Users can't log in to the web portal – IT support restarts the service. Problem temporarily solved.

#### Problem:
> Logs show that the issue recurs every Monday after patching. RCA finds a memory leak. Engineering team patches the application.

---

#### 📝 Summary

| Key Takeaway | Incident = "Restore now" | Problem = "Fix forever" |
|--------------|---------------------------|---------------------------|

---


#### 📌 Summary: Incident Management vs. Problem Management

| Aspect               | **Incident Management**                      | **Problem Management**                           |
| -------------------- | -------------------------------------------- | ------------------------------------------------ |
| **Purpose**          | Restore normal service operation **quickly** | Identify and **eliminate root cause** of issues  |
| **Focus**            | Short-term fix / workaround                  | Long-term resolution / prevention                |
| **Trigger**          | User reports, alerts, monitoring tools       | Recurring incidents, major incident analysis     |
| **Goal**             | Minimize **downtime and impact**             | Prevent future incidents / reduce recurrence     |
| **Time Sensitivity** | **High priority** – resolved ASAP            | Less time-sensitive – root cause analysis driven |
| **Output**           | Resolved incident or workaround implemented  | Root Cause Analysis (RCA), known error database  |
| **Example**          | Restarting a failed VM to restore access     | Investigating why the VM crashes every week      |
| **Handled by**       | L1/L2 support teams                          | L3 teams, engineering, or problem managers       |

#### 🧠 Key Differences

Incident Management = Firefighting

    “Get it working now.”

Problem Management = Fire prevention

    “Why did this happen and how do we stop it from happening again?”

#### 🛠️ Real-World Cloud Examples

### 🐧 Linux System Admin Scenarios: Incident vs. Problem Management + Commands

| **Scenario**                             | **Incident Management (Quick Fix)**        | **Problem Management (Root Cause Analysis)**             | 🔧 **Linux Command(s)**                                       |
|------------------------------------------|---------------------------------------------|----------------------------------------------------------|---------------------------------------------------------------|
| Web server goes down                     | Restart service, restore site               | Investigate recurring crashes in logs                    | `sudo systemctl restart apache2` or `nginx`                   |
| Network latency spikes to on-prem        | Reroute or restart interface                | Identify packet drop or driver issue                    | `ip route`, `ping`, `ethtool`, `traceroute`                  |
| Login failure to a critical application  | Clear sessions, unlock accounts             | Analyze auth flow and session timeouts                  | `sudo passwd user`, `last`, `journalctl -xe`                 |
| Root partition full (100%)               | Clean `/tmp`, delete logs                   | Fix logrotate config or backup retention logic           | `du -shx /*`, `find / -size +100M`, `logrotate -f`           |
| SSH login failure                        | Restart SSHD, unlock user                   | Review PAM logs, SELinux/AppArmor                        | `sudo systemctl restart sshd`, `tail -f /var/log/secure`     |
| High memory usage / OOM kill             | Kill memory-hog process                     | Analyze leaks, tune app                                 | `top`, `ps aux --sort=-%mem`, `kill -9 <PID>`                |
| CPU usage at 100%                        | Renice or kill process                      | Profile app, check threads                              | `top`, `htop`, `nice`, `renice`, `strace -p <PID>`           |
| File system I/O latency                  | Remount FS or restart NFS                   | Check block device or dmesg                             | `mount -o remount`, `iostat`, `dmesg | grep XFS`             |
| Time drift detected on VM                | Restart NTP                                 | Check peer sync, clocksource                            | `timedatectl`, `ntpq -p`, `chronyc sources`                  |
| Service port not listening               | Restart service                             | Check config, firewall                                  | `ss -tuln`, `systemctl status`, `netstat -tulpen`            |
| Cron job didn’t execute                  | Run job manually                            | Check cron syntax, perms                                | `crontab -e`, `cat /var/log/cron`, `run-parts --test`        |
| Kernel panic / VM crash                  | Reboot VM                                   | Analyze `vmcore`/`kdump`                                | `journalctl -k -b -1`, `ls /var/crash`, `crash vmcore`       |
| Firewall blocking app port               | Allow port temporarily                      | Set permanent rule in correct zone                      | `ufw allow 8080`, `firewall-cmd --add-port=8080/tcp`         |
| SELinux denial causing service failure   | Set SELinux to permissive                   | Analyze AVC logs, apply policy                          | `setenforce 0`, `ausearch -m avc`, `semanage`, `audit2allow` |
| Package manager fails (yum/apt)          | Clear cache or switch mirror                | Check repo config, GPG key                              | `yum clean all`, `apt update`, check `/etc/yum.repos.d/`     |
| Slow boot time                           | Disable unnecessary services                | Profile boot, systemd units                             | `systemd-analyze blame`, `systemctl disable <svc>`           |
| User cannot sudo                         | Add to sudo group                           | Fix sudoers file or plugin error                        | `usermod -aG wheel user`, `visudo`, `groups user`            |
| High zombie process count                | Reboot or kill parent                       | Fix parent signal handler                               | `ps aux | grep Z`, `pstree -p`, `strace -p <PID>`             |
| NIC goes down or disappears              | Reload NIC driver                           | Check udev rules, kernel modules                        | `ip link set <nic> up`, `modprobe -r <driver>; modprobe <driver>` |
| Log rotation not happening               | Force logrotate manually                    | Fix config path, cron triggers                          | `logrotate -f /etc/logrotate.conf`, `cat /etc/cron*`         |


#### Network Incident vs. Problem Management

| **Scenario**                                              | **Incident Management (Quick Fix)**              | **Problem Management (Root Cause Analysis)**                                                |
| --------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| **BGP session down between edge routers**                 | Clear BGP neighbor, restore route advertisements | Analyze flapping, MTU mismatch, timer mismatches, or ACLs blocking TCP 179                  |
| **Interface on switch/router flapping**                   | Shut/no shut the interface or migrate to backup  | Investigate cable faults, faulty transceivers, or duplex mismatches                         |
| **High CRC errors on access port**                        | Change patch cable or switch port                | Determine if there's electromagnetic interference, aging cables, or faulty NIC              |
| **STP loop detected in access layer**                     | Disable suspected interface, restore network     | Investigate unauthorized switches, BPDU filter misconfig, or STP misalignment               |
| **HSRP/VRRP failover triggered**                          | Re-enable primary router or move VIP manually    | Investigate interface tracking, high CPU, or preempt misconfig                              |
| **User can't access internal network resource**           | Reassign IP, flush DNS or restart DHCP client    | Investigate duplicate IP, DHCP scope exhaustion, or VLAN misassignment                      |
| **WAN link experiencing high latency**                    | Reroute traffic via backup MPLS/VPN circuit      | Analyze QoS policy, carrier issues, or congestion at the CPE device                         |
| **IP phone registering intermittently**                   | Restart phone or reset PoE port                  | Investigate VLAN mismatch, DHCP option 150 TFTP config download issue, or switch firmware bug|
| **Firewall denying outbound internet traffic**            | Temporarily allow IP/port in ACL or NAT          | Investigate policy group misassignment, NAT overload issue, or IPS signature false positive |
| **Access switch not reachable from core**                 | Use OOB or physically restart                    | Investigate Spanning Tree blockage, trunk misconfig, or dead supervisor module              |
| **SNMP monitoring alerts for high interface utilization** | Apply QoS or increase bandwidth                  | Investigate excessive broadcast/multicast traffic, or L2 loop                               |
| **NTP sync broken on routers/firewalls**                  | Set time manually, reconfigure peer              | Investigate firewall port blocks (UDP 123), wrong NTP server, or drift threshold            |
| **Dynamic routing not propagating prefixes**              | Clear OSPF/BGP sessions                          | Analyze route filtering, summarization, or RIB-to-FIB failure                               |

