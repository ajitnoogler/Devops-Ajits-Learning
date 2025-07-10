## 🌐 Public vs Private IP Address Ranges

| 🏷️ Type     | 🔢 CIDR Range           | 🌍 Address Range           | 📘 Description                                         | ☁️ Cloud Usage Example                            |
|------------|-------------------------|----------------------------|--------------------------------------------------------|--------------------------------------------------|
| **Private** | `10.0.0.0/8`           | `10.0.0.0 – 10.255.255.255` | Large private range (Class A)                         | VPC/VCN CIDR in AWS/OCI                          |
| **Private** | `172.16.0.0/12`        | `172.16.0.0 – 172.31.255.255` | Medium private range (Class B)                        | VPCs, Kubernetes internal networks               |
| **Private** | `192.168.0.0/16`       | `192.168.0.0 – 192.168.255.255` | Small private range (Class C)                         | Home routers, small cloud test VPCs              |
| **Public**  | All others not reserved | e.g. `8.8.8.8`, `3.0.0.0/8`  | Routable over the Internet                           | Public IPs assigned to LB, NAT, or EC2           |
| **Loopback**| `127.0.0.0/8`          | `127.0.0.1 – 127.255.255.254` | Localhost, loopback                                   | Diagnostics, local testing                        |
| **Link-Local** | `169.254.0.0/16`   | `169.254.0.0 – 169.254.255.255` | Auto-IP / Metadata service IPs                       | AWS/OCI metadata endpoint (`169.254.169.254`)     |
| **Multicast** | `224.0.0.0/4`        | `224.0.0.0 – 239.255.255.255` | Used for multicast routing                           | Not typically used in cloud                      |
| **Reserved by OCI** | `100.96.0.0/16` | `100.96.0.0 – 100.96.255.255` | Internal SNAT/routing by Oracle                      | Automatically used by OCI VCN backend            |

---

### ✅ Summary

- **Private IPs** are used inside cloud networks (VCNs/VPCs) and are not routable on the public Internet.
- **Public IPs** are globally routable and must be allocated by cloud providers or ISPs.
- **Metadata service** (like `169.254.169.254`) is used in cloud VMs for identity tokens, instance data, etc.
- **Loopback** is only valid on the local instance.
- **OCI reserves `100.96.0.0/16`** — avoid using this in your own subnet plan.

---

### ☁️ Common Examples in AWS / OCI

| Use Case                      | IP Example          | Notes                              |
|------------------------------|---------------------|-------------------------------------|
| Public LB in AWS             | `13.x.x.x`          | Elastic IP assigned by AWS         |
| Public LB in OCI             | `152.x.x.x`         | Reserved Public IP from Oracle     |
| Private App Server           | `10.0.2.15`         | In private subnet                  |
| NAT Gateway Interface        | `10.0.254.5`        | Private IP, routes to public NAT   |
| Metadata Endpoint (all cloud)| `169.254.169.254`   | AWS, OCI, Azure all use this       |
