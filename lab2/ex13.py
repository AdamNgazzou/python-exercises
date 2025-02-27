#ex13
import random
def play():
    number = randint(1,100)
    print(number)
    while (True):
        x=int(input("guess the number "))
        if(x == number ):
            print('Bravooo')
            break
        elif(x>number):
            print("too high")
        else:
            print("too low")

play()