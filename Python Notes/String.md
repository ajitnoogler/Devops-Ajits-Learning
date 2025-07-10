# 🧵 Python String Handling Examples for Interview

---

## 🔤 1. Reverse a String

```python
text = "DevOps"
reversed_text = text[::-1]
print(reversed_text)  # Output: spOv eD
```

---

## 🔍 2. Check if a String is a Palindrome

```python
s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

---

## 🪓 3. Split and Iterate Words

```python
sentence = "Welcome to OCI DevOps"
for word in sentence.split():
    print(word)
```

✅ Output:
```
Welcome  
to  
OCI  
DevOps  
```

---

## 🔄 4. Replace Substring

```python
log = "Status: failed"
updated_log = log.replace("failed", "success")
print(updated_log)  # Output: Status: success
```

---

## 📏 5. String Length and Case Conversion

```python
s = "Cloud Engineer"
print(len(s))           # 14
print(s.upper())        # CLOUD ENGINEER
print(s.lower())        # cloud engineer
```

---

## 🔢 6. Extract Digits or Letters Only

```python
s = "User123Log"
digits = ''.join(filter(str.isdigit, s))  # "123"
letters = ''.join(filter(str.isalpha, s)) # "UserLog"
```

---

## 🔗 7. String Formatting

```python
name = "Ajit"
role = "DevOps Engineer"
print(f"My name is {name} and I work as a {role}.")
```

---

## 🛠️ 8. Remove Special Characters (Regex)

```python
import re
s = "Error#404: Not_Found!"
clean = re.sub(r'\W+', ' ', s)
print(clean)  # Output: Error 404 Not_Found
```

---

## 🧪 9. Startswith / Endswith

```python
filename = "config.yaml"
print(filename.endswith(".yaml"))  # True
print(filename.startswith("conf")) # True
```

---

## 📎 10. Count Substring

```python
log_data = "fail fail pass fail"
print(log_data.count("fail"))  # 3
```

---
