Awesome! Here's a **real-world automation script** to detect brute-force SSH attacks from `/var/log/auth.log` (Debian/Ubuntu) or `/var/log/secure` (RHEL/CentOS), along with **alerts, blocking options, and reporting**.

======================================================================================================================

## ✅ Overview: What This Script Does

* ✅ Detects brute-force IPs from failed SSH logins
* ✅ Finds usernames being attacked
* ✅ Optionally blocks those IPs using `iptables` or `firewalld`
* ✅ Sends daily report to a file or via email
* ✅ Can run via `cron` every hour or daily

======================================================================================================================

## 📜 Script: `ssh_bruteforce_monitor.sh`

```bash

#!/bin/bash

# 📂 Log file location
LOG_FILE="/var/log/auth.log"
[ -f /var/log/secure ] && LOG_FILE="/var/log/secure"

# 📁 Output report
REPORT="/var/log/ssh_bruteforce_report_$(date +%F).txt"
MAX_FAILED=10   # Threshold for action
BAN_MODE=false  # Set true to block IPs

echo "🛡️ SSH Brute-force Report - $(date)" > "$REPORT"
echo "Log File: $LOG_FILE" >> "$REPORT"
echo "----------------------------------------" >> "$REPORT"

# 🔎 Find top attacking IPs
echo "🔍 Top IPs with failed login attempts:" >> "$REPORT"
grep "Failed password" "$LOG_FILE" | awk '{print $(NF)}' | sort | uniq -c | sort -nr | head >> "$REPORT"

# 👤 Usernames being attacked
echo -e "\n👤 Top usernames being attacked:" >> "$REPORT"
grep "Failed password" "$LOG_FILE" | awk '{print $(NF-5)}' | sort | uniq -c | sort -nr | head >> "$REPORT"

# ⏱ Failed attempts per timestamp
echo -e "\n⏱ Failed attempts by timestamp:" >> "$REPORT"
grep "Failed password" "$LOG_FILE" | awk '{print $1, $2, $3}' | sort | uniq -c | sort -nr | head >> "$REPORT"

# 🚫 Optional: Ban IPs exceeding MAX_FAILED
if $BAN_MODE; then
    echo -e "\n🚫 Blocking IPs with more than $MAX_FAILED failed attempts:" >> "$REPORT"
    grep "Failed password" "$LOG_FILE" | awk '{print $(NF)}' | sort | uniq -c | awk -v max="$MAX_FAILED" '$1 > max {print $2}' | while read ip; do
        if ! iptables -L -n | grep -q "$ip"; then
            iptables -A INPUT -s "$ip" -j DROP
            echo "Blocked IP: $ip" >> "$REPORT"
        fi
    done
fi

# 📧 Optional: Email report (configure mailx or postfix)
# mail -s "SSH Brute Force Report - $(hostname)" you@example.com < "$REPORT"
```

======================================================================================================================

## ⚙️ Setup

1. **Save the script**

   ```bash
   sudo nano /usr/local/bin/ssh_bruteforce_monitor.sh
   chmod +x /usr/local/bin/ssh_bruteforce_monitor.sh
   ```

2. **(Optional) Enable banning**
   Set `BAN_MODE=true` in the script to **automatically block IPs** via `iptables`.

3. **(Optional) Cron job**
   Add to crontab for hourly or daily monitoring:

   ```bash
   crontab -e
   ```

   Example daily at 11PM:

   ```
   0 23 * * * /usr/local/bin/ssh_bruteforce_monitor.sh
   ```

======================================================================================================================

## 🛡️ Bonus: Fail2Ban (Easier Long-Term Solution)

```bash
sudo apt install fail2ban  # Ubuntu/Debian
sudo systemctl enable --now fail2ban
```

Fail2ban watches `/var/log/auth.log`, detects brute-force, and automatically blocks bad IPs with `iptables` or `firewalld`.

Custom jail for SSH (optional):

```bash
sudo nano /etc/fail2ban/jail.local
```

```ini
[sshd]
enabled = true
port    = ssh
filter  = sshd
logpath = /var/log/auth.log
maxretry = 5
findtime = 600
bantime = 86400
```

Then restart:

```bash
sudo systemctl restart fail2ban
```

======================================================================================================================

## ✅ Output Sample (Report)

```
🛡️ SSH Brute-force Report - 2025-07-06
Log File: /var/log/auth.log
----------------------------------------

🔍 Top IPs with failed login attempts:
112 185.231.72.99
45 203.0.113.45
30 91.121.91.12

👤 Top usernames being attacked:
108 root
42 admin
15 test

⏱ Failed attempts by timestamp:
14 Jul 06 02:10
12 Jul 06 02:11
9  Jul 06 02:12

🚫 Blocking IPs with more than 10 failed attempts:
Blocked IP: 185.231.72.99
```

======================================================================================================================

Let me know if you'd like this integrated with:

* ✅ Slack alerts
* ✅ UFW or `firewalld`
* ✅ ELK/Graylog/Splunk
* ✅ JSON log support

Happy to tailor this for your environment!
