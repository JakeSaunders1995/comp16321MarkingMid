import sys
import os

inputFolder = sys.argv[1]
outputFolder = sys.argv[2]

def calScore(f):
    scoresFile = f.read()
    justScoreFile = scoresFile.rstrip()
    eachTeamScore = []
    for i in range(0, len(justScoreFile), 3):
        eachTeamScore.append(justScoreFile[i:i + 3])

    t1Score = 0
    t2Score = 0

    for score in eachTeamScore:
        if score[0:2] == "T1":
            if score[2] == "t":
                t1Score += 5
            elif score[2] == "c":
                t1Score += 2
            elif score[2] == "p":
                t1Score += 3
            elif score[2] == "d":
                t1Score += 3
        elif score[0:2] == "T2":
            if score[2] == "t":
                t2Score += 5
            elif score[2] == "c":
                t2Score += 2
            elif score[2] == "p":
                t2Score += 3
            elif score[2] == "d":
                t2Score += 3
    with open(outputFilePath, "w") as o:
        print(str(t1Score) + ":" + str(t2Score), file = o)

for fileName in os.listdir(inputFolder):
    if fileName.endswith(".txt"):
        inputFilePath = os.path.join(inputFolder, fileName)
        outputFilePath = str(outputFolder) + "/" + str(fileName[:10]) + "_q57044nc" + str(fileName[10:])
        with open(inputFilePath, "r") as j:
            inputFileName = j
            calScore(inputFileName)
