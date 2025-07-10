**OCI Web App Access Troubleshooting Guide**

---

## 🧩 **Scenario**

A user reports: --> "I cannot access the internal company web application hosted in OCI. When I open the web URL, the browser times out or gives a connection refused error."

---

## 🐧 **Step-by-Step Troubleshooting – Linux VM (App Server)**

1. **Check if Web App is Running**

```bash
sudo systemctl status nginx  # or apache2/app service
```

2. **Check Listening Ports**

```bash
sudo netstat -tulnp | grep :80
sudo lsof -i -P -n | grep LISTEN
```

3. **Check UFW / firewalld**

```bash
sudo ufw status verbose
sudo firewall-cmd --list-all
```

4. **Try Curl or Wget Locally**

```bash
curl http://localhost
curl http://<private_ip>
```

---

## ☁️ **Step-by-Step Troubleshooting – OCI Console**

1. **Check Security List and NSG**

   * Allow ingress on port 80/443 for the source CIDR

2. **Check Route Table**

   * Ensure correct route to Internet Gateway / NAT Gateway

3. **Check Public/Private IP**

   * Ensure public IP assigned if public access is needed

4. **Check Load Balancer (if used)**

   * Confirm backend health, listener port, subnet, and NSG

5. **Check DNS**

   * `nslookup` or `dig` to resolve hostname to correct IP

6. **Logs and Monitoring**

   * Use Flow Logs and Instance Metrics for deeper analysis

---

## 🌐 **Client-Side Verification**

1. Ping the app:

```bash
ping <web_app_ip>
```

2. Traceroute to the app:

```bash
traceroute <web_app_ip>
```

3. Curl with verbose:

```bash
curl -v http://webapp.example.com
```

4. Use **browser developer tools** to analyze:

   * SSL issues
   * Timeouts
   * HTTP errors (403, 404, etc.)

---

## ⚠️ **Common Root Causes**

| Issue Type          | Root Cause Example                         |
| ------------------- | ------------------------------------------ |
| DNS Resolution      | Wrong DNS entry or not registered          |
| Port not open       | Missing NSG/Security List rule             |
| App not running     | Web server crashed                         |
| Load Balancer error | Backend unhealthy / Listener misconfigured |
| Route issue         | No route to Internet Gateway/NAT           |
| Local firewall      | UFW or firewalld blocking traffic          |
| SSL Error           | Expired or invalid certificate             |

---

## ✅ **Fix Example - Open Port 80 in NSG**

1. Go to **Network Security Groups**
2. Click on the NSG attached to the instance
3. Add Ingress Rule:

   * Protocol: TCP
   * Source: `0.0.0.0/0`
   * Port: `80`

---

## 🛠️ **Bonus – Automation Script (Run on VM)**

```bash
#!/bin/bash
echo "Checking Web App Status..."
curl -s -o /dev/null -w "%{http_code}" http://localhost
echo ""
echo "Open Ports:"
sudo netstat -tulnp | grep 80
echo "Firewall Rules:"
sudo ufw status verbose
```
