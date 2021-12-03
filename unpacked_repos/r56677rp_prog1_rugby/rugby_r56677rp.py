import argparse
import os

def calculateScore(team):
    score = 0;
    for char in team:
        if char == "t":
            score += 5
        if char == "c":
            score += 2
        if char == "p":
            score += 3
        if char == "d":
            score += 3
    return score

parser = argparse.ArgumentParser()
parser.add_argument("inputFolder")
parser.add_argument("outputFolder")
args = parser.parse_args()

for files in os.walk(args.inputFolder):
    index = 0
    while index < len(files[2]):
        if ".txt" in files[2][index]:
            with open(args.inputFolder + "/" + files[2][index], "r") as currentFile:
                for line in currentFile:

                    # SPLIT STRING AFTER T
                    scoreList = line.split("T")

                    #SET or RESET SCORE
                    team_1 = []
                    team_1_score = 0
                    team_2 = []
                    team_2_score = 0

                    #APPEND SCORE TO EACH TEAM
                    for score in scoreList:
                        if "1" in score:
                            team_1.append(score[-1])
                        elif "2" in score:
                            team_2.append(score[-1])

                    # CONVERT CHAR TO POINTS
                    team_1_score = calculateScore(team_1)
                    team_2_score = calculateScore(team_2)

                    # WRITE TO FILES IN FOLDER
                    with open(args.outputFolder + "/" + files[2][index][:-4] + "_r56677rp.txt", "w") as writeFile:
                        writeFile.write(str(team_1_score) + ":" + str(team_2_score))
                    writeFile.close()
            currentFile.close()
        index += 1