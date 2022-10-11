# алгоритм rle

stroka = input("Enter stroku: ")
strstr = ""
i = 0
while (i < len(stroka)):
    second = i+1

    while (second < len(stroka)) and (stroka[i] == stroka[second]):
        second += 1

    strstr = strstr + str(second-i) + stroka[i]
    i = second

print(stroka + " => " + strstr)