"""
Sets
=> A set is a collection which is unordered and unindexed, that is iterable, mutable and has no duplicate element
=> in python sets are  written with curly bracket.

1. it is unordered
2. it is unindexing
3. it is passed unique elements
4. 'set' object is not subscriptable
5.

Sets Function
1. set(): convert any datatype in set mainly tuple and list
2. add() : add the new elements in set
3. pop(): randomly delete the elements
4. remove(): remove value to passed in remove function #if the item to remove does not exist, remove() will raise and error
5. clear() : clear the element with show the details
6. discard() :  discard the elements in passed the value  #if the item to remove does not exist, remove() will not raise and error
7. update() : update new data in sets
"""

# l =[1,2,3,4,5,6,7]
# s1 = set(l)
# print(s1)
#
s = {2, 3, 4, 5, 6, 7, 7, 3, 4, 5, 6}
ln = len(s)
# print(s)
#
# s.add(10)
# print(s)
#
# print(s.pop())
# print(s)
#
# s.remove(4)
# print(s)
#
# s.discard(6)
# print(s)

# s.clear()
# print(s)

# s.update({40,60,70})
# print(s)
#
# for i in s:
#     print(s[i])
