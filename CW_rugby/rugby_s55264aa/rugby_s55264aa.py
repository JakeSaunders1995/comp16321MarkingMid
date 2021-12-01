import os, sys

for file in (os.listdir(sys.argv[1])):
    f = open(os.path.join(sys.argv[1],file),"r")
    matchRsults = f.read()
    f.close()

    scoreList = []
    for c in matchRsults:
        scoreList.append(c)

    newList = []
    for i in range(len(scoreList)):
        if scoreList[i]== "1":
            newList.append([1,scoreList[i +1]])
        elif scoreList[i]== "2":
            newList.append([2,scoreList[i +1]])

    def pointChecker(point):
        finalScore = 0
        for i in point:
            if i == "t":
                finalScore += 5
            elif i == "c":
                finalScore += 2
            else:
                finalScore += 3
        return(finalScore)

    T1 = ""
    T2 = ""
    for j in range(len(newList)):
        if newList[j][0] == 1:
            T1 = T1 + newList[j][1]
        elif newList[j][0] == 2:
                T2 = T2 + newList[j][1]

    T1finalScore = pointChecker(T1)
    T2finalScore = pointChecker(T2)

    newFile = open(os.path.join(sys.argv[2],file[0:len(file) - 4] + "_s55264aa.txt"),"w")
    newFile.write(str(T1finalScore) + ":"+ str(T2finalScore))
    newFile.close()