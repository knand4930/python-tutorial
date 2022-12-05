"""

1. A set is an unordered collection of items.
2. Every set element is unique (no duplicate) and must be immutable (cannot be changed)
3. sign = {}

"""

s1 = {1,2,3,1,2}
s2 = {1,2,3, 'hello', 'hello'}

print(s1, type(s1))
print(s2, type(s2))

s1[2] = 5
print(s1, type(s1))