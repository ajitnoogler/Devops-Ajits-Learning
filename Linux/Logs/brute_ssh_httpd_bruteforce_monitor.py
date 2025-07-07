import re
import subprocess
import datetime
import os
import requests

# === CONFIGURATION ===
LOG_FILE_SSH = "/var/log/auth.log"
LOG_FILE_HTTPD = "/var/log/apache2/access.log"  # Or /var/log/httpd/access_log
MAX_FAILED = 10
BAN_MODE = True
USE_FIREWALLD = False
SLACK_WEBHOOK = "https://hooks.slack.com/services/XXXXX/YYYYY/ZZZZZ"
REPORT = f"/var/log/bruteforce_report_{datetime.date.today()}.txt"

# === HELPER FUNCTIONS ===
def send_slack_alert(message):
    if not SLACK_WEBHOOK:
        return
    data = {"text": f"🛡️ Brute Force Alert on {os.uname().nodename}:\n{message}"}
    try:
        requests.post(SLACK_WEBHOOK, json=data, timeout=5)
    except Exception:
        pass

def block_ip(ip):
    if USE_FIREWALLD:
        subprocess.run([
            "firewall-cmd", "--permanent",
            f"--add-rich-rule=rule family='ipv4' source address='{ip}' port port=22 protocol=tcp reject"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["firewall-cmd", "--reload"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        existing = subprocess.run(["iptables", "-C", "INPUT", "-s", ip, "-j", "DROP"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if existing.returncode != 0:
            subprocess.run(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
    send_slack_alert(f"Blocked IP: {ip} (Too many failed logins)")
    with open(REPORT, "a") as f:
        f.write(f"Blocked IP: {ip}\n")

# === SSH ANALYSIS ===
with open(REPORT, "w") as f:
    f.write(f"\n\n=== SSH Brute-force Detection ({datetime.datetime.now()}) ===\n")
    f.write(f"Log File: {LOG_FILE_SSH}\n----------------------------------------\n")

ip_counts = {}
try:
    with open(LOG_FILE_SSH, "r") as f:
        for line in f:
            if "Failed password" in line:
                match = re.search(r'from ([0-9.]+)', line)
                if match:
                    ip = match.group(1)
                    ip_counts[ip] = ip_counts.get(ip, 0) + 1
except FileNotFoundError:
    pass

with open(REPORT, "a") as f:
    for ip, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True):
        f.write(f"{count} {ip}\n")
        if BAN_MODE and count > MAX_FAILED:
            block_ip(ip)

# === SSH Usernames ===
username_counts = {}
with open(LOG_FILE_SSH, "r") as f:
    for line in f:
        if "Failed password" in line:
            parts = line.split()
            if "for" in parts:
                idx = parts.index("for")
                if idx + 1 < len(parts):
                    user = parts[idx + 1]
                    username_counts[user] = username_counts.get(user, 0) + 1

with open(REPORT, "a") as f:
    f.write("\nTop SSH Usernames Targeted:\n")
    for user, count in sorted(username_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        f.write(f"{count} {user}\n")

# === HTTPD ANALYSIS ===
ip_httpd_counts = {}
ua_counts = {}
try:
    with open(LOG_FILE_HTTPD, "r") as f:
        for line in f:
            if "POST /login" in line:
                ip = line.split()[0]
                ip_httpd_counts[ip] = ip_httpd_counts.get(ip, 0) + 1
                ua_match = re.findall(r'"[^"]*"', line)
                if len(ua_match) >= 6:
                    ua = ua_match[5]
                    ua_counts[ua] = ua_counts.get(ua, 0) + 1
except FileNotFoundError:
    pass

with open(REPORT, "a") as f:
    f.write("\n\n=== HTTP Login Brute-force Detection ===\n")
    f.write(f"Log File: {LOG_FILE_HTTPD}\n----------------------------------------\n")
    for ip, count in sorted(ip_httpd_counts.items(), key=lambda x: x[1], reverse=True):
        f.write(f"{count} {ip}\n")
        if BAN_MODE and count > MAX_FAILED:
            block_ip(ip)

    f.write("\nSuspicious User-Agents on HTTP POST /login:\n")
    for ua, count in sorted(ua_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        f.write(f"{count} {ua}\n")

print(f"✅ Report written to: {REPORT}")
