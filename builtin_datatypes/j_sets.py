var = {"geeks", "for", "geeks"}
print(type(var))
# O(1), O(1)

# set is unordered
lst = ["a","b","c","d"]
myset = set(lst)
print(myset)

myset.add("e")
print(myset)


# set cannot have duplicate items
mysett = {"dee", "7", "dee"}
print(mysett)

# values cannot be changed in set
# myset[1] = "10"
# print(mysett)

# heterogeneous element inn set
mysettt = {"dee", 22, 9.2, True}
print(mysettt)

# frozen set
normal_set = set(["a","b","c","d"])
print(normal_set)
frozen_set = frozenset(["a","b","c"])
# frozen_set.add("i")
print(frozen_set)

# method for set

people = {"dee","kri","var"}
print(people)
people.add("kum")
people.add('dee')
for i in range(6):
    people.add(i)
print(people)

# union operation on set
# O(len(s1) +len(s2))
people = {"dee", "kri","var"}
vampires = {"bal","kat"}
dracula = {"abc", "def"}

population = people.union(vampires)
print(population)
population = people|dracula
print(population)

# intersection operation on set
# O(min(len(s1), len(s2))

set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)
for i in range(3, 9):
    set2.add(i)

set3 = set1.intersection(set2)
print(set3)

set3 = set1 & set2
print(set3)

set3 = set1.difference(set2)
# set3 = set1-set2
print(set3)

# clearing python set
set1.clear()
print(set1)
