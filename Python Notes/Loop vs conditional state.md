
Loop vs ⚖️ Conditional Statement

| **Aspect**           | **Loop** (`for`, `while`)                              | **Conditional Statement** (`if`, `elif`, `else`)               |
| -------------------- | ------------------------------------------------------ | -------------------------------------------------------------- |
| **Purpose**          | To **repeat** a block of code multiple times           | To **make decisions** and execute code **based on conditions** |
| **Repetition**       | Yes – runs code **multiple times**                     | No – runs code **only once** if condition is true              |
| **When to Use**      | When you need to **iterate** over data or repeat tasks | When you need to **choose** between code blocks                |
| **Keywords Used**    | `for`, `while`, `break`, `continue`, `else`            | `if`, `elif`, `else`                                           |
| **Example Use Case** | Print all items in a list                              | Check if user is eligible to vote                              |

## 🧠 Example: Loop

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    square = num ** 2
    print(f"Square of {num} is {square}")
```

### ✅ Output:
```
Square of 1 is 1  
Square of 2 is 4  
Square of 3 is 9  
Square of 4 is 16  
Square of 5 is 25  
```

---

## 🧠 Example: Conditional Statement

```python
age = 20

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
```

### ✅ Output:
```
Eligible to vote
```

---

Let me know if you want to add:
- `while` loop or `range()` examples  
- More conditional cases (nested, elif)  
- Real-world examples like health check or disk usage alert  



✅ Summary

    Use a loop when you want to repeat actions.
    Use a conditional statement when you want to choose what to do based on conditions.
