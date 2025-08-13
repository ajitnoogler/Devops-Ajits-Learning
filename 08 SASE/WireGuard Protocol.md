

WireGuard is a modern, lightweight VPN protocol designed to be faster, simpler, and more secure than traditional VPN technologies like IPsec and OpenVPN.

#### What is WireGuard?
- Type: Layer 3 (network layer) VPN protocol
- Transport: Runs over UDP only
- Encryption: Uses state-of-the-art cryptography (Noise Protocol Framework)
- Key Exchange: Curve25519 ECDH
- Data Encryption: ChaCha20 for symmetric encryption + Poly1305 for authentication
- Handshake: Minimal (2 messages) with short-lived session keys (rotated every ~2 mins)
- Codebase: Extremely small (~4,000 lines) compared to OpenVPN/IPsec (100k+ lines) → Easier to audit & less attack surface
---
#### Why WireGuard is Used for VPN
WireGuard is chosen for speed, simplicity, and security:

| Feature            | Why it Matters for VPN                     | WireGuard Advantage                                  |
| ------------------ | ------------------------------------------ | ---------------------------------------------------- |
| **Performance**    | Faster browsing, gaming, file transfers    | Uses UDP + ChaCha20 (fast on all CPUs)               |
| **Security**       | Protects data confidentiality & integrity  | Modern, strong crypto suite, forward secrecy         |
| **Low Latency**    | Needed for real-time apps like VoIP        | Small handshake, minimal overhead                    |
| **Cross-Platform** | VPN must work everywhere                   | Runs on Linux, Windows, macOS, Android, iOS, routers |
| **Simplicity**     | Easier deployment, fewer misconfigurations | Only 2 message handshake, static keys, simple config |
| **Reliability**    | Needs to survive roaming & NAT             | Built-in roaming support via endpoint detection      |

---
#### Where WireGuard is Used
- Corporate remote access VPNs
- Site-to-site secure tunnels between branch offices
- Privacy-focused consumer VPN services (e.g., Mullvad, NordVPN, ProtonVPN)
- Embedded systems/routers (e.g., OpenWrt, Mikrotik, Ubiquiti)
- Mobile VPNs (low CPU usage, battery-friendly)
---
#### WireGuard in VPN Context
A VPN (Virtual Private Network) needs:
- Encryption – Hide traffic from eavesdroppers
- Authentication – Verify endpoints are trusted
- Tunneling – Encapsulate packets to send them privately over the internet
---
#### WireGuard delivers these by:
- Creating a virtual network interface (wg0) on each peer
- Encrypting outgoing packets and sending via UDP
- Decrypting incoming packets before passing them to the OS
- Using public/private key pairs to authenticate peers (no usernames/passwords)
---

``` bash
+----------------+                                  +----------------+
| Peer A         |                                  | Peer B         |
| (Initiator)    |                                  | (Responder)    |
+----------------+                                  +----------------+

    | --[Message 1: Handshake Initiation]----------------------------> |
    |   - Initiator ephemeral pubkey (X25519)                          |
    |   - Encrypted static pubkey                                      |
    |   - Encrypted timestamp                                          |
    |   - MAC1 (identity binding)                                      |
    |   - MAC2 (cookie proof, if required)                             |

    | <----------------[Message 2: Handshake Response]---------------- |
    |   - Responder ephemeral pubkey (X25519)                          |
    |   - Encrypted static pubkey                                      |
    |   - Encrypted timestamp                                          |
    |   - MAC1 / MAC2                                                  |

    | *** Key derivation complete – both peers have session keys ***   |

    | --[Message 3: Transport Data]----------------------------------> |
    |   - Receiver index                                               |
    |   - Encrypted payload (ChaCha20-Poly1305)                        |
    |   - Message counter                                              |

    | <----------------[Message 4: Transport Data]-------------------- |
    |   - Receiver index

```

#### Flow Summary
- Message 1 – Initiator sends handshake initiation.
- Message 2 – Responder sends handshake response.
- Message 3+ – Encrypted data packets start flowing in both directions.
- Optional Cookie Reply – Used for DoS protection before accepting handshake.

---

  WireGuard can be used for **both**:

---

## **1. Site-to-Site VPN**

* **Use Case:** Connects two or more fixed networks (e.g., branch office to HQ).
* **How WireGuard Fits:**

  * Each peer (router, firewall, or Linux box) runs a WireGuard interface.
  * Static public IPs or dynamic DNS used for endpoints.
  * Routes are exchanged manually in config.
  * Minimal overhead → high throughput between sites.

**Example:**

```
Branch Office LAN 10.10.1.0/24
   |
[WireGuard Router]
   ↔ Internet ↔
[WireGuard Router]
   |
HQ LAN 10.10.2.0/24
```

---

## **2. Remote Access VPN (RAVPN)**

* **Use Case:** Securely connects individual remote users (laptops, phones) to a corporate network.
* **How WireGuard Fits:**

  * Client devices run WireGuard client software.
  * Server in HQ or cloud runs WireGuard and allows user’s public key.
  * Supports roaming (good for mobile users).
  * Lower battery usage compared to OpenVPN on phones.

**Example:**

```
Remote User Laptop/Phone (WireGuard)
   ↔ Internet ↔
WireGuard VPN Server @ HQ
   |
Corporate LAN 10.10.0.0/24
```

---

## **Key Difference in Use**

| Feature       | Site-to-Site            | Remote Access                     |
| ------------- | ----------------------- | --------------------------------- |
| **Purpose**   | Connects whole networks | Connects single users             |
| **Endpoints** | Routers/firewalls       | Laptops, mobiles, home PCs        |
| **Routing**   | Subnet-based            | Single IP per user or small range |
| **Scaling**   | Few tunnels             | Many user tunnels                 |

---

💡 **In practice:**

* Enterprises often deploy WireGuard for **site-to-site** because of high performance and easy router integration.
* Many privacy VPN providers and companies deploy it for **RAVPN** because it’s lightweight and secure for end-users.

---

#### WireGuard VPN Deployment Scenarios

<img width="512" height="307" alt="image" src="https://github.com/user-attachments/assets/3f960cdd-b282-4884-9407-636e93f47604" />

---

#### WireGuard Cryptographic Suite

WireGuard uses a fixed modern crypto suite: Curve25519 for key exchange, ChaCha20 for encryption, and Poly1305 for authentication. 
BLAKE2s for hashing, and HKDF for key derivation, all implemented via the Noise_IK pattern. 
No cipher negotiation is allowed, which avoids downgrade attacks and keeps configs simple

| Function                          | Algorithm                               | Purpose                                                                          |
| --------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------- |
| **Key Exchange**                  | **Curve25519**                          | Elliptic Curve Diffie–Hellman (ECDH) for fast and secure key agreement           |
| **Symmetric Encryption**          | **ChaCha20**                            | Stream cipher for encrypting data (fast on all CPUs, including mobile/low-power) |
| **Message Authentication**        | **Poly1305**                            | MAC (Message Authentication Code) for ensuring packet integrity                  |
| **Hash Function**                 | **BLAKE2s**                             | Fast, secure hashing for key derivation and message digests                      |
| **Key Derivation Function (KDF)** | **HKDF** (using BLAKE2s)                | Derives keys from ECDH shared secrets                                            |
| **Random Number Generation**      | **System RNG** + `libsodium` primitives | Secure randomness for key material                                               |
| **Protocol Framework**            | **Noise\_IK**                           | Noise Protocol handshake pattern (“Initiator-Known”)                             |

