import argparse
import os

parserVariable = argparse.ArgumentParser()
parserVariable.add_argument("inputFolderPath", type = str)
parserVariable.add_argument("outputFolderPath", type = str)
arguments = parserVariable.parse_args()


files = os.listdir(arguments.inputFolderPath)
files.sort()
for file in files :
	if len(file) >= 4 :
		if file[-4 :] == ".txt" :

			inputFilePath = (arguments.inputFolderPath + "/" + file)
			inputFile = open(inputFilePath)
			outcomeString = inputFile.read()
			inputFile.close()

			team1Score = 0
			team2Score = 0

			iterations = int((len(outcomeString) / 3)) 

			for x in range (iterations) :

				goalType = outcomeString[x * 3 : (x * 3) + 3]
				score = 0

				if goalType[2] == "t" :
					score = 5
				elif goalType[2] == "c" :
					score = 2
				elif goalType[2] == "p" or goalType[2] == "d" :
					score = 3

				if goalType[1] == "1" :
					team1Score += score
				else :
					team2Score += score

			if team1Score > team2Score :
				print("Team 1 won.")
			elif team1Score < team2Score :
				print("Team 2 won.")
			else :
				print("Both teams drew.")

			outputFilePath = arguments.outputFolderPath + "/" + file[0 : len(file) - 4] + "_h00203pb.txt" 
			outputFile = open(outputFilePath, "w")
			outputFile.write(str(team1Score) + ":" + str(team2Score))
			outputFile.close()