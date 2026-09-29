# There are 4 types of data structures
# 1) List       2) Tuple        3) Dictionary       4) Set

# custom data structure ---> Stack, Queues, Trees, Heap   || but we have to use these by using libraries


# 1] List
# -> Mutable
# -> Duplicates
# -> Ordered (Asc, Desc)
# -> Heterogenius (multiple data types can be stored in single list)

# Creation of list
# a = [12, 13, 14, 15, 16, 18.5, True, print()]
# # print(a[1])  # indexing access starts by 0
# # print(a[0:5]) # slicing based on 1 indexing
# # print(a[-1])  # prints from last indexes since last is print and it has not anything hence op is -> none
# # print(a[-2]) # True
# # print(a[-3]) # 18.5

# #  1st way using index
# for i in range(len(a)):  # whatever the length is the limit of running this loop (stop condition)
#     print(a[i])

# # 2nd directly by using elements
# for i in a:
#     print(i)


# help(list)      #to know about list things

newList = [1,2,3, 4,5]
newList.append(6) 
newList.append(7)

newList.insert(1, 2)   # 1st index pe 2 insert kardo
newList.insert(7, "Kunal") # 7th index pe Kunal insert krdo

newList.remove(5)


print(newList)

