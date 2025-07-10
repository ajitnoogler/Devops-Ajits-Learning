
# 🔧 OCI Web App + Load Balancer Troubleshooting Guide

---

## 🧩 SCENARIO

> “The web application hosted in OCI is intermittently inaccessible via its public URL. Sometimes it works, other times it shows ‘Bad Gateway’ (502), ‘Gateway Timeout’ (504), or the page loads partially.”

---

## ✅ CLIENT-SIDE CHECKLIST

### 1. DNS Resolution
```bash
dig +short app.example.com
nslookup app.example.com
```

### 2. Packet Tracing
```bash
traceroute app.example.com
```

### 3. Curl or Browser Debug
```bash
curl -v http://app.example.com
```

Use browser DevTools → Network tab → inspect for delays, SSL issues, redirects, or timeouts

---

## ☁️ OCI LOAD BALANCER TROUBLESHOOTING

### 1. Load Balancer Status
- OCI Console → Networking → Load Balancers
- Check if **Lifecycle State** = ACTIVE
- Check if **Listeners** (HTTP/HTTPS) are configured properly

### 2. Backend Set Health
```bash
oci lb backend-set get-health \
  --load-balancer-id <lb_ocid> \
  --backend-set-name <name>
```

Sample Output:
```json
{
  "status": "CRITICAL",
  "backends": [{
    "ip-address": "10.0.1.5",
    "status": "CRITICAL",
    "statusDetails": "Health check failed with status 500"
  }]
}
```

### 3. Logs

Sample Load Balancer Access Log:
```
2025-07-07T11:45:02.123Z - 203.0.113.25 - GET /app - 502 - "Bad Gateway"
2025-07-07T11:45:10.981Z - 203.0.113.25 - GET /login - 504 - "Gateway Timeout"
```

---

## 🐧 BACKEND VM (LINUX) CHECKLIST

### 1. App Status
```bash
sudo systemctl status nginx
```

### 2. Ports Listening
```bash
sudo lsof -i -P -n | grep LISTEN
```

### 3. Local Response
```bash
curl -v http://localhost
curl -v http://<private_ip>
```

### 4. Firewall
```bash
sudo ufw status verbose
sudo firewall-cmd --list-all
```

### 5. App Logs
```bash
tail -f /var/log/nginx/error.log
```

Sample Error:
```
upstream timed out while reading response header from upstream
```

---

## 🔐 NETWORK AND SECURITY CHECKS

| Element               | What to Check |
|-----------------------|----------------|
| NSG / Security List   | Ingress on ports 80/443 from Load Balancer subnet |
| Subnet Routes         | Proper return path via IGW or DRG |
| Backend Ports         | Correct port in backend set and app server |
| Sticky Sessions       | App must support session stickiness if enabled |

---

## 🛠️ COMMON ROOT CAUSES

| Symptom                 | Root Cause Example                       |
|-------------------------|------------------------------------------|
| 502 Bad Gateway         | Backend app returned HTTP 500            |
| 504 Gateway Timeout     | App didn't respond in time               |
| Intermittent Access     | Load Balancer backend unhealthy          |
| Health Check Failing    | Incorrect path or app returns non-200    |
| Slow Page Load          | Backend overloaded or database slow      |
| NSG Blocking Traffic    | Missing port rule in NSG or Sec List     |

---

## 🧪 TEST SCRIPT (RUN ON APP VM)

```bash
#!/bin/bash
echo "Simulating LB Health Probe..."
curl -s -o /dev/null -w "Status: %{http_code}\nTime: %{time_total}s\n" http://localhost/health
echo ""
echo "Open Ports:"
sudo lsof -i -P -n | grep LISTEN
echo ""
echo "Firewall:"
sudo ufw status verbose
```

---

## 📘 TROUBLESHOOTING FLOW SUMMARY

Client → DNS/Traceroute → Load Balancer Logs → Backend Health → App Logs

---

### 🔄 OCI CLI Commands to Know

```bash
oci lb load-balancer get --load-balancer-id <lb_ocid>
oci lb listener list --load-balancer-id <lb_ocid>
oci lb backend-set get-health --load-balancer-id <lb_ocid> --backend-set-name <name>
oci logging-search search-logs --search-query "<query>"
```
