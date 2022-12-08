"""
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

To create a class, use the keyword class



The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

Note: The __init__() function is called automatically every time the class is being used to create a new object.



The __str__() Function
The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned:



Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.


Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:


Delete Object Properties
You can delete properties on objects by using the del keyword:


The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.



"""


# #class
# class Demo:
#     a = 10
# print(type(Demo()), Demo())
#
#
# #class with objects
# class DemoClass:
#     a = 10
# demoobject = DemoClass()
# print(demoobject.a)


# class with method
class Data:
    a = 10
    def sum(self):
        print(20 + 30)
object1 = Data()
print(object1.a)
object2 = Data()
object2.sum()
