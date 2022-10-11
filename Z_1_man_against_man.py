# игра конфеты человек против человека

from random import randint

side = randint(1,2)
n = 221 #2021

while (n > 0):
    print("Player " + str(side) + ". remains " + str(n))
    while (True):
        t = int( input("enter number of candies: "))
        if (t < 1) or (t > 28):
            print("You can take from 1 to 28 candies")
        else:
            break

    if (n <= t):
        print("Player " + str(side) + " winner! WOW!")
        break

    n -= t
    side = 3-side

print("The and!")

