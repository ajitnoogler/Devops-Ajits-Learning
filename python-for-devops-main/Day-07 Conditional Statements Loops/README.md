# Conditional Statements in Python

Conditional statements are a fundamental part of programming that allow you to make decisions and execute different blocks of code based on certain conditions. In Python, you can use `if`, `elif` (short for "else if"), and `else` to create conditional statements.

## `if` Statement

The `if` statement is used to execute a block of code if a specified condition is `True`. If the condition is `False`, the code block is skipped.

```python
if condition:
    # Code to execute if the condition is True
```

- Example:

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

## `elif` Statement

The `elif` statement allows you to check additional conditions if the previous `if` or `elif` conditions are `False`. You can have multiple `elif` statements after the initial `if` statement.

```python
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition2 is True
elif condition3:
    # Code to execute if condition3 is True
# ...
else:
    # Code to execute if none of the conditions are True
```

- Example:

```python
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but not greater than 15")
else:
    print("x is not greater than 5")
```

## `else` Statement

The `else` statement is used to specify a block of code to execute when none of the previous conditions (in the `if` and `elif` statements) are `True`.

```python
if condition:
    # Code to execute if the condition is True
else:
    # Code to execute if the condition is False
```

- Example:

```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

| **Type**       | **Use When**                                                                        |
| -------------- | ----------------------------------------------------------------------------------- |
| `for` loop     | You **know** in advance **how many times** you want to iterate (e.g., list, range). |
| `while` loop   | You **don't know** how many times to loop — run **until a condition is met**.       |
| `nested loops` | You need to loop inside another loop — e.g., for matrix or grid operations.         |
| `break`        | To **exit a loop early** when a condition is met.                                   |
| `continue`     | To **skip current iteration** and move to the next one.                             |

# Example: for loop

for i in range(5):  # Run exactly 5 times
    print(i)

# Example: while loop

count = 0
while count < 5:  # Run until condition is false
    print(count)
    count += 1

# CONDITIONAL STATEMENTS

| **Type**           | **Use When**                                                 |
| ------------------ | ------------------------------------------------------------ |
| `if`               | To **check a condition** and run code only if it's True.     |
| `if...else`        | To run one block if condition is True, **another if False**. |
| `if...elif...else` | To **check multiple conditions in sequence**.                |
| Nested `if`        | To check **sub-conditions inside another condition**.        |


# Example: if statement

x = 10
if x > 5:
    print("x is greater than 5")

# Example: if...elif...else

age = 18
if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
else:
    print("Adult")

# Real-World Use Case Summary:

| **Scenario**                      | **Use**                     |
| --------------------------------- | --------------------------- |
| Repeating an action 10 times      | `for` loop with `range(10)` |
| Reading all items from a list     | `for` loop over a list      |
| Waiting for a user to input "yes" | `while` loop                |
| Running a menu until user quits   | `while` loop + `break`      |
| Checking if a number is positive  | `if` statement              |
| Choosing from multiple options    | `if...elif...else`          |
