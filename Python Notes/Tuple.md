✅ What is a Tuple in Python?

A tuple is a built-in Python data type used to store multiple items in a single variable. It is very similar to a list, 
but tuples are immutable, meaning once a tuple is created, you cannot change, add, or remove its elements.

| Feature                     | Description                                                          |
| --------------------------- | -------------------------------------------------------------------- |
| **Immutable**               | Cannot modify items after creation (no `append()`, `remove()`, etc.) |
| **Ordered**                 | Maintains the order of elements (like lists)                         |
| **Indexed**                 | Accessed by index starting at 0                                      |
| **Allows Duplicates**       | Yes, a tuple can have repeated values                                |
| **Can Contain Mixed Types** | Supports strings, numbers, lists, other tuples, etc.                 |


✅ Note: Unlike lists, tuples are immutable, which means you cannot change, add, or remove elements once the tuple is created.

# 1. Creating a Tuple
fruits = ('apple', 'banana', 'cherry')
print("Tuple:", fruits)

# 2. Accessing Elements (Indexing)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 3. Slicing a Tuple
print("Sliced tuple (first two items):", fruits[:2])

# 4. Looping through a Tuple
for fruit in fruits:
    print("Fruit in loop:", fruit)

# 5. Tuple Length
print("Length of tuple:", len(fruits))

# 6. Tuple with One Element (add comma!)
single_item = ('apple',)
print("Single item tuple:", single_item)
print("Type:", type(single_item))  # Should be tuple, not str

# 7. Nested Tuple
nested_tuple = (1, 2, ('a', 'b', 'c'))
print("Nested Tuple:", nested_tuple)
print("Access nested element:", nested_tuple[2][1])  # Output: b

# 8. Tuple Concatenation
colors = ('red', 'green')
combined = fruits + colors
print("Concatenated Tuple:", combined)

# 9. Tuple Repetition
repeat = ('Hi!',) * 3
print("Repeated Tuple:", repeat)

# 10. Membership Test
print("'apple' in fruits:", 'apple' in fruits)
print("'grape' not in fruits:", 'grape' not in fruits)

# 11. Index of Element
print("Index of 'banana':", fruits.index('banana'))

# 12. Count Occurrences
print("Count of 'apple':", fruits.count('apple'))

# 13. Convert List to Tuple
fruit_list = ['kiwi', 'mango']
fruit_tuple = tuple(fruit_list)
print("Converted List to Tuple:", fruit_tuple)
