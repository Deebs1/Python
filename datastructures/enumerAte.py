l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
obj1 = enumerate(l1)
obj2 = enumerate(s1)
print(list(enumerate(l1)))
print(list(enumerate(s1)))

for ele in enumerate(l1):
    print(ele)

for count, ele in enumerate(l1, 100):
    print(count, ele)

for count, ele in enumerate(l1):
    print(count)
    print(ele)