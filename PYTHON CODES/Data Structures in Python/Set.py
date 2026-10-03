# Set is one of the most used data type
#  It can be made by using curly braces { }


# Set Properties
# 1) Mutable --> can make changes even after creating
# 2) Non- Duplicates --> can't have duplicate values
# 3) Unordered --> are unordered and cannot access through the indexes
# 4) Semi-Heterogenous --> can store some datatypes but not all 

# s = {1 , 2, 1, 5, 3, 2, 1}
# print(s)

# while it does not have any ordered or indexes so we cant use for loop for len(a)
# for i in range(len(s)):
#     print(s[i])           --> this will give error coz its printing by using indexes while i can do this instead

# for i in s:
#     print(i)

# s.remove(2) # removes only 2 from set
# print(s)

# s.clear()  # removes everything from set 
# print(s)


# Important Set Functions for two or more sets
# 1) union of sets      2) Intersection         3) Difference       4) Symmetric difference         5) Venn Diagram

# 1) Unions of sets
# ---> a = {1, 2, 3}   b = {4, 5, 6}  ===> c = {1, 2, 3, 4, 5}
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}   --> set automatically cancels duplicate elements bydefault

# c = a.union(b)
# print(c)

# 2) Intersection of sets     
# a = {1, 2, 3, 4, 5}        # ===> c = {4, 5}   common elements from both sets
# b = {4, 5, 6, 7, 8}  

# c = a.intersection(b)
# print(c)
# Shortcut print(a&b)
# print(a&b)


# 3) Difference (oneWay)
# a = {1, 2, 3, 4, 5}        # ===> c = {1, 2, 3}  prints those which are not common in b only 
# b = {4, 5, 6}              # ===> if want both common like 1, 2, 3, 6 then use symmetric difference

# c = a.difference(b)
# print(c)



# 4) Symmetric Difference
# a = {1, 2, 3, 4, 5}        # ===> c = {1, 2, 3, 6}  prints those which are not common in a and b both
# b = {4, 5, 6}    

# c = a.symmetric_difference(b)
# # shortcut print(a ^ b)
# print(a ^ b)
# print(c)