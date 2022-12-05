"""
String formatting

1. format(): the format() method formats the specified values(s) and insert them inside the string's placeholder.
2. The placeholder is defined using curl brackets:{}. Read more about the placeholders in the Placeholder section below.
#named indexe:
values = "welcome to {fname} {lname}".format(fname="Nand", lname="kishore")

#numbered indexes:
values2 = "welcome to {0} {1}".format("Nand", "Kishore")

#empty placeholders:
values3 = "welcome to {} {}".format("Nand", "Kishore")


"""

values = "welcome to {fname} {lname}".format(fname="Nand", lname="kishore")
print(values)

values2 = "welcome to {0} {1}".format("Nand", "Kishore")
print(values2)

values5 = "welcome to {1} {0}".format("Nand", "Kishore")
print(values5)

values3 = "welcome to {} {}".format("Nand", "Kishore")
print(values3)

a = "nand"
b = "kishore"
values4 = f"welcome to {a} {b}"
print(values4)


values6 = f"welcome to {a:^10} {b}"
print(values6)
values7 = f"welcome to {a:<10} {b}"
print(values7)
values8 = f"welcome to {a:>10} {b}"
print(values8)

