import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("inputFolder")
parser.add_argument("outputFolder")
parsedArgs = parser.parse_args()

files = os.listdir(parsedArgs.inputFolder)

for x in files:
    if "txt" not in x:
        files.remove(x)

for y in files:

    filepath = (str(parsedArgs.inputFolder) + "/" + y)
    file  = open(str(filepath))
    score = file.readline()

    length = len(score)
    team1Score = 0
    team2Score = 0
    for x in range(0, length, 3):
        if (score[x+1] == "1") and (score[x+2] == "t"):
            team1Score = team1Score + 5
        elif (score[x+1] == "1") and (score[x+2] == "c"):
            team1Score = team1Score + 2
        elif (score[x+1] == "1") and (score[x+2] == "p"):
            team1Score = team1Score + 3
        elif (score[x+1] == "1") and (score[x+2] == "d"):
            team1Score = team1Score + 3
        elif (score[x+1] == "2") and (score[x+2] == "t"):
            team2Score = team2Score + 5
        elif (score[x+1] == "2") and (score[x+2] == "c"):
            team2Score = team2Score + 2
        elif (score[x+1] == "2") and (score[x+2] == "p"):
            team2Score = team2Score + 3
        else:
            team2Score = team2Score + 3
    finalScore = str(team1Score) + ":" + str(team2Score)

    file.close()

    filename = y.split(".")

    outputFile = open((str(parsedArgs.outputFolder) + "/" + filename[0] + "_t09329lw.txt"), "x")
    outputFile.write(finalScore)