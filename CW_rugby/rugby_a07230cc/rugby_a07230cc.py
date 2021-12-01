import argparse
import os

##start funct

def calculateScores(fileToRead):

	allScores = fileToRead.read()
	fileToRead.close()

	scores = allScores.split('T')

	scores.remove(scores[0])

	team1points = 0
	team2points = 0

	for i in scores:
		if i[0] == "1":
			if i[1] == "t":
				team1points += 5
			elif i[1] == "c":
				team1points += 2
			elif i[1] == "p":
				team1points += 3
			else:
				team1points += 3
		elif i[0] == "2":
			if i[1] == "t":
				team2points += 5
			elif i[1] == "c":
				team2points += 2
			elif i[1] == "p":
				team2points += 3
			else:
				team2points += 3

	if team1points > team2points:
		winner = "The winner is Team 1"
	elif team1points < team2points:
		winner = "The winner is Team 2"
	else:
		winner = "There was a draw!"


	output = str(team1points) + ":" + str(team2points)

	print("Team 1's points = " + str(team1points))
	print("Team 2's points = " + str(team2points))
	print(winner)
	return output
	# print(allScores)
	# print(scores)


arg = argparse.ArgumentParser()

arg.add_argument("inFolderPath")
arg.add_argument("outFolderPath")

File = arg.parse_args()

direct = os.scandir(File.inFolderPath)

for f in direct:
	folderInput = File.inFolderPath + "/" + f.name
	fileToRead = open(folderInput, "r")
	output = calculateScores(fileToRead)
	folderOutput = File.outFolderPath + "/" + f.name
	folderOutput = folderOutput.replace(".txt", "_a07230cc.txt")

	fileToSave = open(folderOutput, "w")
	fileToSave.write(output)
	fileToSave.close()