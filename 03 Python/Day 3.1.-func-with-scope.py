def user_input():
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: ")) # This user input values are local scope variables 
    return num1, num2                       # This function returns the values of num1 and num2 to the main program

def add(num1, num2): # This Line of code is called Parameter and num1, num2 values are called Arguments as it is passed by user_input
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2
    
def subtract(num1, num2):
    return num1 - num2  

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

num1, num2 = user_input()

print("Addition:", add(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Division:", divide(num1, num2))


addition_result = add(num1, num2)
print("The addition of num1 and num2 is " + str(addition_result))# Type casting is done to convert the result into string for concatenation
print("The addition of num1 and num2 is", addition_result) # This is another way of printing the result without type casting
