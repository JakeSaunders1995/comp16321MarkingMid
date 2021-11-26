import argparse
import os
import re

def calculateScore(filepath):
	global outputFilePath
	inputFile = open(filepath)
	scorings = inputFile.readline()

	scoringsArr = re.findall(r'T\d[a-z]', scorings)
	# print(scoringsArr)

	T1Score = 0
	T2Score = 0

	for scoring in scoringsArr:
		scoringType = scoring[2]

		if scoringType == "t":
			score = 5
		elif scoringType == "c":
			score = 2
		elif scoringType == "d" or scoringType == "p":
			score = 3

		if scoring[1] == "1":
			T1Score += score
		elif scoring[1] == "2":
			T2Score += score

	inputFile.close()

	outputFile = open(os.path.join(outputFilePath, os.path.basename(filepath[0:-4]+"_x62967rr.txt")), "w")

	outputFile.write(f"{T1Score}:{T2Score}")

	outputFile.close()

parser = argparse.ArgumentParser()
parser.add_argument("inputFilePath")
parser.add_argument("outputFilePath")
args = vars(parser.parse_args())

outputFilePath = args["outputFilePath"]

for parent, dirnames, filenames in os.walk(args["inputFilePath"]):
    for fn in filenames:
        filepath = os.path.join(parent, fn)
        if (os.path.join(args["inputFilePath"], os.path.basename(filepath)) == filepath) and os.path.basename(filepath)[-4:] == ".txt":
        	calculateScore(filepath)




