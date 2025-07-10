import calculator_module as calc

def main():
    num1, num2 = calc.user_input()
    print("Addition:", calc.add(num1, num2))
    print("Multiplication:", calc.multiply(num1, num2))
    print("Subtraction:", calc.subtract(num1, num2))
    print("Division:", calc.divide(num1, num2))
    addition_result = calc.add(num1, num2)
    print("The addition of num1 and num2 is " + str(addition_result))
    print("The addition of num1 and num2 is", addition_result)
if __name__ == "__main__":  
    main()
    
# This code imports the calculator module and uses its functions to perform arithmetic operations.
# It defines a main function that gets user input and prints the results of addition, multiplication,
# subtraction, and division. The main function is called only if the script is run directly.
# This allows the code to be used as a module in other scripts without executing the main function
# automatically.
# The code is structured to be modular, making it easy to maintain and extend.
# The use of functions allows for better organization and reusability of code.
# The calculator module can be reused in other scripts or projects without modification.
# The main function serves as the entry point for the script, ensuring that the code runs only
# when the script is executed directly, not when imported as a module.
# This is a good practice in Python programming, allowing for better code organization and reusability.
# The code is simple and straightforward, making it easy to understand and modify if needed.        

