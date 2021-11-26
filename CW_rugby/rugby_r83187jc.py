import argparse, os

parser = argparse.ArgumentParser()

parser.add_argument("inputFolder")
parser.add_argument("outputFolder")
args = parser.parse_args()

inputFolderName = args.inputFolder
outputFolderName = args.outputFolder

filesList = os.listdir(inputFolderName)

for fileName in filesList:
	inputDirectory = inputFolderName + '/' + fileName
	f = open(inputDirectory , "r")
	inputContent = f.read()
	f.close()

	inputList = list(inputContent)

	team1Score = 0
	team2Score = 0
	currentTeam = 0

	for i in range(0, len(inputList)):
		score = 0
		if i % 3 == 1:
			#Will be team number (1 or 2)
			currentTeam = inputList[i]
			if inputList[i+1] == "t":
				score = 5
			elif inputList[i+1] == "c":
				score = 2
			elif inputList[i+1] == "p":
				score = 3
			elif inputList[i+1] == "d":
				score = 3

			if currentTeam == "1":
				team1Score += score
			elif currentTeam == "2":
				team2Score += score

	dotIndex = fileName.find(".")
	outputFileName = fileName[:dotIndex] + "_r83187jc" + fileName[dotIndex:]
	outputDirectory = outputFolderName + '/' + outputFileName
	
	f = open(outputDirectory, "w")
	outputContent = str(team1Score) + ":" + str(team2Score)
	f.write(outputContent)
	f.close()
