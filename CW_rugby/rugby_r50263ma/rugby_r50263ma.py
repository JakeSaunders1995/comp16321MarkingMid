import argparse
import os

parser = argparse.ArgumentParser(description="Calculating the rugby scores")
parser.add_argument("inputFolder")
parser.add_argument("outputFolder")
args = parser.parse_args()

files = os.listdir(args.inputFolder)
for f in files:
    if f != ".DS_Store":
        inputFile = open(args.inputFolder + "/" + f, 'r')
        outputFileName = f[:-4] + "_r50263ma" + ".txt"
        outputFile = open(args.outputFolder + "/" + outputFileName, "w")
        scoreCard = inputFile.read()
        score1 = 0
        score2 = 0
        print(scoreCard)
        for i in range(0, len(scoreCard), 3):
            if scoreCard[i: i+2] == "T1":
                print("Team 1 scored a ", end="")
                if scoreCard[i+2] == "t":
                    print("Try")
                    score1 += 5
                elif scoreCard[i+2] == "c":
                    print("Goal Kick")
                    score1 += 2
                elif scoreCard[i+2] == "p":
                    print("Penalty")
                    score1 += 3
                elif scoreCard[i+2] == "d":
                    print("Drop Goal")
                    score1 += 3
            elif scoreCard[i: i+2] == "T2":
                print("Team 2 scored a ", end="")
                if scoreCard[i+2] == "t":
                    print("Try")
                    score2 += 5
                elif scoreCard[i+2] == "c":
                    print("Goal Kick")
                    score2 += 2
                elif scoreCard[i+2] == "p":
                    print("Penalty")
                    score2 += 3
                elif scoreCard[i+2] == "d":
                    print("Drop Goal")
                    score2 += 3
        outputFile.write(str(score1) + ":" + str(score2))
        inputFile.close()
        outputFile.close()
