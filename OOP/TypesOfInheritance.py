# Single inheritance
# Python program to demonstrate
# single inheritance
#
# Base class
# class Parent:
# 	def func1(self):
# 		print("This function is in parent class.")
# # Derived class
# class Child(Parent):
# 	def func2(self):
# 		print("This function is in child class.")
#
# # Driver's code
# object = Child()
# object.func1()
# object.func2()
# ------------------------------------------------------------------------------------------------------------------------
# MultipleInheritance
# class Mother:
#     mothername= ""
#     def mother(self):
#         print(self.mothername)
# class Father:
#     fathername = ""
#     def father(self):
#         print(self.fathername)
#
# class Son(Mother, Father):
#     def parents(self):
#         print(self.fathername)
#         print(self.mothername)
#
# s1 = Son()
# s1.mothername = "DEE"
# s1.fathername = "KAT"
# s1.parents()
# ------------------------------------------------------------------------------------------------------------------------
# Multilevel
# class Grandfather:
#     def __init__(self,grandfathername):
#         self.grandfathername = grandfathername
#
# class Father(Grandfather):
#     def __init__(self, fathername, grandfathername):
#         self.fathername = fathername
#         Grandfather.__init__(self, grandfathername)
#
# class Son(Father):
#     def __init__(self, sonname, fathername, grandfathername):
#         self.sonname = sonname
#         Father.__init__(self, fathername, grandfathername)
#
#     def print_name(self):
#         print(self.grandfathername)
#         print(self.fathername)
#         print(self.sonname)
#
# s1 = Son("Kat", "Dee", "KD")
# s1.print_name()
# --------------------------------------------------------------------------------------------------------------------------------------------
# Python program to demonstrate
# Hierarchical inheritance
#
#
# Base class
# class Parent:
#     def func1(self):
#         print("This function is in parent class.")
#
#
# # Derived class1
#
#
# class Child1(Parent):
#     def func2(self):
#         print("This function is in child 1.")
#
#
# # Derivied class2
#
#
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child 2.")
#
#
# # Driver's code
# object1 = Child1()
# object2 = Child2()
# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()
# ------------------------------------------------------------------------------------------------------------------------------
# Hybrid
# class School:
#     def func1(self):
#         print("This function is in school.")
#
#
# class Student1(School):
#     def func2(self):
#         print("This function is in student 1. ")
#
#
# class Student2(School):
#     def func3(self):
#         print("This function is in student 2.")
#
#
# class Student3(Student1, School):
#     def func4(self):
#         print("This function is in student 3.")
#
#
# # Driver's code
# object = Student3()
# object.func1()
# object.func2()