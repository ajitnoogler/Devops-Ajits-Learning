
#### What is WireGuard?
WireGuard is a modern, lightweight VPN protocol designed to be faster, simpler, and more secure than traditional VPN technologies like IPsec and OpenVPN.
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
    |   - MAC1 / MAC2                                                   |

    | *** Key derivation complete – both peers have session keys ***   |

    | --[Message 3: Transport Data]----------------------------------> |
    |   - Receiver index                                               |
    |   - Encrypted payload (ChaCha20-Poly1305)                        |
    |   - Message counter                                              |

    | <----------------[Message 4: Transport Data]------------------- |
    |   - Receiver index                                               |
    |   - Encrypted payload                                            |
    |   - Message counter                                              |

    | --[Optional: Cookie Reply]-------------------------------------> |
    |   (Only if DoS protection triggered)                             |
    |   - Receiver index                                               |
    |   - Encrypted MAC key                                            |

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

---

<img width="1193" height="733" alt="image" src="https://github.com/user-attachments/assets/6c893ce1-9745-4448-a2ce-890345fc4ceb" />


---

Here’s a **step-by-step sample WireGuard deployment** on **Ubuntu** for a **Remote Access VPN client** scenario.
We’ll configure:

* **Server**: Ubuntu (acts as VPN gateway)
* **Client**: Ubuntu laptop (remote user)

---

## **1. Install WireGuard**

On **both server and client**:

```bash
sudo apt update
sudo apt install wireguard
```

---

## **2. Generate Keys**

### On the **Server**:

```bash
cd /etc/wireguard
umask 077
wg genkey | tee server_private.key | wg pubkey > server_public.key
```

### On the **Client**:

```bash
cd /etc/wireguard
umask 077
wg genkey | tee client_private.key | wg pubkey > client_public.key
```

---

## **3. Server Configuration**

File: `/etc/wireguard/wg0.conf`

```ini
[Interface]
Address = 10.0.0.1/24
ListenPort = 51820
PrivateKey = SERVER_PRIVATE_KEY
# Enable IP forwarding
PostUp   = sysctl -w net.ipv4.ip_forward=1; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = sysctl -w net.ipv4.ip_forward=0; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE

[Peer]
# Client configuration on server side
PublicKey = CLIENT_PUBLIC_KEY
AllowedIPs = 10.0.0.2/32
```

Replace:

* `SERVER_PRIVATE_KEY` → contents of `/etc/wireguard/server_private.key`
* `CLIENT_PUBLIC_KEY` → contents of `/etc/wireguard/client_public.key`

---

## **4. Client Configuration**

File: `/etc/wireguard/wg0.conf`

```ini
[Interface]
Address = 10.0.0.2/24
PrivateKey = CLIENT_PRIVATE_KEY
DNS = 1.1.1.1

[Peer]
# Server configuration on client side
PublicKey = SERVER_PUBLIC_KEY
Endpoint = SERVER_PUBLIC_IP:51820
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
```

Replace:

* `CLIENT_PRIVATE_KEY` → contents of `/etc/wireguard/client_private.key`
* `SERVER_PUBLIC_KEY` → contents of `/etc/wireguard/server_public.key`
* `SERVER_PUBLIC_IP` → public IP of your VPN server

---

## **5. Enable & Start WireGuard**

On **both server and client**:

```bash
sudo wg-quick up wg0
```

Enable at boot:

```bash
sudo systemctl enable wg-quick@wg0
```

---

## **6. Verify Connection**

On **Server**:

```bash
sudo wg
```

You should see the client’s public key and latest handshake time.

On **Client**:

```bash
ping 10.0.0.1
ping 8.8.8.8
```

If `AllowedIPs = 0.0.0.0/0`, all internet traffic will route through the VPN.

---

## **7. Firewall & NAT Notes**

* Ensure UDP port **51820** is open on the server’s firewall:

```bash
sudo ufw allow 51820/udp
```

* NAT is handled by the `iptables` `MASQUERADE` rule in **PostUp**.

---

✅ **Result:**

* Remote client connects to WireGuard server over UDP.
* Client gets IP `10.0.0.2`, can reach `10.0.0.1` and the corporate network.
* All traffic is encrypted using WireGuard’s fixed crypto suite.

---

#### WireGuard Remote Access VPN setup

```bash
[Remote Client: Ubuntu Laptop]                  [VPN Server: Ubuntu @ HQ]
     PrivateKey: client_private.key                  PrivateKey: server_private.key
     PublicKey:  client_public.key                   PublicKey:  server_public.key
     Address:    10.0.0.2/24                         Address:    10.0.0.1/24
     Endpoint:   SERVER_PUBLIC_IP:51820 (UDP)        ListenPort: 51820/UDP
     AllowedIPs: 0.0.0.0/0                           AllowedIPs: 10.0.0.2/32
     DNS:        1.1.1.1

          |---------------- Handshake Initiation ---------------->|
          |<--------------- Handshake Response -------------------|
          |<====== Encrypted Tunnel (ChaCha20 + Poly1305) =========>|
          |             10.0.0.2 ↔ 10.0.0.1 (VPN subnet)            |
          |                 Internet / Corporate LAN                |
```

---

####  Ubuntu Remote Access VPN setup and the WireGuard handshake + data flow messages in one view.

``` bash
[Remote Client: Ubuntu Laptop]                     [VPN Server: Ubuntu @ HQ]
  PrivateKey: client_private.key                      PrivateKey: server_private.key
  PublicKey:  client_public.key                       PublicKey:  server_public.key
  Address:    10.0.0.2/24                             Address:    10.0.0.1/24
  Endpoint:   SERVER_PUBLIC_IP:51820 (UDP)            ListenPort: 51820/UDP
  AllowedIPs: 0.0.0.0/0                               AllowedIPs: 10.0.0.2/32
  DNS:        1.1.1.1                                 NAT to Internet / Corp LAN

   --------------------------- WIREGUARD PACKET FLOW ---------------------------

  (1) Handshake Initiation  -->  
        - Ephemeral pubkey (Curve25519)
        - Encrypted static pubkey
        - Encrypted timestamp
        - MAC1 / MAC2

  <---  (2) Handshake Response
        - Ephemeral pubkey (Curve25519)
        - Encrypted static pubkey
        - Encrypted timestamp
        - MAC1 / MAC2

  *** Session keys derived via ECDH + HKDF (BLAKE2s) ***

  <===> (3) Encrypted Data (Transport Message)
        - Receiver index
        - Encrypted payload (ChaCha20)
        - Poly1305 authentication tag
        - Counter for replay protection

  *** Tunnel Established ***
       VPN Subnet: 10.0.0.2 ↔ 10.0.0.1
       All client internet traffic passes via server (AllowedIPs = 0.0.0.0/0)
```

