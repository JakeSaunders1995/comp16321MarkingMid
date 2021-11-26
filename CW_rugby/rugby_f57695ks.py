import argparse
import re
import os

docParse = argparse.ArgumentParser(description="InputFile")
docParse.add_argument('Path', metavar='path', type=str, help='filepath to input')
docParse.add_argument('Path2', metavar='path', type=str, help='filepath to output')
args = docParse.parse_args()

inputDir = args.Path
for file in os.listdir(args.Path):
    inputfile = open(args.Path +"/"+ file)
    WinCode = inputfile.read()
    Team1Score = 0
    Team2Score = 0
    ScoreInfoList = re.findall("...", WinCode)
    for ScoreInfo in ScoreInfoList:
        if ScoreInfo[1] == "1":
            if ScoreInfo[2] == "t":
                Team1Score += 5
            elif ScoreInfo[2] == "c":
                Team1Score += 2
            elif ScoreInfo[2] == "p":
                Team1Score += 3
            elif ScoreInfo[2] == "d":
                Team1Score += 3
        elif ScoreInfo[1] == "2":
            if ScoreInfo[2] == "t":
                Team2Score += 5
            elif ScoreInfo[2] == "c":
                Team2Score += 2
            elif ScoreInfo[2] == "p":
                Team2Score += 3
            elif ScoreInfo[2] == "d":
                Team2Score += 3
    FinalScore = str(Team1Score) + ":" + str(Team2Score)
    if not os.path.exists(args.Path2):
        outputDir = os.mkdir(args.Path2)
    filename = file[:-4]
    outputfile = open(args.Path2 +"/"+filename+ "_f57695ks.txt", "w")
    outputfile.write(FinalScore)
    outputfile.close()
    