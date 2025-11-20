
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

---

Here’s a structured overview of **common issues when a client tries to connect to OpenVPN**, along with **sample log entries** from a Windows OpenVPN client (`.ovpn.log`) and explanations of what each entry usually means.

---

## 1. **TLS Handshake Failures**

**Symptoms:** Client cannot authenticate or connect. Often caused by mismatched certificates, incorrect keys, or firewall blocking UDP/TCP.

**Sample Log:**

```
TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
TLS Error: TLS handshake failed
```

**Explanation:**

* The client is unable to complete the TLS handshake with the server.
* Causes:

  * Incorrect `remote` IP or port in `.ovpn`.
  * UDP/TCP blocked by firewall/NAT.
  * Expired or mismatched certificates/keys.

---

## 2. **Authentication Failures**

**Symptoms:** Username/password authentication fails.

**Sample Log:**

```
AUTH: Received control message: AUTH_FAILED
SIGUSR1[soft,auth-failure] received, process restarting
```

**Explanation:**

* User credentials are incorrect.
* Might also occur if PAM, LDAP, or RADIUS integration fails on server side.

---

## 3. **Network Connectivity Issues**

**Symptoms:** Client connects but cannot reach VPN resources.

**Sample Log:**

```
Initialization Sequence Completed
PING: sendto failed: Network is unreachable
```

**Explanation:**

* VPN tunnel established, but routing is misconfigured.
* Causes:

  * Wrong `route` or `redirect-gateway` setting.
  * Conflicting local network (LAN overlaps VPN subnet).
  * Firewall blocks VPN traffic inside the network.

---

## 4. **Certificate Revoked or Expired**

**Sample Log:**

```
VERIFY ERROR: depth=1, error=certificate has expired: CN=OpenVPN-CA
TLS_ERROR: BIO read tls_read_plaintext error
```

**Explanation:**

* The client or server certificate has expired or is revoked in the CA.
* Solution: Renew certificates and update client configuration.

---

## 5. **Configuration Mismatch (Cipher/Protocol)**

**Sample Log:**

```
Options error: Unrecognized option or missing parameter(s) in client config
WARNING: 'cipher' is used inconsistently, local='AES-256-CBC', remote='AES-128-CBC'
```

**Explanation:**

* Server and client use different encryption algorithms.
* Make sure `cipher` and `auth` settings match on both ends.

---

## 6. **Firewall/NAT Issues**

**Symptoms:** Connection times out or handshake fails intermittently.

**Sample Log:**

```
UDPv4 link local: [undef]
UDPv4 link remote: [AF_INET]203.0.113.10:1194
TLS Error: cannot locate HMAC in incoming packet from [AF_INET]203.0.113.10:1194
```

**Explanation:**

* NAT device or firewall may block UDP packets or drop fragmented packets.
* Using TCP instead of UDP can help in restrictive networks.

---

## 7. **Client Routing/DNS Issues**

**Symptoms:** Can connect, but cannot resolve domain names.

**Sample Log:**

```
Initialization Sequence Completed
DHCP option push failed: route/push
```

**Explanation:**

* VPN server did not push correct DNS or routes.
* Solution:

  * Push `dhcp-option DNS x.x.x.x` from server.
  * Verify client routing table.

---

### ✅ Key Log Phases to Observe

1. **Resolving Server Address**

```
TCP/UDP: Connecting to [server_ip]:1194...
```

2. **TLS Handshake**

```
TLS: Initial packet from [server_ip]:1194, sid=...
```

3. **Authentication**

```
AUTH: Sent control message: AUTH
```

4. **Tunnel Initialization**

```
Initialization Sequence Completed
```

If any step fails, logs usually give a clue about whether it’s **TLS/auth/network/config** related.

---
