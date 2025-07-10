🌐 HTTP Status Codes – Categorized with Meanings

| Code  | Meaning                      | Description / When Encountered                              |
| ----- | ---------------------------- | ----------------------------------------------------------- |
| `200` | OK                           | Success; app is responding normally                         |
| `301` | Moved Permanently            | Permanent redirect (often misconfigured URL)                |
| `302` | Found / Temporary Redirect   | Temporary redirect                                          |
| `400` | Bad Request                  | Client sent malformed request (e.g., bad JSON)              |
| `401` | Unauthorized                 | Authentication required or invalid token                    |
| `403` | Forbidden                    | Request is understood but refused (e.g., IP block, ACL)     |
| `404` | Not Found                    | URL/path doesn't exist on backend                           |
| `408` | Request Timeout              | Client request took too long to reach server                |
| `413` | Payload Too Large            | Request size exceeds configured limits                      |
| `429` | Too Many Requests            | Rate limiting (e.g., WAF or API Gateway throttling)         |
| `500` | Internal Server Error        | App crashed or failed backend code                          |
| `502` | Bad Gateway                  | Load balancer received invalid response from backend        |
| `503` | Service Unavailable          | App server overloaded or down (e.g., autoscaling lag)       |
| `504` | Gateway Timeout              | Backend didn’t respond in time (common with load balancers) |
| `521` | Web Server Down (Cloudflare) | Load balancer can't reach the web server                    |
| `522` | Connection Timed Out (CF)    | TCP handshake timeout between edge and origin               |
