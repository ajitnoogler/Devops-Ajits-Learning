
# OCI Load Balancing:
- It loadbalance traffic between multiple Compute Instances.
- It reduces slowness and Downtime to the backend application.

# When to use ALB | NLB | GwLB
ALB - Application LB: when you want to perform loadbalancing on Layer 7 application layer 
i.e HTTP | HTTPS | SSL-TLS Offloading-Termination | WAF Integration | Pathbased-URL Based Routing | Host-Based-Routing based on Host Header in HTTP Request

NLB - Network LB: When you want to perform loadbalancing on Layer 4 TCP and UDP traffic and requirement is extremely low latency. 
i.e To Preserve SRC-IP | TLS Termination on NGFW 

GwLb - Not available in OCI, workaround with VCN routing + NGFW.

# Path Based Routing:
https://example.com/api/       →  Target Group A (API servers)
https://example.com/images/    →  Target Group B (Image servers)
https://example.com/login      →  Target Group C (Auth service)

Use Case: Microservices architecture | Single domain with multiple apps (e.g., /admin, /user, /blog) | API Gateway-like use case

#  Host-Based Routing (Hostname-based)
https://api.example.com     →  Target Group A (API servers)
https://admin.example.com   →  Target Group B (Admin dashboard)
https://www.example.com     →  Target Group C (Main website)

Use Case: Hosting multiple websites on a single ALB | Multi-tenant environments (SaaS) | Blue/Green deployments on different subdomains

Assume you have Application which is new and have not much traffic and can be handled by a Single Instance.
Your Application became popular and lot of traffic started hitting the Single Instance causing slowness and Downtime.
Here, you can deploy a Load Balancer and multiple backend server to serve user request.
User traffic will hit the loadbalancer URL and then LB will be responsible to distribute load to backend server.


# Application Loadbalancer: 
It provides Reverse Proxy solution that hides the IP of the client from Backend App Server
It is capable of performing advance Layer 7 (HTTP/HTTPA), Layer 4 TCP load-balancing and SSL Offloading
Best For - Websites, Mobile-Apps, SSL Termination, and advance HTTP Handling.

# Network Loadbalancer: 
It provides a pass-through non-proxy-solution that is capable of preserving the Client header (Src-IP and Dst-IP).
Its is Built for Speed, Optimized for long running connection.
Best For - VoIP, IoT, and Trading PLatforms.

**Lets Deploy a Load-Balancer**

Servers: Both Service Running Apache Service on port :80
-----------------------------------------------------------------
Name              Public-IP        Private-IP    AD     FD
-----------------------------------------------------------------
web-instance-01 - 152.69.186.222 - 10.50.0.215 - AD-1   FD-3
web-instance-02 - 158.179.27.237 - 10.50.0.111 - AD-1   FD-3
-----------------------------------------------------------------

# Create Load-Balancer:
Hamburger-Icon -> Networking -> Load balancer <Click-it>
    -> <Click-On> Create Load-balancer
            - Name: Demo-Lb
            - Choose Visibility: Public (Public/Private)
            - Assign Public IP: Ephemeral IP add (Ephemeral-IP/ Reserved-IP)
            - Shapes: Flexible Shapes <Bandwidth-Shapes>
                - Minimum Bandwidth: 10 Mbps
                - Maximum Bandwidth: 10 Mbps -> Max Service Limit 5000 Mbps
                - Choose Networking: demo_VCN_1
                - Subnet: mgmt(Regional)
                - Network Security GRP: "Note configure later after testing"
                - <Click-On> Next.
                    - Choose Backend: Weighted Round Robin | IP-Hash | Least Connections
                    - <Click-On> Add Backend Server, select web-instance-01 && web-instance-02
                    - Specify Health Check Policy: Protocol = HTTP | HTTPS
                                                   Port = 80 | 443
                    - <Click-On> Next.
                        - Configure Listner:
                            - Listner Name: Demo-Lb-Listener
                            - Specify the type of Traffic: HTTP | HTTPS
                            - Specify Port for listner to monitor: 80 | 443
                            - <Click-On> Next.
                                - Manage Logging:
                                    - Error Logs: Enable it.
                                    - Compartment: Demo_Compartment
                                    - Access Logs: Enable it
                                    - Request ID: Enable it. -> Select "X-Request-Id"
                                    - <Click-On> Submit.

 # Check Status of LB:

Go-to - Hamburger-Icon -> Networking -> Load balancer <Click-it>
Here you will see status of your loadbalancer from provisioning -> Active
Here you will see Overall health of LB.
To get LB Public Facing IP
-------------------------------------------------------------------------------------
Name        State  IP-Address            Shapes    Overall Health  Created
-------------------------------------------------------------------------------------
Demo_LB     Active 158.179.21.93(Public) Flexible  Healthy         Tue, July 6, 2025
--------------------------------------------------------------------------------------  

Ephemeral-IP: You can have IP add from pool automatically assigned to you. (Temporary Public IP)
Reserved-IP: You can provide either existing reserved IP address or
             Create a new one by assigning a name and source IP Pool.

Flexible Shapes: It has minimum and maximum size range.

**Weighted Round-Robin:** It distribute incoming traffic sequentially to each backend server.
**IP Hash:** It Ensures that request from a particular Client are always directed to same backend server.
**Least Connection:** Routes incomming request traffic to the backend server who has fewest active connections.

Request ID: Its in Manage Logging, Its a Unique identifier for tracking and managing an incident that can be associated with the log entry in the Logging service.

Nginx
Envoy
Citrix Netscaler
F5

Scenario: User trying to access LinkedIN.com
Following is layer by layer activity
Application Layer  - https://www.linkedIn.com
Presentation Layer - Secure Request SSL/TLS.
Session Layer      - Session Setup and maintainance.

Transport Layer    - TCP or UDP Port Assignement -  In our case src-port 32345 Dst-Port 443 - 3-way Handhsake | Segmentation
Network Layer      - IP addressing and Routing - SRC-IP | DST-IP | Protocol
DataLink Layer     - Mac-Address Learning and Hop by Hop Mac-add Learning.
Physical Layer     - Physical Connectivity (Bit by Bit Transmission)

✅ Scenario: User trying to access https://www.linkedin.com In Detail:

| OSI Layer                        | Actual Activity                                                                                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Application Layer (Layer 7)**  | User initiates connection to `https://www.linkedin.com` via browser (e.g., Chrome).                                                              |
| **Presentation Layer (Layer 6)** | SSL/TLS encryption/decryption, data format translation (e.g., HTML, JPEG, JSON).                                                                 |
| **Session Layer (Layer 5)**      | Establishes and maintains session (SSL/TLS handshake, session cookies, tokens).                                                                  |
| **Transport Layer (Layer 4)**    | TCP used (not UDP) → Source Port: Random (e.g., 32345), Destination Port: 443 → TCP 3-Way Handshake, segmentation, retransmission, flow control. |
| **Network Layer (Layer 3)**      | IP addressing (SRC-IP, DST-IP), routing decisions, IP packet creation.                                                                           |
| **Data Link Layer (Layer 2)**    | MAC addressing, ARP resolution, frame encapsulation, switch MAC learning.                                                                        |
| **Physical Layer (Layer 1)**     | Bit-level transmission over cable/wireless medium (e.g., Ethernet, Wi-Fi).                                                                       |



# OCI GWLB-Like Inline Firewall Architecture Diagram:

                      ┌────────────────────────────┐
                      │        Internet Gateway     │
                      └────────────┬───────────────┘
                                   │
                         ┌─────────▼───────────┐
                         │    Route Table:     │
                         │  0.0.0.0/0 → NGFW    │
                         └─────────┬───────────┘
                                   │
                         ┌────────▼───────────┐
                         │    Spoke VCN A      │
                         │   (App/Web Tier)    │
                         └────────┬────────────┘
                                  │
                    ┌────────────▼─────────────┐
                    │ Local Peering Gateway    │
                    └────────────┬─────────────┘
                                 │
                      ┌──────────▼─────────────┐
                      │       Hub VCN          │
                      │  (Security VCN/NGFW)   │
                      └──────────┬─────────────┘
                                 │
             ┌──────────────────┴───────────────────┐
             │              NGFW HA                 │
             │ (e.g., Palo Alto / FortiGate VMs)    │
             └────────────┬─────────────┬───────────┘
                          │             │
             ┌────────────▼──────┐ ┌────▼─────────────┐
             │ Egress Route      │ │ Ingress Route     │
             │ (To Internet/NAT) │ │ (From Internet/LPG)│
             └────────────┬──────┘ └────────────┬──────┘
                          │                     │
                   ┌──────▼──────┐       ┌──────▼───────┐
                   │ Internet GW │       │ NAT Gateway  │
                   └─────────────┘       └──────────────┘

