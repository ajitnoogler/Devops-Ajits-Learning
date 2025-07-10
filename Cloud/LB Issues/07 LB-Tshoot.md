**OCI Load Balancer + Web App Troubleshooting Guide**:

---

### 🧩 **Scenario**

Users report intermittent access issues to a web app hosted in OCI via a public Load Balancer — symptoms include timeouts, `502 Bad Gateway`, and `504 Gateway Timeout`.

---

### ✅ **Troubleshooting Overview**

#### 1. **Client-Side Checks**

* Validate DNS (`dig`, `nslookup`)
* Trace network path (`traceroute`)
* Test with `curl` and browser DevTools

#### 2. **OCI Load Balancer Checks**

* Check **lifecycle state**, **listeners**, and **backend health**
* Verify **health check config** (path, timeout, response code)
* Review **access logs** and **error logs** for `502/504`

#### 3. **Backend VM Diagnostics**

* Ensure web server is **running** and **listening on correct port**
* Test app locally with `curl`
* Check `ufw` or `firewalld` for open ports
* Review web server logs (`/var/log/nginx/error.log`)

#### 4. **Network & Security**

* NSG/Security Lists: Ensure ingress on ports 80/443 from LB subnet
* Route Tables: Validate return path to LB subnet
* Sticky Sessions: Check app compatibility

---

### 🔍 **Common Root Causes**

| Symptom              | Cause                              |
| -------------------- | ---------------------------------- |
| 502 Bad Gateway      | App returned error or crashed      |
| 504 Gateway Timeout  | App didn’t respond in time         |
| Intermittent Access  | Unhealthy backend or wrong routing |
| Health Check Failure | Bad path, app not returning 200 OK |
| NSG Blocked Traffic  | Missing inbound port rule          |

---

### 🧪 **Test Script Sample** -- lb_health_check.sh

A shell script to simulate LB health check and print port/firewall status on backend VM.

# 🔧 OCI Load Balancer Backend Health Check Script

This script helps you troubleshoot issues with Oracle Cloud Infrastructure (OCI) Load Balancer backends by simulating health checks, verifying listening ports, and inspecting firewall settings.

---

## 🧪 Script: `lb_health_check.sh`

```bash
#!/bin/bash

echo "🔍 Simulating OCI Load Balancer Health Probe..."
echo "-----------------------------------------------"
curl -s -o /dev/null -w "HTTP Status: %{http_code}\nTime: %{time_total}s\n" http://localhost/health
echo ""

echo "📡 Checking Listening Ports..."
echo "-----------------------------"
sudo lsof -i -P -n | grep LISTEN

echo ""
echo "🧱 Checking Firewall Rules (UFW)..."
echo "----------------------------------"
sudo ufw status verbose

echo ""
echo "🔥 Checking Firewall Rules (firewalld)..."
echo "-----------------------------------------"
sudo firewall-cmd --list-all 2>/dev/null || echo "firewalld not active"

```bash

---

# 🛠️ Example Output

🔍 Simulating OCI Load Balancer Health Probe...
HTTP Status: 200
Time: 0.034s

📡 Checking Listening Ports...
nginx     1234 www-data    6u  IPv4  123456      0t0  TCP *:80 (LISTEN)

🧱 Checking Firewall Rules (UFW)...
Status: active
To                         Action      From
--                         ------      ----
80/tcp                     ALLOW       Anywhere

🔥 Checking Firewall Rules (firewalld)...
public (active)
  services: ssh http https
  ports: 80/tcp 443/tcp


✅ What the Script Does
| Section                   | Description                                     |
| ------------------------- | ----------------------------------------------- |
| `curl` check              | Simulates LB health probe to `/health` endpoint |
| `lsof` check              | Lists open and listening ports                  |
| `ufw` / `firewalld` check | Ensures no firewall rules block HTTP/HTTPS      |

---

### 📘 **Key OCI CLI Commands**

* `oci lb backend-set get-health`
* `oci lb listener list`
* `oci logging-search search-logs`

---

