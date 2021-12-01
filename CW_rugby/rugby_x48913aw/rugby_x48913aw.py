import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("inputFolder")
parser.add_argument("outputFolder")
args = parser.parse_args()

inputFolder = str(args.inputFolder)
listFiles = os.listdir(inputFolder)

for x in listFiles:
    if ".txt" not in x:
        listFiles.remove(x)

noOfFiles = len(listFiles)

for y in range(noOfFiles):
    inputFile = open(inputFolder+"/"+listFiles[y])
    score = inputFile.read()

    position = 0
    T1score = 0
    T2score = 0
    loop = int((len(score)/3))

    for x in range(loop):
        team = score[position] + score[position+1]
        type = score[position+2]
        if (team == "T1"):
            if (type == "t"):
                T1score = T1score + 5
            elif (type == "c"):
                T1score = T1score + 2
            elif (type == "p"):
                T1score = T1score + 3
            else:
                T1score = T1score + 3
        else:
            if (type == "t"):
                T2score = T2score + 5
            elif (type == "c"):
                T2score = T2score + 2
            elif (type == "p"):
                T2score = T2score + 3
            else:
                T2score = T2score + 3
        position = position + 3

    finalscore = str(T1score) + ":" + str(T2score)

    fileName = ""
    name = str(listFiles[y])

    for i in name:
        if i == ".":
            break
        else:
            fileName = fileName + i

    outputfile = open((str(args.outputFolder)+"/"+fileName+"_x48913aw.txt"), "x")
    outputfile.write(finalscore)
