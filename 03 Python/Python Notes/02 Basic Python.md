Great! Here's a clean, **DevOps-relevant list of sample programs for *Basic Python topics only*** — keeping it beginner-friendly and practical.

---

## 🧰 **Basic Python Topics — Sample Programs (For DevOps Beginners)**

| **Topic** | **Sample Program** |
| --------- | ------------------ |

### ✅ 1. **Variables & Data Types**

```python
name = "Ajit"
age = 35
is_devops = True
print(f"{name} is {age} years old - DevOps: {is_devops}")
```

---

### ✅ 2. **Input / Output**

```python
username = input("Enter your name: ")
print("Welcome,", username)
```

---

### ✅ 3. **Operators**

```python
a, b = 10, 3
print("Sum:", a + b)
print("Modulus:", a % b)
```

---

### ✅ 4. **If-Else (Decision Making)**

```python
cpu_usage = 85
if cpu_usage > 80:
    print("High CPU alert!")
else:
    print("CPU usage normal.")
```

---

### ✅ 5. **Loops (for, while)**

```python
for i in range(1, 4):
    print("Checking server", i)

count = 1
while count <= 3:
    print("Retry", count)
    count += 1
```

---

### ✅ 6. **Functions**

```python
def ping(host):
    print(f"Pinging {host}...")

ping("8.8.8.8")
```

---

### ✅ 7. **Lists**

```python
servers = ["web1", "web2", "db1"]
for s in servers:
    print("Rebooting", s)
```

---

### ✅ 8. **Tuples**

```python
config = ("Ubuntu", 22.04)
print("OS:", config[0], "Version:", config[1])
```

---

### ✅ 9. **Dictionaries**

```python
server = {"name": "web1", "status": "active"}
print(server["name"], "is", server["status"])
```

---

### ✅ 10. **Sets**

```python
unique_ips = {"192.168.1.1", "192.168.1.2", "192.168.1.1"}
print(unique_ips)  # Removes duplicates
```

---

### ✅ 11. **String Methods**

```python
log = "error: disk full"
print(log.upper())
```

---

### ✅ 12. **List Comprehension**

```python
ports = [22, 80, 443]
open_ports = [p for p in ports if p != 22]
print("Open:", open_ports)
```

---

### ✅ 13. **Basic File Read/Write**

```python
with open("servers.txt", "w") as f:
    f.write("web1\nweb2\n")

with open("servers.txt", "r") as f:
    print(f.read())
```

---

### ✅ 14. **Exception Handling**

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Error: Division by zero.")
```

---

### ✅ 15. **Basic Module Import**

```python
import math
print("Square root of 16 is", math.sqrt(16))
```

---

### ✅ 16. **Loops with Break / Continue**

```python
for i in range(5):
    if i == 2:
        continue  # Skip 2
    if i == 4:
        break  # Stop at 4
    print(i)
```

---

### ✅ 17. **Pass Statement**

```python
def deploy():
    pass  # Placeholder for future code
```

---

### ✅ 18. **Boolean Logic**

```python
is_up = True
is_healthy = True
if is_up and is_healthy:
    print("Server OK")
```

---

### ✅ 19. **Type Conversion**

```python
cpu = "90"
print(int(cpu) > 80)
```

---

### ✅ 20. **f-Strings**

```python
host = "db1"
status = "running"
print(f"{host} is {status}")
```

