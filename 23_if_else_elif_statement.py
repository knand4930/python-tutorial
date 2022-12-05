"""

if [condition expression]:
    [statement to execute]
elif [condition expression]:
    [statement to execute]
else:
    [statement to execute]


"""


a = eval(input("Enter Your Value: "))

if a % 2 == 0:
    print("This is even number ", a)

elif a %2 ==1:
    print("This is odd number ", a)
else:
    print("please input correct value", a)
