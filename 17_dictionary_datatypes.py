"""
1. Dictionary is an unordered collection of key-value pairs.
2. in python, dictionaries are defined within braces {} with each item being a pair in the from key:value
3. sign = {a:b}
"""

d1 = {'name': 'kishore',
      'email': 'hello@gmail.com',
      'username': 'kishore'}
d2 = {'name': 'kishore', 'email': 'hello@gmail.com', 'name': 'username'}

print(d1, type(d1))
print(d2, type(d2))
print(d1['name'])

d1['name'] = 'nand'
print(d1, type(d1))
