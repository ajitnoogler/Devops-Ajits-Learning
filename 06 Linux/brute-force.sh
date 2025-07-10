#!/bin/bash

# Location of log files
SSH_LOG="/var/log/auth.log"    # Use /var/log/secure for CentOS/RHEL
HTTPD_LOG="/var/log/apache2/access.log"  # Or /var/log/httpd/access_log for RHEL

# Temp log output
OUTPUT_LOG="/tmp/bruteforce_monitor.log"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

# Thresholds
SSH_THRESHOLD=5
HTTP_THRESHOLD=10

# Function to detect SSH brute force
check_ssh_brute() {
    echo "[$DATE] Checking SSH brute-force attempts..." >> "$OUTPUT_LOG"
    grep "Failed password" $SSH_LOG | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | while read count ip
    do
        if [ "$count" -ge "$SSH_THRESHOLD" ]; then
            echo "[SSH] $ip has $count failed login attempts" >> "$OUTPUT_LOG"
        fi
    done
}

# Function to detect HTTP brute force
check_http_brute() {
    echo "[$DATE] Checking HTTP brute-force attempts..." >> "$OUTPUT_LOG"
    awk '{print $1}' $HTTPD_LOG | sort | uniq -c | sort -nr | while read count ip
    do
        if [ "$count" -ge "$HTTP_THRESHOLD" ]; then
            echo "[HTTP] $ip has $count access attempts" >> "$OUTPUT_LOG"
        fi
    done
}

# Run both checks
check_ssh_brute
check_http_brute

echo "[$DATE] Brute force check complete." >> "$OUTPUT_LOG"
