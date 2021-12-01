import argparse
import os


def actualScore(types):
    if types == "t":
        return 5
    elif types == "c":
        return 2
    elif types == "p":
        return 3
    elif types == "d":
        return 3


parser = argparse.ArgumentParser(description="Rugby winner")
parser.add_argument("input_folder_location", metavar="inp", type=str)
parser.add_argument("output_folder_location", metavar="outp", type=str)
args = parser.parse_args()
inputFolder = args.input_folder_location
outputFolder = args.output_folder_location
for eachFile in os.scandir(inputFolder):
    inFile = open(eachFile.path, "r")
    newstr = os.path.basename(eachFile.path)[:-4]
    outFile = open(outputFolder + "/" + newstr + "_r82969js.txt", "w")
    score = inFile.readline().split("T")
    score.pop(0)
    team1 = []
    team2 = []
    for i in range(len(score)):
        if score[i][0] == "1":
            team1.append(actualScore(score[i][1]))
        elif score[i][0] == "2":
            team2.append(actualScore(score[i][1]))
    print("team1:", team1, "team2:", team2)
    result = str(sum(team1)) + ":" + str(sum(team2))
    outFile.write(result)
    inFile.close()
    outFile.close()
