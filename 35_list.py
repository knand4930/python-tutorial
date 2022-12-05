"""
1. list are mutable
2. list common separated with square brackets
3. nested list are list to use under the list
4. create tuple, set, dictionary and list in the single list

"""

l1 = [1, 2, 3, 4, 5]
print(l1[2])

l2 = [1, 2, 3, 4, [2, 3, 4, 5]]  # nested list
print(l2[4][2])

l3 = [1, 2, 3, 4, 'name', 'email', [1, 2, 3, 4]]
l4 = [1, 2, 3, 4, 'name', 'email', [1, 2, 3, 4, 5, 6], (1, 2, 3, 4, 5)]


print(type(l1))
print(type(l2))
print(type(l3))
print(type(l4))

result = l1+l2
print(result)
