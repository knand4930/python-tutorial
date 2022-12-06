"""
List Queue

1. The Queue is a liner data Structure
2. Stores items in first in first out (FIFO) manner.

Queue Operations
1. Enqueue : Adds an item to the Queue.
2. Dequeue : Removes an item from the Queue.
3. Front : Get the front item from queue.
4. Rear Get the last item from queue.

"""


l = []
while True:
    c = int(input(
        '''
        1. Enqueue Elements
        2. Dequeue Elements
        3. Front Elements
        4. Rear Elements
        5. Display Elements 
        6. Exit
        '''
    ))
    if c ==1 :
        n = input("Enter The Value: ")
        l.append(n)
        print(l)

    elif c == 2:
        if len(l) == 0:
            print("Empty Queue ")
        else:
            del l[0]
            print(l)
    elif c == 3:
        if len(l) == 0:
            print("Empty Stack")
        else:
            print("First Queue Value: ", l[0])
    elif c == 4:
        if len(l) == 0:
            print("Empty Queue")
        else:
            print("last Queue Value: ", l[-1])

    elif c == 5:
        print("Display queue", l)

    elif c == 6:
        break
    else:
        print("Invalid Operation...")