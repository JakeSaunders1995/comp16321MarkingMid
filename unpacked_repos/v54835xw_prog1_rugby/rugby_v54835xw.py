import argparse
import os

def rugbyMark(pathIn, pathOut, fileName):
    with open(pathIn, "r") as In:
        mark = In.read()
        print(mark)
        temp1 = 0
        temp2 = 0
        for i in range(len(mark)):
            if mark[i] == "1":
                if mark[i + 1] == "t":
                    temp1 = temp1 + 5
                elif mark[i + 1] == "c":
                    temp1 = temp1 + 2
                else:
                    temp1 = temp1 + 3
            elif mark[i] == "2":
                if mark[i + 1] == "t":
                    temp2 = temp2 + 5
                elif mark[i + 1] == "c":
                    temp2 = temp2 + 2
                else:
                    temp2 = temp2 + 3
        print(temp1, ":", temp2)
        In.close()
    fileOutput = open(pathOut + "/" + fileName + "_v54835xw" + ".txt", "w")
    fileOutput.write(str(temp1) + ":" + str(temp2))
    fileOutput.close()

def OpenFolder(pathIn, pathOut):
    path = os.path.abspath(pathIn)
    outputPathFolder = os.path.abspath(pathOut)
    fileList = os.listdir(path)
    for i in range(len(fileList)):
        rugbyMark(path + "/" + fileList[i], outputPathFolder, fileList[i])


parser = argparse.ArgumentParser(description="Rugby")
parser.add_argument("pathIn", type=str)
parser.add_argument("pathOut", type=str)
args = parser.parse_args()

OpenFolder(args.pathIn, args.pathOut)