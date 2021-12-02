import sys
from os import walk

def mainP(input1, output1):
    def toLower(s):
        l = ""
        for i in range(0, len(s)):
            if (ord(s[i]) >= 65 and ord(s[i]) <= 90):
                #num = ord(s[i])
                l += chr((ord(s[i]) + 32))
            else:
                l += s[i]
        #print (l)
        return l

    def MC(k):
        letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        mC = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]  
        mD = [".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----", ]
        mP = [".-.-.-", "--..--", "..--..", ".----.", "-.-.--", "-.--.", "-.--.-", "---...", "-.-.-.", "-....-", "..--.-", ".-..-."]
        #norP = [".", ",", "?", "'", "!", "(", ")", ":", ";", "-", "_"]
        aP = [46, 44, 63, 39, 33, 40, 41, 58, 59, 45, 95, 34]

        res = ""
        for i in range(0, len(k)):
            #k[i].rstrip()
            #print(k[i])
            if (k[i] == "/"):
                res += " "
            for j in range(0, len(mC)):
                if (k[i] == mC[j]):
                    res += letter[j]
                    break
            for j in range(0, len(mD)):
                if (k[i] == mD[j]):
                    res += letter[j]
                    break
            for j in range(0, len(mP)):
                if (k[i] == mP[j]):
                    res += chr(int(aP[j]))
                    break

        return res

    def HtoE(h):
        #hexS = ['a', 'b', 'c', 'd', 'e', 'f']
        #hexC = ['A', 'B', 'C', 'D', 'E', 'F']

        n1 = 0
        d = 0
        #print(h)

        if (ord(h[1]) >= 48 and ord(h[1]) <= 57):
            #print (h)
            d = int(h[0]) * 16 + int(h[1]) 
        elif (ord(h[1]) >= 97 and ord(h[1]) <= 102):
            n1 = int(ord(h[1])) - 87
            d = int(h[0]) * 16 + int(n1)
        elif (ord(h[1]) >= 65 and ord(h[1]) <= 70):
            n1 = int(ord(h[1])) - 55
            d = int(h[0]) * 16 + int(n1)

        #print(h, " ", chr(d))
        return chr(d)

    def CC(s):
        res = ""
        p = 0
        k = 0

        while (p < int(len(s))):
            if (s[p] == " "):
                res = str(res) + " "
            elif(s[p] == "\n"):
                k = 1
            elif (ord(s[p]) >= 33 and ord(s[p]) <= 47) or (ord(s[p]) >= 58 and ord(s[p]) <= 64) or (ord(s[p]) >= 91 and ord(s[p]) <= 96) or (ord(s[p]) >= 123 and ord(s[p]) <= 126):
                #print(s[p])
                res = str(res) + str(s[p])
            else:
                if (ord(s[p]) >= 97 and ord(s[p]) <= 99):
                    c = str(s[p])
                    a = ord(c)
                    a += 23
                    #print(s[p], " ", chr(a))
                    res = str(res) + str(chr(a))
                else:
                    c = str(s[p])
                    a = ord(c)
                    a -= 3
                    #print(s[p], " ", chr(a))
                    res = str(res) + str(chr(a))
            p += 1
        #print(k)
        return res

    def out(res, output1):
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
        with open(output1,'w') as f:
            f.write(res)
        f.close()
    with open(input1) as f:
        s = f.read()
    f.close()

    type = 0
    if (s[0] == "H" or s[0] == "h"):
        type = 1
    elif (s[0] == "C" or s[0] == "c"):
        type = 2
    elif (s[0] == "M" or s[0] == "m"):
        type = 3

    res = ""
    l = ""
    ifTrue = 0
    for i in range(0, len(s)):
        if (ifTrue == 1):    
            l += s[i]
        if (s[i] == ":"):
            ifTrue = 1
    #print(l)

    if (type == 1):
        for i in range (0, len(l)):
            subS = ""
            if (l[i] == " "):
                subS += l[i - 2]
                subS += l[i - 1]
                #print("subS: ", subS)
                res += HtoE(subS)
        #print(l)
        subS = ""
        subS += l[len(l) - 2]
        subS += l[len(l) - 1]

        if (subS[0] == " " or subS[1] == " " or len(subS) == 1 or subS[0] == "\n" or subS[1] == "\n"):
            subS = ""
            subS += l[len(l) - 3]
            subS += l[len(l) - 2]
            #print("subS: ", subS, " ", len(subS))

        #print("subS: ", subS, " ", len(subS))
        res += HtoE(subS)
        ans = toLower(res)
        #print(ans)
        out(ans, output1)

    elif (type == 2):
        res = CC(l)
        #print(res)
        #print(l)
        #print(l)
        ans = toLower(res)
        out(ans, output1)

    elif (type == 3):
        k = []
        mL = ""
        for i in range (0, len(l)):
            if (l[i] != " " and l[i] != "\n"):
                mL +=  l[i]
            else:
                k.append(mL)
                #print(mL)
                mL = ""
        #mL2 = mL[:-1]
        k.append(mL)
        #print(mL)
        #print (input1, " ", mL)
        #print(k)
        #print("l: ", l[len(l) - 1])
        #print("l: ", l[len(l) - 2])
        #print("l: ", l[len(l) - 3])
        res = MC(k)
        ans = toLower(res)
        out(ans, output1)

#with open("output.txt",'w') as f:
    #f.write()

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





