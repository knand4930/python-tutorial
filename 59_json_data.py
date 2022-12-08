"""
JSON:
1. JSON(javascript Object Notation)
2. It is mainly used for storing and transferring data between the browser and the server
3. JSON is text, written with JavaScript Object Notation
4. Python too supports JSON with a built-in package called json.
5. import json


Python	                JSON
dict	                Object
list	                Array
tuple	                Array
str	                    String
int	                    Number
float	                Number
True	                true
False	                false
None	                null


"""

import json

# d = {
#     'name': 'nand kishore',
#     'email': 'knand4930@gmail',
#     'phone': '12345678990',
#     'occupation': 'software developer'
# }
# f = json.dumps(d)
# print(f, "Types of Data: ", type(f))


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# j = json.dumps(l)
# print(j, type(j))


d = '{"name": "nand kishore", "email": "knand4930@gmail", "phone": "12345678990", "occupation": "software developer"}'
print(type(d))

p = json.loads(d)
print(p, type(p))
for i in p:
    print(i, p[i])