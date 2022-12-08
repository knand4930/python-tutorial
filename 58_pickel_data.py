"""
You Can pickle objects with the following data types:
1. Boolean
2. Integers
3. Floats
4. complex Number
5. (normal and unicode) string
6. Tuples
7. Lists
8. sets
9. dictionaries

Usage:
1. To use pickle, start by importing it in python
2. pickle has two main methods. The first one is dump, which dumps
an object to a file object and the second one is load, which load s an object from a file object

Pickle Function
1. dump() :- This function is called to serialize an object hierarchy
2. load() :- This function is called to de-serialize a data stream.

pickle dump: Pickle data is done via the dump() function. It accepts data and a file object. The dump() function then
serializes the data and writes it to the file. The Syntax of dump() is as follow:

syntax :
dump(obj, file)

obj :- object to be pickle
file :- File object where pickle data will be written

pickle load: the load() function takes a file object, reconstruct the objects from the pickled representation, and returns it.

syntax:
import pickle
f = open("data.txt", "rb")
pickle.load(f)

"""

import pickle
#
# examples = {1: "name", 2: "Email", 3: "dob", 4: "occupation"}
#


# file = open("data.txt", "wb")
# pickle.dump(examples, file)
# file.close()



# f = open('data.txt', "rb")
# l = pickle.load(f)
# print(l)