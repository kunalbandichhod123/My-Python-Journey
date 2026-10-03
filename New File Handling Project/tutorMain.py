from pathlib import Path
import os

def ReadFileAndFolder():
    # Path('') targets your current working folder (where your terminal is open).
    # It converts the folder path into an advanced Python object instead of just a text string.
    path = Path('')

    # rglob('*') scans recursively—meaning it searches this folder AND all subfolders inside it.
    # '*' is a wildcard that grabs absolutely everything (all files, text documents, and folders).
    # list() takes all those found items and locks them into a neat, readable Python list.
    all_files = list(path.rglob('*'))


    for i, all_files in enumerate(all_files):
        print(f"{i + 1} : {all_files}")

def CreateFile():
    try:
        ReadFileAndFolder()
        name = input("Please tell the file name to create : ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as given_file:
                data = input("what you want to write in this file : ")
                given_file.write(data)

            print(f"File {name} Created Successfully !!!")
        else:
            print("this file already exist")

    except Exception as err:
        print(f"An error occured as {err}")


def readFile():
    try:
        ReadFileAndFolder()
        name = input("Please tell file name you want to read : ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as given_file:
                data = given_file.read()
                print(data)

            print("File Read successfull")
        else:
            print("the file does not exists")
    except Exception as err:
        print(f"There is an exception occured as {err}")


def updateFile():
    try:
        ReadFileAndFolder()
        name = input("Enter the file name to update the data in it : ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 5 to change the name of your file")
            print("Press 6 to overwrite the data of your file")
            print("Press 7 to appending some content in your file")

            res = int(input("Enter the number you want : "))
            if res == 5:
                name2 = input("tell your new file name : ")
                p2 = Path(name2)
                p.rename(p2)     ## rename the file p 

            if res == 6:
                with open(p, 'w') as given_file:
                    data = input("Tell what you want to write inside this file : ")
                    given_file.write(data)

            if res == 7:
                with open(p, 'a') as given_file:
                    data = input("tell what you want to append in file : ")
                    given_file.write(data)

    except Exception as err:
        print(f"An Error occured as {err}")



def deleteFile():
    try:
        ReadFileAndFolder()
        name - input("Tell the name of your file")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)
            print("File deleted Successfully")

        else:
            print("No such file found in the given directory")

    except Exception as err:
        print(f"There is an error occurred as {err}")


print("Press 1 to create a file")
print("Press 2 to read the file")
print("Press 3 to update or write inside file")
print("Press 4 to delete the file")

check = int(input("Enter the number for operation to perform : "))

if check == 1:
    CreateFile()

if check == 2:
    readFile()

if check == 3:
    updateFile()

if check == 4:
    deleteFile()




    