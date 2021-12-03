import sys
import os
inputFolder = sys.argv[1]
outputFolder = sys.argv[2]



for inputFile in os.listdir(inputFolder):

	with open(inputFolder + "/" + inputFile, 'r') as i:
		inptxt = i.readlines()[0]
		
	team1score = 0
	team2score = 0
	result = ""

	for x in range(len(inptxt)):
		if inptxt[x: x+2] == "T1":
			if inptxt[x+2] == "t":
				team1score += 5
			elif inptxt[x+2] == "c":
				team1score += 2
			elif inptxt[x+2] == "p":
				team1score += 3
			elif inptxt[x+2] == "d":
				team1score += 3
		elif inptxt[x: x+2] == "T2":
			if inptxt[x+2] == "t":
				team2score += 5
			elif inptxt[x+2] == "c":
				team2score += 2
			elif inptxt[x+2] == "p":
				team2score += 3
			elif inptxt[x+2] == "d":
				team2score += 3

	if team1score == team2score:
		result = "Draw."
	elif team1score > team2score:
		result = "Team 1 win."
	else:
		result = "Team 2 win."

	scoreline = str(team1score) + ":" + str(team2score)


	with open(outputFolder + "/" + inputFile[:-4] + "_s78014sh.txt", 'w+') as o:
			o.write(scoreline)


