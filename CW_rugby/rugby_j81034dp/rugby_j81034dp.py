# Program 1 - Rugby
import sys
import os
# input example: T1tT2pT2pT1pT1d

InputFolder = sys.argv[1]
InputFolderList = os.listdir(InputFolder)
InputFolderList.sort()
OutputFolder = sys.argv[2]
OutputFolderList = os.listdir(OutputFolder)

for folder in InputFolderList:
	files = open(os.path.join(InputFolder, folder))
	content = files.read()
	folderstring = folder.replace(".txt","_j81034dp.txt")

	team1 = 0
	team2 = 0

	def Calc(pos):
		if pos == "t":
			return 5
		elif pos == "c":
			return 2
		elif pos == "p":
			return 3
		elif pos == "d":
			return 3
		else:
			return 0


	length = len(content)
	for i in range(1, length, 3):
		point = content[i+1]
		if content[i] == "1":
			team1 = team1 + Calc(point)
		else:
			team2 = team2 + Calc(point)


	finalscore = (str(team1) + ":" + str(team2))


	for folders in OutputFolder:
		outputFile = open(os.path.join(OutputFolder, folderstring), 'w')
		outputFile.writelines(finalscore)