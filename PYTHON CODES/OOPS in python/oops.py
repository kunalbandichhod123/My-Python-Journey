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

# Self ---> We write self only when we want to track any object or instance or function to get access of their elements or data or attributes

# Cls ----> locate class location instead of self we use cls when we work on decorators or classs methods


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

# class Factory:
#     # self targets the location
#     def __init__(self, material, zips, pockets):     # ---> these are initializers called as dunders and are used to initialize objects data
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

# # # hence we wil wrap this up inside a function and pass by values
#     def show(self):
#         print(f"Your object details are : {self.material}, {self.zips}, {self.pockets}")

# # Rebook is the instance or object now
# Reebok = Factory("Leather", 3, 2)   # now we have to pass all arguments we passed in initializers
# campus = Factory("Nylon", 3, 1) # this works same like function calling and makes easier to store data without writing repeatedly

# # and now just do
# Reebok.show()
# campus.show()
# print(campus.material)
# print(Reebok.pockets)


# # also we can print these by using constructor call 
# items = Factory(*Reebok)
# print(items.material, items.zips, items.pockets)
# #  but we have to do it for everuy new object or instance



## ANOTHER EXAMPLE

# class Animal:
#     name = "Lion"   # Class Attribute

#     def __init__(self, age):  # Instance methods
#         self.age = age   ## instance or object attribute

#     def show(self):
#         print(f"How are you, your age is {self.age}")

#     @classmethod
#     def hello(cls):                #-----> class methods 
#         print("How are you brother")

#     @staticmethod
#     def static():                  #-----> Static method
#         print("How are you ?? ")


# # now calling objects
# obj = Animal(12)    # created object and passed age 12
# obj.show()
# obj.hello()             # ----> so objects can call any method whether it is normal or static or class
# obj.static()


# Types of methods : 
# 1) Instance Methods  ---> the moment we write (self) inside any function it considered as instance upto now everything is instance only

# 2) Class Methods    ---> needs decorator to use cls instead of self and use @classmethod
# Example :  @classmethod

# 3) Static method ---> used as static method 
# example : @staticmethod
#           def static():
#               print("How are you?")


## INHERITANCE

# It has two things or classes 
# 1) Child class                2) Parent class

# class FactoryAmravati:   # parent or superclass
#     a = "Hi i am Attribute mentioned inside class Factory (class Attribute)"

#     def hello(self):
#         print("hello I am method mentioned inside Factory")

#     # we we used variables inside self function it will become instance variables

# class Factorypune(FactoryAmravati):   # here we are calling parent class inside child class    child or subclass
#     # now this has the power to access anything from inside the parent class
#     pass

# obj = FactoryAmravati()    # ----> this makes it accessible from parent class
# print(obj.a)    # ---> getting value of a from parent class

# obj2 = Factorypune()    # now even though we tell that its pune but inside pune we wrote amravati hence it still access from parent class
# print(obj2.hello())


## CONSTRUCTOR in Inheritance

# class Animal:
#     def __init__(self, name):    ## Constructor Function 
#         self.name = name     

#     def show(self):
#         print(f"Hello your name is : {self.name}, {self.age}")


# # class Human(Animal):
# #     pass

# # person1 = Human("Neha") # Instance of child class ----->    now you see even if we call human which have no name attribute still we have to write name coz we are calling animal to it which has name
# # person1.show()
# # # OR
# # print(person1.show())


# # person2 = Animal("Modih")
# # person2.show()   # Instance of parent class  


# # Now lets learn super keyword
# class Human(Animal):
#     def __init__(self, name, age):    # this time we additionally gave age to it
#         super().__init__(name)                      # Targets the parent class or super class (Animal)
#         self.age = age

#     def show(self):
#         print(f"Your name is : {self.name}, {self.age}")    # but we already have show in parent class hence this is called method overriding


# Animal1 = Animal("Neha")
# Person1 = Human("Kunal", 23)    # as we mentioned age in human class 
# # Person1.show() # but this will not print age as we only print name in parent class hence we have to print {age} in child class too by using show functionality
# Animal1.show()




# Types of INHERITANCE

# 1) Single Level Inheritance  ----> everything we did above is about single level inheritance


# 2) Multiple Inheritance ----> 

# class Animal:
#     name1 = "Lion"

# class Human:
#     name2 = "Kunal"

# class Robots(Animal, Human):     # ----> this is called multiple inheritance
#     name3 = "Dall-E"

# obj = Robots()
# print(obj.name3)    # ---> targets first which is written (animal)

# now lets try different thing by asking age name combination


# class Animal:
#     def __init__(self, name):
#         pass

# class Human:
#     def __init__(self, name, age):
#         pass

# class Robots(Animal, Human):     # ----> this is called multiple inheritance
#     name3 = "Dall-E"

# obj = Robots()    # ---> targeting animal as we wrote it first




# 3) Multilevel Inheritance

class Factory:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips

class BhopalFactory(Factory):
    def __init__(self, material, zips, color):
        super().__init__(material, zips)
        self.color = color

class PuneFfactory(BhopalFactory):
    def __init__(self, material, zips, color, pockets):    # ---> this is called multilevel inheritance
        super().__init__(material, zips, color)
        self.pockets = pockets



# Hierarchial Inheritance
# same as  multilevel inheritance

## POLYMORPHISM 
# same functions having different things to do in different classes or functions
# For example show function in earlier codes where in one show we was showing age and  in one show we was printing name

# Example )
# def show():
#     print("Ye kya hai bhai")

# def show():
#     print("ab dusra chaleg kyuki python overwrite karta hai functions ko")

# show()
# but i want is like the second one should not overwrite the first one hence here comes oops cconcepts of polym



# METHOD OVERRIDING

# class Animal:
#     def show(self):
#         print("Hello i am kunal")

# class Human(Animal):
#     def show(self):
#         print("Made to override")
# # now if we have inheritance of child and parent and same functions in both classes then we can perform overriding of methods
# obj = Human()
# obj.show()


# METHOD OVERLOADING
# method overloading does not exists in python 


# ḌUCK TYPING

# class Animal:
#     def show(self):
#         print("I am kunal")

# class Human:
#     def show(self):
#         print("I am neha")


# obj1 = Animal()
# obj2 = Human()

# obj1.show()       # ---> gives from Animal
# obj2.show()       # ---> gives from Human




# ENCAPSULATION 

# This is built for privacy of codes
#Example ) we have this code which we can access or change the info or code

# class Factory:
#     a = "pune"

#     def show(self):
#         print("hello i am a pune factory")

# obj = Factory()
# obj.show()   #--> here we can access the methods  or
# print(obj.a)  # ---> access variables/ attributes
# obj.a = "Akola"
# print(obj.a)    # ----> here we can change in code too or change in variable data

# hence to avoid this and keep security


# Access modifiers ---> means we can control like how we give access to our attributes and methods
# Types of Access modifiers

# 1) Public Attribute ---> means their attributes can be accessed by anyone from any code

# 2) protected Attribute ---> just use _ before writing variables
# but still we can access them outside the class
# Example:
# class Factory:
#     _a = "pune"

#     def _show(self):
#         print("Hello i am kunal")

# class Bhopal(Factory):
#     def show2(self):
#         print(super()._a)

# obj = Bhopal()
# obj.show2()    # ---> still we can access so whats the point hence it not usefull in python


# 3) Private Attributes
# Cant be access outside the class   &  use __ instead of _ 
# Example:
# class Factory:
#     __a = "pune"

#     def __show(self):
#         print("Hello i am kunal")

# class Bhopal(Factory):
#     def show2(self):
#         print(super().__a)

# obj = Factory()
# print(obj.__a)
# print(obj.__show())
# obj.show2()    # ---> now this will not run throws error coz we cannot access outside class its secure now

#  but if we have this : 
# class Factory:
#     __a = "pune"

#     def show(self):
#         print(Factory.__a)

# obj = Factory()
# obj.show()    # ---> now this can be accessed 



## ABSTRACTION  4th pillar of oops

# It has defined rules like a franchise ---> same taste, same banner, same chairs, etc

# class Square:
#     def __init__(self, side):
#         self.side = side

# class Cirle:
#     def __init__(self, radius):
#         self.radius = radius

# Currently it has no rules like perimeter etc so if we want to apply those we have to use abstraction 
# to use abstraction wew need to import one library   from abc import ABC, abstractmethod
# from abc import ABC, abstractmethod
# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass

#     def area(self):
#         pass


# class Square(abstract):
#     def __init__(self, side):
#         self.side = side

# class Cirle(abstract):
#     def __init__(self, radius):
#         self.radius = radius

#     def perimeter(self):
#         print("I have created")

#     def area(self):
#         print("This too")

# obj = Cirle(15)
# # now take abstract inside classes square and circle and see what it runs
# # now it gives error coz perimeter and area are now strict rules
# # hence now create two methods(functions) for are and perimeter and check again now it willnow give any error

# obj2 = Square(4)   #now this will give error coz we havent followed rules in this




## Dunder methods
# Starts and ends with __   eg) __init__, __str__
 
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Hello my name is {self.name}"

#     # def __add__(self, other):
#     #     return f"Your sum of ages are : {self.age + other.age}"

#     def __add__(self, other):
#         sum = 0
#         for i in other:
#             sum = sum + i.age

#         return f"Your sum of ages are {self.age + sum}"   

# obj = Animal("Lion", 22)
# obj2 = Animal("Dolphin", 22)
# obj3 = Animal("Dog", 14)

# # now can we add age by print(obj1 + obj2) no hence we can create one more dunder method which is up here
# print(obj + obj2)
# print(obj + (obj2, obj3))  ## like send them in tuple

# now if we want to add 3rd age we cant write like other, other2 etc instead we have to code more
#     def __add__(self, other):
#         sum = 0
#         for i in other:
#             sum = sum + i.age

#         return f"Your sum of ages are {self.age + sum}"   

# print(obj + (obj2, obj3))  ## like send them in tuple


