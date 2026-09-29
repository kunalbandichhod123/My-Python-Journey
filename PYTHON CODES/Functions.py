# print("hello") # in built functions

# create function (user defined functions)
# use def to create functions(defined)

# def hello():
#     print("This is hello function ")

# hello() # function call

# def sum(a, b):
#     print(f"The sum of your number is : {a + b}" )

# sum(5, 10)

# def hello(name, age):
#     print(f"your name is {name} and your age is {age}")

# hello("kunal", 21) ## OR 
# hello(name = "neha", age = 22)

# def sum(a, b = 54):
#     print(f"the sum is {a + b}")
# sum(12, )
# # OR
# sum(12, 34)


# Check string is PALINDROME OR NOT
# def palindrome(st):
#     rev = ""
#     for i in range(len(st)-1, -1, -1):
#         rev = rev + st[i]
#     if rev == st:
#         print("is Palindrome")
#     else:
#         print("Not Palindrome")

# palindrome("madam")



#  Return type functions
def hello():
    return "Kunal"

print(hello())