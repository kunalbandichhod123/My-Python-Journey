# We can perform CRUD operations by using file handling about files
# We can create, Read, Update, Delete files

# we have open function to open any file but we should know its path first
# example ---> goto file and copy as path

# a = open("PYTHON CODES/File Handling/file.py")

# print(a.read())
# a.close()

# doing CRUD operations by using modes
# W ---> creates or overrites files
# r ---> Reads files 
# a ---> Append -- adds to end of file
# x ---> Creates new file (fails if already exists)

# this can just create a file cannot read now first we have to write inside it by using functions
a = open("superman.txt", 'a')   # now i put w hence it will create a file if not exists and reads it

a.write("\naee saale du kya re tere ko ek jhapad")  # now if we write something again it will replace the things we write now
# hence use append instead of w (a)

a.close()    # to save changes 

b = open("superman.txt")
print(b.read())
