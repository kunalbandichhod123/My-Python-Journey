# Ternory operators
# a = 12
# print("even") if a % 2 == 0 else print("Odd")

# l = []
# for i in range(1, 21):
#     if i % 2 == 0:
#         l.append(i)

# print(l)    ---> but this is lengthy code we have to write it in short

# # List Comprehension
# l = [i for i in range(1,21) if i % 2 == 0]
# print(l)


# Dictionary Comprehension
# D = {i : i**2 for i in range(1, 10)}
# print(D)


# Set Comprehension


# Lambda Keyword/ function

# def addition(a, b):
#     print(a+b)

# addition(13, 4)

# lambda function makes this above code to again very short form
# addition = lambda a,b : a + b
# print(addition(2,4))

# addition = lambda a,b : "even" if a % 2 == 0 else "odd"
# print(addition(12,13))


# modules and packages
# we have module maths.py  module is a file which we can use in another file
# import maths

# print(maths.addition(13, 5))



#  we also have inbuilt madules
# multiple modules in folder called package

# from models import hello,maths


# if we have multiple folders then use dots
from models.model import hello, maths
hello()
maths()