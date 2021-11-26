import argparse
import os

#Takes in the point type and returns the value. Fairly clear coding.
def Calc(point):
	if point == 't':
		return 5
	elif point == 'c':
		return 2
	elif point == 'p':
		return 3
	elif point == 'd':
		return 3

#The main bulk of code, takes in a file path and outputs the overall score of the match.
def scoreCalculator(filePath):
	#Opens the file to work with the string inside and sets up some variables for updating team scores and making the while loop possible.
	score = open(filePath, "r").read()
	team1Score = 0
	team2Score = 0
	i = 0

	#Loops through the string 3 characters at a time, checking for which team it is and then passing the point type to the Calc() function. It then updates the relevant team score.
	while i < len(score):
		if score[i+1] == '1':
			team1Score += Calc(score[i+2])
		else:
			team2Score += Calc(score[i+2])
		i += 3

	#Here the team winner is determined, but apparently it's useless? It doesn't appear to be neccesary for the output, so it'll stay here I guess.
	if team2Score > team1Score:
		teamWinner = 'Team 2'
	elif team1Score > team2Score:
		teamWinner = 'Team 1'
	elif team1Score == team2Score:
		teamWinner = 'Draw'

	#opens an output file in the given file path, names it the same as the input filepath, but with the .txt replaces with [username].txt. It also writes the score in the format required to the file
	open(args.Output_Path + '\\' + os.path.splitext(os.path.basename(filePath))[0] + "_e55646sa.txt", 'w').write(str(team1Score) + ':' + str(team2Score))

my_parser = argparse.ArgumentParser(description='Spell Checker')

my_parser.add_argument(
	'Input_Path',
    metavar='path',
    type=str,
    help='the path to the input file')

my_parser.add_argument(
	'Output_Path',
    metavar='path',
    type=str,
    help='the path to output directory')

args = my_parser.parse_args()

inputFolder = args.Input_Path

#Checks whether the input file path is a text file, where it would just calculate for that file. If it is a folder, then it would iterate through that folder and calculate for all text files in the folder.
if os.path.isdir(inputFolder):
	for entry in os.scandir(inputFolder):
	    if entry.path.endswith(".txt") and entry.is_file():
	        scoreCalculator(entry.path)
else:
	print("Please input a text file or an existing folder/directory")