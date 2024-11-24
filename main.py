# Introduction to Python
# A simple program to demonstrate the basics of Python.

# Multi-line program example
print("Welcome to Python!")  # Print a greeting message
print("This is a multi-line program example.")
print("Let's get started!\n")

# Basic Data Types
integer_value = 10  # Integer
float_value = 3.14  # Float
string_value = "Python"  # String
boolean_value = True  # Boolean

print("Basic Data Types:")
print("Integer:", integer_value)
print("Float:", float_value)
print("String:", string_value)
print("Boolean:", boolean_value, "\n")

# Variables
age = 22
name = "Aidan"
is_student = False

print("Variables:")
print(f"My name is {name}, I am {age} years old. Am I a student? {is_student}\n")

# Integer Arithmetic: Basic Operations
a = 15
b = 4

print("Integer Arithmetic: Basic Operations")
print(f"{a} + {b} = {a + b}")  # Addition
print(f"{a} - {b} = {a - b}")  # Subtraction
print(f"{a} * {b} = {a * b}")  # Multiplication
print(f"{a} / {b} = {a / b}")  # Division
print(f"{a} // {b} = {a // b}")  # Floor Division
print(f"{a} % {b} = {a % b}")  # Modulus
print(f"{a} ** {b} = {a ** b}\n")  # Exponentiation

# Integer Arithmetic: Special Operations
x = 5
y = 3

print("Special Operations:")
print(f"Bitwise AND: {x & y}")
print(f"Bitwise OR: {x | y}")
print(f"Bitwise XOR: {x ^ y}")
print(f"Left Shift: {x << 1}")
print(f"Right Shift: {x >> 1}\n")

# PEP 8: Coding Style Guide
# Keep code clean and readable. Follow indentation rules.

# Taking User Input
print("Taking User Input:")
name = input("What is your name? ")
print(f"Hello, {name}!\n")

# Program with Numbers
print("Program with Numbers:")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The sum of {num1} and {num2} is {num1 + num2}\n")

# Invoking Functions
def greet_user(username):
    """Function to greet a user."""
    print(f"Welcome, {username}!")

print("Invoking Functions:")
greet_user(name)
print()

# Boolean Type and Operations
is_sunny = True
is_weekend = False

print("Boolean Operations:")
print(f"Is it sunny and weekend? {is_sunny and is_weekend}")
print(f"Is it sunny or weekend? {is_sunny or is_weekend}")
print(f"Is it not sunny? {not is_sunny}\n")

# Comparisons
print("Comparisons:")
x = 10
y = 20
print(f"Is {x} equal to {y}? {x == y}")
print(f"Is {x} not equal to {y}? {x != y}")
print(f"Is {x} greater than {y}? {x > y}\n")

# If Statement
print("If Statement:")
if x < y:
    print(f"{x} is less than {y}\n")

# Else Statement
print("Else Statement:")
if x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is not greater than {y}\n")
