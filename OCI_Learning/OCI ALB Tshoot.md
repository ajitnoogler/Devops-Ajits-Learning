
**Step-by-Step troubleshooting runbook** for **access issues to a server behind OCI Load Balancers (ALB and NLB)**, covering two scenarios:

---

## 🔧 **OCI Load Balancer Troubleshooting Runbook**

### 👤 **Use Case**

Users report they **cannot access a backend server** (e.g., web app or API) hosted **behind:**

* **Application Load Balancer (ALB)**
* **Network Load Balancer (NLB)**

---

## ⚙️ ENVIRONMENT

* **Cloud**: Oracle Cloud Infrastructure (OCI)
* **Components**:

  * Load Balancer (ALB or NLB)
  * Backend servers (e.g., Compute instances)
  * Network Security Groups (NSGs), Subnets, Route Tables
  * Optional: WAF, SSL/TLS, OCI DNS

---

# 📌 SCENARIO 1: **Access Issue via ALB (Layer 7 HTTP/HTTPS)**

### ✅ Where to test from:

* **From a client system** (e.g., Internet or private VCN)
* **From bastion/jump server** (if private access)
* **From backend instance itself**

---

## 🔍 Step-by-Step Troubleshooting for ALB:

### 1️⃣ **Initial Reachability Check**

* ✅ Run from **your machine or a bastion**:

  ```bash
  curl -v http://<ALB-DNS-Name>  # or https://
  telnet <alb-dns-name> 80    # For HTTP
  telnet <alb-dns-name> 443   # For HTTPS    
  nc -zv <ALB-IP or DNS> 443    
  ```

* ❓Error Codes to note:

  * `curl: (7) Failed to connect` → Load Balancer not reachable
  * `curl: (52) Empty reply from server` → Backend not responding
  * `curl: (60) SSL certificate problem` → TLS issue

---

### 2️⃣ **Validate ALB Configuration (Console / CLI)**

* Listener present on required port (80/443)?
* Rule Set correctly mapped to listener?
* Health Check protocol and port?
* Backend Set attached?

> ✅ **From Console:** Go to **Load Balancer > Listeners / Backend Sets / Health Checks**

---

### 3️⃣ **Check Health Status of Backend**

* **CLI/Console**:

  ```bash
  oci lb backend list --backend-set-name <name> --load-balancer-id <ocid>
  ```

* Look for:

  * `status: OK`
  * `status: CRITICAL` → Health Check failing

* 🛠️ **On Backend Server**:

  * Run this from the backend itself:

    ```bash
    sudo netstat -tulnp | grep 80     # Or 443, or app port
    curl -v http://localhost:80
    ```

---

### 4️⃣ **Network Check**

* **Security List or NSG**:

  * Allow **ALB subnet CIDR** to backend port
  * Allow outbound from backend to ALB health check source

* **Routing**:

  * Route table points to Internet Gateway or NAT Gateway?
  * Ensure backend subnet can respond to health checks

---

### 5️⃣ **SSL/TLS Check (if HTTPS)**

* Certificate properly configured in ALB?
* Hostname matches?
* Use:

  ```bash
  openssl s_client -connect <alb-dns>:443
  ```

---

### 6️⃣ **Logs and Metrics**

* Enable **Access Logs and Error Logs** in ALB
* View **Metrics → Response code (4xx/5xx)**

---

## ✅ Outcome:

* Backend UP and healthy
* ALB responding with 200 OK
* App accessible from client or bastion

---

# 📌 SCENARIO 2: **Access Issue via NLB (Layer 4 TCP)**

### ✅ Where to test from:

* **Client machine or Bastion Host**
* **From backend server**
* **From inside same subnet (for VCN-native test)**

---

