# L = ["deebiga\n","krithi\n","varuna\n"]

# file = open("sample.txt","w+")
# # file.write("deebiga")
# file.writelines(L)
# file.seek(0)
# file.close()
# print(file.read())

# Python program to illustrate
# Append vs write mode
# file1 = open("myfile.txt", "w")
# L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
# file1.writelines(L)
# file1.close()
#
# # Append-adds at last
# file1 = open("myfile.txt", "a")  # append mode
# file1.write("Today \n")
# file1.close()
#
# file1 = open("myfile.txt", "r")
# print("Output of Readlines after appending")
# print(file1.read())
# print()
# file1.close()
#
# # Write-Overwrites
# file1 = open("myfile.txt", "w")  # write mode
# file1.write("Tomorrow \n")
# file1.close()
#
# file1 = open("myfile.txt", "r")
# print("Output of Readlines after writing")
# print(file1.read())
# print()
# file1.close()

# with statement in Python is used in exception handling to make the code cleaner and much more readable. It simplifies the management of common resources like file streams. Unlike the above implementations, there is no need to call file.close() when using with statement. The with statement itself ensures proper acquisition and release of resources.
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Writing to file
with open("myfile.txt", "w") as file1:
    # Writing data to a file
    file1.write("Hello \n")
    file1.writelines(L)

# Reading from file

with open("myfile.txt", "r+") as file1:
    # Reading form a file
    print(file1.read())