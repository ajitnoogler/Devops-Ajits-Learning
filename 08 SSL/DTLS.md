
### 1. DTLS in Harmony SASE

#### DTLS = Datagram Transport Layer Security

- It’s basically TLS over UDP instead of TCP.

- Provides the same encryption/authentication as TLS but avoids TCP’s handshake/retransmission delays.

- In Harmony SASE, the Harmony Connect Agent can use DTLS over UDP 443 for its tunnel instead of standard TLS over TCP 443.

- Why it matters for remote users:

    - Better performance on high-latency or lossy connections (like Wi-Fi, LTE).

    - Avoids “TCP over TCP meltdown” that happens when tunneling TCP inside TCP.

    - Often auto-selected if UDP 443 is open on the network; falls back to TLS/TCP if blocked.
 

####  Example in Harmony Flow:

User Device → SASE Client  (DTLS/UDP 443) →  DNS Resolution → Tunnel to SASE POP → ZTNA → SWG → CASB → FWaaS → DLP → O365 Optimization → Egress to Microsoft 365 Edge → Microsoft Tenant Services

#### DTLS Apps:

- Browsers and apps (Google Meet, Zoom Web, MS Teams Web, etc.) use DTLS for encrypting media and data channels.

- SIP over DTLS (SIP-DTLS-SRTP) – secure VoIP calls.
