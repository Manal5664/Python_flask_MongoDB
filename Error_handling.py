# Exception Handling using try-except
# Python provides try-except blocks to handle errors gracefully without crashing the program.


# try:
    # Code that may cause an error
# except:
    # Code to handle the error

try:
    num = 10
    print(num / 0)
except:
    print("An error occurred.")


# Handling Specific Exceptions

# Instead of catching all errors, we can catch specific exceptions.


try:
    num = int(input("Enter a number: "))
    print(10 / num)

# ZeroDivisionError Python ka built-in exception class hai. Iski jagah koi random naam nahi likh sakte.
# ValueError: Jab value galat ho lekin data type sahi ho. Example: int("abc")
# TypeError :Jab incompatible data types par operation karein. Example: "10" + 5
# NameError: Jab undefined variable use karein. Example: print(name)
# ZeroDivisionError:Jab kisi number ko 0 se divide karein. Example: 10 / 0
# IndexError: Jab list ke invalid index ko access karein. Example: my_list[10]


except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter a valid number.")


# Handling Multiple Exceptions

# Multiple exceptions can be handled using multiple except blocks.

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")


# Using else Block

# The else block executes only if no exception occurs.

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print("You entered:", num)

# Using finally Block
# The finally block always executes whether an exception occurs or not.

try:
    print(10 / 2)

except ZeroDivisionError:
    print("Error")

finally:
    print("Program finished.")

# Custom Exceptions
# We can create our own exception classes for better error management.

class AgeError(Exception):
    pass

age = int(input("Enter age: "))

if age < 18:
    raise AgeError("Age must be 18 or above.")

print("Access Granted")