"""
A Python module is a file containing Python definitions and statements. A module can define functions, classes,
and variables. A module can also include runnable code. Grouping related code into a module makes the code easier to
understand and use. It also makes the code logically organized.

"""

a = int(input("Enter Your Values: "))
b = int(input("Enter Your Values: "))


def sum(*args):
    c = a + b
    return c


def mul(*args):
    c = a * b
    return c
