# List vs Tuple

| Feature               | **List**                              | **Tuple**                            |
| --------------------- | ------------------------------------- | ------------------------------------ |
| **Syntax**            | `my_list = [1, 2, 3]`                 | `my_tuple = (1, 2, 3)`               |
| **Mutable?**          | ✅ Yes (can be changed)                | ❌ No (immutable once created)        |
| **Methods Available** | Many (e.g., `append()`, `pop()`)      | Few (e.g., `count()`, `index()`)     |
| **Performance**       | Slower than tuple (due to mutability) | Faster (better for read-only data)   |
| **Use Case**          | When data needs to change             | When data should remain constant     |
| **Memory Usage**      | Uses more memory                      | Uses less memory                     |
| **Hashable?**         | ❌ No (can’t be used as dict key)      | ✅ Yes (if all elements are hashable) |
| **Iteration Speed**   | Slower                                | Faster                               |

✅ When to Use:

    List: Use when you need to modify, sort, or append elements.
    Tuple: Use when you want fixed data or use the object as a dictionary key or set element.

🔍 Example:

# List
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)  # ['apple', 'banana', 'mango']

# Tuple
colors = ("red", "green", "blue")
#### colors.append("yellow")  # ❌ Error: 'tuple' object has no attribute 'append'


