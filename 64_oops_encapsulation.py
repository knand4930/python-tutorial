"""
Python Encapsulation

1. An objects variable should not always be directly accessible
2. The methods can ensure the correct values are set. If an incorrect value is set , the method can return an error



Getter and Setter

To implement proper encapsulation in Python, we need to use setters and getters. The primary purpose of using getters
and setters in object-oriented programs is to ensure data encapsulation. Use the getter method to access data members
and the setter methods to modify the data members.

"""


# class Student:
#     __name = "kishore"
#
# obj=Student()
# print(obj.__name)
# AttributeError: 'Student' object has no attribute '__name'


# class Student:
#     __name = "Kishore"
#     def __init__(self):
#         print(self.__name)
# obj = Student()
# # print(obj.__name)
#
#


class Student:
    __name = "kishore"
    def __init__(self):
        print(self.__name)
        self.__displayInfo()
    def __displayInfo(self):
        print("Hello Python World")
obj = Student()




#
# class Student:
#     def __init__(self):
#         self.name = ""
#
#     def getName(self):
#         return self.__name
#
#     def setName(self, name):
#         self.__name = name
#
#
# obj = Student()
# obj.setName("Nand Kishore")
# name = obj.getName()
# print(name)
