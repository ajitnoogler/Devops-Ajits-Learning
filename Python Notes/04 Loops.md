
## 🔁🧠 **Expanded Python Conditional Statements and Loops Examples**

---

### ✅ 1. **Basic `if-else` Statement**

```python
disk_usage = 92
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

---
