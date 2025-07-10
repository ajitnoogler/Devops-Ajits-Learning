## 🔍 Step-by-Step Troubleshooting for NLB:

### 1️⃣ **Connectivity Test**

* **From client**:

  ```bash
  nc -zv <NLB-IP> <Port>          # Check if port open
  telnet <NLB-IP> <Port>
  curl -v <NLB-IP>:<Port>         # If HTTP
  ```

---

### 2️⃣ **Check NLB Configuration**

* Target Type: **IP or Compute**
* Backend port correct?
* Health Check:

  * Port reachable
  * Protocol matches (TCP, HTTP)

> Check from **OCI Console > NLB > Backends**

---

### 3️⃣ **Check Backend Health**

* From Console or CLI:

  ```bash
  oci network-load-balancer backend-health list --backend-set-name <set-name> --network-load-balancer-id <id>
  ```

* Status: `OK` or `UNKNOWN`, `CRITICAL`

---

### 4️⃣ **Security & Network**

* NSG or Security List:

  * Allow NLB IP range to backend on required port
  * Backend outbound allowed (health check)

* Route Table:

  * No blackhole route
  * Subnet can return traffic

---

### 5️⃣ **Backend Debug**

* From Backend:

  ```bash
  sudo netstat -tulnp | grep <port>
  sudo tcpdump -nn port <port>
  tail -f /var/log/<your_app>.log
  ```

* If health check port is not listening → NLB marks backend `CRITICAL`

---

### 6️⃣ **Load Balancer Metrics**

* OCI > Monitoring > Metrics:

  * BackendConnectionErrors
  * TcpConnections
  * HealthCheckResults

---

## ✅ Outcome:

* Port reachable through NLB IP
* Backend status is healthy
* App or service is running and responsive

---

## 📘 Troubleshooting Flow Summary Table

| Checkpoint             | ALB (L7)                     | NLB (L4)                | Where to Run                    |
| ---------------------- | ---------------------------- | ----------------------- | ------------------------------- |
| `curl`, `nc`           | ✅                            | ✅                       | Client or Bastion               |
| Load Balancer Listener | HTTP/HTTPS config            | TCP port config         | OCI Console or CLI              |
| Health Check           | HTTP or TCP-based            | TCP-based or HTTP       | OCI Console & Backend instance  |
| Backend Listener       | Apache/Nginx or app running? | App or DB port open?    | Backend instance                |
| Logs                   | Access/Error logs in ALB     | App logs                | OCI Logging & Backend           |
| Metrics                | 4xx/5xx, Latency, Throughput | BackendConnectionErrors | OCI Monitoring                  |
| Security/NSG           | ALB subnet to backend        | NLB IPs to backend      | OCI Console / Security settings |

---

## 🧪 Advanced Test Suggestions

* `curl -k -X GET "https://<alb-ip>/?q='<script>alert(1)</script>"` → XSS validation
* `curl -v -H "Host: backend.local" http://<alb-ip>` → Host header test
* `traceroute <alb-ip>` / `mtr` → Path test

---

Let me know if you want a **.md version**, **diagram**, or **Terraform-based health check tester**.
