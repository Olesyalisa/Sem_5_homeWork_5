# игра конфеты человек против бота(компьютера)

from random import randint

side = randint(0,1)+1
n = 221 #2021

while (n > 0):
    print("Player " + str(side) + ". remains " + str(n))

    if (side == 1):
        while (True):
            t = int(input("enter number of candies: "))
            if (t < 1) or (t > 28):
                print("You can take from 1 to 28 candies")
            else:
                break
    else: #ход бота
        if (n<=28):
            t = n
        elif (n<=28*2):
            t = n-29
        else:
            t = randint(1,28)

    if (n<=t):
        print("Player " + str(side) + " winner! WOW!")
        break

    n -= t
    side = 3-side

print("The and!")
