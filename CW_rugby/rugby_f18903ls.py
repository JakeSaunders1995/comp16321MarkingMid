import sys
import os

def getArguments():
    arguments = sys.argv
    source = arguments[1]
    destination = arguments[2]
    return source, destination

def readSource(fileName):
    file = open(fileName)
    scores = file.read()
    file.close()
    return scores

def scoreSpilt(scores):
    scoreList = []
    scoreCount = int(len(scores)/3)
    count = -3
    for i in range(scoreCount):
        count += 3
        scoreList.append(scores[count: count + 3])
    return scoreList

def scoreCalculator(list):
    t1, t2 = 0, 0
    for match in list:
        if (match[0:2] == "T1"):
            #team 1 win
            if (match[2] == "t"):
                t1 += 5
            elif (match[2] == "c"):
                t1 += 2
            elif (match[2] == "p"):
                t1 += 3
            elif (match[2] == "d"):
                t1 += 3
        elif (match[0:2] == "T2"):
            #team 2 win
            if (match[2] == "t"):
                t2 += 5
            elif (match[2] == "c"):
                t2 += 2
            elif (match[2] == "p"):
                t2 += 3
            elif (match[2] == "d"):
                t2 += 3
    return t1, t2

def writeResult(inputFile, inPath, outPath, result):
    outputName = inputFile.replace(".txt", "_f18903ls.txt")
    os.chdir(outPath)
    file = open(outputName , "w")
    file.write(result)
    file.close()
    os.chdir(inPath)

#main
source, destination = getArguments()

#calculate number of files in dir and adds to fileList and creates relative paths
fileList = []
pathOfCurrentFile = os.path.dirname(os.path.abspath("rugby_f18903ls.py"))
sourcePath = os.path.join(pathOfCurrentFile, source)
destinationPath = os.path.join(pathOfCurrentFile, destination)
for file in os.listdir(os.path.join(sourcePath)):
    fileList.append(file)

os.chdir(sourcePath)
for file in fileList:
    scores = readSource(file)
    scoreList = scoreSpilt(scores)
    t1Score, t2Score = scoreCalculator(scoreList)
    result = str(t1Score) + ":" + str(t2Score)
    writeResult(file, sourcePath, destinationPath, result)
