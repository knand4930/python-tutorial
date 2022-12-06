"""
Single line code or compressed code
1. List comprehension is an elegant way to define and create lists based on exiting lists.
2. List comprehension is generally more compact and faster than normal functions and loop for create list
3. syntax : [expression for item in list]

"""

# l = []
#
# for a in range(10):
#     if a % 2 == 0:
#         l.append(a)
# print(l)
#
# n = [x for x in range(10) if x % 2 == 0]
# print(n)


s = "hello"

d = [i for i in s]
print(d)