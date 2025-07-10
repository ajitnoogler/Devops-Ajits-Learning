Here’s a **cheat sheet-style comparison** of **List vs Tuple vs Set vs Dictionary** in Python — perfect for interviews and quick recall:

---

### ✅ **Quick Comparison Table**

| Feature        | List (`[]`)       | Tuple (`()`)     | Set (`{}` or `set()`)  | Dictionary (`{key: value}`) |
| -------------- | ----------------- | ---------------- | ---------------------- | --------------------------- |
| **Ordered**    | ✅ Yes             | ✅ Yes            | ❌ No                   | ✅ Yes                       |
| **Mutable**    | ✅ Yes             | ❌ No (Immutable) | ✅ Yes                  | ✅ Yes                       |
| **Duplicates** | ✅ Allowed         | ✅ Allowed        | ❌ Not Allowed          | ❌ Keys not duplicated       |
| **Indexable**  | ✅ Yes (`[0]`)     | ✅ Yes (`[0]`)    | ❌ No                   | ✅ Yes (`dict['key']`)       |
| **Use-case**   | Sequence of items  | Fixed sequence   | Unique unordered items | Key-value mapping                |
| **Syntax**     | `[1, 2, 3]`        | `(1, 2, 3)`      | `{1, 2, 3}` or `set()` | `{"a": 1, "b": 2}`               |

---

### 📌 **When to Use What?**

* **List**: Use when you need an **ordered**, **mutable** collection of items with possible duplicates.
  → *E.g., processing a list of files, user input, etc.*

* **Tuple**: Use when you need an **ordered**, **immutable** collection — typically for **fixed data**, like coordinates, or returning multiple values from a function.
  → *E.g., `return (name, age)`*

* **Set**: Use when you need to store **unique items**, and **don’t care about order**. Great for membership tests or eliminating duplicates.
  → *E.g., finding common elements in two datasets.*

* **Dictionary**: Use when you need to **associate keys with values** (like a map or hash table).
  → *E.g., user profiles, configuration data.*

---

### 🧠 **Memory & Performance Tips**

* **Tuples** are more **memory efficient** and slightly **faster** than lists.
* **Sets** and **dictionaries** use **hashing** for fast lookup — O(1) average time complexity.
* **Lists** and **tuples** use indexing — O(n) for search unless the index is known.

---

### 🧪 Example Code

```python
# List
fruits = ['apple', 'banana', 'apple']
fruits.append('cherry')

# Tuple
coordinates = (10.5, 20.3)

# Set
unique_numbers = {1, 2, 3, 2}
unique_numbers.add(4)

# Dictionary
person = {'name': 'Ajit', 'age': 35}
person['city'] = 'Mumbai'
```

---
| Symbol  | Name                | Common Use (Python & Programming)                               |
| ------- | ------------------- | --------------------------------------------------------------- |
| `(` `)` | **Parentheses**     | Function calls, grouping, tuples → `print("Hi")`, `x = (1, 2)`  |
| `[` `]` | **Square brackets** | Lists, indexing, slices → `my_list[0]`, `a[1:3]`                |
| `{` `}` | **Curly braces**    | Dictionaries, sets, f-strings → `{"key": "value"}`, `f"{name}"` |

🧠 Memory Trick:

    Parentheses → Perform (functions)
    Square → Slice or Subscript (lists)
    Curly → Collections (dicts/sets)
---

### ❗ Common Interview Questions

1. Difference between list and tuple?
2. When would you use a set instead of a list?
3. Can dictionary keys be mutable?
4. How does Python ensure uniqueness in sets?

---

Let me know if you'd like a **PDF version**, **flashcards**, or **code-based practice quiz** on this topic!
