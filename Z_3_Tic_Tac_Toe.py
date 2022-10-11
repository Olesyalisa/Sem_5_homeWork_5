# крестики нолики против компьютера

from random import randint

field = [[0 for y in range(3)] for y in range(3)]

def inside(x, y):
    return (0 <= x) and (x < 3) and (0 <= y) and (y < 3)

def follow(sx, sy, dx, dy, v):
    sx += dx
    sy += dy
    c = 0

    while (inside(sx,sy) and (field[sx][sy] ==  v)):
        sx += dx
        sy += dy
        c += 1

    return c

dirs = [[0,1], [1,0], [1,1], [-1,1]]

def checkWin(mx, my, side):
    if (field[mx][my] != 0):
        return False

    for dir in dirs:
        s = follow(mx, my, dir[0], dir[1], side)
        s += follow(mx, my, -dir[0], -dir[1], side)

        if (s == 2):
            return True

    return False

side = randint(1,2)

while (True):
    print("Field: ")
    print(" ABC")
    for y in range(3):
        s = str(y+1)
        for x in range(3):
            s = s + "_XO"[field[x][y]]
        print(s)

    fc = 0
    for y in range(3):
        for x in range(3):
            if (field[x][y] == 0):
                fc += 1
    if (fc == 0):
        print("DRAW!")
        break

    if (side == 1):
        move = input("Enter your more (к примеру B3): ")
        mx = ord(move[0].lower()) - ord('a')
        my = ord(move[1].lower()) - ord('1')

        if (field[mx][my] != 0):
            print("The cage is occupied")
            continue
    else:
        fc = 0

        for y in range(3):
            for x in range(3):
                if (field[x][y] == 0):
                    fc += 1

                    if (checkWin(x,y,2)):
                        fc = -1
                        mx, my = x, y
                        break

        if (fc > 0):
            fc = randint(0,fc)

            # случайный ход
            for y in range(3):
                for x in range(3):
                    if (field[x][y] == 0):
                        if (fc == 0):
                            mx, my = x, y
                            break
                        fc -= 1

    if (checkWin(mx,my, side)):
        print("WOW! Winner player" + str(side))
        break

    field[mx][my] = side
    side = 3-side

print("The and")