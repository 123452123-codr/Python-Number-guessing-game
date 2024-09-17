import random
import math

n = 9
print("This game involves guessing a number between 1 and 100. You get hints and have 10 tries. Good Luck!")

while n > 0:
    a = int(input("\nEnter the number:"))
    num = random.randint(1,100)

    if a != num:
        if math.fabs(a-num) <= 10:
            print("That was kinda close! Try again")
            print("You have ",n,"tries left")
            n -= 1
        else:
            print("That was not close. Try again.")
            print("You have ",n,"tries left")
            n -= 1
    else:
        print("Wohoo! You have guessed it right! The number is ",num)
        break
    if n == 0:
        print("You have lost! The number was ",num)
