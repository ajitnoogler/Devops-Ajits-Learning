# ✅ SSL Troubleshooting Checklist

Use this checklist to debug and resolve common SSL/TLS issues in cloud, on-prem, and web server environments.

---
## 🔐 SSL Troubleshooting Checklist (Summary Table)

| ✅ Checkpoint Category         | 🔍 What to Verify                                              | 🛠️ Suggested Command / Fix                                    |
|-------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|
| **1. Certificate Validity**   | Is the cert expired? Does domain match CN/SAN?                | `openssl x509 -in cert.pem -noout -dates`                     |
| **2. Certificate Chain**      | Is the full chain installed (leaf + intermediates)?           | `openssl s_client -connect domain:443 -showcerts`             |
| **3. Key Pair Match**         | Does private key match the cert?                              | `openssl rsa/x509 -modulus | openssl md5`                    |
| **4. Listener Configuration** | Is HTTPS listener bound on port 443 correctly?                | Check server/LB listener settings                             |
| **5. Load Balancer Settings** | Is SSL termination set up? Backend set using right protocol? | Check LB SSL config and backend health check protocols        |
| **6. TLS/SSL Protocols**      | Are modern protocols (TLS 1.2/1.3) enabled?                   | `nmap --script ssl-enum-ciphers -p 443 domain`                |
| **7. Cipher Suites**          | Are weak ciphers (e.g., RC4, 3DES) disabled?                  | Check server or LB cipher list                                |
| **8. Time Sync**              | Is system clock synced via NTP?                              | `timedatectl` or `chronyc sources`                            |
| **9. DNS Mapping**            | Does the cert cover all subdomains via CN/SAN or wildcard?    | Verify DNS records and cert SAN list                          |
| **10. Client Errors**         | Are browsers or curl showing specific SSL handshake errors?   | Review client logs and run `curl -v https://yourdomain.com`   |
```

---

✅ Paste this in your GitHub `.md` file as-is.  
Let me know if you’d like this in collapsible `<details>` sections or with links to deeper docs per row!


---

## 🔍 1. Certificate Validity

- [ ] Is the SSL certificate expired?
- [ ] Does the certificate match the domain name (CN or SAN)?
- [ ] Is the certificate issued by a trusted CA?

> 💡 Use:
> ```bash
> openssl x509 -in cert.pem -noout -dates
> ```

---

## 🔗 2. Certificate Chain (Trust Path)

- [ ] Is the **intermediate certificate** properly installed?
- [ ] Is the full certificate chain provided (Root → Intermediate → Leaf)?
- [ ] Are all clients/browsers able to validate the chain?

> 💡 Use:
> ```bash
> openssl s_client -connect yourdomain.com:443 -showcerts
> ```

---

## 🔐 3. SSL Key Pair Matching

- [ ] Does the private key match the public certificate?
- [ ] Are you loading the correct `.crt`, `.key`, and `.ca-bundle` files?

> 💡 Test match:
> ```bash
> openssl x509 -noout -modulus -in cert.pem | openssl md5
> openssl rsa -noout -modulus -in key.pem | openssl md5
> ```

---

## 🌐 4. Listener & Port Configuration

- [ ] Is SSL/TLS listener configured on port 443?
- [ ] Is the SSL cert bound to the correct listener?
- [ ] Are backend servers using the expected port (443 or custom)?

---

## 🔁 5. Load Balancer Settings (OCI / AWS / Nginx)

- [ ] Is SSL termination enabled at the load balancer?
- [ ] Is backend set using HTTPS or HTTP correctly?
- [ ] Are health checks failing due to SSL mismatch?
- [ ] Are correct cipher suites and TLS versions configured?

---

## 🧱 6. Protocols and Ciphers

- [ ] Is the server using modern TLS (1.2 or 1.3)?
- [ ] Are insecure protocols (SSLv2, SSLv3, TLS 1.0) disabled?
- [ ] Are weak ciphers removed?

> 💡 Use:
> ```bash
> nmap --script ssl-enum-ciphers -p 443 yourdomain.com
> ```

---

## ⏲️ 7. Server Clock Sync

- [ ] Is system time synced with NTP?
- [ ] Is there a time drift that may cause validation errors?

---

## 🌍 8. DNS and Domain Issues

- [ ] Is the domain pointed to the correct IP?
- [ ] Is there a wildcard or SAN mismatch?
- [ ] Are subdomain certs properly configured?

---

## 🔧 9. Client-Side SSL Errors

- [ ] What’s the exact browser or curl error?
- [ ] Is the full error trace captured (e.g., SSL handshake, trust failure)?
- [ ] Are proxy or firewall settings interfering with SSL?

---

## 📤 10. Tools & Debugging Commands

```bash
# Test SSL connection
openssl s_client -connect yourdomain.com:443

# View certificate details
openssl x509 -in cert.pem -text -noout

# Fetch certificate from server
echo | openssl s_client -servername yourdomain.com -connect yourdomain.com:443 2>/dev/null | openssl x509 -text

# Check protocol support
nmap --script ssl-enum-ciphers -p 443 yourdomain.com
```

---

## 🛠 Recommended SSL Best Practices

- Always enable TLS 1.2 or 1.3 only.
- Redirect HTTP → HTTPS using 301.
- Enable HSTS headers for HTTPS-only enforcement.
- Rotate expiring certs 15–30 days before expiration.
- Use Let's Encrypt for automation or OCI Certificate Management.

---

> 🧠 Pro Tip: Document cert issuance and renewal procedures in your DevOps runbooks to avoid surprises!

