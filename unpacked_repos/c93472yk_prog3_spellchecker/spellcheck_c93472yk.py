import sys
from os import walk

def mainP(input1, output1):
    words = []
    qq = []
    #f = open("Words1.txt", "r")
    #for i in f:
        #words.append(i)

    wordDoc = sys.argv[1]

    with open(wordDoc) as f:
        q = f.read().splitlines()
        qq.append(q)
    f.close()

    for i in range(0, len(qq)):
        for j in range(0, len(qq[i])):
            words.append(qq[i][j])
#21
    def lCheck(l):
        if ((ord(l) >= 65 and ord(l) <= 90) or (ord(l) >= 97 and ord(l) <= 122)):
            return 1
        return 0
    def pCheck(l):
        #(ord(s[i]) >= 33 and ord(s[i]) <= 47) or (ord(s[i]) >= 58 and ord(s[i]) <= 64) or (ord(s[i]) >= 91 and ord(s[i]) <= 96) or (ord(s[i]) >= 123 and ord(s[i]) <= 126)
        
        if ((ord(l) >= 33 and ord(l) <= 34) or (ord(l) >= 39 and ord(l) <= 41) or (ord(l) >= 44 and ord(l) <= 46) or (ord(l) >= 58 and ord(l) <= 59) or ord(l) == 63 or ord(l) == 91 or ord(l) == 93 or (ord(l) >= 95 and ord(l) <= 96) or ord(l) == 123 or ord(l) == 125):
            return 1
        return 0

    def check(word):
        #print(word)

        for i in range(0, len(words)):
            if (word == words[i]):
                return 0
        return 1

    def out(uC, pR, nR, nW, nCW, nIW, output1):
        v = 15
        if ((ord(input1[len(input1) - 5]) >= 48 and ord(input1[len(input1) - 5]) <= 57) and (ord(input1[len(input1) - 6]) >= 48 and ord(input1[len(input1) - 6]) <= 57)):
            v = 16
        else:
            v = 15
        if (output1[len(output1) - 1] == "/"):
            k = ""
            for i in range(len(input1) - 1, v, -1):
                k += input1[i]
            for i in range(len(k) - 1, 3, -1):
                output1 += k[i]
            output1 += "_c93472yk.txt"
            #print(output1)
        else:
            k = ""
            for i in range(len(input1) - 1, v, -1):
                k += input1[i]
            for i in range(len(k) - 1, 3, -1):
                output1 += k[i]
            #print(k)
            output1 += "_c93472yk.txt"
        f = open(output1, "w")
        f.write("c93472yk\n")
        f.close()
        f = open(output1, "a")
        f.write("Formatting ###################")
        f.write("\nNumber of upper case letters changed: " + str(uC))
        f.write("\nNumber of punctuations removed: " + str(pR))
        f.write("\nNumber of numbers removed: " + str(nR))
        f.write("\nSpellchecking ###################")
        f.write("\nNumber of words: " + str(nW))
        f.write("\nNumber of correct words: " + str(nCW))
        f.write("\nNumber of incorrect words: " + str(nIW))
        f.close()

    with open(input1) as f:
        q = f.read()
    f.close()

    uC = 0
    pR = 0
    nR = 0
    nW = 0
    nCW = 0
    nIW = 0

    word = ""
    s = ""

    for i in range(0, len(q)):
        ok = 1
        if ((i <= len(q) - 3) and q[i] == "."):
            if (q[i + 1] == "." and q[i + 2] == "."):
                pR += 1
            elif ((q[i - 1] != "." and q[i + 1] != ".") or (q[i - 1] != "." and q[i - 2] != ".")):
                pR += 1
        elif (i >= len(q) - 3 and q[i] == "." and (q[i - 1] != "." and q[i - 2] != ".")):
            pR += 1
            #print(q[i - 2], q[i - 1], q[i], q[i + 1], q[i + 2])
        if (ord(q[i]) >= 65 and ord(q[i]) <= 90):
            uC += 1
        elif (q[i] != "." and pCheck(q[i]) == 1):
            pR += 1
            ok = 0
        elif (ord(q[i]) >= 48 and ord(q[i]) <= 57):
            nR += 1
            ok = 0
        if (lCheck(q[i]) == 1):
            ok = 1
        if (ok == 1):
            s += q[i].lower()
    #print(s)
    for i in range(0, len(s)):
        if (lCheck(s[i]) == 1 and s[i] != " " and (ord(s[i]) < 48 or ord(s[i]) > 57)): 
            word += s[i].lower()
        elif ((pCheck(s[i]) == 1 and (ord(s[i - 1]) < 48 or ord(s[i - 1]) > 57)) or (s[i] == " " and pCheck(s[i - 1]) != 1)):
            if (len(word) != 0 and word != "t"):
                nIW += check(word.lower())
                nW += 1
                #print(nW, " ", word)
                word = ""
            elif (word == "t" and s[i - 2] != "'"):
                nIW += check(word.lower())
                nW += 1
                #print(nW, " ", word)
                word = ""
            elif (word == "t" and s[i - 2] == "'"):
                word = ""


    if (len(word) != 0 and word != "t"):
        nIW += check(word.lower())
        nW += 1


    nCW = nW - nIW

    out(uC, pR, nR, nW, nCW, nIW, output1)

    #print (uC, " ", pR, " ", nR, " ", nW, " ", nCW, " ", nIW)
    #with open("output.txt",'w') as f:
        #f.write()

input1 = sys.argv[2]
output1 = sys.argv[3]

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
    mainP(inP, output1)







