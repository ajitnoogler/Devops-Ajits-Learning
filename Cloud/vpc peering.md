

🖧 Sample VPC Peering Architecture 

           🟩 VPC-A (App VPC - 10.0.0.0/16)
           Region: ap-south-1 (Mumbai)
┌──────────────────────────────────────┐
│                                      │
│  +------------------------------+    │
│  | App Server (10.0.1.10)       |    │
│  +------------------------------+    │
│          |                           │
│     +----v-----+                     │
│     | Route Table|                  │
│     | 10.0.0.0/16|------------------┼─┐
│     | + Peering: 192.168.0.0/16     │ │
└─────┴────────────┘                  │ │
                                      │ │
                                      ▼ ▼
                              🌉 VPC Peering Connection
                          (Peering ID: pcx-123abc / Accepted)

                                      ▲ ▲
           🟦 VPC-B (Logging VPC - 192.168.0.0/16)
           Region: ap-south-1 (Mumbai)
┌──────────────────────────────────────┐
│                                      │
│  +-------------------------------+   │
│  | Logging Server (192.168.1.5)  |   │
│  +-------------------------------+   │
│          |                           │
│     +----v-----+                     │
│     | Route Table|                  │
│     | 192.168.0.0/16|---------------┘
│     | + Peering: 10.0.0.0/16        │
└─────┴───────────────────────────────┘

🔑 Key Points:

    Two VPCs in the same region, different CIDR blocks (must not overlap).

    Peering connection (pcx-123abc) allows private IP-based communication.

    Both VPCs have updated route tables to reach each other.

    No public IPs, NATs, or internet gateways are involved.

    Use case: App VPC sends logs to SIEM/Logging VPC over private peering.