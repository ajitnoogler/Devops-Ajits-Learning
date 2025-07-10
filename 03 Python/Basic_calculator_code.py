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

def main():
    num1, num2 = user_input()
    print("Addition:", add(num1, num2))
    print("Multiplication:", multiply(num1, num2))
    print("Subtraction:", subtract(num1, num2))
    print("Division:", divide(num1, num2))
    addition_result = add(num1, num2)
    print("The addition of num1 and num2 is " + str(addition_result))
    print("The addition of num1 and num2 is", addition_result)

if __name__ == "__main__":
    main()