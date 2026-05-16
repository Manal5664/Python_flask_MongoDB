# =========================
# FUNCTIONS IN PYTHON
# =========================

# Function → block of reusable code


# 1. SIMPLE FUNCTION
def greet():
    print("Hello Student!")

greet()


# =========================
# FUNCTION ARGUMENTS
# =========================

# 2. POSITIONAL ARGUMENTS
def add(a, b):
    print("Sum:", a + b)

add(5, 3)


# 3. KEYWORD ARGUMENTS
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=20, name="Ali")


# 4. DEFAULT ARGUMENTS
def greet_user(name="User"):
    print("Welcome", name)

greet_user()
greet_user("Sara")


# =========================
# RETURN VALUE
# =========================

# return → function gives result back

def multiply(a, b):
    return a * b

result = multiply(4, 5)
print("Multiplication Result:", result)


# =========================
# FUNCTION WITH LOGIC
# =========================

def grade_calculator(marks):
    if marks >= 80:
        return "Grade A"
    elif marks >= 70:
        return "Grade B"
    elif marks >= 60:
        return "Grade C"
    else:
        return "Fail"

print(grade_calculator(85))
print(grade_calculator(72))
print(grade_calculator(50))


# =========================
# MODULES IN PYTHON
# =========================

# module → file containing reusable code

import math   # built-in module

print("Square root:", math.sqrt(25))
print("Factorial:", math.factorial(5))


# =========================
# CUSTOM MODULE EXAMPLE (concept)
# =========================

# suppose you created file: mymodule.py
# inside it:
# def hello(name):
#     print("Hello", name)

# then use it like:
# import mymodule
# mymodule.hello("Ali")


# =========================
# MINI FLOW USING FUNCTION
# =========================

def calculator(a, b):
    print("Add:", a + b)
    print("Subtract:", a - b)
    print("Multiply:", a * b)
    print("Divide:", a / b)

calculator(10, 5)