#######################################
#>> CLI Calculator (Using Functions)  #
#>>Features                           #
# Supports: +, -, *, /                #
#                                     #
#I Using functions for each operation.#
                                      #                     
#Runs continuously until user exits   #
#######################################

import math  # needed for exponential

# Function definitions

# Addition function
def add(a, b):
    return a + b
# Substruction function
def subtract(a, b): 
    return a - b
# Multiplication function
def multiply(a, b):
    return a * b
# Division function
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Power function
def power(a, b):
    return a ** b

# Exponential function (e^x)
def exponential(x):
    return math.exp(x)


def calculator():
    print("CLI Calculator")
    print("Operations: +  -  *  /  ^ (power)  exp (e^x)")
    print("Type 'exit' to quit\n")

    while True: # Keeps calculator running until user types "exit"
        num1 = input("Enter first number (or 'exit'): ") # Taking input form user. 
        if num1.lower() == "exit":
            print(" Exiting calculator...")
            break

        operator = input("Enter operator (+, -, *, /, ^, exp): ")

        # Special case: exponential needs only ONE input
        if operator == "exp":
            try:
                x = float(num1)
                result = exponential(x)
                print(f"The Result (e^{x}): {result}\n")
            except ValueError:
                print(" Invalid number.\n")
            continue

        num2 = input("Enter second number: ")

        try:
            a = float(num1)
            b = float(num2)
        except ValueError:
            print(" Invalid number. Try again.\n")
            continue

        if operator == "+":
            result = add(a, b)
        elif operator == "-":
            result = subtract(a, b)
        elif operator == "*":
            result = multiply(a, b)
        elif operator == "/":
            result = divide(a, b)
        elif operator == "^":
            result = power(a, b)
        else:
            print("Invalid operator.\n")
            continue

        print(f" Result: {result}\n")


if __name__ == "__main__": # The file is the main program.
    calculator()
#########################################
# Author: Hunde Tolera                  #
# Date: 04/05/2026                      #
#########################################






