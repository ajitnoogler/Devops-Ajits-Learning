

Great question! 🔐 Brute-force attempts on **SSH** are **very common**, and they show up in `/var/log/auth.log` (on Ubuntu/Debian) or `/var/log/secure` (on CentOS/RHEL).

Let’s walk through how a DevOps/cloud expert detects **SSH brute-force attacks** using log analysis.

============================================================================================================
## 🔎 Step-by-Step: Detect SSH Brute Force from Logs
============================================================================================================

### ✅ 1. Log File Location (depends on OS)

| OS            | SSH log file        |
| ------------- | ------------------- |
| Ubuntu/Debian | `/var/log/auth.log` |
| CentOS/RHEL   | `/var/log/secure`   |

============================================================================================================

### 🚨 2. Detect Failed SSH Login Attempts

```bash
grep 'Failed password' /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -nr | head
```

🔍 **Explanation:**

* Looks for `Failed password` entries.
* Extracts the IP address field (usually `$11`).
* Shows top IPs trying and failing to log in.

**Sample output:**

```
112 185.231.72.99
45  203.0.113.45
30  91.121.91.12
```

============================================================================================================

### 👤 3. Find Targeted Usernames

```bash
grep 'Failed password' /var/log/auth.log | awk '{print $(NF-5)}' | sort | uniq -c | sort -nr | head
```

🔍 Shows which usernames are being targeted (e.g. `root`, `admin`, `test`, etc.)

============================================================================================================

### ⏱️ 4. Detect Frequency by Time

```bash
grep 'Failed password' /var/log/auth.log | awk '{print $1, $2, $3}' | sort | uniq -c | sort -nr | head
```

🔍 Shows which timestamps had the highest number of failed attempts.

============================================================================================================

### 👣 5. See All Attempts From a Single IP

```bash
grep '185.231.72.99' /var/log/auth.log
```

🔍 Investigate behavior of a suspicious IP.

============================================================================================================

### ✅ 6. Find Successful Logins (check for compromise)

```bash
grep 'Accepted password' /var/log/auth.log
```

🔍 Helps you verify if any of the brute-force attempts actually succeeded.

============================================================================================================

## 🛡️ Bonus: Block Brute Force with `fail2ban`

Automatically block IPs after N failed attempts:

```bash
sudo apt install fail2ban   # Debian/Ubuntu
sudo systemctl enable --now fail2ban
```

Fail2Ban watches `/var/log/auth.log` and updates `iptables` or `firewalld` to block bad IPs.

---

## 📋 Summary Table

| Task                   | Command                                                                            |
| ---------------------- | ---------------------------------------------------------------------------------- |
| Top attacking IPs      | `grep 'Failed password' /var/log/auth.log \| awk '{print $11}' \| sort \| uniq -c` |
| Top attacked usernames | `awk '{print $(NF-5)}'` on same                                                    |
| Attempts per timestamp | `awk '{print $1, $2, $3}'`                                                         |
| All logs from IP       | `grep 'IP' /var/log/auth.log`                                                      |
| Successful logins      | `grep 'Accepted password' /var/log/auth.log`                                       |

---

## ✅ Real-World Tip

To **automate** SSH brute-force detection:

* Set up a cron job or `fail2ban`
* Alert on spikes using `logwatch` or `Grafana + Loki`
* Store logs in `ELK` or `Graylog` for dashboards & search

---

Let me know your Linux distro and I can tailor the commands or even give you a shell script to automate this 👨‍💻
