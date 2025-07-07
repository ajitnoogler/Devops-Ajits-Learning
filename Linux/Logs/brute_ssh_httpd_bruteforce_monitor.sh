#!/bin/bash

# ✅ Here's your unified brute-force detection script for both:
#    SSH log analysis (/var/log/auth.log)
#    HTTP login brute force (/var/log/apache2/access.log)
#        ✅ Optional auto-blocking via iptables or firewalld
#        ✅ Slack alerts
#        ✅ Generates a daily report (/var/log/bruteforce_report_<date>.txt)

# === CONFIGURATION ===
LOG_FILE_SSH="/var/log/auth.log"
LOG_FILE_HTTPD="/var/log/apache2/access.log"  # Or /var/log/httpd/access_log for RHEL
MAX_FAILED=10
BAN_MODE=true  # Set false to disable IP blocking
USE_FIREWALLD=false  # Set true if firewalld is used instead of iptables
SLACK_WEBHOOK="https://hooks.slack.com/services/XXXXX/YYYYY/ZZZZZ"
REPORT="/var/log/bruteforce_report_$(date +%F).txt"

# === HELPER FUNCTIONS ===
send_slack_alert() {
    local message="$1"
    [ -z "$SLACK_WEBHOOK" ] && return
    curl -X POST -H 'Content-type: application/json' \
        --data "{\"text\": \"\ud83d\udee1\ufe0f Brute Force Alert on $(hostname):\\n$message\"}" \
        "$SLACK_WEBHOOK" >/dev/null 2>&1
}

block_ip() {
    local ip="$1"
    if $USE_FIREWALLD; then
        firewall-cmd --permanent --add-rich-rule="rule family='ipv4' source address='$ip' port port=22 protocol=tcp reject"
        firewall-cmd --reload
    else
        iptables -C INPUT -s "$ip" -j DROP 2>/dev/null || iptables -A INPUT -s "$ip" -j DROP
    fi
    send_slack_alert "Blocked IP: $ip (Too many failed logins)"
    echo "Blocked IP: $ip" >> "$REPORT"
}

# === SSH LOG MONITORING ===
echo "\n\n=== SSH Brute-force Detection ($(date)) ===" > "$REPORT"
echo "Log File: $LOG_FILE_SSH" >> "$REPORT"
echo "----------------------------------------" >> "$REPORT"

awk '/Failed password/ {print $(NF)}' "$LOG_FILE_SSH" | sort | uniq -c | sort -nr | while read count ip; do
    echo "$count $ip" >> "$REPORT"
    if $BAN_MODE && [ "$count" -gt "$MAX_FAILED" ]; then
        block_ip "$ip"
    fi
done

echo -e "\nTop SSH Usernames Targeted:" >> "$REPORT"
grep 'Failed password' "$LOG_FILE_SSH" | awk '{print $(NF-5)}' | sort | uniq -c | sort -nr | head >> "$REPORT"

echo -e "\nAccepted SSH Logins (Check for compromise):" >> "$REPORT"
grep 'Accepted password' "$LOG_FILE_SSH" | tail -n 10 >> "$REPORT"

# === HTTPD LOG MONITORING ===
echo "\n\n=== HTTP Login Brute-force Detection ===" >> "$REPORT"
echo "Log File: $LOG_FILE_HTTPD" >> "$REPORT"
echo "----------------------------------------" >> "$REPORT"

grep 'POST /login' "$LOG_FILE_HTTPD" | awk '{print $1}' | sort | uniq -c | sort -nr | while read count ip; do
    echo "$count $ip" >> "$REPORT"
    if $BAN_MODE && [ "$count" -gt "$MAX_FAILED" ]; then
        block_ip "$ip"
    fi
    done

echo -e "\nSuspicious User-Agents on HTTP POST /login:" >> "$REPORT"
grep 'POST /login' "$LOG_FILE_HTTPD" | awk -F\" '{print $6}' | sort | uniq -c | sort -nr | head >> "$REPORT"

# === FINAL OUTPUT ===
echo -e "\n\n\ud83d\udcc4 Report written to: $REPORT"

# === OPTIONAL: Email report (requires mail utils) ===
# mail -s "Brute Force Report on $(hostname)" you@example.com < "$REPORT"

exit 0
