import sys
from os import walk

def mainP(input1, output1):
    with open(input1) as f:
        score = f.read()
    #print(score)
    f.close()
    #print(output1)
    #print(input1)


    sType = []
    team = []
    t1 = 0
    t2 = 0

    def points(k):
        if (k == "t"):
            return 5
        if (k == "c"):
            return 2
        if (k == "p"):
            return 3
        if (k == "d"):
            return 3

    for i in range(0, len(score)):
        if (score[i] == "t" or score[i] == "c" or score[i] == "p" or score[i] == "d"):
            sType.append(score[i])
        elif (score[i] == "1" or score[i] == "2"):
            team.append(score[i])

    for i in range(0, len(sType)):
        p = points(sType[i])
        if (team[i] == "1"):
            t1 += p
        else:
            t2 += p

    v = 15
    if ((ord(input1[len(input1) - 5]) >= 48 and ord(input1[len(input1) - 5]) <= 57) and (ord(input1[len(input1) - 6]) >= 48 and ord(input1[len(input1) - 6]) <= 57)):
        v = 16
    else:
        v = 15

    if (output1[len(output1) - 1] == "/"):
        k = ""
        for i in range(len(input1) - 1, len(input1) - v, -1):
            k += input1[i]
        for i in range(len(k) - 1, 3, -1):
            output1 += k[i]
        output1 += "_c93472yk.txt"
        #print(output1)
    else:
        k = ""
        output1 += "/"
        for i in range(len(input1) - 1, len(input1) - v, -1):
            k += input1[i]
        for i in range(len(k) - 1, 3, -1):
            output1 += k[i]
        #print(k)
        output1 += "_c93472yk.txt"
        #print(output1)
      
    #print(str(t1) + ":" + str(t2))  
    #print(output1)
    with open(output1,'w') as f:
        f.write(str(t1) + ":" + str(t2))

input1 = sys.argv[1]
output1 = sys.argv[2]

fileNum1 = []
fileNum = []

for dirpath, dirnames, filenames in walk(input1):
    fileNum1.append(filenames) 
for i in range(0, len(fileNum1[0])):
    fileNum.append(fileNum1[0][i])
#for i in range(0, len(fileNum)):
    #print(fileNum[i])
#print(fileNum)
#print(len(fileNum))
#print(input1)

for i in range (0, len(fileNum)):
    if (input1[len(input1) - 1] == "/"):
        inP = ""
        inP += input1
        inP += fileNum[i]
        #print("asd")
    elif (input1[len(input1) - 1] != "/"):
        inP = ""
        inP += input1
        inP += "/"
        inP += fileNum[i]
 #   print(inP)
    #print(fileNum[i])
    mainP(inP, output1)




