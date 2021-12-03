import argparse, os, re

parser = argparse.ArgumentParser()
parser.add_argument("inputFolder")
parser.add_argument("outputFolder")
args = parser.parse_args()

if not os.path.exists(args.inputFolder):
    print("Error! The input folder does not exist: ", args.inputFile)
    exit(0)

if not os.path.exists(args.outputFolder):
    os.mkdir(args.outputFolder)
    print("Create new folder for output: ", args.outputFolder)

pattern = r"T[12][tcpd]"

for fileName in os.listdir(args.inputFolder):
    filePath = os.path.join(args.inputFolder, fileName)
    if os.path.isdir(filePath):
        continue

    team1Points = 0
    team2Points = 0

    fin = open(filePath, "r")
    for line in fin.readlines():
        line.strip()

    for str in re.findall(pattern, line):
        num = 0
        if str[2] == "t":
            num = 5
        if str[2] == "c":
            num = 2
        if str[2] == "p":
            num = 3
        if str[2] == "d":
            num = 3

        if str[1] == "1":
            team1Points += num
        if str[1] == "2":
            team2Points += num
    fin.close()

    print(f"{team1Points:d}:{team2Points:d}")

    fname, ext = os.path.splitext(fileName)
    fname += "_g21434rb" + ext
    outputFilePath = os.path.join(args.outputFolder, fname)

    fout = open(outputFilePath, "w")
    fout.write("%d:%d" % (team1Points, team2Points))
    fout.close()








