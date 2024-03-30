# A simple Python function

# def fun():
#     print("Welcome to GFG")

# fun()
# ====================================================================

# Defining and calling a function with parameters
#
#  def function_name(parameter: data_type) -> return_type:
#     """Docstring"""
#     # body of the function
#     return expression

# example
# def add(num1: int, num2: int) -> int:
#     """Add two numbers"""
#     num3 = num1 + num2
#
#     return num3
#
#
# # Driver code
# num1, num2 = 5, 15
# ans = add(num1, num2)
# print(f"The addition of {num1} and {num2} results {ans}.")
# =========================================================================

# Default arguments
# # Python program to demonstrate
# # default arguments
# def myFun(x, y=50):
#     print("x: ", x)
#     print("y: ", y)
#
#
# # Driver code (We call myFun() with only
# # argument)
# myFun(10)

# Like C++ default arguments, any number of arguments in a function can have a default value.
# But once we have a default argument, all the arguments to its right must also have default values.

# =========================================================================

# Keyword Arguments
# The idea is to allow the caller to specify the argument name with values so that the caller does not need to remember the order of parameters.
#
# # Python program to demonstrate Keyword Arguments
# def student(firstname, lastname):
#     print(firstname, lastname)
#
#
# # Keyword arguments
# student(firstname='Geeks', lastname='Practice')
# student(lastname='Practice', firstname='Geeks')

# =============================================================================

# position arguments

# def nameAge(name, age):
#     print("Hi, I am", name)
#     print("My age is ", age)
#
#
# # You will get correct output because
# # argument is given in order
# print("Case-1:")
# nameAge("Suraj", 27)
# # You will get incorrect output because
# # argument is not in order
# print("\nCase-2:")
# nameAge(27, "Suraj")

# ============================================================================

# Arbitrary arguments

# *args in Python (Non-Keyword Arguments)
# **kwargs in Python (Keyword Arguments)

# # Python program to illustrate
# # *args for variable number of arguments
# def myFun(*argv):
#     for arg in argv:
#         print(arg)
#
#
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# # Python program to illustrate
# # *kwargs for variable number of keyword arguments
#
#
# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))
#
#
# # Driver code
# myFun(first='Geeks', mid='for', last='Geeks')

# ========================================================================
# Docstring
# The first string after the function is called the Document string or Docstring in short. This is used to describe the functionality of the function.
# The use of docstring in functions is optional but it is considered a good practice.
# # A simple Python function to check
# # whether x is even or odd
#
#
# def evenOdd(x):
#     """Function to check if the number is even or odd"""
#
#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")
#
#
# # Driver code to call the function
# print(evenOdd.__doc__)

# ============================================================================
# Pass by Reference and Pass by Value
# One important thing to note is, in Python every variable name is a reference.
# When we pass a variable to a function, a new reference to the object is created.
# Parameter passing in Python is the same as reference passing in Java.
#
# # Here x is a new reference to same list lst
# def myFun(x):
#     x[0] = 20
#
#
# # Driver Code (Note that lst is modified
# # after function call.
# lst = [10, 11, 12, 13, 14, 15]
# myFun(lst)
# print(lst)

# When we pass a reference and change the received reference to something else,
# the connection between the passed and received parameters is broken. For example, consider the below program as follows:
#
# def myFun(x):
#
#     # After below line link of x with previous
#     # object gets broken. A new object is assigned
#     # to x.
#     x = [20, 30, 40]
#
#
# # Driver Code (Note that lst is not modified
# # after function call.
# lst = [10, 11, 12, 13, 14, 15]
# myFun(lst)
# print(lst)


# Another example demonstrates that the reference link is broken if we assign a new value (inside the function).
#
# def myFun(x):
#
#     # After below line link of x with previous
#     # object gets broken. A new object is assigned
#     # to x.
#     x = 20
#
#
# # Driver Code (Note that x is not modified
# # after function call.
# x = 10
# myFun(x)
# print(x)


# def swap(x, y):
#     temp = x
#     x = y
#     y = temp
#
#
# # Driver code
# x = 2
# y = 3
# swap(x, y)
# print(x)
# print(y)
# ================================================================================
