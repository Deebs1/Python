course = "Python's course for 'beginners'"
print(course)
print(course[0])
print(course[-1])
print(course[-2])
print(course[0:3])
# End index assumed to be last char if not mentioned
print(course[0:])
print(course[1:])
# Start index assumed to be zero if not mentioned
print(course[:5])
# Both index assumed to be zero and last char if not mentioned
print(course[:])
# Triple quotes
course1 = '''
Hi Deebiga,

Here is ur first email.
'''
print(course1)
# Formatted strings - Dynamically generate text with variables
first = 'John'
last = 'Smith'
# Not Ideal:
message = first + ' [' + last + '] is a coder'
# Ideal:
msg = f'{first} [{last}] is a coder'
print(msg)

# String methods - Methods are specific to an object like str but functions are general purpose like print and input can be used generally.
course2 = "Python for beginners"
print(len(course2))
print(course2.upper())
# In the above and below method, a new string is created and then changed to uppercase and lowercase
print(course2.lower())
# Find method returns the index of the first occurence of the character
print(course.find('P'))
print(course2)


