
### Flow:

   <img width="321" height="488" alt="image" src="https://github.com/user-attachments/assets/5179c0d7-870a-4a62-97c2-626f1c232031" />


User Device → DNS Resolution for office 365 → Tunnel to SASE POP → ZTNA → SWG → CASB → FWaaS → DLP → O365 Optimization → Egress to Microsoft 365 Edge → Microsoft Tenant Services

Key Features:

- ZTNA (Zero Trust Network Access) — Identity and device posture validation before granting access.

- SWG (Secure Web Gateway) — URL filtering, malware scanning, DLP enforcement.

- DLP: Content Inspection | SSL Decrypt | Regex Pattern Match PCI, GDPR, Credit Card, Social Sec No. | Context aware where data is going.

- CASB Enforcement — Monitors SaaS activity for sanctioned/unsanctioned use.

- O365 Optimization — Routes Office 365 traffic directly via optimized peering.

- Split Tunnel Support — Allows selective breakout of non-corporate traffic.

--- 

* **Common packet flow issues**
* **Harmony-specific CLI/GUI checks**
* **Packet capture points**
* **Quick fix steps**

---

## **Check Point Harmony SASE – Office 365 Troubleshooting Runbook**

| Step | Issue                             | Possible Cause                                            | Harmony-Specific Checks                                                                                                                   | Resolution                                                                                 |
| ---- | --------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| 1    | **Slow O365 performance**         | User connected to distant POP; O365 traffic not optimized | GUI → *Portal* → **Monitoring → Users** → Check POP location; `cpdiag logs` for latency; verify *Microsoft 365 Optimized Routing* setting | Force POP selection via policy; enable *Microsoft 365 Egress Optimization* in SWG settings |
| 2    | **DNS resolution failures**       | Harmony DNS proxy blocked or wrong policy                 | GUI → *Policy → Web Filtering* → check DNS rules; CLI: `cpview` → *DNS Queries*; packet capture with `fw monitor`                         | Allow O365 FQDNs in policy; verify *DNS over HTTPS* (DoH) settings                         |
| 3    | **ZTNA authentication failure**   | Posture check fail; SSO misconfig                         | GUI → *Policy → Zero Trust Access* → check device posture rules; CLI: `show logs user <username>`                                         | Fix posture profile; verify Azure AD SAML integration; re-enroll endpoint                  |
| 4    | **SSL inspection breaks O365**    | TLS interception unsupported for some O365 endpoints      | GUI → *Policy → HTTPS Inspection* → add O365 URL categories to bypass list; CLI: `cat /opt/CPsuite-R81/fw1/conf/https_inspection.xml`     | Follow Check Point’s *M365 SSL Inspection Bypass List* KB                                  |
| 5    | **CASB over-blocking**            | Strict policy for SaaS actions                            | GUI → *Cloud App Control* → search for “Microsoft 365” → check allowed actions; logs in *SmartEvent*                                      | Allow sanctioned O365 functions; whitelist tenant domains                                  |
| 6    | **DLP false positives**           | Pattern matches legit uploads                             | GUI → *Policy → Data Loss Prevention* → check matched rules; logs in *SmartEvent* with “DLP” filter                                       | Adjust regex/patterns; exclude trusted O365 services                                       |
| 7    | **Firewall blocking O365**        | FWaaS policy missing service tags                         | GUI → *Policy → Access Control* → ensure Microsoft 365 category/service is allowed; CLI: `fw log`                                         | Add Microsoft 365 service category; use dynamic objects instead of static IPs              |
| 8    | **Tunnel drops frequently**       | ISP instability; MTU mismatch                             | Endpoint: `vpn tu` or Harmony Client logs; `tcpdump` on WAN interface                                                                     | Adjust MTU in Harmony Client; change tunnel keepalive interval; test alternate connection  |
| 9    | **High latency for non-O365**     | All traffic hairpinned via same POP                       | GUI → *Policy → Application Control* → configure *Local Breakout* for non-sensitive traffic                                               | Enable split-tunnel for non-critical SaaS and browsing                                     |
| 10   | **Clientless access not working** | Not enabled in ZTNA policy                                | GUI → *Policy → Zero Trust Access → Clientless Access* → check app list                                                                   | Add O365 to clientless access; verify portal URL is accessible externally                  |

---

## **Packet Capture & Log Points**

1. **On Endpoint (Harmony Client)**

   * Location: `%AppData%\CheckPoint\Logs` (Windows) or `/var/log/harmony/` (Linux/macOS)
   * Capture command (Windows):

     ```powershell
     netsh trace start capture=yes tracefile=C:\temp\capture.etl
     ```

2. **On SASE POP (TAC-Only for Deep Debug)**

   * `fw monitor -e "accept;"` — captures all traffic
   * `tcpdump -i <interface> host <O365_IP>`

3. **On Management Portal**

   * *Logs & Monitoring* → Filter by user & application “Microsoft 365”
   * Check: latency, POP name, SSL bypass applied, policy matched

---

## **Quick Fix Checklist**

✅ Verify user lands on nearest POP
✅ Ensure Microsoft 365 category bypasses SSL inspection
✅ Use dynamic service tags instead of static IPs
✅ Enable *Microsoft 365 Egress Optimization* in Harmony
✅ Check posture profile & SSO integration for ZTNA
✅ Use split-tunnel for non-O365 traffic to reduce POP load

---
