import re
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("inputFolderPath", help = "input file path")
parser.add_argument("outputFolderPath", help = "output file path")
args = parser.parse_args()

inputFolderPath = args.inputFolderPath
outputFolderPath = args.outputFolderPath
inputFiles = os.listdir(inputFolderPath)
z = 0

while z < len(inputFiles):
    inputFile = inputFiles[z]
    inputFilePath = (inputFolderPath + "/" + inputFile)
    f = open(inputFilePath)
    teamScores = f.read()
    a = 2
    team1Score = 0
    team2Score = 0
    while a < len(teamScores):
        if teamScores[a - 1] == '1':
            if teamScores[a] == 't':
                team1Score += 5
            elif teamScores[a] == 'c':
                team1Score += 2
            elif teamScores[a] == 'p':
                team1Score += 3
            elif teamScores[a] == 'd':
                team1Score += 3
            else:
                break
        elif teamScores[a - 1] == '2':
            if teamScores[a] == 't':
                team2Score += 5
            elif teamScores[a] == 'c':
                team2Score += 2
            elif teamScores[a] == 'p':
                team2Score += 3
            elif teamScores[a] == 'd':
                teamScores += 3
            else:
                break
        else:
            break
        a += 3

    # if team1Score > team2Score:
    #     print("Team 1 wins!")
    # elif team1Score < team2Score:
    #     print("Team 2 wins!")
    # elif team1Score == team2Score:
    #     print("Draw!")

    answer = (str(team1Score) + ":" + str(team2Score))
    outputFile = (inputFile[:-4] + "_t56091yd" + inputFile[-4:])
    outputFilePath = (outputFolderPath + "/" + outputFile)
    f = open(outputFilePath, "w")
    f.write(answer)
    z += 1