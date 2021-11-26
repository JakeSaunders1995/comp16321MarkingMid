import sys
import os

inputFolder = sys.argv[-2]
outputFolder = sys.argv[-1]

if not os.path.isdir(outputFolder):
	os.mkdir(outputFolder)
else:
	pass


def Rugby(inputFile):
	
	matchScore = inputFile #T1pT2c

	team1 = []
	team2 = []

	index = 0

	for item in matchScore:
		if item == "T":
			index += 1

		elif item == "1":
			team1.append(matchScore[index+1])
			index += 1

		elif item == "2":
			team2.append(matchScore[index+1])
			index += 1

		else:
			index+=1
			pass


	def ScoreTally(team):
				#t = 5
				#c = 2
				#p = 3
				#d = 3
		for num in range(0,len(team)):
			if team[num] == "t":
				team[num] = 5
			elif team[num] == "c":
				team[num] = 2 
			else:
				team[num] = 3

	ScoreTally(team1)
	ScoreTally(team2)

	score1 = sum(team1)
	score2 = sum(team2)

	
	score = str(score1)+":"+str(score2)
	return score

for testFile in os.listdir(inputFolder):
	with open(os.path.join(inputFolder,testFile), "r") as inputFile:
		
		inputFile = inputFile.read()
		output = Rugby(inputFile)

		testVal = testFile.rstrip(".txt")
		testFileAndID = testVal + "_s11642lf.txt"

		with open(os.path.join(outputFolder,testFileAndID),"w+") as outputFile:
			outputFile.write(output)
			outputFile.close()