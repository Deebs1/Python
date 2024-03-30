numbers = [12, 13, 14]
doubled = [i * 2 for i in numbers]
# for i in numbers:
#     x = i * 2
#     doubled.append(x)
print(doubled)

numbers1 = [1, 2,3,4,5]
squared = [x ** 2 for x in numbers1]
print(squared)

List = [character for character in [1, 2, 3]]
print(List)

List1 = [i for i in range(11) if i % 2 == 0]
print(List1)

matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)

List2 = [character for character in "Geeks 4 Geeks"]
print(List2)

numbers = [i*10 for i in range(1,6)]
print(numbers)

lis = ["Even number" if i%2==0 else "Odd number" for i in range(11)]
print(lis)
