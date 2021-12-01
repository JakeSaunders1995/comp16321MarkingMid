#Program which outputs two rugby teams' scores based on how they scored

import argparse, os


def init(): #reads the input data from file, opens output file
		parser = argparse.ArgumentParser()
		parser.add_argument("dirIn")
		parser.add_argument("dirOut")

		args = parser.parse_args()
		dirs = vars(args)

		return dirs["dirIn"], dirs["dirOut"]

def simplify(string): #strips score types from each string and concatenates them into separate team variables
	team1 = ""
	team2 = ""
	for i in range(len(string)):
		if string[i] == "1":
			i+=1
			team1+=string[i]
		if string[i] == "2":
			i+=1
			team2+=string[i]
	return team1, team2

def summate(string): #adds up the score of the team based on scoring types and quantity
	score = 0
	for i in range(len(string)):
		if string[i] == "t": # try
			score+=5
		elif string[i] == "c": # goal kick
			score+=2
		elif string[i] in ("pd"): #penalty or drop goal
			score+=3
	return score


def output(string, fileOut):
	fileOut.write(string)
	fileOut.close()

dirIn, dirOut = init()
currentFile = ""
for file in os.listdir(dirIn):
	currentFile = os.path.join(dirIn,file)
	
	currentFile = open(currentFile, "r")

	inputData = currentFile.read()
	team1, team2 = simplify(inputData)
	team1 = summate(team1)
	team2 = summate(team2)
	finalScore = str(team1) + ":" + str(team2)
	
	file = os.path.join(dirOut,file.rsplit(".",1)[0])

	fileOut = open(file+"_q44958jp.txt", "w")

	output(finalScore, fileOut)
