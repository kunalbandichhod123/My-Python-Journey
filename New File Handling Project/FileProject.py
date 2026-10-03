import os   # needed to delete files

print()
print("Press 1 for creating a file")
print("Press 2 for reading the file")
print("Press 3 for updating a file")
print("Press 4 for deletion a file")
print()

check = int(input("Enter your operation to perform : "))


if check == 1:
    file_name = input("Enter the file name to create : ")
    a = open(f"{file_name}", 'w')
    a.close()


if check == 2:
    file_path = input("Please enter the file path to open the file : ")
    a = open(f"{file_path}", 'r')
    print(a.read())
    a.close()


if check == 3:
    file_path = input("Enter the file name Or Path you want to update : ")
    text_to_add = input("Please write whatever you want to update in file : ")
    a = open(f"{file_path}", 'a')
    a.write(f"now write : {text_to_add}")
    a.close()
    print("File update successfully!!!!")

    
if check == 4:
    file_delete = input("Please enter the path of the file you want to delete : ")
    if os.path.exists(file_delete):
        os.remove(file_delete)
        print(f"File {file_delete} deleted successfully...!!")

    else:
        print("Invalid path???")