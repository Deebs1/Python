
# Read Only (‘r’) : Open text file for reading. The handle is positioned at the beginning of the file. If the file does not exists, raises I/O error. This is also the default mode in which file is opened.
# Read and Write (‘r+’) : Open the file for reading and writing. The handle is positioned at the beginning of the file. Raises I/O error if the file does not exists.
# Append and Read (‘a+’) : Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

# file = open("sample.txt", "r")
# print(file.read())
# file.seek(0)
# print(file.readline())
# file.seek(0)
# print(file.readlines())
# file.seek(0)
# print(file.readlines())
# file.close()

# Program to show various ways to
# read data from a file.

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Creating a file
with open("sample.txt", "w+") as file1:
    # Writing data to a file
    file1.write("Hello \n")
    file1.writelines(L)
    file1.seek(0)
    print(file1.read())
    file1.close()  # to change file access modes

# with open("sample.txt", "r+") as file1:
    # Reading from a file
    # print(file1.read())