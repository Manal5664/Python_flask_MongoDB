# ==================================================
# 🐍 DAY 5: OBJECT-ORIENTED PROGRAMMING (OOP) - BASICS
# ==================================================

# OOP (Object-Oriented Programming) is a programming style
# where we create classes and objects to organize code.

# ==================================================
# 1. INTRODUCTION TO CLASS & OBJECT
# ==================================================

# class = blueprint (design)
# object = real thing created from class

class Student:
    # method inside class
    def show(self):
        print("This is Student Class")

# creating object of class
s1 = Student()

# calling method using object
s1.show()


# ==================================================
# 2. INSTANCE VARIABLES & INSTANCE METHODS
# ==================================================

# instance variable = variables that belong to object
# instance method = function that uses object data

class Student:
    def __init__(self, name, age):
        # __init__ runs automatically when object is created
        # self refers to current object

        self.name = name   # instance variable
        self.age = age     # instance variable

    def display(self):
        # accessing instance variables using self
        print("---------------------")
        print("Student Details")
        print("Name:", self.name)
        print("Age:", self.age)

# creating objects with different data
s1 = Student("Ali", 20)
s2 = Student("Sara", 22)

# calling method
s1.display()
s2.display()


# ==================================================
# 3. CLASS VARIABLES & CLASS METHODS
# ==================================================

# class variable = shared by all objects
# class method = method that works with class variable

class Student:
    school = "ABC School"  # class variable (shared)

    def __init__(self, name):
        self.name = name

    def show(self):
        print("---------------------")
        print("Name:", self.name)
        print("School:", Student.school)

# objects
s1 = Student("Ali")
s2 = Student("Sara")

s1.show()
s2.show()


# class method example
class Student2:
    school = "ABC School"

    @classmethod
    def change_school(cls, new_school):
        # cls refers to class itself
        cls.school = new_school

# changing class variable
Student2.change_school("XYZ School")
print("Updated School:", Student2.school)


# ==================================================
# 4. ENCAPSULATION (DATA HIDING)
# ==================================================

# encapsulation = hiding internal data using __ (private variable)

class Bank:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def show_balance(self):
        print("---------------------")
        print("Bank Balance:", self.__balance)

# object
b1 = Bank(5000)

# accessing through method only (safe way)
b1.show_balance()

# NOTE:
# __balance cannot be accessed directly outside class


# ==================================================
# 5. INHERITANCE (BASIC)
# ==================================================

# inheritance = one class uses another class features

class Animal:
    def sound(self):
        print("Animal makes sound")

# Dog inherits Animal class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# object of child class

d1 = Dog()

# parent class method
d1.sound()

# child class method
d1.bark()


# ==================================================
# 6. POLYMORPHISM (BASIC)
# ==================================================

# polymorphism = same method name, different behavior

class Cat:
    def sound(self):
        print("Meow")

class Dog2:
    def sound(self):
        print("Bark")

# list of different objects
animals = [Cat(), Dog2()]

# loop through objects
for animal in animals:
    animal.sound()

