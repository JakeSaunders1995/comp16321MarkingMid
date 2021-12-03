import argparse
import os

test = []
t = 5
c = 2
p = 3
d = 3
count1 = 0
count2 = 0
count3 = 0

i = 1
z = 0


parser = argparse.ArgumentParser()
parser.add_argument('input', type=str)
parser.add_argument('output', type=str)
args = parser.parse_args()
# print(args.input + args.output)

path = args.input
line = args.output
test = os.listdir(path)

if path[-1] != "/":
    path += "/"
if line[-1] != "/":
    line += "/"

for x in test:
    count1 = 0
    count2 = 0
    count3 = 0
    i=1
    file = open(path + x, "r")
    w = file.read()
    count = len(w)
    count3 = count/3
    for a in w:
        if i <=count3:
            a = w.split('T')[i]
            if (a[0] == "1"):
                if a[1] == "t":
                    count1 = count1 + t
                elif a[1] == "c":
                    count1 = count1 + c
                elif a[1] == "p":
                    count1 = count1 + p
                else:
                    count1 = count1 + d
            else:
                if a[1] == "t":
                    count2 = count2 + t
                elif a[1] == "c":
                    count2 = count2 + c
                elif a[1] == "p":
                    count2 = count2 + p
                else:
                    count2 = count2 + d
            i+=1


    # print(count1)
    # print(count2)
    if count1 > count2:
        print("team 1 wins the game")
    elif count1 < count2:
        print("team 2 wins the game")
    else:
        print("They draw")
    result = str(count1) + ':' + str(count2)
    q = x[0:-4]

    f = open(str(line) + str(q)+"_u18382zh.txt", "w")

    f.write(result)
    f.close()
    file.close()


