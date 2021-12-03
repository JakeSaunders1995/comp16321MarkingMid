import sys

inputFilePath = sys.argv[1]
outputFilePath = sys.argv[2]
teamOneScore = 0
teamTwoScore = 0

with open(inputFilePath, 'r') as f:
    inputFileData = f.readline()

for i in range(2, len(inputFileData), 3):
    if inputFileData[i-1] == "1":
        if inputFileData[i] == "t":
            teamOneScore += 5
        elif inputFileData[i] == "c":
            teamOneScore += 2
        else:
            teamOneScore += 3
    else:
        if inputFileData[i] == "t":
            teamTwoScore += 5
        elif inputFileData[i] == "c":
            teamTwoScore += 2
        else:
            teamTwoScore += 3

outputString = str(teamOneScore) + ":" + str(teamTwoScore)

with open(outputFilePath, 'w') as f:
    f.write(outputString)


       
