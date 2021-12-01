import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('inputPath', type=str)
parser.add_argument('outputPath', type=str)
args = parser.parse_args()

def calculateScore(type):
    if type == "t":
        return 5
    elif type == "c":
        return 2
    elif type == "p":
        return 3
    elif type == "d":
        return 3
    else:
        return 0

def rugby(inputFilename):
    #Read scores into a variable
    with open(args.inputPath + "/" + inputFilename) as file:
        scores = file.read()

    t1Score = 0
    t2Score = 0

    #Iterate through each 3 characters
    for i in range(0, len(scores), 3):
        if scores[i:i+2] == "T1":
            t1Score += calculateScore(scores[i+2])
        elif scores[i:i+2] == "T2":
            t2Score += calculateScore(scores[i+2])

    #Output scores
    outputFilename = inputFilename[0:-4] + "_w25478ia.txt"
    with open(args.outputPath + "/" + outputFilename, "w") as file:
        file.write(str(t1Score) + ":" + str(t2Score))

dirs = os.listdir(args.inputPath)

for file in dirs:
    if file[-4:] == ".txt":
        rugby(file)
