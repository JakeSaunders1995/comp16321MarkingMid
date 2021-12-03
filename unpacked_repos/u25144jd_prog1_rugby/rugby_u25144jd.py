import sys
import os

def rugbyScore(scoreSheet):

    T1 = {"t":0, "c":0, "p":0, "d":0}
    T2 = {"t":0, "c":0, "p":0, "d":0}

    posInList = -1

    for i in scoreSheet:
        posInList = posInList + 1
        if i == "1":
            if scoreSheet[posInList + 1] == "t":
                T1["t"] = T1["t"] + 1
            elif scoreSheet[posInList + 1] == "c":
                T1["c"] = T1["c"] + 1
            elif scoreSheet[posInList + 1] == "p":
                T1["p"] = T1["p"] + 1
            elif scoreSheet[posInList + 1] == "d":
                T1["d"] = T1["d"] + 1

        elif i == "2":
            if scoreSheet[posInList + 1] == "t":
                T2["t"] = T2["t"] + 1
            elif scoreSheet[posInList + 1] == "c":
                T2["c"] = T2["c"] + 1
            elif scoreSheet[posInList + 1] == "p":
                T2["p"] = T2["p"] + 1
            elif scoreSheet[posInList + 1] == "d":
                T2["d"] = T2["d"] + 1

    scoreT1 = T1["t"]*5 + T1["c"]*2 + T1["p"]*3 + T1["d"]*3
    scoreT2 = T2["t"]*5 + T2["c"]*2 + T2["p"]*3 + T2["d"]*3

    return str(scoreT1) + ":" + str(scoreT2)

inputFiles = os.listdir(sys.argv[1])
print(inputFiles)
for inputFile in inputFiles:
    print(inputFile)
    outputFile = open(sys.argv[2] + inputFile[:-4] + "_u25144jd.txt", "x")
    outputFile.write(rugbyScore(open(sys.argv[1] + inputFile, "r").read()))
