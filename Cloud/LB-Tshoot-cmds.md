**The OCI Load Balancer + Web App Troubleshooting Overview**, with **exact Linux and OCI CLI commands** included for each step:

---

## ✅ **Troubleshooting Overview – With Commands**

---

### 🔹 1. **Client-Side Checks**

#### 🔍 DNS Resolution

```bash
dig +short app.example.com
nslookup app.example.com
```

#### 🔍 Network Path & Latency

```bash
ping app.example.com
traceroute app.example.com
```

#### 🔍 Test Web App Response

```bash
curl -v http://app.example.com
```

#### 🔍 Use Browser DevTools (GUI)

* Open browser
* Press `F12` → Go to **Network** tab
* Refresh the page and inspect:

  * HTTP codes (502, 504, etc.)
  * Slow/blocked requests
  * SSL issues

---

### 🔹 2. **OCI Load Balancer Checks**

#### ✅ Get Load Balancer Details

```bash
oci lb load-balancer get --load-balancer-id <LB_OCID>
```

#### ✅ List Listeners

```bash
oci lb listener list --load-balancer-id <LB_OCID>
```

#### ✅ Check Backend Set Health

```bash
oci lb backend-set get-health \
  --load-balancer-id <LB_OCID> \
  --backend-set-name <BACKEND_SET_NAME>
```

#### ✅ View Logs via Logging Search

```bash
oci logging-search search-logs \
  --search-query 'search "502" within logs'
```

#### ✅ Check Metrics (Web Console)

Go to:

> OCI Console → Monitoring → Metrics Explorer → Select “Load Balancer” → View error/connection count.

---

### 🔹 3. **Backend VM (Linux) Checks**

#### ✅ Check App Service Status

```bash
sudo systemctl status nginx
# or
sudo systemctl status apache2
```

#### ✅ Check Listening Ports

```bash
sudo lsof -i -P -n | grep LISTEN
# or
sudo netstat -tulnp | grep :80
```

#### ✅ Test App Locally

```bash
curl -v http://localhost
curl -v http://<private_ip>
```

#### ✅ Check Web Server Logs

```bash
tail -n 50 /var/log/nginx/access.log
tail -n 50 /var/log/nginx/error.log
```

#### ✅ Firewall Checks

```bash
sudo ufw status verbose         # For Ubuntu
sudo firewall-cmd --list-all    # For RHEL/CentOS
```

---

### 🔹 4. **Network & Security Configuration**

#### ✅ Check NSG Ingress Rules (OCI Console)

Navigate to:

> Networking → Network Security Groups → Your NSG → Ingress Rules
> Ensure port `80/443` is allowed from LB Subnet or `0.0.0.0/0`

#### ✅ Check Security Lists (OCI Console)

Ensure port `80/443` is open in the associated **VCN Subnet Security List**.

#### ✅ Validate Route Table

Navigate to:

> Networking → Route Tables → Check routes for Internet Gateway or Service Gateway.

---

### 🔹 5. **Test LB Health Check Behavior on Backend VM**

```bash
curl -s -o /dev/null -w "Status: %{http_code}\\nTime: %{time_total}s\\n" http://localhost/health
```

---

Let me know if you'd like this troubleshooting overview saved as an `.md` or `.pdf` file with commands and output examples!
