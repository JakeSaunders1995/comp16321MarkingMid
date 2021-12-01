from sys import *
from os import listdir

def determineScore(scoreSnippet):
    if scoreSnippet[1] == "t":
        return 5
    elif scoreSnippet[1] == "c":
        return 2
    elif scoreSnippet[1] == "p" or "d":
        return 3

def main(fileToRead):
    team1Score = 0
    team2Score = 0
    fileText = fileToRead.read()
    scoreList = fileText.split("T")
    scoreList.pop(0)
    for score in scoreList:
        if score[0] == "1":
            team1Score += determineScore(score)
        elif score[0] == "2":
            team2Score += determineScore(score)
    return (str(team1Score)+":"+str(team2Score))

for item in sorted(listdir("./"+argv[1])):
    inputFile = open(argv[1]+"/"+item, "r")
    outputFile = open(argv[2]+"/"+item[:-4]+"_y77372db"+".txt", "w")
    outputFile.write(main(inputFile))
    outputFile.close()
    inputFile.close()

    