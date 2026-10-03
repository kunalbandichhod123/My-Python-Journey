# We can perform CRUD operations by using file handling about files
# We can create, Read, Update, Delete files

# we have open function to open any file but we should know its path first
# example ---> goto file and copy as path

file = open("C:\Python Full course\PYTHON CODES\Functions.py")

print(file.read())


# doing CRUD operations by using modes
# W ---> creates or overrites files
# r ---> Reads files 
# a ---> Append -- adds to end of file
# x ---> Creates new file (fails if already exists)


a = open("superman.txt", 'w')
# print(a.read())