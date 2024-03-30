Tuple1 = ()
print(Tuple1)

Tuple2 = ("deebiga", "Optimism")
print(Tuple2)

list = [1,2,3,4,5,6]
print(tuple(list))

Tuple1 = tuple("deebiga")
print(Tuple1)

Tuple1 = (5, "Hi", 4, "deebiga")
print(Tuple1)

Tuple1 = (0, 1, 2, 3)
Tuple2 = ("deebiga", "dee")
Tuple3 = (Tuple1, Tuple2)
print(Tuple3)

Tuple1 = ('Geeks,') * 3
print(Tuple1)

Tuple1 = ("Geeks")
n = 5
for i in range(n):
    Tuple1 = (Tuple1,)
    print(Tuple1)

# complexity for creating tuple = O(1)
# Auxiliary space = O(N)

test_list = ["dee", "is"]
test_str = "best"
print(test_list)
print(test_str)
# res = tuple(test_list + [test_str])
res = (test_str, ) + tuple(test_list)
print((res))

