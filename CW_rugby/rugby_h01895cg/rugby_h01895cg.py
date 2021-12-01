import argparse,sys,os

inputFolder = sys.argv[1]
outputFolder= sys.argv[2]
if not os.path.exists(outputFolder):
	os.mkdir(outputFolder)

inFolderList=os.listdir(inputFolder)
for file in inFolderList:
	if file.endswith('.txt'):
		inputFile=open(inputFolder + '/' + file)
		scoringSystem={
			't':5,
			'c':2,
			'p':3,
			'd':3
		}
		team1Points=0
		team2Points=0
		scores=inputFile.read()
		inputFile.close()

		for i in range(0,len(scores),3):
			if scores[i]=="T":
				if scores[i+1]=="1":
					team1Points+=scoringSystem[scores[i+2]]
				elif scores[i+1]=="2":
					team2Points+=scoringSystem[scores[i+2]]

		if team1Points>team2Points:
			winner="Team 1"
		elif team1Points==team2Points:
			winner="There was no winner as the two teams drew"
		else:
			winner="Team 2"

		newFile=file[:-4]

		outputFile=open(outputFolder + '/' + newFile + "_h01895cg.txt","w")
		outputFile.write(str(team1Points) + ":" + str(team2Points))

