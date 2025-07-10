• List is a collection which is ordered and changeable. Allows duplicate members.
• A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

1. Installation Example:
my_list = ["apple", "banana", "cherry"]

2. Accessing the List:
print(my_list[0])

3. Range of index:
print(my_list[1:3])

| **Method / Concept**       | **Syntax / Example**       | **Description**                                                                   |
| -------------------------- | -------------------------- | --------------------------------------------------------------------------------- |
| `append()`                 | `list.append(item)`        | Adds an item to the **end** of the list.                                          |
| `insert()`                 | `list.insert(index, item)` | Inserts an item at a **specified position**.                                      |
| `remove()`                 | `list.remove(item)`        | Removes the **first occurrence** of the specified item.                           |
| `len()`                    | `len(list)`                | Returns the **number of elements** in the list.                                   |
| `pop()`                    | `list.pop(index)`          | Removes and returns the item at the specified **index** (last item if not given). |
| `count()`                  | `list.count(item)`         | Returns the **number of occurrences** of the specified item.                      |
| `clear()`                  | `list.clear()`             | Removes **all items** from the list (empties the list).                           |
| `sort()`                   | `list.sort()`              | Sorts the list in **ascending** order by default.                                 |
| `reverse()`                | `list.reverse()`           | Reverses the **order** of the list.                                               |
| `copy()`                   | `list.copy()`              | Returns a **shallow copy** of the list.                                           |
| **Nested List**            | `list = [1, 2, [3, 4]]`    | A list **inside** another list.                                                   |
| `range(start, stop, step)` | `list(range(1, 10, 2))`    | Generates a list of numbers with a **specific range and step**.                   |

# 1. append()
fruits = ['apple', 'banana']
fruits.append('cherry')  # Adds 'cherry' at the end
print("After append:", fruits)

# 2. insert()
fruits.insert(1, 'orange')  # Inserts 'orange' at index 1
print("After insert:", fruits)

# 3. remove()
fruits.remove('banana')  # Removes first occurrence of 'banana'
print("After remove:", fruits)

# 4. len()
print("Length of list:", len(fruits))

# 5. pop()
popped_item = fruits.pop(1)  # Removes item at index 1
print("After pop:", fruits)
print("Popped item:", popped_item)

# 6. count()
fruits.append('apple')
print("Count of 'apple':", fruits.count('apple'))

# 7. clear()
temp_list = ['a', 'b', 'c']
temp_list.clear()  # Empties the list
print("After clear:", temp_list)

# 8. sort()
numbers = [5, 3, 1, 4, 2]
numbers.sort()  # Sorts in ascending order
print("Sorted numbers:", numbers)

# 9. reverse()
numbers.reverse()  # Reverses the list
print("Reversed numbers:", numbers)

# 10. copy()
copy_list = fruits.copy()
print("Original list:", fruits)
print("Copied list:", copy_list)

# 11. Nested list
nested = [1, 2, [3, 4, 5], 6]
print("Nested list:", nested)
print("Access inner element (3rd item in inner list):", nested[2][2])

# 12. range(start, stop, step)
range_list = list(range(0, 10, 2))  # Creates [0, 2, 4, 6, 8]
print("Range list:", range_list)
