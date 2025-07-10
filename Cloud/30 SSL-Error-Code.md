# 🔐 Common SSL/TLS Errors – with Meaning

| Error Code / Message                                | Description / Scenario                                             |
| --------------------------------------------------- | ------------------------------------------------------------------ |
| `SSL_ERROR_RX_RECORD_TOO_LONG`                      | SSL on port 80 (misconfiguration — should be HTTP not HTTPS)       |
| `SSL_ERROR_BAD_CERT_DOMAIN`                         | Certificate Common Name doesn’t match domain name                  |
| `ERR_CERT_DATE_INVALID`                             | Expired or future-dated certificate                                |
| `ERR_CERT_AUTHORITY_INVALID`                        | Self-signed cert not trusted by browser or system                  |
| `ERR_SSL_VERSION_OR_CIPHER_MISMATCH`                | Client and server don’t support common TLS version                 |
| `SSL_ERROR_HANDSHAKE_FAILURE_ALERT`                 | TLS negotiation failed (e.g., cipher mismatch or policy violation) |
| `SSL_ERROR_SYSCALL`                                 | Unexpected connection closure during SSL handshake                 |
| `SSL routines:ssl3_get_record:wrong version number` | TLS expected but received non-TLS traffic (wrong port?)            |
| `PR_END_OF_FILE_ERROR`                              | Server abruptly closed TLS connection (e.g., firewall, misconfig)  |
| `handshake_failure`                                 | Cipher suite mismatch or certificate rejected                      |

# 🔎 Use Cases in Cloud & LB Environments

| Use Case                | Likely Code or Error                       | Troubleshooting Tip                 |
| ----------------------- | ------------------------------------------ | ----------------------------------- |
| Backend App Crashed     | `500`, `502`, `504`                        | Check app logs and system resources |
| Wrong SSL on port 80    | `SSL_ERROR_RX_RECORD_TOO_LONG`             | Ensure HTTP traffic on port 80      |
| LB Health Check Failing | `503`, `502`, `404`, `500`                 | Test health check URL locally       |
| User reports SSL error  | `ERR_CERT_DATE_INVALID`, `BAD_CERT_DOMAIN` | Inspect cert validity + CN          |
| App Slow on Web         | `504`, `408`, `503`                        | Check response times, database, CPU |
| Too many login attempts | `429`, `403`                               | Rate limiting or WAF policy         |


# 🛠️ Tools to Inspect Codes in Practice

| Tool                           | Use                                            |
| ------------------------------ | ---------------------------------------------- |
| `curl -v`                      | Inspect HTTP codes and SSL handshake           |
| `openssl s_client -connect`    | Diagnose SSL/TLS cert and cipher info          |
| Browser DevTools → Network Tab | Analyze HTTP/HTTPS behavior per request        |
| Load Balancer Access Logs      | View request status and backend response codes |
| `dig` / `nslookup`             | Validate DNS and SSL CN matching               |

# 🛠️ Tools to Inspect HTTP Codes and SSL Errors – Cmds

| **Tool**                        | **Purpose**                                               | **Exact Command**                                                                                                              |
| ------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `curl -v`                       | View detailed HTTP/HTTPS status, redirects, SSL handshake | `curl -v http://app.example.com`<br>`curl -vk https://app.example.com`                                                         |
| `curl -I`                       | Show only HTTP headers (status, content-type, etc.)       | `curl -I http://app.example.com`                                                                                               |
| `openssl s_client`              | Inspect SSL cert, handshake, ciphers, CN mismatch, expiry | `openssl s_client -connect app.example.com:443`<br>`openssl s_client -connect app.example.com:443 -servername app.example.com` |
| `dig`                           | Quick DNS resolution (A record)                           | `dig +short app.example.com`                                                                                                   |
| `nslookup`                      | DNS resolution & server info                              | `nslookup app.example.com`                                                                                                     |
| `traceroute`                    | Check network path/hops to server                         | `traceroute app.example.com`                                                                                                   |
| `ping`                          | Verify host/network availability                          | `ping app.example.com`                                                                                                         |
| **Browser DevTools**            | Inspect HTTP status, latency, SSL, CORS                   | Press `F12` → Network Tab → Refresh → Click request                                                                            |
| `journalctl` / `tail`           | View app logs for backend errors                          | `sudo journalctl -u nginx -f`<br>`tail -f /var/log/nginx/error.log`<br>`tail -f /var/log/nginx/access.log`                     |
| `oci logging-search`            | Search for error logs in OCI Logging                      | `oci logging-search search-logs --search-query 'search "502" within logs'`                                                     |
| `oci lb backend-set get-health` | Get OCI Load Balancer backend health                      | `oci lb backend-set get-health --load-balancer-id <ocid> --backend-set-name <name>`                                            |

