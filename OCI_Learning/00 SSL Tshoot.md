Here’s a comprehensive list of **common SSL issues** that DevOps, cloud engineers, or network security engineers often encounter, along with explanations and tips for resolving them.

---

## 🔐 Common SSL Issues

### 1. **Expired SSL Certificate**

* 🔍 **Symptom**: Browser shows "Your connection is not private" or `ERR_CERT_DATE_INVALID`
* 🛠 **Fix**: Renew the SSL certificate and reload it into your server/load balancer.

---

### 2. **Mismatched Domain (CN or SAN)**

* 🔍 **Symptom**: "Certificate not valid for this domain"
* 🛠 **Fix**: Ensure the **Common Name (CN)** or **Subject Alternative Names (SAN)** in the certificate match the domain (e.g., `www.example.com` ≠ `example.com`).

---

### 3. **Incomplete Certificate Chain (Missing Intermediate CA)**

* 🔍 **Symptom**: Works in some browsers but fails in others
* 🛠 **Fix**: Install the **full certificate chain**, including intermediate CAs, especially on load balancers like Nginx, Apache, OCI LB, or AWS ALB.

---

### 4. **Self-Signed Certificate in Production**

* 🔍 **Symptom**: Clients/browsers reject the connection
* 🛠 **Fix**: Use certificates from a **trusted Certificate Authority (CA)** such as Let's Encrypt, DigiCert, or OCI-issued certs via Certificate Management.

---

### 5. **Incorrect SSL Binding/Listener Configuration**

* 🔍 **Symptom**: "Connection refused" or "No SSL configured"
* 🛠 **Fix**:

  * For web servers: Ensure port 443 is listening with SSL context.
  * For cloud LBs (OCI/AWS): Make sure correct cert is attached to the **HTTPS listener**.

---

### 6. **SSL Protocol Mismatch / Weak Ciphers**

* 🔍 **Symptom**: SSL handshake failure; `sslv3 alert handshake failure`
* 🛠 **Fix**: Ensure both client and server support a common protocol (e.g., TLS 1.2 or 1.3) and strong ciphers. Disable SSLv2, SSLv3, TLS 1.0.

---

### 7. **Wrong Certificate Key Pair**

* 🔍 **Symptom**: Web server won’t start or shows key mismatch error
* 🛠 **Fix**: Ensure the **certificate, private key**, and **intermediate bundle** are from the same request (matching key-pair).

---

### 8. **Load Balancer with Backend SSL**

* 🔍 **Symptom**: Backend health checks fail, 502/504 errors
* 🛠 **Fix**: Make sure backend servers are:

  * Using valid certificates (trusted or self-signed with trust override)
  * Using correct ports (e.g., 443 or custom)
  * In sync with LB's backend configuration (SSL vs non-SSL)

---

### 9. **Time Skew on Server**

* 🔍 **Symptom**: SSL validation errors (even with valid certs)
* 🛠 **Fix**: Ensure **system time is accurate**. Use `ntpd` or `chronyd` on Linux to sync time.

---

### 10. **Wildcard vs Subdomain Certificate Mismatch**

* 🔍 **Symptom**: `api.dev.example.com` fails with cert for `*.example.com`
* 🛠 **Fix**: Wildcards only match one level (e.g., `*.example.com` matches `app.example.com`, not `dev.app.example.com`)

---

## 🔧 Useful Commands to Debug SSL

```bash
# Test SSL certificate and chain
openssl s_client -connect yourdomain.com:443 -showcerts

# Check expiry date
openssl x509 -in cert.pem -noout -dates

# Test TLS handshake and supported protocols
nmap --script ssl-enum-ciphers -p 443 yourdomain.com
```

---

