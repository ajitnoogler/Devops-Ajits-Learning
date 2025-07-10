num1, num2 = map(float, input("Enter two numbers separated by space: ").split())


sum_result = num1 + num2
multiply_result = num1 * num2
subtract_result = num1 - num2
divide_result = num1 / num2 if num2 != 0 else "Cannot divide by zero"

print(f"Addition: {sum_result}")
print(f"Multiplication: {multiply_result}")
print(f"Subtraction: {subtract_result}")
print(f"Division: {divide_result}") 