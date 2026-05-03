x = 10 # Global Variable
y = 20
def my_function():
    x = 5 # Local Variable
    print("Inside the function, x =", x) # Calling Local Variable
    print("Inside the function, y =", y) # Calling Global Variable
my_function()
print("Outside the function, x =", x) # Calling Global Variable
print("Outside the function, y =", y) # Calling Global variable
