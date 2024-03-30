# #Getting user from input using the input function
name = input("What is your name? ")
# # String concatenation
print("Hi "+ name)
name = input("What is your name? ")
colour = input("What is your favourite colour? ")
print(name + " likes " + colour)
# Type conversion--int(), float(), bool()
birth_year = input("Birth year: ")
print(type(birth_year))
age = 2023 - int(birth_year)
print(type(age))
print(age)
