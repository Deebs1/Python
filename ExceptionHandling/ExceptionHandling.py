#Syntax error==missing colon, unbalanced parenthesis, indentation, wrong variable name
# amt = 10000
# if(amt>100):
#     print("You are eligible")

# Exceptions
# ZeroDivisionError
# marks = 100
# a = marks/0
# print(a)

# TypeError
# x = 5
# y = "hello"
# z = x+y


# Handling the exception
# x = 5
# y = "hello"
# try:
#     z = x+y
# except:
#     print("Error: cannot add an int and a str")

# # IndexError
# a = [1, 2, 3]
# try:
#     print(a[1])
#     print(a[3])
# except:
#     print("An error occured")

# Catching specific exception
# try:
#     statement(s)
# except IndexError:
#     statement(s)
# except ValueError:
#     statement(s)

# Example
# def fun(a):
#     if a<4:
#         b = a/(a-3)
#     print("Value of b= ", b)
# try:
#     fun(3)
#     fun(5)
# except ZeroDivisionError:
#     print("ZeroDivisionError occured and handled")
# except NameError:
#     print("name error occured and handled")

# With else clause
# def AbyB(a, b):
#     try:
#         c = ((a+b)/(a-b))
#     except ZeroDivisionError:
#         print("a/b result in 0")
#     else:
#         print(c)
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)

# Finally keyword
# try:
#     # Some Code....
#
# except:
#     # optional block
#     # Handling of exception (if required)
#
# else:
#     # execute if no exception
#
# finally:
#     # Some code .....(always executed)

# Example
# try:
#     k = 5 // 0
#     print(k)
#
# except ZeroDivisionError:
#     print("Can't divide by zero")
#
# finally:
#     print('This is always executed')

# Raisingexceptions
# try:
#     raise NameError("Hi there")
# except NameError:
#     print ("An exception")
#     raise

# try:
#     amount = 1999
#     if amount < 2999:
#         raise ValueError("Please add money to your account")
#     else:
#         print("You are eligible to purchase DSA Self Paced course")
# except ValueError:  # Indented one level further
#     print("Value error")

# try:
#     amount = 1999
#     if amount < 2999:
#         raise ValueError("Please add money to your account")
#     else:
#         print("You are eligible to purchase DSA Self Paced course")
# except ValueError as e:  # Indented one level further
#     print(e)


