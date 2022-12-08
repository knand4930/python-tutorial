"""

Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.



"""


# class Parent:
#     def displayParent(self):
#         print("Hello python World")
#
#
# class Child(Parent):
#     def displayChild(self):
#         print("Hello Kishore")
#
#
# class GrandChild(Child):
#     def displayGrand(self):
#         print("Grand Child")
#
#


# obj = Parent()
# obj.displayParent()

# childObj= Child()
# childObj.displayParent()
# childObj.displayChild()

# GrandObj = GrandChild()
# GrandObj.displayParent()
# GrandObj.displayChild()
# GrandObj.displayGrand()


class Parent:
    def displayParent(self):
        print("Hello python World")


class Child:
    def displayChild(self):
        print("Hello Kishore")


class GrandChild(Child):
    def displayGrand(self):
        print("Grand Child")


class MultiInheritance(Parent, Child):
    def displayInheritance(self):
        print("Multi label Inheritance")




MultiObj = MultiInheritance()
MultiObj.displayInheritance()
MultiObj.displayChild()
MultiObj.displayParent()
