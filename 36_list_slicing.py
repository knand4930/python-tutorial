"""
Slicing of list
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15]
print(l1[1:3])  # second value to 3rd value

print(l1[-1::-1])  # reverse

print(l1[1:])  # second value to last
print(l1[::-1])  # last to first
print(l1[1::2])  # starting to end but 2-2 range
print(l1[1:9:2])  # starting to 10 value but 2-2 range

l2 = [1, 2, 3, 4, "hello world"]
print(l2[4][2:6])  # nested slicing to list in string value slice
