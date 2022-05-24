import random

computer= random.randint(1, 100)
guess = int(input("enter no:"))
while True:
    if computer==guess:
        print("correct")
        break
    elif guess>computer:
        print("greater")
        guess = int(input("enter no:"))
    elif guess<computer:
        print("low")
        guess = int(input("enter no:"))    
