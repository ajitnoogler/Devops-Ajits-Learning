OPEN-VPN:

<img width="623" height="432" alt="image" src="https://github.com/user-attachments/assets/49f26175-c49a-4b00-adef-cec43a0a6e14" />


#### Sample OpenVPN Server Connection Log (Access Server)
```bash
2025-08-13 09:15:07+0000 [INFO] User 'alice' connecting from 203.0.113.45:1194 (UDP)
2025-08-13 09:15:07+0000 [INFO] TLS: Received ClientHello (TLSv1.2) from 203.0.113.45:1194
2025-08-13 09:15:07+0000 [INFO] TLS: Client certificate verified for user 'alice'
2025-08-13 09:15:07+0000 [INFO] MULTI: new connection by client 'alice' via [AF_INET]203.0.113.45:1194
2025-08-13 09:15:07+0000 [INFO] MULTI: primary virtual IP for 'alice' is 10.8.0.2
2025-08-13 09:15:07+0000 [INFO] MULTI: new session for 'alice'
2025-08-13 09:15:07+0000 [INFO] PUSH: Received control message: 'PUSH_REQUEST'
2025-08-13 09:15:07+0000 [INFO] SENT CONTROL [alice]: 'PUSH_REPLY,redirect-gateway def1,dhcp-option DNS 8.8.8.8' (status=1)
2025-08-13 09:15:07+0000 [INFO] Data Channel: using negotiated cipher 'AES-256-GCM'
2025-08-13 09:15:07+0000 [INFO] alice/203.0.113.45:1194 MULTI: pool returned IPv4=10.8.0.2, IPv6=(null)
2025-08-13 09:15:07+0000 [INFO] alice/203.0.113.45:1194 MULTI: route 10.8.0.0/24 via 10.8.0.2
2025-08-13 09:15:07+0000 [INFO] alice/203.0.113.45:1194 Initialization Sequence Completed
```

#### What These Entries Mean on server side

| Log Entry                                        | Description                                                                |
| ------------------------------------------------ | -------------------------------------------------------------------------- |
| `User 'alice' connecting from 203.0.113.45:1194` | Connection request initiated from client `alice`.                          |
| `ClientHello` & `Client certificate verified`    | OpenVPN performs TLS negotiation, validating the user’s certificate.       |
| `new connection`, virtual IP assignment          | Provides a secure session and assigns the client a tunnel IP (`10.8.0.2`). |
| `PUSH_REPLY` with routing options                | Server pushes client configuration (e.g., default gateway, DNS settings).  |
| `Data Channel` cipher confirmation               | Confirms which cipher is used for encrypting data.                         |
| `Initialization Sequence Completed`              | Indicates full successful setup of the VPN tunnel.                         |


#### Sample Client Log (Windows OpenVPN Connect / ovpn.log)
```bash
Tue Aug 13 09:15:06 2025 OpenVPN 2.5.9 x86_64-w64-mingw32 [...]
Tue Aug 13 09:15:06 2025 Attempting to establish TCP connection with [AF_INET]server.example.com:443
Tue Aug 13 09:15:06 2025 TCP connection established with [AF_INET]203.0.113.123:443
Tue Aug 13 09:15:07 2025 TLS: Initial packet from [AF_INET]203.0.113.123:443, sid=abc123...
Tue Aug 13 09:15:07 2025 VERIFY OK: depth=1, CN=CA
Tue Aug 13 09:15:07 2025 VERIFY OK: depth=0, CN=server
Tue Aug 13 09:15:07 2025 Control Channel: TLSv1.2, cipher TLSv1.2 ECDHE-RSA-AES256-GCM-SHA384
Tue Aug 13 09:15:07 2025 Data Channel: using negotiated cipher 'AES-256-GCM'
Tue Aug 13 09:15:07 2025 [alice] Peer Connection Initiated with [AF_INET]203.0.113.123:443
Tue Aug 13 09:15:08 2025 TUN/TAP device opened: \\.\Global\{...}
Tue Aug 13 09:15:08 2025 ROUTE: default_gateway=192.168.1.1
Tue Aug 13 09:15:08 2025 Initialization Sequence Completed
```
#### #### What These Entries Mean on Client Side

| Log Entry                             | What It Means                                                      |
| ------------------------------------- | ------------------------------------------------------------------ |
| `VERIFY OK: ...`                      | Server’s certificate chain is trusted—authenticity confirmed       |
| `Control Channel: TLSv1.2, cipher...` | Secure control channel (handles auth and negotiation) is encrypted |
| `Data Channel: ...`                   | Data tunnel is now encrypted with AES-256-GCM                      |
| `Peer Connection Initiated`           | VPN session established with the server endpoint                   |
| `TUN/TAP device opened`               | Virtual network interface created for routing secure traffic       |
| `ROUTE: default_gateway=...`          | Routing updated—traffic now flows through the VPN tunnel           |
| `Initialization Sequence Completed`   | Final confirmation that VPN is fully functional and ready for use  |

---

###  Common Push Configurations
| Push Directive                                   | Purpose                                                                        | Example                                                                                         |
| ------------------------------------------------ | ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| **`route`**                                      | Pushes network routes so the client can reach internal subnets through the VPN | `push "route 10.0.0.0 255.255.255.0"` → routes client traffic to internal network `10.0.0.0/24` |
| **`redirect-gateway`**                           | Sends all client traffic through the VPN (full-tunnel)                         | `push "redirect-gateway def1 bypass-dhcp"`                                                      |
| **`dhcp-option` (DNS)**                          | Sets DNS servers for the client while connected                                | `push "dhcp-option DNS 8.8.8.8"` <br> `push "dhcp-option DNS 8.8.4.4"`                          |
| **`dhcp-option` (Domain)**                       | Sets search domain for DNS resolution                                          | `push "dhcp-option DOMAIN example.com"`                                                         |
| **`block-outside-dns`** (Windows only)           | Prevents DNS leaks on Windows clients                                          | `push "block-outside-dns"`                                                                      |
| **`topology`**                                   | Specifies client subnet topology (net30, p2p, etc.)                            | `push "topology subnet"`                                                                        |
| **`route-metric`**                               | Assigns priority to pushed routes                                              | `push "route 10.0.0.0 255.255.255.0 1"`                                                         |
| **`ping/ping-restart`**                          | Keepalive to maintain VPN connectivity                                         | `push "ping 10"` <br> `push "ping-restart 120"`                                                 |
| **`compression`** (deprecated in latest OpenVPN) | If enabled, client uses compression                                            | `push "compress lz4"`                                                                           |
| **`client-config-dir`**                          | Can push client-specific config options                                        | Example: different routes or access per client                                                  |

### Sample Push Config from Server
```bash
server 10.8.0.0 255.255.255.0
push "route 10.0.1.0 255.255.255.0"
push "route 10.0.2.0 255.255.255.0"
push "redirect-gateway def1 bypass-dhcp"
push "dhcp-option DNS 10.0.0.53"
push "dhcp-option DOMAIN corp.local"
push "block-outside-dns"
```

#### Explanation:

- VPN subnet: 10.8.0.0/24
- Internal routes pushed: 10.0.1.0/24, 10.0.2.0/24
- All traffic routed through VPN (redirect-gateway)
- DNS server pushed: 10.0.0.53
- Domain search: corp.local
- Block DNS leaks on Windows clients

#### Client log example for Push Config:

```bash
PUSH: Received control message: 'PUSH_REPLY,route 10.0.1.0 255.255.255.0,route 10.0.2.0 255.255.255.0,dhcp-option DNS 10.0.0.53,dhcp-option DOMAIN corp.local,redirect-gateway def1,b
lock-outside-dns'
Options error: --block-outside-dns is not supported on this platform
Initialization Sequence Completed
```
