# Errors --> error in code which prevents from running
# ----> syntax errors      &&      Indentation Errors


# Exceptions
# --> unexpected events that occurs and make program halt in mid processing or compile during execution   eg) divide by 0
# like array boundary errors

# try ---> if you think that ye line error cause kr sakti hai so wrap it in try:
# except ---> handles if exception occurs
# else   ---> 
# finally
# raise



# a = int(input("Tell your number : "))  # consider a = 0

# try:
#     print(10/a)
# # except ZeroDivisionError:  # this is inbuilt function but lets say the errors are rather than 0 then how? 
#     # so use this universal function
# except Exception as err:     # err is varible you can give any name to it
#     print(f"Sorry there is an error as {err}")

# else:
#     print("Good there is no exception")

# finally:
#     print("i will run no matter what!!")

# print("Ok i have done the division")

# Raise
age = int(input("Tell your age : "))

if age < 10 or age > 18:
    raise ValueError("your age must be between 10 and 18")
else:
    print("Welcome to the club")


print("The club will start soon!!")