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

### OpenVPN Client Connection Issues Reference Table

| #  | Issue                                                  | Sample Client Log                                                                                                                                                    | Root Cause                                                                   | Quick Fix                                                                                      |
| -- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 1  | **TLS Handshake Failure**                              | `TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)`<br>`TLS Error: TLS handshake failed`                            | Mismatched certificates, wrong server IP/port, firewall/NAT blocking UDP/TCP | Verify server IP/port, check firewall, ensure correct client/server certs and keys             |
| 2  | **Authentication Failure**                             | `AUTH: Received control message: AUTH_FAILED`<br>`SIGUSR1[soft,auth-failure] received, process restarting`                                                           | Wrong username/password, failed PAM/LDAP/RADIUS integration                  | Check credentials, verify authentication backend, reset password if needed                     |
| 3  | **Network Connectivity Issue (No Internet/Resources)** | `Initialization Sequence Completed`<br>`PING: sendto failed: Network is unreachable`                                                                                 | Routing misconfiguration, overlapping subnets, firewall blocking VPN traffic | Verify `redirect-gateway` or pushed routes, check local network conflicts, adjust firewall/NAT |
| 4  | **Certificate Expired or Revoked**                     | `VERIFY ERROR: depth=1, error=certificate has expired: CN=OpenVPN-CA`<br>`TLS_ERROR: BIO read tls_read_plaintext error`                                              | Client/server certificate expired or revoked by CA                           | Renew/reissue certificates, update client configs                                              |
| 5  | **Cipher/Protocol Mismatch**                           | `Options error: Unrecognized option or missing parameter(s)`<br>`WARNING: 'cipher' is used inconsistently, local='AES-256-CBC', remote='AES-128-CBC'`                | Server and client use different encryption algorithms or TLS versions        | Align `cipher` and `auth` settings on client and server, check protocol version                |
| 6  | **Firewall/NAT Blocking**                              | `UDPv4 link local: [undef]`<br>`UDPv4 link remote: [AF_INET]203.0.113.10:1194`<br>`TLS Error: cannot locate HMAC in incoming packet from [AF_INET]203.0.113.10:1194` | NAT/firewall drops fragmented packets or blocks UDP/TCP                      | Try TCP instead of UDP, allow VPN port through firewall/NAT                                    |
| 7  | **DNS/Name Resolution Failure**                        | `Initialization Sequence Completed`<br>`DHCP option push failed: route/push`                                                                                         | VPN server did not push DNS or routing info                                  | Push `dhcp-option DNS x.x.x.x` from server, verify client routing table                        |
| 8  | **Server Unreachable / Timeout**                       | `TCP/UDP: Connecting to [server_ip]:1194...`<br>`Connection timed out`                                                                                               | Wrong IP, server down, firewall blocking                                     | Check server status, verify IP/port, test connectivity via ping/traceroute                     |
| 9  | **Configuration File Errors**                          | `Options error: unknown option 'xyz' in client config`                                                                                                               | Typo in `.ovpn` file or unsupported option                                   | Review config file, remove unsupported options, check OpenVPN version compatibility            |
| 10 | **MTU/Fragmentation Issues**                           | `TLS Error: incoming packet too large`<br>`Packet_write_timeout errors`                                                                                              | Network drops large packets, VPN MTU mismatch                                | Set `tun-mtu` or `fragment` in client/server config, enable `mssfix`                           |
| 11 |**TLS Peer Certificate Verification Failed** | `VERIFY ERROR: depth=0, error=self-signed certificate in certificate chain`                                                                                              | Certificate not trusted, self-signed                                              | - Add CA to client trusted store<br>- Use proper signed certificates                             |



