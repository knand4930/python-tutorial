"""

Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign
values) to the data members of the class when an object of the class is created. In Python the __init__() method is
called the constructor and is always called when an object is created

"""


# class DemoClass:
#     a = 50
#
#     def show(self):
#         # print(a)
#         # print(self.a)
#         self.c = self.a * self.a
#         print(self.c)
#
#     def show1(self, a, b):
#         print(a * b)
#         print("Hello World !!")
#
#
# obj = DemoClass()
# obj.show()
# obj.show1(10, 20)


class Const:
    # default constructor
    def __init__(self):
        self.name = "Hello Python world"

    # a method for printing data members
    def print_Name(self):
        print(self.name)


# creating object of the class
obj = Const()

# calling the instance method using the object obj
obj.print_Name()


class DemoValue:
    # error value
    def __init__(self):
        self.data = {"name": "nand Kishore", "email": "heello@gmail.com", "dob": "1999"}

    def print_data(self):
        print(self.data)


obj1 = DemoValue()
obj1.print_data()
