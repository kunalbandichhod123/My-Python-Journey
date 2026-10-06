# ## Decorators
# class Animal:
#     @property
#     def show(self):
#         print("hello how are you??")

# obj = Animal()
# # obj.show()
# obj.show ## this will not print anything hence to make it work as a decorator we have to use @property


# decorator in function calls

# def decorate(func):
#     def wrapper():
#         print("I will print myself before the function hello")
#         func()
#         print("I will print after the function")
#     return wrapper

# # to use this properly we have to make wrapper function
# @decorate
# def hello():
#     print("hello I am kunal bhai")


# hello()



# *Args and arguments
# def addition(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i

#     print(sum)

# addition(12, 42, 23, 56)    used to capture multiple arguments


# Kwargs ---> Keywords Arguments ---> have to use **

# def information(**kwargs):
#     print("your information is \n\n ")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")

# information(name = "kunal", age = 20, designation = "AiML")

# we can do other way too : 

def information(**kwargs):
    print("your information is \n\n ")
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")

information(name = "kunal", age = 20, designation = "AiML")