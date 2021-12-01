import argparse
import os

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("inFolder")
arg_parser.add_argument("outFolder")
arguments = arg_parser.parse_args()

inFolder = arguments.inFolder
outFolder = arguments.outFolder

for root, dirs, files in os.walk(inFolder, topdown=False):
	for name in files:
		fileInName = os.path.join(root, name)

		fileIn = open(fileInName, "r")

		match = fileIn.readline().strip("\n")
		fileIn.close()

		scores = {"T1":0, "T2":0}

		for i in range(0,len(match),3):
			if match[i+2] == "t":
				scores[match[i:i+2]] += 5
			elif match[i+2] == "c":
				scores[match[i:i+2]] += 2
			elif match[i+2] == "p":
				scores[match[i:i+2]] += 3
			elif match[i+2] == "d":
				scores[match[i:i+2]] += 3

		fileOutName = fileInName[8:-4] + "_h04151jk.txt"

		fileOut = open(outFolder + fileOutName, "w")
		fileOut.write(str(scores["T1"]) + ":" + str(scores["T2"]))
		fileOut.close()



