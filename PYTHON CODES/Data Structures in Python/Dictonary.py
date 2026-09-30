# help(dict)
# Most Used in development and other things
# Its Hashmaps but called dictionary in python
#  Create by using curly braces but should be empty or should have key value pairs

# Dictionary Properties
# 1) Mutable  ---> can change, add, remove anything
# 2) Duplicate ---> Keys must be unique but can have duplicate values
# 3) Order   ---> Follows Insertion Order
# 4) Heterogenous ---> can different types of data 

# d = {1:"hello", 2:56, 3:True}
# print(type(d))
# print(d)
# # Updation of values
# d[1] = 1000
# # Creation of values
# d[20] = 400
# # Access values by using keys
# print(d[1])
# # delete
# del d[20]
# print(d)


# Dictionary Traversing
# d = {10:100, 20:200, 30:300, 40:400}
# for i in d:
#     print(i, end = "  ")  # gives keys
# print()
# for j in d:
#     print(d[j], end = " ")  # gives values 



# Shallow Copy
# Instead of creating original copy and giving it to third variable we make shallow copy so that our main thing will remain unchanged
# Eg) a = [1, 2, 4, 5]   now if i write  b = a      and b[0] = 100 and print(a)  ,, i will see that even if i made changes in b still i got changes in a
# To avoid this things we make shallow copy

# a = [1, 2, 4, 5, 6]
# b = a.copy()     # now b has copy of a

# b[0] = 100
# print(a)
# print(b)


# create one python dictionary which merges two different dictionaries
# d1 = {10:100, 20:200, 30:300}
# d2 = {40:400, 50:500, 60:600}

# for i in d2:
#     d1[i] = d2[i]
# print(d1)


# Sum all values in dictionary
# d1 = {10:100, 20:200, 30:300}

# sum = 0
# for i in d1:
#     sum = sum + d1[i]
# print(sum)


# Count the frequency of elements or values
# a = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8]
# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)


# If found same elements or keys then add their values
d1 = {10:100, 20:200, 30:300}
d2 = {40:400, 20:500, 10:600}

for i in d2:
    if i in d1.keys(): # i matlab key hai so key agar d1 me bhi hai
        d1[i] += d2[i]  # to d1 ka i'th key vala element + karo d2 ke i'th elements ke sath (matching)
    else:
        d1[i] = d2[i]  # otherwise both values ko equal kro 

print(d1)