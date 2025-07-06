import sys

def add(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

if len(sys.argv) != 4:
    print("Usage: python calc-sys-arg.py <num1> <num2> <operation>")
    sys.exit(1)

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
    result = add(num1, num2)
elif operation == "subtract":
    result = subtract(num1, num2)
elif operation == "multiply":
    result = multiply(num1, num2)
elif operation == "divide":
    result = divide(num1, num2)
else:
    result = "Invalid operation"
print(f"The result of {operation} {num1} and {num2} is: {result}")


# This code takes command line arguments to perform basic arithmetic operations.
# It uses sys.argv to get the numbers and the operation from the command line.
# The first argument is the first number, the second argument is the second number,
# and the third argument is the operation (add, subtract, multiply, divide).
# The code checks the operation and calls the corresponding function to perform the calculation.
# Finally, it prints the result of the operation.   