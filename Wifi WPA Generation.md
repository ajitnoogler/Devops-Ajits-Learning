
#### 📡 What Is WPA in Wi-Fi?

WPA (Wi-Fi Protected Access) is a family of security protocols developed by the Wi-Fi Alliance to protect wireless computer networks. 

It encrypts data over wireless connections and authenticates users connecting to a Wi-Fi network.

WPA (Wi-Fi Protected Access)** handshakes for **WPA1**, **WPA2**, and **WPA3**, including their workflow and known **vulnerabilities**:

---

#### 🔐 WPA1, WPA2, WPA3 – Handshake & Vulnerabilities Explained

---

#### 📘 Overview

| WPA Version  | Introduced | Key Protocol Used                           | Encryption |
| ------------ | ---------- | ------------------------------------------- | ---------- |
| **WPA (v1)** | 2003       | TKIP (RC4-based)                            | TKIP       |
| **WPA2**     | 2004       | 4-Way Handshake (CCMP)                      | AES        |
| **WPA3**     | 2018       | SAE (Simultaneous Authentication of Equals) | AES-GCMP   |

---

#### 🔄 WPA/WPA2 4-Way Handshake Workflow

Applies to **WPA1 and WPA2-Personal (Pre-Shared Key)**. WPA2 replaces TKIP with AES, but the handshake logic is similar.

```plaintext
Client            ↔             Access Point
   |                               |
   |<------ (1) ANonce ------------| ← AP sends a random nonce
   |                               |
   |------ (2) SNonce, MIC ------->| ← Client responds with its nonce and MIC
   |                               |
   |<------ (3) GTK, MIC ----------| ← AP sends group key and MIC
   |                               |
   |------ (4) ACK --------------->| ← Client sends acknowledgment
```

* Both sides derive the **PTK (Pairwise Transient Key)** from:

  * PMK (Pre-Shared Key derived from passphrase)
  * ANonce, SNonce
  * MAC addresses
 
#### Definations:

| Term       | Full Form              | Who Generates It        | Purpose / Role                                                         |
| ---------- | ---------------------- | ----------------------- | ---------------------------------------------------------------------- |
| **ANonce** | Authenticator Nonce    | Access Point (AP)       | Random number used in PTK derivation, sent in Message 1                |
| **SNonce** | Supplicant Nonce       | Client (STA/Supplicant) | Random number used in PTK derivation, sent in Message 2                |
| **MIC**    | Message Integrity Code | Both AP and Client      | Ensures integrity/authenticity of handshake messages using derived PTK |

---

#### 📦  WPA2 Handshake Messages

| Msg | From → To   | Contains                               | Purpose                       |
| --- | ----------- | -------------------------------------- | ----------------------------- |
| 1   | AP → Client | **ANonce**, RSN Info                   | Begin key negotiation         |
| 2   | Client → AP | **SNonce**, MIC, RSN Info              | Sends its nonce + verifies AP |
| 3   | AP → Client | **Group Temporal Key (GTK)**, MIC      | Sends GTK securely            |
| 4   | Client → AP | ACK with MIC (optional in some traces) | Confirms install of keys      |


#### 🧪 Wireshark Filter for WPA Handshake

eapol

eapol && wlan.fc.type_subtype == 0x08      // or for more specific filtering:

---

#### ❗ WPA/WPA2 Vulnerabilities

| Attack                | Affected Version  | Description                                                          |
| --------------------- | ----------------- | -------------------------------------------------------------------- |
| **KRACK**             | WPA2              | Key Reinstallation Attack — allows decryption by resetting keys.     |
| **Dictionary Attack** | WPA/WPA2-Personal | Capturing the handshake and brute-forcing weak passphrases.          |
| **PMKID Attack**      | WPA/WPA2          | Offline cracking using RSN IE field instead of full 4-way handshake. |
| **TKIP Attacks**      | WPA1              | RC4-based TKIP is vulnerable to replay and MIC key recovery.         |

---

#### 🔐 WPA3 SAE Handshake Workflow

WPA3 replaces the PSK-based handshake with a more secure **SAE** handshake using **Dragonfly Key Exchange**.

```plaintext
Client              ↔            Access Point
   |                               |
   |<-- Commit Message (AP) -------| ← Contains scalar & element (public keys)
   |-- Commit Message (Client) -->| ← Client responds with its commit
   |<-- Confirm Message ---------- | ← Confirm messages verify both identities
   |-- Confirm Message ----------->| ← Mutual confirmation
   |                               |
 (Both derive same PMK securely using password-authenticated key exchange)
```

---

#### ✅ WPA3 Security Improvements

| Feature                         | Benefit                                                                   |
| ------------------------------- | ------------------------------------------------------------------------- |
| **SAE (Dragonfly)**             | Resistant to offline dictionary attacks (no captured handshake to crack). |
| **Forward Secrecy**             | Past sessions can't be decrypted even if password is known later.         |
| **Protected Management Frames** | Prevents de-auth attacks, spoofing management frames.                     |
| **192-bit Mode (Enterprise)**   | Stronger cryptographic algorithms for high-security environments.         |

---

#### 📋 Summary of WPA3 SAE Exchange

| Message | Direction  | Payload               | Function                           |
| ------- | ---------- | --------------------- | ---------------------------------- |
| 1       | STA → AP   | SAE Commit            | Sends scalar & element             |
| 2       | AP → STA   | SAE Commit            | Responds with own scalar & element |
| 3       | STA → AP   | SAE Confirm           | Verifies AP scalar/element         |
| 4       | AP → STA   | SAE Confirm           | Verifies STA scalar/element        |
| 5–8     | (Optional) | EAPOL 4-Way Handshake | Same as WPA2, using PMK from SAE   |

---

#### ❗ WPA3 Vulnerabilities

| Vulnerability           | Description                                                              | Mitigation                            |
| ----------------------- | ------------------------------------------------------------------------ | ------------------------------------- |
| **Dragonblood Attacks** | Side-channel leaks in SAE implementation; can lead to password recovery. | Patch firmware; use constant-time ops |
| **Downgrade Attacks**   | Devices fall back to WPA2 if WPA3 not supported by client.               | Disable WPA2 fallback if possible     |

---

#### 🔐 Key Security Benefits of WPA3 SAE

| Feature                              | Benefit                                    |
| ------------------------------------ | ------------------------------------------ |
| 🔒 **No Offline Dictionary Attacks** | Each attempt requires active handshake     |
| 🔁 **Forward Secrecy**               | Keys are not reused across sessions        |
| ❌ **No PSK in Air**                  | Password is never sent or derived directly |

---

#### 🧪 Summary Comparison Table

| Feature               | WPA1            | WPA2            | WPA3 (SAE)       |
| --------------------- | --------------- | --------------- | ---------------- |
| Key Exchange          | 4-Way Handshake | 4-Way Handshake | SAE (Dragonfly)  |
| Encryption            | TKIP (RC4)      | AES-CCMP        | AES-GCMP         |
| Offline Attack Risk   | High            | High            | Low              |
| Forward Secrecy       | ❌               | ❌               | ✅                |
| PMF (Mgmt Protection) | ❌               | Optional        | Mandatory        |
| Status                | Deprecated      | Widely Used     | Current Standard |

---

