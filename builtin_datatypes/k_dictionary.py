# Creation of dictionary
# O(len(dict)), O(N)
Dict = {1: 'Geeks', 2: 'for', 3:'Geeks'}
print(Dict)

Dict = {"Name":"Geeks", 1:[1, 2, 3, 4]}
print(Dict)

Dict = {}
print(Dict)

# using dict() function. Uses dict() constructor
Dict = dict({1:"dee", 2:"good", 3:"nice"})
print(Dict)

Dict = dict([(1, 'Geeks'), (2, "for")])
print(Dict)

# nested dictionary
Dict = {1:"Geeks", 2:"For", 3:{'A':'Welcome', 'B':"To", 'C':'Geeks'}}
print(Dict)

# Adding elements to dictionary
# O(1)/O(N), O(1)
Dict = {}
Dict[0]= "geeks"
Dict[2]= "For"
Dict[3] = 9
print(Dict)
Dict['Value_set'] = [2,3,4]
print(Dict)
Dict[2] = 'Welcome'
print(Dict)
Dict[5] = {'Nested':{'1':'Dee', '2': "kat"}}
print(Dict)

# Access a value in dictionary
# O(1), O(1)
Dict = {1:"dee", 'name': 'kat', 3:"kri"}
print(Dict['name'])
print(Dict[1])
print(Dict.get(2))
# get() method avoids keyError if key doesnt exist, provides safe way of accessing dict

Dict = {'Dict1':{1:'Geeks'}, 'Dict2':{'Name':'For'}}
print(Dict["Dict1"])
print(Dict['Dict1'][1])
print(Dict['Dict2']["Name"])

# Deleting an element in a dictionary
Dict = {1:"Geeks","name":"dee",3:"geeks"}
del(Dict[1])
print(Dict)

# dict methods
dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
dict2 = dict1.copy()
print(dict2)
dict1.clear()
print(dict1)
print(dict2.get(1))
print(dict2.items())
print(dict2.keys())
dict2.pop(4)
print(dict2)
dict2.popitem()
print(dict2)
dict2.update({3: "Scala"})
print(dict2)
print(dict2.values())

# MOST COMMONLY USED AND EFFICIENT METHODS TO ADD ELEMENTS IN DICT
# merge 2 dict using update
veg_dict = {0: 'Carrot', 1: 'Raddish',
			2: 'Brinjal', 3: 'Potato'}

veg_dict.update({4: 'Tomato', 5: 'Spinach'})
print(veg_dict)

# add values to dictionary using 2 lists of same length
roll_no = [10, 20, 30, 40, 50]
names = ['Ramesh', 'Mahesh', 'Kamlesh',
         'Suresh', 'Dinesh']

students = dict(zip(roll_no, names))
print(students)

# Converting a list to the dictionary
vegetables = ['Carrot', 'Raddish',
              'Brinjal', 'Potato']

veg_dict = dict(enumerate(vegetables))
print(veg_dict)

# works only in 3.9 plus
# Add values to dictionary Using the merge( | ) operator
veg1 = {0: 'Carrot', 1: 'Raddish'}
veg2 = {2: 'Brinjal', 3: 'Potato'}

veg_dict = (veg1 | veg2)
print(veg_dict)

# Add values to dictionary Using the in-place merge( |= ) operator.
veg1 = {0: 'Carrot', 1: 'Raddish'}
veg2 = {2: 'Brinjal', 3: 'Potato'}

veg1 |= veg2
print(veg1)

# keys method
D = {1: "dee", 2: "kri", 3: "bal"}
for key in D.keys():
    print(key,"",D[key], end=" ")
# values method
for value in D.values():
    print(value, end=" ")
# in
for i in D:
    print(i, D[i])
# list comprehension
print([(k, D[k]) for k in D])
# items()
for key, value in D.items():
    print(key, value)
# enumerate()
for i in enumerate(D.items()):
    print(i)

key_value_pairs = []

# Using a for loop to iterate over the items in the dictionary
# and append each key-value pair to the list
for key, value in test_dict.items():
    key_value_pairs.append((key, value))

# Printing the key-value pairs
print("Dict key-value are : ")
for pair in key_value_pairs:
    print(pair)
