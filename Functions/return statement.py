# returning a single value

# def add(a, b):
#
#     # returning sum of a and b
#     return a + b
#
# def is_true(a):
#
#     # returning boolean of a
#     return bool(a)
#
# # calling function
# res = add(2, 3)
# print("Result of add function is {}".format(res))
#
# res = is_true(2<5)
# print("\nResult of is_true function is {}".format(res))

# ==================================================================

# return multiple values

# using objects

# class Test:
#     def __init__(self):
#         self.str = "geeksforgeeks"
#         self.x = 20
#
# # This function returns an object of Test
# def fun():
#     return Test()
#
# # Driver code to test above method
# t = fun()
# print(t.str)
# print(t.x)


# using tuple
# # A Python program to return multiple
# # values from a method using tuple
#
# # This function returns a tuple
# def fun():
#     str = "geeksforgeeks"
#     x = 20
#     return str, x;  # Return tuple, we could also
#                     # write (str, x)
#
# # Driver code to test above method
# str, x = fun() # Assign returned tuple
# print(str)
# print(x)


# using list

# # A Python program to return multiple
# # values from a method using list
#
# # This function returns a list
# def fun():
#     str = "geeksforgeeks"
#     x = 20
#     return [str, x];
#
# # Driver code to test above method
# list = fun()
# print(list)


# dictionary
# # A Python program to return multiple
# # values from a method using dictionary
#
# # This function returns a dictionary
# def fun():
#     d = dict();
#     d['str'] = "GeeksforGeeks"
#     d['x']   = 20
#     return d
#
# # Driver code to test above method
# d = fun()
# print(d)
# ====================================================================================


# # Python program to illustrate functions
# # can return another function
#
# def create_adder(x):
#     def adder(y):
#         return x + y
#
#     return adder
#
# add_15 = create_adder(15)
#
# print("The result is", add_15(10))
#
# # Returning different function
# def outer(x):
#     return x * 10
#
# def my_func():
#
#     # returning different function
#     return outer
#
# # storing the function in res
# res = my_func()
#
# print("\nThe result is:", res(10))