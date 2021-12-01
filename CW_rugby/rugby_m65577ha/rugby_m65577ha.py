import os
import argparse


def slice(input):
    return [char for char in input]

parser = argparse.ArgumentParser()
parser.add_argument("path")
parser.add_argument("path2")

startDir = os.getcwd()
inputPath = parser.parse_args()
dir_list = os.listdir(inputPath.path)
os.chdir(inputPath.path)

for file in dir_list:
	if file.endswith(".txt"):
		os.chdir(startDir)
		os.chdir(inputPath.path)
		print("For the " + file + " game: ")
		inputFile = open(file)
		input = inputFile.read()
		currentLetter = 0
		currentTeam = 0
		team1Score = 0
		team2Score = 0
		scoreTracker = 0
		currentPosition = 0
		inputLength = len(input)
		slicedInput = slice(input)

		currentLetter = slicedInput[currentPosition]
		while currentPosition != inputLength:
			currentLetter = slicedInput[currentPosition]
			if currentLetter == "T":
				currentPosition = currentPosition + 1				
				currentLetter = slicedInput[currentPosition]
				if currentLetter == "1":
					currentTeam = 1
				elif currentLetter == "2":
					currentTeam = 2
				else:
					print("Error: Missing team number.")				
				currentPosition = currentPosition + 1
				currentLetter = slicedInput[currentPosition]
				if currentLetter == "t":
					scoreTracker = scoreTracker + 5
				elif currentLetter == "c":
					scoreTracker = scoreTracker + 2
				elif currentLetter == "p":
					scoreTracker = scoreTracker + 3
				elif currentLetter == "d":
					scoreTracker = scoreTracker + 3
				else:
					print("Error: Missing score type.")
				if currentTeam == 1:
					team1Score = team1Score + scoreTracker
				elif currentTeam == 2:
					team2Score = team2Score + scoreTracker
				currentPosition = currentPosition + 1
				scoreTracker = 0
		if team1Score > team2Score:
			print("Team 1 is the winner!")
		elif team1Score < team2Score:
			print("Team 2 is the winner!")
		elif team1Score == team2Score:
			print("The game is a draw!")
		print("The final score is: " + str(team1Score) + ":" + str(team2Score))
		os.chdir(startDir)
		os.chdir(inputPath.path2)
		filename = file.replace(".txt", "_m65577ha.txt")
		outputFile = open(filename, "w")
		outputFile.write(str(team1Score) + ":" + str(team2Score))
		inputFile.close()
	else:
		print("Error: No .txt files in input folder.")

