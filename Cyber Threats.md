

#### 🛡️ Cyber Threat Categories

A categorized view of various cyber threats, their types, and short descriptions:

| 🔒 Category                    | 🧨 Threat Type                          | 💡 Description |
|------------------------------|----------------------------------------|----------------|
| **1. Malware**               | Virus, Worm, Trojan, Ransomware        | Malicious software that infects, damages, or steals data from systems. |
|                              | Spyware, Adware, Rootkits              | Used for spying, displaying ads, or gaining privileged access. |
| **2. Phishing & Social Eng.**| Phishing, Spear Phishing               | Deceptive emails or messages trick users into revealing sensitive data. |
|                              | Vishing, Smishing                      | Voice or SMS-based phishing attacks. |
|                              | Pretexting, Baiting                    | Psychological manipulation to gain trust and access. |
| **3. Denial of Service (DoS)**| DoS, DDoS                              | Overwhelms systems/networks to make them unavailable. |
|                              | Application-layer attacks              | Targets specific apps (e.g., HTTP flood). |
| **4. Insider Threats**       | Malicious Insider                      | Employee intentionally causing harm. |
|                              | Negligent Insider                      | Unintended errors like misconfigurations or data leaks. |
|                              | Compromised Insider                    | Account hijacked by attacker. |
| **5. Credential Attacks**    | Brute Force, Dictionary Attack         | Repeated login attempts to guess passwords. |
|                              | Credential Stuffing                    | Reusing stolen credentials from other breaches. |
|                              | Keylogging                             | Capturing keystrokes to steal credentials. |
| **6. Web-Based Threats**     | SQL Injection, XSS, CSRF               | Exploits vulnerabilities in web apps to gain access or run scripts. |
|                              | Drive-by Downloads                     | Malware downloaded without user consent. |
|                              | Malvertising                          | Ads that deliver malware when clicked or viewed. |
| **7. Network Threats**       | Man-in-the-Middle (MitM)               | Eavesdropping or altering communication between two parties. |
|                              | DNS Spoofing, ARP Poisoning            | Redirecting traffic to malicious sites or machines. |
| **8. Cloud Threats**         | Misconfigured Cloud Storage            | Open buckets or containers leaking data. |
|                              | Cloud Jacking, Insecure APIs           | Gaining unauthorized access or exploiting cloud interfaces. |
| **9. Mobile Threats**        | Malicious Apps, Jailbreak Exploits     | Apps with hidden malware or rooting devices. |
|                              | Bluetooth/Wi-Fi Sniffing               | Intercepting unprotected data over wireless networks. |
| **10. Advanced Persistent Threats (APT)** | Nation-state/targeted attacks | Long-term, stealthy attacks aimed at specific entities (govt, corp). |
| **11. IoT Threats**          | Botnets (e.g., Mirai), Device Hijack   | Exploiting poorly secured smart devices for attacks. |
| **12. Supply Chain Attacks** | Software/Tainted Updates               | Compromising trusted software or vendors to infiltrate systems. |
| **13. Ransomware-as-a-Service (RaaS)** | Leased attack kits            | Ransomware provided as a service to cybercriminals. |
| **14. Zero-Day Exploits**    | Unknown vulnerabilities                | Attacks exploiting bugs before they’re patched. |


---

### 🎯 Advanced Persistent Threat (APT) Groups and Attacks

#### 🔍 What is APT (Advanced Persistent Threat)?

APT stands for Advanced Persistent Threat — a type of stealthy, continuous cyberattack typically sponsored by nation-states or highly organized criminal groups. 

These attackers target specific entities, often for espionage, intellectual property theft, sabotage, or long-term surveillance.

#### 🧠 Key Characteristics of APT

| 🧩 Attribute   | 📌 Description                                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Advanced**   | Uses sophisticated tools (e.g., zero-days, custom malware) and multi-stage attack chains (initial access, persistence, exfiltration). |
| **Persistent** | Maintains long-term access to systems without detection; attacker goal is not quick theft, but deep surveillance.                     |
| **Threat**     | Indicates a coordinated, well-funded adversary — often with political, military, or economic motivations.                             |

---
  
#### 🎯 APT Goals:

Espionage: Stealing sensitive government, military, or corporate data

Sabotage: Disrupting infrastructure (e.g., power grid, oil refineries)

Data Theft: Intellectual property, source code, research data

Surveillance: Tracking targets silently for months or years

Influence: Manipulating public opinion (e.g., election interference)

---

#### 🛠️ Common Techniques Used

| Tactic                        | Description                                |
| ----------------------------- | ------------------------------------------ |
| 🧬 **Spear Phishing**         | Targeted emails to gain initial access     |
| 🪝 **Zero-Day Exploits**      | Using unpatched vulnerabilities            |
| 🛠 **Custom Malware**         | Tailor-made spyware, backdoors, keyloggers |
| 📦 **Supply Chain Attacks**   | Infiltrating trusted software vendors      |
| 🌐 **C2 (Command & Control)** | Remote access to control infected systems  |
| 🕵️ **Lateral Movement**      | Expanding inside the network after breach  |
| 📤 **Data Exfiltration**      | Secretly transferring sensitive data out   |

---

### 🎯 Advanced Persistent Threat (APT) Groups and Attacks (with Years)

APT (Advanced Persistent Threat) groups are stealthy, nation-state-backed or highly organized cyber threat actors targeting sensitive industries with long-term campaigns.

| 🔢 No. | 🧠 APT Group (Alias)        | 🌍 Origin          | 🗓️ Year / Active Since       | 🎯 Common Targets                    | 🗂️ Notable Attacks / Campaigns                    |
|-------|-----------------------------|--------------------|-----------------------------|--------------------------------------|--------------------------------------------------|
| 1     | **APT1** (Comment Crew)     | China              | 2006–2013                  | U.S. defense, aerospace, tech        | Operation Shady RAT, Unit 61398 report           |
| 2     | **APT3** (Buckeye)          | China              | ~2010                      | Aerospace, critical infrastructure   | Pirpi malware, Windows zero-days                 |
| 3     | **APT10** (Stone Panda)     | China              | 2009–2017                  | MSPs, government, healthcare         | Operation Cloud Hopper                           |
| 4     | **APT28** (Fancy Bear)      | Russia             | ~2007–present              | NATO, political orgs, media          | DNC Hack (2016), Olympic Destroyer               |
| 5     | **APT29** (Cozy Bear)       | Russia             | ~2008–present              | Governments, think tanks, embassies  | SolarWinds Attack (2020)                         |
| 6     | **Sandworm** (BlackEnergy)  | Russia             | ~2014                      | Energy sector, Ukraine               | Ukraine power grid (2015), NotPetya (2017)       |
| 7     | **Lazarus Group**           | North Korea        | 2009–present               | Banking, crypto, defense             | Sony Hack (2014), WannaCry (2017), crypto thefts |
| 8     | **APT33** (Elfin)           | Iran               | ~2013                      | Aerospace, energy, Saudi firms       | Shamoon variants, phishing                       |
| 9     | **APT34** (OilRig)          | Iran               | ~2014                      | Finance, telecom, Middle East        | DNS hijacking, QUADAGENT                         |
| 10    | **APT35** (Charming Kitten) | Iran               | 2011–present               | Journalists, dissidents, academia    | Spoofed media sites, phishing                    |
| 11    | **APT32** (OceanLotus)      | Vietnam            | ~2012                      | SE Asian govts, businesses           | Watering hole attacks, macOS malware             |
| 12    | **DarkHotel**               | South Korea (suspected) | ~2007                 | Executives in luxury hotels          | WiFi injection, backdoor tools                   |
| 13    | **Turla** (Snake, Venomous Bear) | Russia        | 2004–present               | EU, embassies, diplomats             | Snake malware, satellite C2                      |
| 14    | **SideWinder**              | India              | ~2012                      | Pakistan military & gov              | Android & phishing campaigns                     |
| 15    | **Naikon**                  | China              | 2010–2015, 2020 resurgence | ASEAN governments                    | Aria-body malware, intel gathering               |
| 16    | **Equation Group**          | USA (NSA-linked)   | 2001–2015 (leaked 2016)    | Global infra, telecom, nuclear       | Stuxnet (2010), Flame, DoubleFantasy             |
| 15     | **Equation Group**    | NSA (Tailored Access Operations - TAO) | 2001–2015 (exposed 2016) | Telecom, nuclear, defense, global targets | **Stuxnet**, Flame, DoubleFantasy, Fanny worm |
| 16     | **Regin** (linked)    | NSA (alleged), GCHQ (UK)       | ~2003–2013             | EU telecoms, political targets          | Data exfiltration from telecom backbones      |
| 17     | **Lamberts**          | US (alleged, unconfirmed)      | ~2008–2017             | Middle East, Asia, EU targets           | Complex malware framework (Gray, Red, Blue Lambert) |


---
