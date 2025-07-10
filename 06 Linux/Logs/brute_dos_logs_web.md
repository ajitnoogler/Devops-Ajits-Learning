To detect **brute-force attacks** on a **web application** via logs (like Apache `access.log`, Nginx, or app logs), you look for **suspicious patterns**, such as:

---

### 🔍 Key Indicators of Brute Force in Logs

| Indicator                          | Description                                                                                       |
| ---------------------------------- | ------------------------------------------------------------------------------------------------- |
| 🔁 **Repeated login attempts**     | Same IP hitting `/login`, `/admin`, etc. repeatedly in short time                                 |
| ⏱ **High request frequency**       | Many requests per second from a single IP                                                         |
| ❌ **Repeated failed logins**       | Status codes like `401`, `403`, `302` (redirect on fail), or app-specific "login failed" messages |
| 🌍 **Many usernames from same IP** | Username enumeration or credential stuffing                                                       |
| 📥 **POST method abuse**           | Multiple POSTs to login forms                                                                     |
| 🧪 **User-agent anomalies**        | Missing UA headers or automated tools (e.g., `curl`, `python-requests`)                           |


=================================================================================================================================

## 🔧 Example Using Apache/Nginx Access Logs

### 🧪 1. Find repeated login POSTs

```bash
grep 'POST /login' access.log | awk '{print $1}' | sort | uniq -c | sort -nr | head
```

✅ Shows IPs making most POST login requests.

=================================================================================================================================

### ⛔ 2. Find failed logins by status code (e.g., 401 Unauthorized)

```bash
awk '$7 ~ /\/login/ && $9 == 401 { print $1 }' access.log | sort | uniq -c | sort -nr | head
```

✅ Most frequent IPs returning 401 on `/login`.

=================================================================================================================================

### 📉 3. Detect high-frequency requests (DoS or brute force)

```bash
awk '{print $1}' access.log | sort | uniq -c | sort -nr | head
```

✅ See which IPs made the most total requests.

=================================================================================================================================

### 🧾 4. Check timestamps for frequency

```bash
grep 'POST /login' access.log | awk '{print $1, substr($4,2,17)}' | sort | uniq -c | sort -nr | head
```

✅ Detect high-frequency POSTs per IP and time window.

=================================================================================================================================

### 🕵️ 5. Look for suspicious User-Agents

```bash
awk -F\" '{print $6}' access.log | sort | uniq -c | sort -nr | head
```

✅ Identify bots (`curl`, `python`, `nmap`, `hydra`), empty UAs, or weird tools.

=================================================================================================================================

## 🔐 Bonus: Detect Username Enumeration (from app logs)

If your app logs attempted usernames:

```bash
grep 'login failed' app.log | awk -F'user=' '{print $2}' | cut -d' ' -f1 | sort | uniq -c | sort -nr
```

✅ Reveals usernames being guessed.

==================================================================================================================================

### 🧠 Combine with `fail2ban` or `goaccess` for automation or dashboarding:

* `fail2ban` → auto-block IPs on pattern match.
* `goaccess` → real-time web traffic visualization.

---

## 🧾 Summary
| What to Look For           | Example Command                                | 
| -------------------------- | ---------------------------------------------- | 
| Many login attempts per IP | \`grep 'POST /login' access.log                | 
| High 401/403 errors        | \`awk '\$9==401 {print \$1}' access.log        | 
| Fast repeated requests     | `awk '{print $1, $4}'` and check time patterns |                             
| Suspicious User-Agents     | `awk -F\" '{print $6}'`                        |                              
| Username guessing          | \`grep 'login failed' app.log                  | 

---

Let me know your log format (Apache, Nginx, custom app?) and I’ll tailor the detection script or command for your environment 🔍
