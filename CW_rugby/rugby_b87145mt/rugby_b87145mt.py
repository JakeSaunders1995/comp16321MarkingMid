import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("InputDir", help="Input file path", type=str)
parser.add_argument("OutputDir", help="Output file path", type=str)
args = parser.parse_args()



def GetFileName(inputFile):
    count = 0
    name = ""
    while count < len(inputFile) and inputFile[count] != ".":
        name = name + inputFile[count]
        count += 1
    return name



def addScore(letter):
    score = 0
    if letter == "t":
        score = 5
    elif letter == "c":
        score = 2
    elif letter == "p" or "d":
        score = 3
    return score



#The code below creates a list of files
fileList = os.listdir(args.InputDir)
outputDirectory = args.OutputDir



#The below repeats for each file in the input directory
for fileNumber in range(len(fileList)):
    fileName = fileList[fileNumber]
    location = args.InputDir + "/" + fileName
    f = open(location, "r")
    file = f.read()
    f.close()

    T1Score = 0
    T2Score = 0

    charCounter = 0

    for i in range(len(file)):

        if charCounter == 3:
             charCounter = 0

        if charCounter == 1:
            if int(file[i]) == 1:
                T1Score += addScore(file[i+1])
            elif int(file[i]) == 2:
                T2Score += addScore(file[i+1])

        charCounter += 1

    score = str(T1Score) + ":" + str(T2Score)

    fileTitle = GetFileName(fileName)

    outputPath = outputDirectory + "/" + fileTitle + "_b87145mt.txt"
    out = open(outputPath, "w")
    out.write(score)
    out.close()
