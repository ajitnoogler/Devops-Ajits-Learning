#### The **Active Directory user authentication packet flow with ports** so you can see exactly what’s happening at the network level.

---

## **1. Kerberos Authentication Packet Flow with Ports**

**Scenario:** User `ajit@corp.local` logs into a domain-joined machine and accesses a file share on `fileserver.corp.local`.

```
[Client]                [Domain Controller (KDC)]                [Service Server]
   |                             |                                       |
1. |---- AS-REQ ---------------->| UDP/TCP 88                            |
2. |<--- AS-REP -----------------| UDP/TCP 88                            |
3. |---- TGS-REQ ---------------->| UDP/TCP 88                            |
4. |<--- TGS-REP -----------------| UDP/TCP 88                            |
5. |---- AP-REQ ----------------------------------------------->| TCP 445 (SMB) or service port 443
6. |<--- AP-REP (optional) ------------------------------------| TCP 445 (SMB) or service port 443
``` 

**Step Details with Ports:**

1. **AS-REQ** (Authentication Service Request) → Client → DC over **UDP/TCP 88**.
2. **AS-REP** (Authentication Service Reply) → DC → Client over **UDP/TCP 88**.
3. **TGS-REQ** (Ticket Granting Service Request) → Client → DC over **UDP/TCP 88**.
4. **TGS-REP** (Ticket Granting Service Reply) → DC → Client over **UDP/TCP 88**.
5. **AP-REQ** (Application Request) → Client presents service ticket to server over **TCP 445** (for SMB) or the app’s port (e.g., **TCP 443** for HTTPS).
6. **AP-REP** (optional Application Reply) over same service port.


#### Service Server - File Server | Web-app | DB | Email Etc.

---

## **2. NTLM Authentication Packet Flow with Ports**

**Used when Kerberos fails** (e.g., no SPN, cross-forest without trust).

```
[Client]               [Server]                     [Domain Controller]
   |                      |                                 |
1. |-- Negotiate -------->| TCP 445 (SMB) / TCP 443 (HTTP)  |
2. |<-- Challenge --------| TCP 445 / TCP 443               |
3. |-- Response --------->| TCP 445 / TCP 443               |
4. |                      |-- Verify w/ DC --> TCP/UDP 135 (RPC), TCP 139/445, ephemeral ports
5. |<--- Success/Fail ----| TCP 445 / TCP 443               |
```

**Port Notes:**

* **Client ↔ Server:** SMB (**TCP 445**), HTTP(S) (**TCP 80/443**), or other protocol port.
* **Server ↔ DC:**

  * RPC Endpoint Mapper: **TCP/UDP 135**
  * SMB: **TCP 445**
  * NetBIOS Session: **TCP 139** (legacy)
  * Ephemeral ports for RPC (TCP **49152–65535** by default on Windows)

---

## **3. Combined Flow Diagram with Ports**

```
User Login -> Workstation
    |
    |--> Kerberos Path (Preferred)
    |    AS-REQ / AS-REP / TGS-REQ / TGS-REP  -> UDP/TCP 88 (Client ↔ DC)
    |    AP-REQ / AP-REP  -> TCP 445 (SMB) or target service port
    |
    +--> NTLM Path (Fallback)
         Negotiate/Challenge/Response -> TCP 445 or TCP 443 (Client ↔ Server)
         Server verifies with DC -> TCP/UDP 135, TCP 445, TCP 139, RPC high ports
```
---
