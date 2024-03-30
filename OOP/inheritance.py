# A Python program to demonstrate inheritance (example1)
#
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
# class Person(object):
#
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#     def Display(self):
#         print(self.name, self.id)
#
# class Emp(Person):
#     def Print(self):
#         print("Emp class called")
#
# emp = Person("Deebiga", 7)
# emp.Display()
# # Emp_details = Emp("Deebiga", 7)
# # Emp_details.Display()
# # Emp_details.Print()
# -------------------------------------------------------------------------------------------------------------------
# Example-2
# class Person(object):
#
#     # Constructor
#     def __init__(self, name):
#         self.name = name
#
#     # To get name
#     def getName(self):
#         return self.name
#
#     # To check if this person is an employee
#     def isEmployee(self):
#         return False
#
#
# # Inherited or Subclass (Note Person in bracket)
# class Employee(Person):
#
#     # Here we return true
#     def isEmployee(self):
#         return True
#
#
# # Driver code
# emp = Person("Geek1")  # An Object of Person
# print(emp.getName(), emp.isEmployee())
#
# emp = Employee("Geek2")  # An Object of Employee
# print(emp.getName(), emp.isEmployee())
# --------------------------------------------------------------------------------------------------------------
# without subclassing
#







# ----------------------------------------------------------------------------------------------------------------------
# A program to demonstrate subclassing
# calling parent constructors in child's class
#
# class Person(object):
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
#
# class Employee(Person):
#     def __init__(self,name, idnumber,salary, post):
#         self.salary = salary
#         self.post = post
#         Person.__init__(self, name, idnumber)
#
#
# emp = Employee("dee", 444, 898, "jd")
# emp.display()
# ----------------------------------------------------------------------------------------------------------------------
# Another example without subclassing
# class A:
#     def __init__(self, n='Rahul'):
#         self.name = n
# class B(A):
#     def __init__(self, roll):
#         self.roll = roll
#
# object = B(23)
# print(object.name)
# ----------------------------------------------------------------------------------------------------------------------
# With subclassing
# class A:
#     def __init__(self, n='Rahul'):
#         self.name = n
# class B(A):
#     def __init__(self, n, roll):
#         self.roll = roll
#         A.__init__(self, n)
#
# object = B("Rahul", 23)
# print(object.name)
# ----------------------------------------------------------------------------------------------------------------------
# superclass
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print(self.name, self.age)
#
#
# # child class
# class Student(Person):
#     def __init__(self, name, age):
#         self.sName = name
#         self.sAge = age
#         # inheriting the properties of parent class
#         super().__init__(name, age)
#
#     def displayInfo(self):
#         print(self.sName, self.sAge)
#
#
# obj = Student("Mayank", 23)
# obj.display()
# obj.displayInfo()
# ----------------------------------------------------------------------------------------------------------------------
# Adding properties
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print(self.name, self.age)
#
#
# # child class
# class Student(Person):
#     def __init__(self, name, age, dob):
#         self.sName = name
#         self.sAge = age
#         self.dob = dob
#         # inheriting the properties of parent class
#         super().__init__("Rahul", age)
#
#     def displayInfo(self):
#         print(self.sName, self.sAge, self.dob)
#
#
# obj = Student("Mayank", 23, "16-03-2000")
# obj.display()
# obj.displayInfo()
# Private members of the parent class
# We don’t always want the instance variables of the parent class to be inherited by the child class
# i.e. we can make some of the instance variables of the parent class private, which won’t be available
# to the child class.
#
# In Python inheritance, we can make an instance variable private by adding double underscores before its name. For example:
# Python program to demonstrate private members
# of the parent class
#
# class C(object):
# 	def __init__(self):
# 		self.c = 21
#
# 		# d is private instance variable
# 		self.__d = 42
#
#
# class D(C):
# 	def __init__(self):
# 		self.e = 84
# 		C.__init__(self)
#
# object1 = D()
#
# # produces an error as d is private instance variable
# print(object1.c)
# print(object1.__d)
# ------------------------------------------------------------------------------------------------------------------------
