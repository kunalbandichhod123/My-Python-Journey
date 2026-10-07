import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    try : 
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An exception occured as {err}")



    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data, indent=4))

    @classmethod
    def __accountgenerate(cls):
        alphabets = random.choices(string.ascii_letters, k = 3)
        num = random.choices(string.digits, k = 3)
        spchar = random.choices("!@#$%^&*", k = 1)
        id = alphabets + num + spchar
        random.shuffle(id)
        return "".join(id)

    
    def CreateAccount(self):
        info = {
            "name" : input("Tell your name : "),
            "Age" : int(input("Tell your age : ")),
            "E-mail" : input("Tell your E-mail : "),
            "Pin" : int(input("Tell your pin : ")),
            "Account No." : Bank.__accountgenerate(),
            "Balance" : 0
        }
        if info['Age'] < 18 or len(str(info['Pin'])) != 4:
            print("Sorry you cannot create your account check your age or password!!!")
        else:
            print("Account created Successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number !!")


            Bank.data.append(info)
            Bank.__update()


    def depositmoney(self):
        accnumber = input("Please tell your account number : ")
        pin = int(input("please tell you pin : "))

        userdata = [i for i in Bank.data if i['Account No.'] == accnumber and i['Pin'] == pin]
        if not userdata:
            print("Sorry no records found!! check the pin or account number")

        else:
            amount = int(input("How much money you want to deposit :- "))
            if amount >= 10000 or amount <= 0:
                print("sorry you cannot deposit amount to your bank account")
            else:
                userdata[0]['Balance'] += amount
                Bank.__update()
                print("Amount deposited successfully to your bank account!!")


    
    def withdrawmoney(self):
        accnumber = input("Please tell your account number : ")
        pin = int(input("please tell you pin : "))

        userdata = [i for i in Bank.data if i['Account No.'] == accnumber and i['Pin'] == pin]
        if not userdata:
            print("Sorry no records found!! check the pin or account number")

        else:
            amount = int(input("How much money you want to withdraw from your account :- "))
            if userdata[0]['Balance'] < amount:
                print("sorry you cannot withdraw amount from your bank account")
            else:
                userdata[0]['Balance'] -= amount
                Bank.__update()
                print("Amount deducted from your account successfully !!")



    def showdetails(self):
        accnumber = input("Please tell your account number : ")
        pin = int(input("please tell you pin : "))

        userdata = [i for i in Bank.data if i['Account No.'] == accnumber and i['Pin'] == pin]
        print("Your information is : \n\n")

        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")



    def updatedetails(self):
        accnumber = input("Please tell your account number : ")
        pin = int(input("please tell you pin : "))

        userdata = [i for i in Bank.data if i['Account No.'] == accnumber and i['Pin'] == pin]
        if not userdata:    ## means if its empty
            print("No user found please check your Account number or pin")
        else:
            print("you cannot change the age, account number, balance")

            print("Fill the details for change or leave it empty if no changes")

            newdata = {
                "name" : input("Please tell new name or press enter : "),
                "E-mail" : input("Please tell your new email or press enter to skip : "),
                "Pin" : input("Enter new pin or press enter to skip : ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["E-mail"] == "":
                newdata["E-mail"] = userdata[0]['E-mail']
            if newdata["Pin"] == "":
                newdata["Pin"] = userdata[0]['Pin'] 

            newdata['Age']  = userdata[0]['Age']    
            newdata['Account No.']  = userdata[0]['Account No.']              
            newdata['Balance']  = userdata[0]['Balance']   

            if type(newdata['Pin']) == str :
                newdata['Pin'] = int(newdata['Pin']) 

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]  

            Bank.__update()
            print("Details are updated successfully !!!")



    def delete(self):
        accnumber = input("Please tell your account number : ")
        pin = int(input("please tell you pin : "))

        userdata = [i for i in Bank.data if i['Account No.'] == accnumber and i['Pin'] == pin] 

        if not userdata:    ## means if its empty
            print("No user found please check your Account number or pin")
        else:
            check = input("Press Y if you really want to delete the account or press N")
            if check == 'n' or check == 'N':
                pass
            # if check == 'y' or check == 'Y'
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted successfully !!")

                Bank.__update()




user = Bank()
print("Press 1 for creating an accounting")
print("Press 2 for depositing the money in the bank")
print("Press 3 for withdrawing the money from the bank")
print("Press 4 for getting bank details")
print("Press 5 for updating the details of account holder")
print("Press 6 to delete your bank account")


check = int(input("Tell your response : "))

if check == 1:
    user.CreateAccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.delete()