import random

a = random.randrange(1,106)
userInput = int(input("Enter Your Number: "))

if a >= userInput:
    print("your Number is Less Than Of computer number: ")
    print("Computer Number is: ", a)
elif a <= userInput:
    print("Your NUmber is Greater than of computer number: ")
    print("Computer Number is: ", a)

else:
    print("You have guess the right number: ")
    print("Computer Number is: ", a)
