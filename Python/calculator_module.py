def user_input():
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    return num1, num2

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

