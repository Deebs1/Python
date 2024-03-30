# in-built polymorphism
# print(len("geeks"))
# print(len([10, 20, 30]))
# ===================================================================================================
# user_defined polymorphism
# def add(x, y, z=0):
#     return x+y+z
# print(add(2,3))
# print(add(2,3,4))
# =========================================================================================================
# polymorphism usiing class methods
# The below code shows how Python can use two different class types, in the same way.

# We create a for loop that iterates through a tuple of objects.
# Then call the methods without being concerned about which class type each object is.
# We assume that these methods actually exist in each class.
# class India:
#     def capital(self):
#         print("New delhi")
#     def language(self):
#         print("Hindi")
#     def type(self):
#         print("developing")
#
# class USA:
#     def capital(self):
#         print("Washington")
#     def language(self):
#         print("English")
#     def type(self):
#         print("developed")
#
# obj_ind = India()
# obj_USA = USA()
#
# for country in (obj_ind, obj_USA):
#     country.capital()
#     country.language()
#     country.type()
# =====================================================================================================================
# Polymorphism with inheritance(method overriding)
# class Bird:
#   def intro(self):
#     print("There are many types of birds.")
#
#   def flight(self):
#     print("Most of the birds can fly but some cannot.")
#
# class sparrow(Bird):
#   def flight(self):
#     print("Sparrows can fly.")
#
# class ostrich(Bird):
#   def flight(self):
#     print("Ostriches cannot fly.")
#
# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()
#
# obj_bird.intro()
# obj_bird.flight()
#
# obj_spr.intro()
# obj_spr.flight()
#
# obj_ost.intro()
# obj_ost.flight()
# ======================================================================================================================
# Polymorphism with function
# class India():
#     def capital(self):
#         print("New Delhi is the capital of India.")
#
#     def language(self):
#         print("Hindi is the most widely spoken language of India.")
#
#     def type(self):
#         print("India is a developing country.")
#
# class USA():
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")
#
#     def language(self):
#         print("English is the primary language of USA.")
#
#     def type(self):
#         print("USA is a developed country.")
#
# def func(obj):
#     obj.capital()
#     obj.language()
#     obj.type()
#
# obj_ind = India()
# obj_usa = USA()
#
# func(obj_ind)
# func(obj_usa)
# ======================================================================================================================
# Method overriding
# class Animal:
#     def speak(self):
#         raise NotImplementedError("Subclass must implement this method")
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
#
# # Create a list of Animal objects
# animals = [Dog(), Cat()]
#
# # Call the speak method on each object
# for animal in animals:
#     print(animal.speak())
