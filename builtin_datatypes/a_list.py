# lists in python are dynamically sized arrays
# lists are heterogeneous
# lists can even store objects and are mutable

# Creating a list
# List = []
# print(List)
#
# List1 = [10, 20, 14]
# print(List1)
#
# List2 = ["Geeks", "for", "geeks"]
# print(List2)

# TC = O(1)
# SC = O(N)
# ===========================================================================
# # Creating a List with
# # the use of Numbers
# # (Having duplicate values)
# List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
# print("\nList with the use of Numbers: ")
# print(List)
#
# # Creating a List with
# # mixed type of values
# # (Having numbers and strings)
# List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
# print("\nList with the use of Mixed Values: ")
# print(List)
# ============================================================================

# # Python program to demonstrate
# # accessing of element from list
#
# # Creating a List with
# # the use of multiple values
# List = ["Geeks", "For", "Geeks"]
#
# # accessing a element from the
# # list using index number
# print("Accessing a element from the list")
# print(List[0])
# print(List[2])
# ===========================================================================
# Negative indexing
# List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
#
# # accessing an element using
# # negative indexing
# print("Accessing element using negative indexing")
#
# # print the last element of list
# print(List[-1])
#
# # print the third last element of list
# print(List[-3])
# TC,SC for accessing is O(1)
# ======================================================================
# getting size
# List2 = [10, 20, 14]
# print(len(List2))
# ==============================================================================
# getting list input
# string = input("Enter elements (Space-separated): ")
#
# lst = string.split()
# print("The list is: ", lst)
# =============================================================================
# # input size of the list
# n = int(input("Enter the size of list : "))
# # store integers in a list using map,
# # split and strip functions
# lst = list(map(int, input("Enter the integer\
# elements:").strip().split()))[:n]
#
# # printing the list
# print('The list is:', lst)
# ====================================================================================
# Adding elements
#
