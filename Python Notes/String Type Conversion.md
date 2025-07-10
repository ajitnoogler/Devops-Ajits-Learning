# 🔁 Python Type Conversion: String ↔ Number

---

## 🔢 1. String to Integer / Float

```python
s = "42"
num = int(s)         # Converts string to integer → 42
price = float("99.99")  # Converts string to float → 99.99
```

📌 Use Case: Converting CLI or config inputs (`sys.argv`, env vars) to numbers.

---

## 🔤 2. Number to String

```python
num = 100
text = str(num)      # "100"

pi = 3.14159
string_pi = str(pi)  # "3.14159"
```

📌 Use Case: Building messages, logs, or filenames dynamically.

---

## 🧮 3. Arithmetic with Converted Strings

```python
a = "5"
b = "10"
result = int(a) + int(b)  # 15
```

🛑 Without conversion, `"5" + "10"` would result in `"510"` (string concatenation).

---

## 🧪 4. Checking Type Before Conversion

```python
value = "123"
if value.isdigit():
    print(int(value) * 2)  # 246
```

📌 Useful when parsing user input or config files.

---

## 🧠 5. String to Boolean (Custom Logic)

```python
flag = "true"
if flag.lower() in ("true", "1", "yes"):
    print(True)
else:
    print(False)
```

---

## ✅ Summary Table

| From      | To        | Function      | Example             |
|-----------|-----------|----------------|---------------------|
| `"42"`    | `int`     | `int()`        | `int("42") → 42`    |
| `"3.14"`  | `float`   | `float()`      | `float("3.14")`     |
| `99`      | `str`     | `str()`        | `str(99)` → `"99"`  |
| `"123abc"`| `int`     | ❌ raises `ValueError` | Must clean string first |
| `"True"`  | `bool`    | Custom logic   | `"True".lower() == "true"` |

---


