#result = str(input("Please enter the score of the games: "))
import sys

total1 = 0
total2 = 0

file = open(sys.argv[1],"r")
result = file.read()


for x in range(len(result)):
    if str(result[x]) == "1":
        if result[x + 1] == "t":
            total1 += 5
        elif result[x + 1] == "c":
            total1 += 2
        elif result[x + 1] == "p":
            total1 += 3
        elif result[x + 1] == "d":
            total1 += 3
    elif str(result[x]) == "2":
        if result[x + 1] == "t":
            total2 += 5
        elif result[x + 1] == "c":
            total2 += 2
        elif result[x + 1] == "p":
            total2 += 3
        elif result[x + 1] == "d":
            total2 += 3

print (total1 , " : ", total2)
output = str(total1) + " : " + str(total2)

file.close()
file2 = open(sys.argv[2],"w")
file2.write(str(output))
file2.close()
