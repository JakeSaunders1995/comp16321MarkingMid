import sys	#gets filenames from command line
import os
inFolder = sys.argv[1]
outFolder = sys.argv[2]

os.mkdir(outFolder)

for inFile in os.listdir(inFolder):

	with open(inFile) as file:	#opens the input file
		inFileData = file.read()

	team1 = 0
	team2 = 0

	inFileData = inFileData[1:len(inFileData)]
	scoreList = inFileData.split("T")	#splits input string by "T" 

	for score in scoreList:	#tallies scores
		if score[0] == "1":
			if score[1] == "t":
				team1 += 5
			elif score[1] == "c":
				team1 += 2
			else:
				team1 += 3
		else:
			if score[1] == "t":
				team2 += 5
			elif score[1] == "c":
				team2 += 2
			else:
				team2 += 3		

	output = str(team1) + ":" + str(team2)

	outputLocation = outFolder + "/" + inFile + "_x57595ts.txt"

	with open(outputLocation, "w") as file:	#writes to file
		file.write(output)