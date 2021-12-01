import argparse
import re
import os
import sys

inputFolder = sys.argv[-2]
outputFolder = sys.argv[-1]

def rugbyCalculator(inputFile):

	refined = re.findall('[A-Z][^A-Z]*', inputFile)
	#print(refined) #Ensure refined has been changed.

	t = 5 #Try

	c = 2 #Goal kick

	p = 3 #Penalty

	d = 3 #Drop goal

	team1 = 0
	team2 = 0

	i = 0
	while i < len(refined):
		if 		refined[int(i)] == "T1t":
					team1 = int(team1) + int(t)
		elif	refined[int(i)] == "T1c":
					team1 = int(team1) + int(c)
		elif	refined[int(i)] == "T1p":
					team1 = int(team1) + int(p)
		elif	refined[int(i)] == "T1d":
					team1 = int(team1) + int(d)
		elif	refined[int(i)] == "T2t":
					team2 = int(team2) + int(t)
		elif	refined[int(i)] == "T2c":
					team2 = int(team2) + int(c)
		elif	refined[int(i)] == "T2p":
					team2 = int(team2) + int(p)
		elif	refined[int(i)] == "T2d":
					team2 = int(team2) + int(d)
		i = i + 1

	output = (str(team1) + ":" + str(team2)) #Ensure the addition and output was correct.

	return output

for inputFile in os.listdir(inputFolder):
	with open (os.path.join(inputFolder, inputFile), "r") as file:
		file = file.read()
		results = rugbyCalculator(file)

		outputFileTemp = inputFile.rstrip(".txt")
		outputFile = outputFileTemp + "_c43480ct.txt"

		with open(os.path.join(outputFolder, outputFile), "w+") as file:
			file.write(results)
