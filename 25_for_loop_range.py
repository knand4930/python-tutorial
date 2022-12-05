"""
Range(predefine) function

1. default run to start with 0 and increment 1 if use single value
2. if use double parameter to start with first value and end second value with increment 1
3. if use triple parameter to start with first value and second value and last one is increment value

"""

for i in range(100):
    print("Single parameter ", i)

for j in range(10, 50):
    print("Double parameter ", j)

for k in range(10, 100, 3):
    print("Triple parameter ", k)
