# ==================================================
# 🐍 DAY 6: OOP (OBJECT-ORIENTED PROGRAMMING) - ADVANCED
# ==================================================

# In Day 6 we learn advanced OOP concepts:
# ✔ Inheritance (Advanced)
# ✔ Method Overriding
# ✔ Polymorphism (Real-world use)
# ✔ Encapsulation (Advanced)
# ✔ Abstraction


# ==================================================
# 1. INHERITANCE (ADVANCED)
# ==================================================

# Inheritance = child class uses parent class features
# super() = used to call parent class constructor/method

class Person:
    def __init__(self, name):
        self.name = name
        # parent class constructor

    def show(self):
        print("---------------------")
        print("Name:", self.name)


# Student class inherits Person class
class Student(Person):
    def __init__(self, name, age):
        # calling parent class constructor
        super().__init__(name)

        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


# creating object
s1 = Student("Ali", 20)
s1.show()         # parent method
s1.show_details() # child method


# ==================================================
# 2. METHOD OVERRIDING
# ==================================================

# Method Overriding = child class replaces parent method

class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    # overriding parent method
    def sound(self):
        print("Dog barks")


# object
obj = Dog()
obj.sound()  # child method will run


# ==================================================
# 3. POLYMORPHISM (REAL WORLD EXAMPLE)
# ==================================================

# Polymorphism = same method name, different behavior

class Bird:
    def move(self):
        print("Bird flies in sky")

class Fish:
    def move(self):
        print("Fish swims in water")

class Dog:
    def move(self):
        print("Dog runs on land")


# same function name, different behavior
animals = [Bird(), Fish(), Dog()]

for animal in animals:
    animal.move()


# ==================================================
# 4. ENCAPSULATION (ADVANCED)
# ==================================================

# Encapsulation = hiding data using private variables (__)

class Account:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    # method to deposit money
    def deposit(self, amount):
        self.__balance += amount

    # method to view balance safely
    def get_balance(self):
        return self.__balance


# creating object
acc = Account(1000)

# depositing money
acc.deposit(500)

# accessing balance safely
print("Current Balance:", acc.get_balance())


# ==================================================
# 5. ABSTRACTION
# ==================================================

# Abstraction = hiding internal complexity
# We use abstract class to enforce rules

from abc import ABC, abstractmethod


class Shape(ABC):
    # abstract method (no body)
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    # implementing abstract method
    def area(self):
        return 3.14 * self.r * self.r


class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w


# objects
c = Circle(5)
r = Rectangle(4, 6)

print("Circle Area:", c.area())
print("Rectangle Area:", r.area())


# ==================================================
# 🧠 SUMMARY (DAY 6)
# ==================================================

# ✔ Inheritance = reuse parent class
# ✔ Method Overriding = replace parent method
# ✔ Polymorphism = same method, different behavior
# ✔ Encapsulation = data hiding
# ✔ Abstraction = hide complexity, show only essentials
