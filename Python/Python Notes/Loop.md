
# What is a Loop in Python?

A loop is a control structure that repeats a block of code multiple times — either a set number of times or until a condition is no longer true.

# ✅ Why Use Loops?

To automate repetitive tasks, such as:

    Processing every item in a list

    Running commands until a condition is met

    Iterating through files, lines, or user input




| **Loop Type**  | **When to Use**                                                                                              | **One-Liner Example**                              |
| -------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- |
| `for` loop     | When you know the number of iterations or you're iterating over a sequence (like list, string, tuple, range) | `for x in range(5): print(x)`                      |
| `while` loop   | When you **don’t know** how many times to loop; repeat until a condition is `False`                          | `while x < 5: print(x); x += 1`                    |
| `break`        | To **exit** a loop prematurely when a condition is met                                                       | `for x in range(10): if x == 5: break`             |
| `continue`     | To **skip** the current iteration and move to the next one                                                   | `for x in range(5): if x == 2: continue; print(x)` |
| `else` in loop | To run a block **after the loop finishes normally (no break)**                                               | `for x in range(3): print(x) else: print("Done")`  |
