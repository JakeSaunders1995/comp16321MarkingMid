import sys
import os 

inputFilePath = sys.argv[1]
outputFilePath = sys.argv[2]

inputFiles = []
for file in os.listdir(inputFilePath):
    if file.endswith(".txt"):
        inputFiles.append(file.split(".")[0])

def addScores(fileName):
    inputFile = open(os.path.join(inputFilePath, fileName + ".txt"))
    rugbyScores = inputFile.read()
    inputFile.close()

    team1 = 0
    team2 = 0

    rugbyScoresArr = rugbyScores.split("T")

    for i in range(len(rugbyScoresArr)):
        chars = list(rugbyScoresArr[i])
        if len(chars) > 0: #Not empty
            points = 0
            if chars[1] == "t":
                points += 5
            elif chars[1] == "c":
                points += 2
            elif chars[1] == "p":
                points += 3
            elif chars[1] == "d":
                points += 3

            if chars[0] == "1":
                team1 += points
            elif chars[0] == "2":
                team2 += points

    outputFile = open(os.path.join(outputFilePath, str(str(fileName) + "_v78643ld.txt")), "w")
    outputFile.write(str(team1) + ":" + str(team2))
    outputFile.close()

for i in inputFiles:
    addScores(i)

