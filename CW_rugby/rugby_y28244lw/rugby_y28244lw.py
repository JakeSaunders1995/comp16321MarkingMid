import sys
import os

FIN = str(sys.argv[1])
FOUT = str(sys.argv[2])

for files in os.listdir(FIN):
	filename = str(files)
	InFilePath = os.path.join(FIN,filename)


	ScoreList = []
	T1score = 0
	T2score = 0


	for line in open(InFilePath, "r"):
		for i in range(0,len(line),3):
	 		ScoreList.append(line[i:i+3])


	for j in range(0,len(ScoreList)):

		ScoreAdded = 0

		if ScoreList[j][2] == "t":
			ScoreAdded = 5
		elif ScoreList[j][2] == "c":
			ScoreAdded = 2
		elif ScoreList[j][2] == "p":
			ScoreAdded = 3
		elif ScoreList[j][2] == "d":
			ScoreAdded = 3

		if ScoreList[j][1] == "1":
			T1score += ScoreAdded
		else:
			T2score += ScoreAdded

	result = str(T1score) + ":" + str(T2score)

	winner = ""

	if T1score > T2score:
		winner = "Team 1"
	elif T1score < T2score:
		winner = "Team 2"
	else:
		winner = "draw"

	pos = filename.index(".")
	outfilename = filename[:pos] + "_y28244lw.txt"
	OutFilePath = os.path.join(FOUT, outfilename)

	f = open(OutFilePath,"w")
	f.write(result)
	f.close()






