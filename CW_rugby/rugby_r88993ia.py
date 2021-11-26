import sys
import os
inDir = sys.argv[1] + "/"
outDir = sys.argv[2] + "/"

for file in os.listdir(inDir):
	ofile = open(inDir + file, "r")
	a = ofile.readline()
	ofile.close()

	team1Score = 0
	team2Score = 0
	
	for i in range(0, len(a),3):
		team = a[i+1]
		sType = a[i+2]
		if sType == "t":
			score = 5
		elif sType == "c":
			score = 2
		elif sType == "p" or sType == "d":
			score = 3

		if team == "1":
			team1Score += score
		elif team == "2":
			team2Score += score

	outputFileName = file[:-4] + "_r88993ia" + file[-4:]

	outFile = open(outDir + outputFileName, "w")
	outFile.write(str(team1Score)+":"+str(team2Score))
	outFile.close()