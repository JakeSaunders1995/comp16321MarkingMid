import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("events")
parser.add_argument("score")
args = parser.parse_args()
inputFolder = args.events
outputFolder = args.score
fileList = os.listdir(inputFolder)
numberFiles = len(fileList)

for i in range (numberFiles):

	fileIn = open(inputFolder + "/" + fileList[i], "r")
	match = fileIn.readline().strip(" ")
	fileIn.close()

	score = {"T1":0, "T2":0}

	for x in range(0, len(match),3):
		if match[x+2] == "t":
			score[match[x:x+2]] +=5
		elif match [x+2] == "c":
			score [match[x:x+2]] +=2
		elif match [x+2] == "p":
			score[match[x: x+2]] += 3
		elif match[x+2] == "d":
			score[match[x:x+2]]+=3

	outputFolder +="/"
	fileName = fileList[i].replace(".txt", "")+ "_x63917cd.txt"
	outputName = os.path.join(outputFolder, fileName)
	fileOut = open(outputName, "w")
	fileOut.write (str(score["T1"])+":"+str(score["T2"]))
	fileOut.close()