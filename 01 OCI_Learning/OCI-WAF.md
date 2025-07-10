# 🔐 What is OCI WAF?

OCI WAF (Web Application Firewall) is a cloud-native security service that protects web applications from common Layer 7 (Application Layer) threats by inspecting HTTP/HTTPS traffic before it reaches your origin servers.
It is fully managed, scalable, and integrated into Oracle Cloud's edge and regional architecture.---

## 🔐 **Does OCI WAF perform SSL Offloading or SSL Decryption?**

# 🧠 Key Capabilities of OCI WAF
| Feature                      | Description                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------ |
| **Global Protection**        | Deployed at OCI's **edge PoPs worldwide** for low-latency protection.          |
| **Layer 7 Threat Detection** | Blocks attacks like **SQL injection, Cross-Site Scripting (XSS), CSRF, etc.**  |
| **Bot Management**           | Detects and mitigates **malicious or abusive bots** (scraping, login abuse).   |
| **Rate Limiting**            | Limits request rates per IP/user to **mitigate DoS and brute-force attacks.**  |
| **Custom Rules & Policies**  | Allows custom **access control rules**, **IP whitelisting/blacklisting**, etc. |
| **SSL Offloading**           | Terminates HTTPS at WAF for inspection; forwards HTTP or HTTPS to backend.     |
| **Logging & Monitoring**     | Integrated with **OCI Logging**, **Monitoring**, and **Alarm services.**       |


# 🛡️ Protection Capabilities

| Category             | Example Threats                          |
| -------------------- | ---------------------------------------- |
| **OWASP Top 10**     | SQLi, XSS, CSRF, Command Injection, etc. |
| **Bot Attacks**      | Credential stuffing, scraping, scanners  |
| **Abuse Prevention** | Rate-limiting login/signup/checkout      |
| **Access Control**   | Block/allow by IP, geo, header, URL path |

🔗 Where is OCI WAF Deployed?
You can attach WAF to:
✅ Public Load Balancers
✅ Web Application Firewall Policy for origin IPs
✅ Content Delivery Network (CDN) endpoints
✅ Edge nodes (global low-latency points)

# 🧱 Architecture Example:

Client (Browser)
    ↓ HTTPS
OCI WAF (Edge or Regional)
    ↓ HTTP or HTTPS
OCI Load Balancer (Public or Private)
    ↓
Backend Web App (Compute/Container)

# 📌 When to Use OCI WAF
Use OCI WAF when you want to:
Secure web apps against internet-based attacks
Comply with PCI-DSS, HIPAA, or ISO 27001
Protect apps without deploying appliances
Centralize L7 security policies in a cloud-native way

# ✅ Summary
OCI WAF = Application Layer Firewall (HTTP/HTTPS)
It performs SSL offloading, deep HTTP inspection, and threat blocking at OCI’s edge.
Works in conjunction with Load Balancers, CDN, or custom origin servers.

**OCI WAF performs SSL Offloading, not SSL Decryption for Deep Packet Inspection like a firewall.**

---

## 📘 **Explanation:**

### 🔸 **SSL Offloading in OCI WAF:**

* **Yes, supported.**
* OCI WAF terminates the **HTTPS (SSL/TLS)** connection from the client.
* This allows the WAF to:

  * Inspect the HTTP request payload
  * Apply **WAF rules** (SQLi, XSS, CSRF, Bot Protection, etc.)
  * Forward the traffic (optionally re-encrypted) to the backend origin.

```text
Client ──HTTPS──▶ OCI WAF (SSL Offload + Inspect) ──HTTP or HTTPS──▶ Backend App
```

* You **upload your TLS certificate** to OCI WAF to enable this.
* WAF rules operate on **Layer 7 HTTP data** (URL, headers, body).

---

### 🔸 **SSL Decryption (Deep Packet Inspection like Palo Alto)?**

* **No, not supported.**
* OCI WAF **does not**:

  * Act as a firewall that inspects all ports/protocols.
  * Analyze or decrypt arbitrary encrypted traffic like Palo Alto NGFW.
  * Do deep TLS session replay, malware detection, or DLP.

---

## 🔍 Summary Table

| Feature                       | **OCI WAF**             | **Palo Alto NGFW**                       |
| ----------------------------- | ----------------------- | ---------------------------------------- |
| **SSL Offloading**            | ✅ Yes                   | ❌ Not the main purpose (but can decrypt) |
| **SSL Decryption (Security)** | ❌ No                    | ✅ Yes (full SSL decryption/inspection)   |
| **Layer**                     | Layer 7 (HTTP/HTTPS)    | Layers 3–7 (Full stack)                  |
| **Purpose**                   | App-layer protection    | Threat prevention, DLP, URL filtering    |
| **Certificate Required?**     | ✅ Yes (uploaded to WAF) | ✅ Yes (for forward trust)                |

---

## 🔐 Use Case of OCI WAF SSL Offloading

* Protect a **web application** (e.g., hosted behind OCI Load Balancer or origin server).
* Terminate HTTPS at WAF → Apply rules → Forward request.
* Reduce certificate management burden on backend services.
* Combine with Load Balancer for better routing/performance.

---

# 🎯 Use Case: Secure HTTPS Web App via WAF with Inspection and Forwarding

           ┌────────────────────────────┐
           │     Internet Clients       │
           │   (Browsers / Mobile Apps) │
           └─────────────┬──────────────┘
                         │ HTTPS (443)
                         ▼
             ┌─────────────────────────┐
             │        OCI WAF          │
             │ (SSL Offload + Rules)   │
             └─────────────┬───────────┘
                      ┌────▼─────┐
                      │WAF Rules │
                      │(SQLi, XSS│
                      │Bot, etc.)│
                      └────┬─────┘
                           │
             ┌─────────────▼─────────────┐
             │   HTTPS or HTTP Forward   │
             │ (To backend with or w/o   │
             │  re-encryption)           │
             └─────────────┬─────────────┘
                           │
               ┌───────────▼────────────┐
               │     OCI Load Balancer │
               │ (Optional - L7/L4 LB) │
               └───────────┬────────────┘
                           │
           ┌───────────────▼──────────────┐
           │   Backend Web Application    │
           │  (Compute VM / Container /   │
           │   Web Server in Private Subnet)│
           └──────────────────────────────┘


# 🧠 Key Flow:
Client sends HTTPS request to https://your-app.com.
OCI WAF terminates SSL (offloading), inspects HTTP Layer 7.
WAF applies security rules: SQLi, XSS, Bot Management, etc.
WAF forwards the request to backend (HTTP or re-encrypted HTTPS).
Backend processes the request and responds via same path.


# 🧰 Components Involved:
| Component                        | Purpose                               |
| -------------------------------- | ------------------------------------- |
| **OCI WAF**                      | SSL Offloading + L7 threat protection |
| **OCI Load Balancer (optional)** | Load balance to backend pool          |
| **Backend App Servers**          | Application tier (private subnet)     |
| **Internet Gateway or WAF Edge** | Enables public HTTPS access           |


Absolutely, Ajit! Here's a detailed, production-grade **OCI WAF Policy Creation Runbook** – ideal for cloud architects or DevSecOps engineers deploying secure web applications.

---

# 🛡️ **OCI WAF Policy Creation Runbook**

### 🎯 **Goal**: Protect a web application with OCI WAF using a custom WAF Policy attached to a public load balancer or origin server.

---

## ✅ **Step 1: Prerequisites**

Make sure you have:

* Oracle Cloud **Tenancy** access with appropriate IAM permissions
* A working **Load Balancer** (HTTP or HTTPS)
* Your **backend web server** or application up and running
* Optional: A **TLS certificate** if terminating HTTPS at WAF

---

## 🧱 **Step 2: Create a WAF Policy**

### 🔹 Navigate to:

**OCI Console → Security → Web Application Firewall → WAF Policies**

### 🔹 Click: **Create WAF Policy**

#### Fill in the following:

| Field                           | Value Example                                 |
| ------------------------------- | --------------------------------------------- |
| **Name**                        | `web-app-prod-waf-policy`                     |
| **Compartment**                 | `prod-applications`                           |
| **Policy Type**                 | `Load Balancer` or `Origin`                   |
| **Protection Rules**            | ✅ Enable recommended OWASP Top 10 protections |
| **Bot Management**              | Enable if needed                              |
| **Protection Capability Level** | Medium or High                                |
| **Logging**                     | Enable Logging for visibility                 |

---

## 🔐 **Step 3: Add Origin / Load Balancer as Protected Resource**

After WAF policy is created:

### 🔹 Click on the WAF Policy → **Protected Resources → Add Resource**

| Field                | Value                                          |
| -------------------- | ---------------------------------------------- |
| **Resource Type**    | Load Balancer or Origin                        |
| **Load Balancer**    | Select your LB (e.g., `prod-lb`)               |
| **Listener**         | `HTTPS:443` (recommended)                      |
| **Protocol**         | HTTPS (to use SSL offloading)                  |
| **Backend Protocol** | HTTP or HTTPS (depends on your backend config) |

---

## 🧠 **Step 4: Add Access Rules (Optional, but Recommended)**

Navigate to **Access Control → Add Rule**

### 🔸 Sample Rule: Block IP Range

```text
Name: block-suspicious-range
Action: BLOCK
Conditions:
  IP Address in Range: 203.0.113.0/24
```

### 🔸 Sample Rule: Allow Only Country

```text
Name: allow-india-traffic
Action: ALLOW
Conditions:
  GEO Location: IN (India)
```

---

## 🚦 **Step 5: Add Rate Limiting Rules (Optional)**

Navigate to **Rate Limiting → Add Rule**

| Field              | Example                   |
| ------------------ | ------------------------- |
| **Name**           | `login-rate-limit`        |
| **Path Condition** | `/login`                  |
| **Threshold**      | 50 requests / minute / IP |
| **Action**         | BLOCK or Delay            |

---

## 🛡️ **Step 6: Enable Bot Management (Optional)**

In **Bot Management Section**:

* Enable **Good Bots** (Googlebot, Bingbot)
* Block or Challenge **Unknown/Bad Bots**
* Add CAPTCHA for suspicious behavior

---

## 📡 **Step 7: Logging and Monitoring**

### 🔸 Enable Logging:

Go to **Logging → Enable**

* Select or create a **Log Group**
* View logs in **OCI Logging → Log Explorer**

### 🔸 Set Alarms:

Use **OCI Monitoring → Alarms** to trigger alerts on:

* Request Rate Spikes
* Blocked Request Count
* Bot Activity

---

## ✅ **Step 8: Validate the WAF Functionality**

* Open the public domain of your app.
* Use tools like **curl**, **Postman**, or **Burp Suite** to simulate:

  * SQL Injection → `curl -X GET "https://yourapp.com/?q=' OR 1=1 --"`
  * Bot user-agent headers
* Confirm expected **WAF blocking** in logs and response.

---

## ✅ Final Tips

| Best Practice                         | Reason                                        |
| ------------------------------------- | --------------------------------------------- |
| Use **HTTPS with WAF**                | Enables SSL offloading + encrypted delivery   |
| Set **Default Action to ALLOW**       | Start in monitor mode before going aggressive |
| **Test before enabling strict rules** | Avoid blocking legit users                    |
| Use **CAPTCHA** or **Challenge**      | For suspicious but not malicious requests     |

---

# 🔁 Summary of What You’re Doing in These Steps:
| Step | What You're Configuring                        | OCI Service Area                        |
| ---- | ---------------------------------------------- | --------------------------------------- |
| 1    | Create WAF policy                              | **Security → Web Application Firewall** |
| 2    | Attach to Load Balancer or Origin server       | **Protected Resource Setup**            |
| 3    | Enable OWASP protections                       | **Protection Rules Section**            |
| 4    | Add access control rules (IP, geo, headers)    | **Access Control Section**              |
| 5    | Add rate limiting (throttle per IP/path)       | **Rate Limiting Section**               |
| 6    | Enable bot protection                          | **Bot Management Section**              |
| 7    | Enable logging and monitoring                  | **OCI Logging / Monitoring**            |
| 8    | Test your setup using tools like curl, Postman | **Validation / Security Testing**       |

# 🧠 OCI Services That Integrate with WAF:
OCI Load Balancer (as the frontend to apps)
OCI Logging (for WAF logs and alerts)
OCI Monitoring / Alarms (track traffic patterns)
Origin Servers or CDNs (optional backend endpoints)

# 🛡️ OCI CLI Runbook – WAF Policy Creation

Perfect, Ajit! Here's a **step-by-step OCI WAF setup using the OCI CLI**, including all key commands you’ll need to **create a WAF policy**, **attach a Load Balancer**, and **configure rules**.

---

# 🛡️ **OCI CLI Runbook – WAF Policy Creation**

## 🧰 **Assumptions:**

* You’ve configured OCI CLI (`oci setup config`)
* You have:

  * **Compartment OCID**
  * **Load Balancer OCID**
  * Optional: **TLS certificate and key** (for SSL offloading)

---

## ✅ Step 1: Create a WAF Policy

```bash
oci waf web-app-firewall-policy create \
  --compartment-id <compartment_ocid> \
  --display-name "webapp-waf-policy" \
  --actions '{}'
```

📌 This creates an empty policy. You will attach rules and origins next.

---

## ✅ Step 2: Attach Protected Resource (Load Balancer)

```bash
oci waf web-app-firewall create \
  --compartment-id <compartment_ocid> \
  --display-name "webapp-waf" \
  --web-app-firewall-policy-id <policy_ocid> \
  --backend-type LOAD_BALANCER \
  --backend-id <load_balancer_ocid> \
  --web-app-firewall-traffic-route-rules '[
    {
      "conditionLanguage": "JMESPATH",
      "actionName": "ACCESS_CONTROL",
      "condition": "request.url.path contains `/`",
      "priority": 1
    }
  ]'
```

---

## ✅ Step 3: Add OWASP Rules (Protection Capabilities)

```bash
oci waf protection-rule add \
  --web-app-firewall-policy-id <policy_ocid> \
  --protection-rule-keys '[
    "981176", "SQLI", "XSS", "CSRF", "COMMAND_INJECTION"
  ]'
```

Or enable all recommended rules:

```bash
oci waf web-app-firewall-policy update \
  --web-app-firewall-policy-id <policy_ocid> \
  --protection-rules '[
    {
      "ruleKey": "981176",
      "action": "DETECT",
      "modSecurityRuleIds": [],
      "isEnabled": true
    }
  ]'
```

---

## ✅ Step 4: Add Access Control Rule (e.g., block IP)

```bash
oci waf access-rule add \
  --web-app-firewall-policy-id <policy_ocid> \
  --access-rules '[
    {
      "name": "block-bad-ip",
      "condition": {
        "addressRateLimiting": {
          "isEnabled": false,
          "allowedRatePerAddress": 0
        },
        "addressList": ["203.0.113.0/24"]
      },
      "action": "BLOCK"
    }
  ]'
```

---

## ✅ Step 5: Add Rate Limiting Rule

```bash
oci waf rate-limiting-rule add \
  --web-app-firewall-policy-id <policy_ocid> \
  --rate-limiting-rules '[
    {
      "name": "limit-login-attempts",
      "action": "BLOCK",
      "criteria": {
        "httpMethod": "POST",
        "urlPath": "/login"
      },
      "rateInRequestsPerSecond": 2
    }
  ]'
```

---

## ✅ Step 6: Enable Logging (Optional but recommended)

First, create a log group:

```bash
oci logging log-group create \
  --compartment-id <compartment_ocid> \
  --display-name "waf-log-group"
```

Then create a WAF log:

```bash
oci logging log create \
  --log-group-id <log_group_ocid> \
  --display-name "waf-logs" \
  --log-type SERVICE \
  --source-service WAF \
  --source-resource <waf_resource_id>
```

---

## ✅ Step 7: Validate

Use `curl` or `browser`:

```bash
curl -k https://your-domain.com/?q='OR 1=1'
```

* Look for `403` or `blocked` in response.
* Confirm logs appear in OCI Logging.

---

## 📁 Optional: Upload SSL Cert for WAF (if origin requires HTTPS)

```bash
oci waf certificate create \
  --compartment-id <compartment_ocid> \
  --display-name "ssl-cert" \
  --certificate-data file://cert.pem \
  --private-key-data file://key.pem
```

Then attach it to the WAF resource.

---

## ✅ Summary

| Task                   | Command Reference                        |
| ---------------------- | ---------------------------------------- |
| Create Policy          | `oci waf web-app-firewall-policy create` |
| Attach to LB           | `oci waf web-app-firewall create`        |
| Add Rules              | `access-rule`, `protection-rule`, etc.   |
| Enable Logs            | `oci logging log create`                 |
| Upload Cert (optional) | `oci waf certificate create`             |

---

# 🧪 OCI WAF Validation via curl – Attack Simulation Cheat Sheet

Absolutely, Ajit! Here’s a list of **advanced `curl` commands** to **validate OCI WAF protection** for real-world web attacks like **SQL Injection**, **XSS**, **CSRF**, and more.

These test patterns simulate **OWASP Top 10** threats and are commonly used to test **Web Application Firewall (WAF) inspection**.

---

# 🧪 **OCI WAF Validation via `curl` – Attack Simulation Cheat Sheet**

Replace:

* `https://your-domain.com` with your actual domain behind OCI WAF

---

## 🔍 1. **SQL Injection (SQLi)**

### 🔸 Basic SQLi (already given)

```bash
curl -k "https://your-domain.com/?q=' OR 1=1 --"
```

### 🔸 UNION-based SQLi

```bash
curl -k "https://your-domain.com/search.php?q=test' UNION SELECT NULL, NULL --"
```

### 🔸 Time-based Blind SQLi

```bash
curl -k "https://your-domain.com/item?id=1'; WAITFOR DELAY '0:0:5' --"
```

### 🔸 Error-based SQLi

```bash
curl -k "https://your-domain.com/?id=1' AND 1=CONVERT(int, 'text') --"
```

---

## 🌐 2. **Cross-Site Scripting (XSS)**

### 🔸 Script Injection (reflected)

```bash
curl -k "https://your-domain.com/?search=<script>alert('XSS')</script>"
```

### 🔸 Event-based XSS

```bash
curl -k "https://your-domain.com/?q=<img src=x onerror=alert('xss')>"
```

### 🔸 JavaScript URI

```bash
curl -k "https://your-domain.com/?url=javascript:alert('xss')"
```

---

## 🛑 3. **Cross-Site Request Forgery (CSRF)**

### 🔸 Simulated CSRF request (change password)

```bash
curl -k -X POST https://your-domain.com/change-password \
  -d "user=admin&newpass=hacked" \
  -H "Referer: https://evil.com" \
  -H "Origin: https://evil.com"
```

> ✅ OCI WAF can block based on suspicious Referer/Origin headers.

---

## 🤖 4. **Bot Signature Testing**

### 🔸 Suspicious User-Agent (scraper)

```bash
curl -k -A "sqlmap/1.3.2" https://your-domain.com/
```

### 🔸 Fake Googlebot

```bash
curl -k -A "Googlebot/2.1 (+http://fake.com/bot.html)" https://your-domain.com/
```

---

## 🧨 5. **Command Injection**

```bash
curl -k "https://your-domain.com/?input=;cat /etc/passwd"
```

---

## 📦 6. **Path Traversal**

```bash
curl -k "https://your-domain.com/download?file=../../../../etc/passwd"
```

---

## 🔐 7. **Credential Stuffing Simulation**

```bash
for i in {1..10}; do
  curl -k -X POST https://your-domain.com/login \
    -d "user=admin&pass=wrong$i"
done
```

> Useful to test **rate-limiting rules** and **bot detection**.

---

## 🧠 8. **Encoded Attack Payload**

### 🔸 URL-encoded XSS

```bash
curl -k "https://your-domain.com/?q=%3Cscript%3Ealert('XSS')%3C/script%3E"
```

### 🔸 SQLi with URL encoding

```bash
curl -k "https://your-domain.com/?id=1%27%20OR%201%3D1--"
```

---

## ✅ Best Practice: Enable Logging

Enable **OCI WAF logging** so you can verify:

* Blocked requests
* Matched rules
* Source IPs and headers

---

## 🧪 Summary Table

| Threat Type       | Example Test   | Expected WAF Action |
| ----------------- | -------------- | ------------------- |
| SQLi              | `' OR 1=1 --`  | Block               |
| XSS               | `<script>`     | Block               |
| CSRF              | Evil `Referer` | Block or CAPTCHA    |
| Bot               | `sqlmap UA`    | Block or Challenge  |
| Path Traversal    | `../`          | Block               |
| Command Injection | `;cat`         | Block               |

---

# 🛡️ create_oci_waf_policy.sh — Automate OCI WAF Setup
#!/bin/bash

### --- CONFIGURATION SECTION --- ###
COMPARTMENT_OCID="<your_compartment_ocid>"
LOAD_BALANCER_OCID="<your_load_balancer_ocid>"
LB_BACKEND_PROTOCOL="HTTP"           # or HTTPS
WAF_POLICY_NAME="ajit-waf-policy"
WAF_NAME="ajit-web-app-firewall"
LOG_GROUP_NAME="ajit-waf-log-group"
ENABLE_LOGGING=true                  # Set to false to skip logging

### --- INTERNAL --- ###
TIMESTAMP=$(date +%F-%H%M)
TMP_FILE="/tmp/waf-policy-setup-$TIMESTAMP.log"

echo "🚀 Starting OCI WAF Policy Setup - $TIMESTAMP"
echo "Log File: $TMP_FILE"

# STEP 1: Create WAF Policy
echo "🧱 Creating WAF Policy..."
WAF_POLICY_OCID=$(oci waf web-app-firewall-policy create \
  --compartment-id "$COMPARTMENT_OCID" \
  --display-name "$WAF_POLICY_NAME" \
  --actions '{}' \
  --query 'data.id' --raw-output)

echo "✅ Created WAF Policy: $WAF_POLICY_OCID" | tee -a "$TMP_FILE"

# STEP 2: Create Web App Firewall & bind to Load Balancer
echo "🔗 Creating Web App Firewall..."
oci waf web-app-firewall create \
  --compartment-id "$COMPARTMENT_OCID" \
  --display-name "$WAF_NAME" \
  --web-app-firewall-policy-id "$WAF_POLICY_OCID" \
  --backend-type LOAD_BALANCER \
  --backend-id "$LOAD_BALANCER_OCID" \
  --web-app-firewall-traffic-route-rules '[
    {
      "conditionLanguage": "JMESPATH",
      "actionName": "ACCESS_CONTROL",
      "condition": "request.url.path contains `/`",
      "priority": 1
    }
  ]' >> "$TMP_FILE"

echo "✅ Web App Firewall Created" | tee -a "$TMP_FILE"

# STEP 3: Add OWASP Protection Rules
echo "🛡️ Enabling OWASP Protection Rules..."
oci waf web-app-firewall-policy update \
  --web-app-firewall-policy-id "$WAF_POLICY_OCID" \
  --protection-rules '[
    {
      "ruleKey": "981176",
      "action": "DETECT",
      "isEnabled": true
    },
    {
      "ruleKey": "SQLI",
      "action": "BLOCK",
      "isEnabled": true
    },
    {
      "ruleKey": "XSS",
      "action": "BLOCK",
      "isEnabled": true
    }
  ]' >> "$TMP_FILE"
echo "✅ OWASP Protection Rules Applied" | tee -a "$TMP_FILE"

# STEP 4: Add Access Rule (Block IP)
echo "🔐 Adding Access Rule..."
oci waf access-rule add \
  --web-app-firewall-policy-id "$WAF_POLICY_OCID" \
  --access-rules '[
    {
      "name": "block-bad-ip",
      "condition": {
        "addressList": ["203.0.113.0/24"]
      },
      "action": "BLOCK"
    }
  ]' >> "$TMP_FILE"
echo "✅ Access Rule Added" | tee -a "$TMP_FILE"

# STEP 5: Add Rate Limiting Rule
echo "🚦 Adding Rate Limiting Rule..."
oci waf rate-limiting-rule add \
  --web-app-firewall-policy-id "$WAF_POLICY_OCID" \
  --rate-limiting-rules '[
    {
      "name": "limit-login-attempts",
      "action": "BLOCK",
      "criteria": {
        "httpMethod": "POST",
        "urlPath": "/login"
      },
      "rateInRequestsPerSecond": 2
    }
  ]' >> "$TMP_FILE"
echo "✅ Rate Limiting Rule Added" | tee -a "$TMP_FILE"

# STEP 6: Optional Logging
if [ "$ENABLE_LOGGING" = true ]; then
  echo "📘 Creating Log Group and WAF Log..."
  LOG_GROUP_OCID=$(oci logging log-group create \
    --compartment-id "$COMPARTMENT_OCID" \
    --display-name "$LOG_GROUP_NAME" \
    --query 'data.id' --raw-output)

  oci logging log create \
    --log-group-id "$LOG_GROUP_OCID" \
    --display-name "waf-log" \
    --log-type SERVICE \
    --source-service WAF \
    --source-resource "$WAF_POLICY_OCID" >> "$TMP_FILE"
  echo "✅ Logging Enabled (Group: $LOG_GROUP_NAME)" | tee -a "$TMP_FILE"
fi

echo "🏁 OCI WAF Setup Complete"
echo "📄 Full Log: $TMP_FILE"

========================================================================================================================



# 🧪 OCI WAF Validation Script (Bash)

#!/bin/bash

TARGET="https://your-domain.com"   # 🔁 Replace with your actual domain
LOG_FILE="/tmp/waf_test_results_$(date +%F_%H-%M-%S).log"

echo "🛡️ OCI WAF Validation Script Started" | tee -a $LOG_FILE
echo "Target: $TARGET" | tee -a $LOG_FILE
echo "Log File: $LOG_FILE"
echo "------------------------------------------" | tee -a $LOG_FILE

test_case() {
  local description=$1
  local curl_cmd=$2

  echo -e "\n🔹 Test: $description" | tee -a $LOG_FILE
  echo "Command: $curl_cmd" >> $LOG_FILE
  echo "------------------------------------------" >> $LOG_FILE
  eval "$curl_cmd" >> $LOG_FILE 2>&1
  echo "==========================================" >> $LOG_FILE
  sleep 1
}

# --- SQL Injection ---
test_case "SQLi Basic" "curl -sk \"$TARGET/?q=' OR 1=1 --\""
test_case "SQLi UNION SELECT" "curl -sk \"$TARGET/search.php?q=test' UNION SELECT NULL,NULL--\""
test_case "SQLi Time-based Blind" "curl -sk \"$TARGET/item?id=1'; WAITFOR DELAY '0:0:5' --\""
test_case "SQLi Error-based" "curl -sk \"$TARGET/?id=1' AND 1=CONVERT(int, 'text') --\""

# --- XSS ---
test_case "XSS <script>" "curl -sk \"$TARGET/?search=<script>alert('XSS')</script>\""
test_case "XSS img onerror" "curl -sk \"$TARGET/?q=<img src=x onerror=alert('xss')>\""
test_case "XSS javascript URI" "curl -sk \"$TARGET/?url=javascript:alert('xss')\""

# --- CSRF ---
test_case "CSRF POST Origin Spoof" \
"curl -sk -X POST $TARGET/change-password -d \"user=admin&newpass=hacked\" -H \"Origin: https://evil.com\" -H \"Referer: https://evil.com\""

# --- Command Injection ---
test_case "Command Injection ;cat" "curl -sk \"$TARGET/?input=;cat /etc/passwd\""

# --- Path Traversal ---
test_case "Path Traversal" "curl -sk \"$TARGET/download?file=../../../../etc/passwd\""

# --- Bot Emulation ---
test_case "User-Agent sqlmap" "curl -sk -A \"sqlmap/1.3.2\" $TARGET"
test_case "Fake Googlebot" "curl -sk -A \"Googlebot/2.1 (+http://fake.com/bot.html)\" $TARGET"

# --- Rate Limiting (Credential Stuffing) ---
echo -e "\n🔹 Test: Credential Stuffing (Rate Limiting Simulation)" | tee -a $LOG_FILE
for i in {1..10}; do
  echo "Attempt $i" >> $LOG_FILE
  curl -sk -X POST "$TARGET/login" -d "user=admin&pass=wrong$i" >> $LOG_FILE 2>&1
  echo "------" >> $LOG_FILE
  sleep 1
done

# --- Encoded Payloads ---
test_case "URL Encoded XSS" "curl -sk \"$TARGET/?q=%3Cscript%3Ealert('XSS')%3C/script%3E\""
test_case "URL Encoded SQLi" "curl -sk \"$TARGET/?id=1%27%20OR%201%3D1--\""

# --- Summary ---
echo -e "\n✅ All WAF validation tests completed." | tee -a $LOG_FILE
echo "📝 Review log at: $LOG_FILE"
