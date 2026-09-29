# print("Hello World!!!")
# # making variables

# sher = "kunal"
# print(sher)

# SheryiansSchool = "MehiHu"
# sheriansSchool = "yes"
# Kunal_bhai = 12

# # understanding datatypes

# a = 12
# b = 6
# c = a / b
# print(type(c))

# string = "Bhai sahab ye to gajab hai12134@#$%&**()"
# str = True
# print(str)
# print(string)
# # string indexing
# print(string[0])

# #slicing
# newstr = "SHER Bhai"
# print(newstr[5::10])


## type conversion

# a = 12

# a = str(a)  #typecasting
# print(type(a))

# prints
# a = "12"
# name = "Kunal"
# print(a, name)
# print(f"my name is {name} and age is {a}")

# ## input functions
# # input("What is your age : ") ## this goes to garbage collectoras no variable is there
# # hence we can assign variables too
# age = input("What is your age : ")
# print(f"so your age is : {age}")


# Arithmetic operators
# a = 10
# b = 2
# print(a + b)
# # orr
# c = a + b
# print(c)

# print(a // b)  # this will give in float like 5.0 but if we want in not floate just use //
# print(a * b)
# print(b % a)
# print(a ** b) # double power


# ## Comparison Operators
# print("ABC" > "ACD")  #ASCII values
# # Logical Operators
# print(not 12 == 12) # makes output to false even if true

# print(12 != 12) # this is also same



# # Conditional Statements (if, if else, else, switch)

# if a > 10 :
#     print("yess")
# else :
#     print("No")


# age = int(input("Please type your age : "))
# if(age >= 18) :
#     print("You can vote !!!")
# elif(age < 18):
#     print("You cannot vote hattt!!!")
# else:
#     print("Incorrect age")


# Loops in python
# a = range(5, 51, 5)
# for i in a:   # range me start ki value default 0 hoti hai but we must declare at least stop value means middle value
#     print(i)

#     # Reverse order in for loop
# for j in range(20, 0, -1):
#     print(j)

# a = "Kunal"

# for char in a:
#     print(char)

# input for making n table
n = int(input("Enter the number you want for table : "))

for i in range(n, (n * 10)+1, n):   # range me start ki value default 0 hoti hai but we must declare at least stop value means middle value
    print(i)

# Printing complete string by for loops 
# a = "Kunal is doing python classes everyday and updating his journey on github"
# print(len(a))
# for i in range(len(a)):
#     print(a[i], end = "") # the end = "," is to print on same line


# Using Break and Continue in loops
# for i in range(1 , 21):
#     if i == 11 :
#         break
#     else :
#         print(i)

# for j in range(1, 21):
#     if j == 15 :   # 15 will skip now instead of stopping like break
#         continue
#     else:
#         print(j)

n =  5 #int(input("Enter the Number for how much time you want to print : "))

# for i in range(n):
#     print("kunal", end = " ")

# for j in range(n, 0, -1):    reverse printing upto 1 from n
#     print(j)
