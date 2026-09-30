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

# newList = [1,2,3, 4,5]
# newList.append(6) 
# newList.append(7)

# newList.insert(1, 2)   # 1st index pe 2 insert kardo
# newList.insert(7, "Kunal") # 7th index pe Kunal insert krdo

# newList.remove(5)  # remove first occurance of 5


# print(newList)




## List questions practice
# Find the negatives and positives from list

# l = [-45, 67, 12, -68, -60, 45]
# print("Positive elements are : ")
# for i in l:
#     if i >= 0:
#         print(i, end = " ")

# print()
# print("Negative elements are : ")
# for j in l:
#     if j < 0:
#         print(j, end = " ")



## Find the mean of the list
# l = [12, 342, 46, 75, 26, 87, 48]

# sum = 0
# for i in l:
#     sum += i
# print(sum/len(l))


# Find the greatest element in the list

# l = [14, 46, 7, 87, 39, 903, 250, 3553]
# largest = 0
# index = 0
# for i in range(len(l)):
#     if largest < l[i]:
#         largest = l[i]
#         index = i

# print(f"Largest element is {largest} at index : {index}")





# find the second largest number and also return its index

# l = [23, 54, 103, 15, 85, 94, 96]

# largest = -1
# second_Largest = -1
# largest_index = -1
# second_Largest_index = -1

# for i in range(len(l)):
#     if l[i] > largest:
#         # now the second largest is past largest
#         # and past largest's index is now second largest's index  
#         second_Largest = largest
#         second_Largest_index = largest_index
#         # update new largest
#         largest = l[i]
#         largest_index = i
        

#     elif l[i] > second_Largest and l[i] != largest:
#         second_Largest = l[i]
#         second_Largest_index = i

# print(f"The second largest element is {second_Largest} at index {second_Largest_index}")



## Check the list is sorted or not
a = [10, 20, 18, 40, 50]

for i in range(len(a)-1):
    if a[i] < a[i + 1]:
        continue
    else:
        print("Your list is not sorted!!!")
        break
else:
    print("List is sorted")