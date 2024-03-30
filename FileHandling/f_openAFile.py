# open function takes read as default if access mode is not mentioned
# file1 = open("sample.txt")
# print(file1.read())
# file1.close()

# file1 = open("sample.txt", "a")
# file1.write("Deebiga")
# file1.close()

# file = open("sample.txt", "w+")
# file.write("hello world")
# file.seek(0)
# print(file.read())
# file.close()

file = open("sample.txt", "r")
line = file.readline()
while line:
    print(line)
    line = file.readline()

