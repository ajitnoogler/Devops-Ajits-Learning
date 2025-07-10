# 🔁 Python Type Conversion – DevOps Examples

These are practical use cases where string ↔ number conversions are commonly used in automation, monitoring, and infrastructure scripts.

---

## 🔧 1. Environment Variable to Integer

```python
import os

timeout = int(os.getenv("TIMEOUT", "30"))  # default to 30 if not set
print(f"Timeout set to {timeout} seconds")
```

✅ Used in container scripts or cron jobs that read ENV variables.

---

## 📉 2. Convert Disk Usage String to Float

```python
disk_percent = "85.4%"  
usage = float(disk_percent.strip('%'))
if usage > 80:
    print("🔴 Disk usage high!")
```

✅ Useful in monitoring scripts parsing `df -h` or Prometheus output.

---

## 📤 3. JSON Response to Integer

```python
import json

response = '{"status": "ok", "users": "200"}'
data = json.loads(response)

users = int(data["users"])  # convert string to int
print(f"Logged in users: {users}")
```

✅ Needed in REST API integrations (many values come as strings).

---

## 📥 4. CLI Argument (sys.argv) to Float

```python
import sys

if len(sys.argv) > 1:
    threshold = float(sys.argv[1])  # e.g., 0.9
    print(f"Alert threshold is {threshold * 100}%")
```

✅ Used in automation or health-check CLI tools.

---

## 📦 5. YAML Boolean/String Conversion (Ansible-style)

```python
enabled = "yes"

if enabled.lower() in ("yes", "true", "1"):
    enabled_flag = True
else:
    enabled_flag = False
```

✅ Converts config values to actual booleans.

---

## 🪵 6. Parsing Log Line with Numbers

```python
log = "Disk usage at 92% on /dev/sda1"
percent = int(log.split()[3].strip('%'))
if percent > 90:
    print("🔴 Critical disk alert")
```

✅ Typical in cron-based log parsing or alert scripts.

---

## 🧠 Summary Table

| Input Source        | From     | To        | Use Case                                 |
|---------------------|----------|-----------|-------------------------------------------|
| ENV var (`os.getenv`) | str      | int/float | Timeouts, port numbers, feature flags     |
| API/JSON            | str      | int       | Response parsing from REST calls          |
| CLI Arg (`sys.argv`) | str      | float     | Thresholds, counts, resource limits       |
| YAML/Config         | str      | bool      | Feature enable flags                      |
| Logs/Monitoring     | str      | int       | Disk, CPU, memory usage alerts            |

---

