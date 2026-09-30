# Does not used that much in development things (Least Used)
#  these can be created by using round braces ( )

# Tuple Properties
# 1) Immutable  --> once declared then you cannot change its values    
# 2) Duplicates --> can have duplicate values
# 3) Ordered    --> all values or elements are in ordered manner of indexes
# 4) Heterogenous --> can have mixed data types values

a = (1, 3, 4, 7, 8, 3, 9, "hello", True, print())

# for i in a:
#     print(i)

# for j in range(len(a)):
#     print(a[j])


# index accessing in tuples
# index = a.index(4)
# print(f"index --> {index}")

# Count the occurances of elements
# count = a.count(3)
# print(count)


# Tuple Unpacking ----> Lets say we have a = (1, 2, 3, 4) and we want a = 1, b = 2, c = 3, d = 4
# Its called Tuple Unpacking 
a,b,c,d = (1, 2, 3, 4)
print(a)
print(b)
print(c)
print(d)