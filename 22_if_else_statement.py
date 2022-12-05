"""
if [condition expression]:
    [statement to execute]
else:
    [next for error]
"""

a = eval(input("Enter your Value: "))

if a % 2 == 0:
    print("This is even number", a)

else:
    print("Please enter even number", a)