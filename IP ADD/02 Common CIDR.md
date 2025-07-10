

### 🌐 Common IP Subnetting & CIDR Blocks in AWS vs OCI

| 🔢 Use Case / Tier                | 🟦 AWS CIDR (Typical)        | 🟥 OCI CIDR (Typical)         | 📘 Notes                                                   |
|----------------------------------|------------------------------|-------------------------------|------------------------------------------------------------|
| **VPC / VCN Main CIDR**          | `10.0.0.0/16` or `172.31.0.0/16` | `10.0.0.0/16` or `172.16.0.0/16` | Default for VPC/VCN address space                         |
| **Public Subnet (LB/Bastion)**   | `10.0.1.0/24`                | `10.0.1.0/24`                 | Used for public load balancer, NAT Gateway, or SSH access |
| **Private Subnet (App Tier)**    | `10.0.2.0/24`                | `10.0.2.0/24`                 | Internal app servers or web backends                      |
| **Private Subnet (DB Tier)**     | `10.0.3.0/24`                | `10.0.3.0/24`                 | Databases or backends not directly exposed                |
| **NAT Gateway Subnet**           | `10.0.254.0/28`              | `10.0.254.0/28`               | NAT Gateway placed in public subnet for egress traffic    |
| **Load Balancer Subnet**         | `10.0.100.0/28`              | `10.0.100.0/28`               | Dedicated subnet for LB interfaces (GWLB or Public LB)    |
| **Peering/Transit VPC CIDRs**    | `10.100.0.0/16`              | `10.100.0.0/16`               | Used for Hub/Spoke, DR, or shared service connectivity     |
| **Reserved by Cloud Provider**   | `169.254.169.254`            | `169.254.169.254`             | AWS/OCI metadata endpoint                                 |
| **OCI Reserved Internal Range**  | N/A                          | `100.96.0.0/16`               | Reserved by Oracle (used for SNAT, host routing)          |

---

### 🛠️ Notes

- Choose **non-overlapping CIDRs** across regions/accounts to simplify **VPC Peering** or **VCN Remote Peering**
- Use **/28 or /29** subnets for services like NAT Gateways and Load Balancers
- OCI reserves `100.96.0.0/16` internally — **do not use** this range for custom subnets
- AWS default VPC often uses `172.31.0.0/16`; custom VPCs commonly use `10.0.0.0/16`

---

### 📘 Example Layout (OCI or AWS)

```text
10.0.0.0/16         ← VPC / VCN main CIDR
 ├── 10.0.1.0/24     ← Public Subnet (LB, Bastion)
 ├── 10.0.2.0/24     ← Private Subnet (App Tier)
 └── 10.0.3.0/24     ← Private Subnet (DB Tier)
```

---

Let me know if you’d like:
- Terraform snippets for both AWS and OCI
- Multi-VPC/VCN CIDR planning sheet
- Diagram with subnet layout visualized
