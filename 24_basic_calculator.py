"""
1. basic calculator to more understanding of previous topics

"""

a = eval(input("Enter your Value: "))
b = eval(input("Enter your Value: "))

opr = input("Enter the Operator : ")

if opr == "+":
    print("Your Value", a + b)

elif opr == "-":
    print("Your Value", a - b)

elif opr == "*":
    print("Your Value", a * b)
elif opr == "/":
    print("Your Value", a / b)
else:
    print('Please input correct operator ', opr)
