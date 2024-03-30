# Before performing any operation on the file like reading or writing, first, we have to open that file. For this, we should use Python’s inbuilt function open() but at the time of opening, we have to specify the mode, which represents the purpose of the opening file.
#
# f = open(filename, mode)
# Where the following mode is supported:
#
# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data, then it will be overridden but if the file is not present then it creates the file as well.
# a:  open an existing file for append operation. It won’t override existing data.
# r+:  To read and write data into the file. The previous data in the file will be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.
# READ
# file = open("sample.txt", "r")
# for lines in file:
#     print(lines)
# # print(file.read())
#
# with open("sample.txt") as file:
#     data = file.read()
#     data = file.read(5)
# print(data)

# with open("sample.txt", "r") as file:
#     data = file.readlines()
#     for line in data:
#         word = line.split()
#         print(word)
# WRITE
# file = open("sample.txt", "w")
# file.write("This is the write command")
# file.write("It allows to write")
# file.close()

# with open("sample.txt", "w") as f:
#     f.write("Hello world")

# APPEND
# file = open("sample.txt", "a")
# file.write("This will add this line")
# file.close()

