import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]
teamOne = 0
teamTwo = 0
file = open(inputFile, "r")

for line in file:
    scoreString = line

file.close()

for i in range(len(scoreString)):
    if scoreString[i] == "T":
        teamNumber = scoreString[i+1]
        goalType = scoreString[i+2]
        if goalType == "t":
            if teamNumber == "1":
                teamOne = teamOne + 5
            else:
                teamTwo = teamTwo + 5
        if goalType == "c":
            if teamNumber == "1":
                teamOne = teamOne + 2
            else:
                teamTwo = teamTwo + 2
        if goalType == "p":
            if teamNumber == "1":
                teamOne = teamOne + 2
            else:
                teamTwo = teamTwo + 2
        if goalType == "d":
            if teamNumber == "1":
                teamOne = teamOne + 1
            else:
                teamTwo = teamTwo + 1

file = open(outputFile, "w")
file.write(str(teamOne) + ":" + str(teamTwo))
file.close()
