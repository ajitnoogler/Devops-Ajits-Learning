
## 🔁🧠 **Expanded Python Conditional Statements and Loops Examples**

---

### ✅ 1. **Basic `if-else` Statement**

```python
disk_usage = 92
if disk_usage > 90:
    print("🔴 Disk usage critical!")
else:
    print("🟢 Disk usage normal.")

---------------------------------------------
# Ask user for disk usage as input
disk_usage = int(input("Enter disk usage percentage: "))

# Conditional check
if disk_usage > 90:
    print("🔴 Disk usage critical!")
else:
    print("🟢 Disk usage normal.")

```

---

### ✅ 2. **`if-elif-else` with Multiple Conditions**

```python
cpu = 75
if cpu > 90:
    print("🔥 CPU Overloaded")
elif cpu > 70:
    print("⚠️ High CPU usage")
else:
    print("✅ CPU normal")
```

---

### ✅ 3. **Nested `if` Statements**

```python
user = "admin"
logged_in = True

if logged_in:
    if user == "admin":
        print("🔐 Access granted to admin panel.")
    else:
        print("🔓 Access granted to user dashboard.")
else:
    print("⛔ Login required.")
```

---

### ✅ 4. **Short-hand if (One-liner)**

```python
temp = 50
print("Too Cold ❄️") if temp < 60 else print("Comfortable 🌤")
```

---

### ✅ 5. **Check Multiple Conditions Using `and`/`or`**

```python
cpu = 80
mem = 70

if cpu > 75 and mem > 60:
    print("⚠️ System under heavy load")
elif cpu < 50 or mem < 50:
    print("✅ System underutilized")
```

---

### ✅ 6. **Using `in` with if (DevOps Example)**

```python
failed_services = ["nginx", "sshd", "docker"]

if "nginx" in failed_services:
    print("🚨 NGINX service failed!")
```

---

## 🔁 **Python Loop Examples**

---

### ✅ 7. **`for` Loop Over a List**

```python
servers = ["web1", "web2", "db1"]
for server in servers:
    print(f"🔁 Rebooting {server}...")
```

---

### ✅ 8. **`for` Loop with `range()`**

```python
for i in range(1, 4):
    print(f"📦 Backup attempt {i}")
```

---

### ✅ 9. **`while` Loop with Condition**

```python
attempt = 1
while attempt <= 3:
    print(f"🔄 Trying to connect... Attempt {attempt}")
    attempt += 1
```

---

### ✅ 10. **`for` Loop with `break`**

```python
for port in [22, 80, 443, 8080]:
    if port == 443:
        print("✅ Found HTTPS port")
        break
```

---

### ✅ 11. **`for` Loop with `continue`**

```python
for service in ["nginx", "none", "sshd"]:
    if service == "none":
        continue
    print(f"Checking status of {service}")
```

---

### ✅ 12. **Nested `for` Loops (Environment x Region)**

```python
envs = ["dev", "prod"]
regions = ["us-east", "eu-west"]

for env in envs:
    for region in regions:
        print(f"🔄 Deploying {env} to {region}")
```

---

### ✅ 13. **Loop With `else` Block**

```python
for port in [21, 22, 23]:
    if port == 25:
        print("Port 25 found")
        break
else:
    print("❌ Port 25 not found")
```

---

### ✅ 14. **While Loop with Input (Simulate Retry Logic)**

```python
retry = 0
while retry < 3:
    print("Trying to connect to database...")
    retry += 1
else:
    print("✅ Connection attempts finished.")
```

---

### ✅ 15. **Enumerate in For Loop**

```python
for index, host in enumerate(["web1", "web2", "db1"]):
    print(f"{index+1}. Pinging {host}")
```

---

### ✅ 16. **Zip Two Lists in For Loop**

```python
servers = ["web1", "web2"]
ips = ["10.0.0.1", "10.0.0.2"]

for srv, ip in zip(servers, ips):
    print(f"{srv} → {ip}")
```


## ✅ **When to Use Which Conditional Statements & Loops**

### 🔍 **1. `if`, `elif`, `else` — Used for Decision Making**

| Use it when you want to...    | Example DevOps Scenario     |
| ----------------------------- | --------------------------- |
| ✅ Handle a single condition   | Check if disk usage > 90%   |
| ✅ Handle multiple choices     | Match HTTP status codes     |
| ✅ Fall back to a default case | Default to "OK" if no alert |

```python
if disk_usage > 90:
    print("🔴 Critical")
elif disk_usage > 70:
    print("⚠️ Warning")
else:
    print("✅ Healthy")
```

---

### 🔐 **2. `Nested if` — For Sub-Conditions (Layered Checks)**

| Use it when...                               | Example DevOps Use Case                        |
| -------------------------------------------- | ---------------------------------------------- |
| ✅ You need to check inside another condition | If user is admin → then check permission level |

```python
if user_logged_in:
    if user_role == "admin":
        print("Grant admin access")
```

---

### 💡 **3. Short-hand `if-else` (Ternary Operator)**

| Use it for...                      | Example                    |
| ---------------------------------- | -------------------------- |
| ✅ Very simple one-liner conditions | Set status based on a flag |

```python
status = "FAIL" if exit_code != 0 else "PASS"
```

---

## 🔁 **When to Use Loops**

### 🔄 **4. `for` Loop — For Known Iterations**

| Use it to...                   | Example DevOps Use Case     |
| ------------------------------ | --------------------------- |
| ✅ Iterate over list of servers | Restart or ping each server |
| ✅ Automate across environments | Deploy to dev/test/prod     |
| ✅ Loop through ports/services  | Check if service is running |

```python
for server in ["web1", "web2", "db1"]:
    print(f"Checking {server}")
```

---

### 🔄 **5. `while` Loop — For Unknown or Retry Conditions**

| Use it to...                          | Example DevOps Use Case          |
| ------------------------------------- | -------------------------------- |
| ✅ Retry until success or max attempts | Wait for a service to be healthy |
| ✅ Keep checking until condition met   | Loop until response is 200       |

```python
attempt = 0
while attempt < 3:
    print("Trying to connect...")
    attempt += 1
```

---

### ✂️ **6. `break`, `continue` — Control Loop Execution**

| Use it to...            | Example DevOps Use Case         |
| ----------------------- | ------------------------------- |
| ✅ Stop early on success | Break when server responds      |
| ✅ Skip known issues     | Continue when service is 'none' |

```python
for service in services:
    if service == "none":
        continue
    if check(service):
        break
```

---

### 🧠 **7. `else` with Loops — When Loop Doesn’t Break**

| Use it to...                   | Example DevOps Use Case           |
| ------------------------------ | --------------------------------- |
| ✅ Alert only if item not found | Alert if no failed services found |

```python
for svc in services:
    if svc == "failed":
        print("Found failed service")
        break
else:
    print("All services running")
```

---

## 🚀 Summary Cheat Sheet

| **Control Structure**  | **When to Use**                | **Typical DevOps Use Case**                 |
| ---------------------- | ------------------------------ | ------------------------------------------- |
| `if` / `elif` / `else` | Simple or multi-step decisions | Health checks, alerting, conditional deploy |
| `for` loop             | Known items or count           | Iterate servers, configs, ports             |
| `while` loop           | Retry or wait logic            | Wait for state or resource                  |
| `break`                | Exit early on condition        | Exit after success                          |
| `continue`             | Skip iteration                 | Skip known bad configs                      |
| `nested if`            | Layered logic                  | Check multiple conditions step-by-step      |
| `loop + else`          | All passes/failures handling   | Only alert if none match                    |

