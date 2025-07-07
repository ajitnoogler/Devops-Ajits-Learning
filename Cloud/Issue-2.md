**realistic extended troubleshooting guide** where the **Oracle Cloud Infrastructure (OCI) Load Balancer** is **misbehaving or not responding correctly to client requests**,
merged with the earlier scenario of the **Web App being inaccessible**.

---

## 🧩 Combined Scenario

> A user reports they **cannot access a web application** hosted in OCI via a public **OCI Load Balancer**. Sometimes the page **partially loads, times out, or gives HTTP 502/504** errors. This issue is **intermittent**, and app works fine when accessed internally.

---

## 🛠️ Root Assumption

* OCI Load Balancer (LB) sits in front of app VMs.
* Backend is running on Compute instances (Apache, Nginx, NodeJS, etc.)
* Users access via public DNS name (e.g. `app.example.com`)

---

## ✅ Step-by-Step Troubleshooting (Merged View)

---

### 🔹 1. **Client-Side Verification**

| Step               | Command or Action                                        |
| ------------------ | -------------------------------------------------------- |
| DNS Resolution     | `dig +short app.example.com`                             |
| Connectivity Check | `ping <LB Public IP>` / `curl -v http://app.example.com` |
| Packet Tracing     | `traceroute app.example.com`                             |
| Browser DevTools   | Look for SSL errors, 502/504, or CORS issues             |

---

### 🔹 2. **OCI Load Balancer Check**

> **Go to: OCI Console → Networking → Load Balancers**

#### ✅ Load Balancer Status

* **Lifecycle State** should be `ACTIVE`
* **Listener** should be correctly configured (HTTP/HTTPS on 80/443)

#### ✅ Backend Set Health Check

* **Health Check Status**: should be `OK` (green)
* If marked `CRITICAL` or `UNKNOWN`, check:

  * Backend port is open
  * App is returning 200 OK
  * App response time is within health check timeout

#### ✅ Log Insight (if enabled)

* Use **OCI Logging** to inspect:

  * Access Logs
  * Error Logs
  * LB Metrics (latency, errors, health)

---

### 🔹 3. **Backend Instance Diagnostics (Linux)**

Run on app VM:

#### ✅ Web App is Running

```bash
sudo systemctl status nginx  # or apache2
```

#### ✅ Listening Port Check

```bash
sudo lsof -i -P -n | grep LISTEN | grep 80
```

#### ✅ Firewall Rules

```bash
sudo ufw status verbose
sudo firewall-cmd --list-all
```

#### ✅ Local App Test

```bash
curl -v http://localhost
curl -v http://<private_ip>:80
```

> **Ensure app returns HTTP 200 OK consistently**

#### ✅ Monitor for Delays

```bash
tail -f /var/log/nginx/access.log  # Check for long request time
```

---

### 🔹 4. **Network Configuration Review**

| Item                    | What to Check                                                        |
| ----------------------- | -------------------------------------------------------------------- |
| **NSG/Security List**   | Allow TCP 80/443 from LB subnet CIDR                                 |
| **Route Table**         | Correct route back to LB subnet                                      |
| **Subnet Placement**    | LB must be in same VCN or peered VCN                                 |
| **Load Balancer Shape** | `100Mbps` shape under heavy traffic may throttle connections         |
| **Sticky Sessions**     | Can cause routing issues with stateful apps if not handled correctly |

---

### 🔹 5. **Health Check Configuration Tips**

| Setting         | Recommendation   |
| --------------- | ---------------- |
| Interval        | 10 seconds       |
| Timeout         | 3 seconds        |
| Protocol        | HTTP or TCP      |
| URL Path        | `/health` or `/` |
| Expected Status | 200              |
| Retry Count     | 3                |

---

### 🔹 6. **Advanced LB Troubleshooting via OCI CLI**

```bash
oci lb load-balancer get --load-balancer-id <lb_ocid>
oci lb backend-set get-health --load-balancer-id <lb_ocid> --backend-set-name <name>
oci lb listener list --load-balancer-id <lb_ocid>
```

---

## 🚩 Common Root Causes – Load Balancer Failures

| Symptom                      | Possible Cause                                     |
| ---------------------------- | -------------------------------------------------- |
| **502/504 Gateway Timeout**  | Backend timeout, slow app, or health check failure |
| **Intermittent Load**        | Backend overloaded or unhealthy                    |
| **Access Logs show retries** | App crashing or restarting                         |
| **Listener not responding**  | Port mismatch or bad NSG rule                      |
| **Health check fails**       | Wrong URL/path, app returns 403/500                |

---

## 🛡️ Fix: Backend Set Health Check Misconfigured

1. Go to LB → **Backend Sets**

2. Edit Health Check:

   * Protocol: HTTP
   * Path: `/health`
   * Port: `80`
   * Expected Status: `200`

3. Confirm backend responds:

```bash
curl -i http://localhost/health
```

---

## 🧪 Bonus Script – On VM to Simulate Load Balancer Probe

```bash
#!/bin/bash
echo "Simulating LB Health Probe..."
curl -s -o /dev/null -w "Status: %{http_code}\nTime: %{time_total}s\n" http://localhost/health
echo "Firewall:"
sudo ufw status verbose
```

---

## 📘 Summary: Checklist for Load Balancer Misbehavior

| Check Area       | What to Look For                        |
| ---------------- | --------------------------------------- |
| App Server       | Running status, open ports, HTTP 200 OK |
| OCI NSG/Sec List | Ports 80/443 open from LB CIDR          |
| Load Balancer    | Backend health = OK, listener = active  |
| Route Tables     | Valid return path to LB subnet          |
| App Logs         | Errors, long response time, crash loops |
| Client Logs      | DNS issues, timeouts, intermittent 502  |

---

![9530d969-defd-4102-88c0-4c5d0d7d4e62](https://github.com/user-attachments/assets/3e1b7ecc-2d26-44a9-950c-8ccd1d1171e3)
