# the oops is made to eliminate repeatitive tasks like arithmetic operations and more



# def addab(a, b):
#     print(a + b)

# # print(addab(12, 5))
# # print(addab(5, 5))
# print(12 + 13)
# addab(12, 2)


# CLASS 
# It is a blueprint of house --> like how much rooms, bathrooms, kitchen etc
# Object --> an object is an actual house built using that blueprint

# Attributes --->
# Variables defined inside a class are attributes

# Methods ---->
# Functions defined inside a class are methods

# for example :
# class Factory:
#     a = 12     # ---> attributes

#     def hello(self):   # ---> methods
#         print("How are you ?? ")

#     print(f"Hello i am kunal and my age is : {a}")


# # Calling class and printing
# print(Factory().a)    # --> will print value of a = 12

# Factory().hello()    # now this will not run, to make this run we have to include def hello(self)


# # Now we want to access one attribute 
# # so we need to make its object first

# my_obj = Factory()    # --> my_obj its just a name we can change it to whatever we want
# print(my_obj.a)

# # similarly we can easily access now def functions too
# my_obj.hello()


## CONSTRUCTOR 

class Factory:
    # self targets the location
    def __init__(self, material, zips, pockets):     # ---> these are initializers called as dunders and are used to initialize objects data
        self.material = material
        self.zips = zips
        self.pockets = pockets

# # hence we wil wrap this up inside a function and pass by values
    def show(self):
        print(f"Your object details are : {self.material}, {self.zips}, {self.pockets}")

# Rebook is the instance or object now
Reebok = Factory("Leather", 3, 2)   # now we have to pass all arguments we passed in initializers
campus = Factory("Nylon", 3, 1) # this works same like function calling and makes easier to store data without writing repeatedly

# and now just do
Reebok.show()
campus.show()
# print(campus.material)
# print(Reebok.pockets)


# # also we can print these by using constructor call 
# items = Factory(*Reebok)
# print(items.material, items.zips, items.pockets)
# #  but we have to do it for everuy new object or instance




