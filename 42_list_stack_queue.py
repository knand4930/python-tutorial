"""
Stack:
1. the Stack is a linear data structure
2. stores items in a last-in/first-out (LIFO) or first-In/Last-out(FILO) manner

Stack Operations
1. Push :-Inserting an Elements
2. pop :- Deletion an element(last element)
3. peek :- Display the last element
4. display :- Display List

"""

l = []

while True:
    c = int(input('''
            1. Push Elements
            2. Pop Elements
            3. Peek Elements
            4. Display Stack
            5. Exit
            '''))
    if c == 1:
        n = input("Enter Your Value: ")
        l.append(n)
        print(l)
    elif c == 2:
        if len(l) == 0:
            print("Empty Stack")
        else:
            p = l.pop(n)
            print(p)
            print(l)

    elif c == 3:
        if len(l) == 0:
            print("Empty Stack")
        else:
            print("last Stack Values: ", l[-1])

    elif c == 4:
        print("Display Stack", l)

    elif c == 5:
        break
    else:
        print("Invalided Operation ")
