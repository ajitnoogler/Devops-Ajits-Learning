 **Multi-region web app architecture with NLB and ALB** 

---

## 🌍 Multi-Region Web App with NLB + ALB (AWS Architecture)

````markdown
# 🌍 Multi-Region Web Application Architecture (AWS)

## 🧭 Flow Overview

```text
1. User accesses https://app.example.com
2. Route 53 (Latency-based or Geo-routing) resolves to nearest region's NLB
3. NLB receives HTTPS traffic on port 443 and forwards it to ALB
4. ALB performs Layer 7 (HTTP) routing to EC2 instances
5. EC2 processes the request and returns response
6. Response goes back → ALB → NLB → Client
```

---

## 🖥️ Single-Region Text Diagram (us-east-1)

```text
🌐 Client (User Browser)
       |
       | 1. DNS Lookup (Route 53 - Geo/Latency Policy)
       v
🔁 NLB (us-east-1)
       |
       | 2. TCP Forwarding (port 443)
       v
🌉 ALB (us-east-1)
       |
       | 3. HTTP Routing (/api, /login, etc.)
       v
🖥️ EC2 Web App (us-east-1)
       |
       | 4. Response
       v
🌉 ALB ← NLB ← Internet ← Client
```

---

## 🌐 Multi-Region Global Architecture

```text
             🌍 Internet Clients
                    |
           +--------▼--------+
           |   Route 53 DNS  |
           | (Latency-based) |
           +--------+--------+
                    |
        +-----------+------------+
        |                        |
+-------▼-------+        +-------▼-------+
| NLB (us-east-1) |      | NLB (ap-south-1) |
|   TCP 443       |      |   TCP 443        |
+-------+-------+        +-------+-------+
        |                         |
+-------▼-------+         +-------▼-------+
| ALB (us-east-1) |       | ALB (ap-south-1) |
| HTTP Routing    |       | HTTP Routing     |
+-------+-------+         +-------+-------+
        |                         |
+-------▼-------+         +-------▼-------+
| EC2 Web Tier   |        | EC2 Web Tier   |
| Auto Scaling   |        | Auto Scaling   |
+---------------+        +---------------+
```

---

## 📦 DNS Configuration (Route 53)

```text
app.example.com (Record Type: A)
├── us-east-1 → NLB DNS: dualstack.nlb-use1.amazonaws.com
└── ap-south-1 → NLB DNS: dualstack.nlb-aps1.amazonaws.com
Routing Policy: Latency-based / Geolocation
```

---

## 🔐 Security Notes

- NLB handles Layer 4 traffic (TCP/SSL passthrough)
- ALB can terminate SSL and inspect headers (Layer 7)
- ALB performs content-based routing (e.g., /api → Target Group A, /admin → Target Group B)
- Each ALB connects to EC2s across multiple AZs for HA

---

## ✅ Use Cases

- Multi-region failover & latency optimization
- Global applications (APIs, customer portals, etc.)
- Layer 4 and Layer 7 separation of concerns
````
