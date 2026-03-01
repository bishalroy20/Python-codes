# ==========================================
# Functions in Python - Full Code Examples
# ==========================================

# 1. Decomposition
# Breaking a problem into smaller functions
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate_expression(x, y):
    # Decomposed into smaller reusable functions
    return add(x, y) + multiply(x, y)

print("Decomposition Example:", calculate_expression(2, 3))
# Output: (2+3) + (2*3) = 11


# 2. Functions
# Defining and calling a simple function
def greet(name):
    print("Hello,", name)

greet("Alice")  # Output: Hello, Alice


# 3. How functions communicate with their environment
# Functions can take input (parameters) and affect global variables
message = "Initial"

def change_message(new_msg):
    global message
    message = new_msg

change_message("Updated by function")
print("Environment Communication:", message)
# Output: Updated by function


# 4. Returning a result from a function
def square(num):
    return num * num

result = square(5)
print("Returning Result:", result)  # Output: 25


# 5. Scopes in Python
x = 10  # Global variable

def scope_example():
    x = 5  # Local variable
    print("Inside function:", x)

scope_example()          # Output: 5
print("Outside function:", x)  # Output: 10


# 6. Recursion
# Function calling itself to solve a problem
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Recursion Example (Factorial of 5):", factorial(5))
# Output: 120