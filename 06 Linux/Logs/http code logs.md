
Here are simple `awk` one‑liners to pull out the same five columns—

**remote host (\$1)**, 
**timestamp (\$4)**, 
**HTTP method (\$6)**, 
**URL path (\$7)**, and 
**status code (\$9)**

—but **filtered by each HTTP status‑code class** or by a **specific code**.

---

### 1. Informational (1xx)

```bash
awk '$9 ~ /^1/ { print $1, substr($4,2), substr($6,2), $7, $9 }' access.log
```

> Matches any status in the 100–199 range (e.g. `100`, `102`).

---

### 2. Success (2xx)

```bash
awk '$9 ~ /^2/ { print $1, substr($4,2), substr($6,2), $7, $9 }' access.log
```

> Matches any status in the 200–299 range (e.g. `200`, `204`).

---

### 3. Redirection (3xx)

```bash
awk '$9 ~ /^3/ { print $1, substr($4,2), substr($6,2), $7, $9 }' access.log
```

> Matches any status in the 300–399 range (e.g. `301`, `304`).

---

### 4. Client Error (4xx)

```bash
awk '$9 ~ /^4/ { print $1, substr($4,2), substr($6,2), $7, $9 }' access.log
```

> Matches any status in the 400–499 range (e.g. `400`, `404`).

---

### 5. Server Error (5xx)

```bash
awk '$9 ~ /^5/ { print $1, substr($4,2), substr($6,2), $7, $9 }' access.log
```

> Matches any status in the 500–599 range (e.g. `500`, `503`).

---

### 6. Specific Status Code (e.g. 404 Not Found)

```bash
awk '$9 == 404 { print $1, substr($4,2), substr($6,2), $7, $9 }' access.log
```

> Use `==` to target an exact code.

---

#### Sample Output (for 4xx)

```
198.51.100.22 06/Jul/2025:23:01:15 GET /missing-page 404
203.0.113.5   06/Jul/2025:23:05:02 POST /login      401
```

---

### When to use each

* **`$9 ~ /^n/`** (where `n` is 1–5) quickly grabs entire classes: informational, success, redirect, client‑error, or server‑error.
* **`$9 == code`** zeroes in on a single status (e.g. `404`, `500`).

Use these to feed alerts (e.g. spike in 5xx), audit traffic (e.g. count of 3xx redirects), or investigate specific failed requests.
