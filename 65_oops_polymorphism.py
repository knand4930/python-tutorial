"""
1. Polymorphism means same function name(but different Signature) being uses for different types.

Method overloading:
1. Method overloading is one concept of polymorphism
2. It comes under the elements of OOPs
3. It is worked in the same method names and different arguments.
4. Arguments different will be based on a number of arguments and types of arguments



Method overriding
1. Method overriding is the method having the same name with the same arguments.
2. It is Implemented with inheritance also.
3. It mostly used for memory reducing processes.

"""


# overloading
# class Student:
#     def displayInfo(self, name=''):
#         print("Hello python World" + "! " + name)
#


# obj = Student()
# obj.displayInfo()
# obj.displayInfo("This side is nand kishore here")


# Overriding
# class Student:
#     def displayInfo(self, name=''):
#         print("Hello python World" + "! " + name)
# class IIP(Student):
#     def displayInfo(self):
#         super().displayInfo()
#         print("welcome to iip")
#
#
# obj = IIP()
# obj.displayInfo()


# overloading Concept

# class Area:
#     def find_area(self, a=None, b=None):
#         if a != None and b!= None:
#             print("Area of Rectangle: ", (a*b))
#         elif a!=None:
#             print("Area of Square: ", (a*a))
#         else:
#             print("Nothing to find")
#
# obj = Area()
# obj.find_area()
# obj.find_area(10,20)
# obj.find_area(20)


# Method Overriding
class A:
    def ShowData(self):
        print("I'm in A")


class B(A):
    def ShowData(self):
        print("I'm in B")


obj = B()
obj.ShowData()