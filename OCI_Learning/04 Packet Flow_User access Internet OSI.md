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


Application Layer  - https://www.linkedIn.com

Presentation Layer - Secure Request SSL/TLS.

Session Layer      - Session Setup and maintainance.

Transport Layer    - TCP Port Assignement -  In our case src-port 32345 Dst-Port 443 - 3-way Handhsake | Segmentation

Network Layer      - IP addressing and Routing - SRC-IP | DST-IP | Protocol

DataLink Layer     - Mac-Addressing, ARP, Frame encap, Switch mac-learning and Hop by Hop Mac-add Learning.

Physical Layer     - Physical Connectivity (Bit by Bit Transmission)
