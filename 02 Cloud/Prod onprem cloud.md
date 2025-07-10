                🏢 On-Premises Data Center
                ┌─────────────────────────────┐
                │                             │
                │  +----------------------+   │
                │  | Edge Router / Switch |◀──┐
                │  +----------------------+   │
                │                             │
                └────────────┬────────────────┘
                             │
                             ▼
             ┌─────────────────────────────────┐
             │     AWS Direct Connect (DX)     │  <-- Dedicated Layer 2 Link
             │    (Private Virtual Interface)  │
             └────────────┬────────────────────┘
                          │
                 ┌────────▼────────┐
                 │ Direct Connect  │
                 │  Gateway (DXGW) │
                 └────────┬────────┘
                          │
                 ┌────────▼────────┐
                 │ Virtual Private │
                 │    Gateway      │
                 └────────┬────────┘
                          │
         ┌────────────────┴──────────────────┐
         │      AWS VPC (Production VCN)     │
         │   Region: ap-south-1 (Mumbai)     │
         │    CIDR: 10.0.0.0/16              │
         └────────────────┬──────────────────┘
                          │
                          ▼
               ┌────────────────────┐
               │ Public Subnet (DMZ)│
               │ AZ1: 10.0.1.0/24   │
               └────────┬───────────┘
                        │
          +-------------+-------------+
          |                           |
          ▼                           ▼
+--------------------+     +--------------------+
|  Palo Alto VM-1    |     |  Palo Alto VM-2    |
| (Active, AZ1)       |     | (Passive, AZ2)     |
| Public & Private NICs |   | Public & Private NICs |
+---------+----------+     +---------+----------+
          |                            |
          +----------------------------+
                          |
                          ▼
              ┌────────────────────┐
              │  Internal Subnet   │
              │  App Tier: 10.0.2.0/24 │
              └────────┬───────────┘
                       │
                +------+------+
                | App Server  |
                | EC2 / ALB   |
                +-------------+



## Traffic Flow Summary (East–West / North–South)

   # North-South (On-Prem ↔ AWS):

        On-prem workloads initiate traffic to AWS VPC (e.g., DB, APIs)

        Traffic enters via Direct Connect, hits VGW → VPC Route Table → Palo Alto (HA) → reaches Internal App Subnet

  # East-West (Inside VPC):

        Internal subnet communication is routed through Palo Alto for inspection/logging.

        Segmentation policies prevent lateral movement (PCI segmentation).

  #  Outbound Internet (if needed):

        Traffic from App Subnet → Palo Alto → NAT Gateway → Internet

        No direct outbound access from App/DB VMs