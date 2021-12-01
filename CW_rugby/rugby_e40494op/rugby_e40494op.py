import sys
import os
#check number of input arguments
#if len(sys.argv) != 3:
	#print("Not enough arguments")
# gets the file location
dirName = sys.argv[1]
outDirName = sys.argv[2]

files = os.listdir(dirName)

#scoreReport = "T1tT2pT2pT1pT1d"

for file in files:
	baseFileName = os.path.splitext(file)[0]
	#print(baseFileName)
	#create full file path name
	fullFileName = dirName + "/" + file
	#print(fullFileName)
	
	# opens, reads, and closes file
	scoreReports = open(fullFileName, "r")
	scoreReport = scoreReports.read()
	scoreReports.close()

	
	outputFullFuleName = outDirName + "/" + baseFileName + "_e40494op.txt"
	answers = open(outputFullFuleName, "w")
	


	team1 = []
	team2 = []
	T1 = 0
	T2 = 0

	count = len(scoreReport)

	for letter in range(len(scoreReport)):
		if scoreReport[letter] == "1":
			team1score = scoreReport[letter+1]
			team1.append(team1score)
		elif scoreReport[letter] == "2":
			team2score = scoreReport[letter+1]
			team2.append(team2score)


	for i in team1:
		if i == "t":
			T1 = T1 + 5
		elif i == "c":
			T1 = T1 + 2
		elif i == "p":
			T1 = T1 + 3
		elif i == "d":
			T1 = T1 + 3

	for i in team2:
		if i == "t":
			T2 = T2 + 5
		elif i == "c":
			T2 = T2 + 2
		elif i == "p":
			T2 = T2 + 3
		elif i == "d":
			T2 = T2 + 3	



	#winner = T1, ":", T2
	#print(winner)
	answers.write("%d:%d" %(T1,T2))



	#print(T1,":",T2)
	