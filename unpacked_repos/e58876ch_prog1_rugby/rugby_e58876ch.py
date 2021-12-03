#Program 1 MidTerm
#Christopher Harrington
#e58876ch

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("inputFolder", type = str)
parser.add_argument("outputFolder", type = str)

args = parser.parse_args()

inputDirectory = args.inputFolder

counterInput = 0

for inputPath in os.listdir(inputDirectory):
	if os.path.isfile(os.path.join(inputDirectory, inputPath)):
		counterInput = counterInput + 1
		
		
counterOutput = 0

outputDirectory = args.outputFolder

for outputPath in os.listdir(inputDirectory):
	if os.path.isfile(os.path.join(outputDirectory, outputPath)):
		counterOutput = counterOutput + 1
		
for nameInput in os.scandir(inputDirectory):
	
	if nameInput.is_file():


		with open(nameInput, "r") as score:
			line = score.readline()
	


		t = 5						#scoring types
		c = 2
		p = 3
		d = 3

		team1 = 0					#score at start of game
		team2 = 0

		count = 0					#used to track the different characters in line
		type = 1



		while count < len(line):

			if line[count] == "1":
	
				if line[type] == "t":
					team1 += t
		
				elif line[type] == "c":
					team1 += c
		
				elif line[type] == "p":
					team1 += p
		
				elif line[type] == "d":
					team1 += d
		

			elif line[count] == "2":
	
				if line[type] == "t":
					team2 += t
		
				elif line[type] == "c":
					team2 += c
		
				elif line[type] == "p":
					team2 += p
		
				elif line[type] == "d":
					team2 += d


	
			count +=1

			type += 1

		if team1 > team2:
			winner = "T1"

		elif team2 > team1:
			winner = "T2"

		elif team1 == team2:
			winner = "Draw"

		scoreFinal = str(team1)+":"+str(team2)
		

		
		
		outputDiretory = args.outputFolder
		checker = os.scandir(outputDirectory)
		filename = nameInput.name.split(".")
	
		if counterOutput < counterInput:
			for count in range(counterInput):
				outputFile = filename[0] + "_e58876ch.txt"
				newFile = args.outputFolder + "/" + outputFile
				
			
				newPath = open(newFile, "x") 
				break
		checker = os.scandir(outputDirectory)
		for writtenText in checker:
			write = writtenText.name.split("_")
			concatenation = write[0] + "_" + write[1]
		
			if filename[0] == concatenation:
				finalFile = open(writtenText, "w")
				finalFile.write(scoreFinal)
			else:
				continue



