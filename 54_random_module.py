"""
Python Random randint() Method
Return a number between 5 and 10 (both include)


Python random choice() Method
return a random choice element from a list

random() : Returns a random float number between 0 and 1
shuffle : Takes a sequence and return the sequence in a random order
uniform : Returns a random float number between two given parameters
"""
import random

n = random.randint(9, 999)
print(n)

n2 = random.randrange(3, 4)
print(n2)

l = [2, 3, 4, 53, 'banana', 'apple', 'grapeas']
c = random.choice(l)
print(c)

r = random.random()
print(r)

l1 = [2, 3, 4, 53]
s = random.shuffle(l1)
print(s)

u = random.uniform(3,6)
print(u)