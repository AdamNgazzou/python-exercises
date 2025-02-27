#ex13
import random

def play():
    number = random.randint(1, 100) 
    print(number)  
    while True:
        x = int(input("Guess the number: "))
        if x == number:
            print("Bravooo")
            break
        elif x > number:
            print("Too high")
        else:
            print("Too low")

play()
