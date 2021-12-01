#Rugby Game Score Calulator
# import os, argphrase, re
import sys
import os

currentfile = os.getcwd()
testfiles = os.listdir(sys.argv[1])
resultsfolder = sys.argv[2]+"/"

for file in testfiles:
	os.chdir(sys.argv[1])
	filename = file[:-4] + "_v80015aa.txt"
	inputfile = open(file, "r")
	x = inputfile.read()
	Team1Score = 0
	Team2Score = 0
	i = 0

	FileLength = len(x)
	while i < FileLength:
		Team = x[0:2]
		Score = x[2:3]
		x = x[3:]
		if Team == "T1":
			if Score == "t":
				Team1Score = Team1Score + 5
			elif Score == "c": 
				Team1Score = Team1Score + 2
			elif Score == "p":
				Team1Score = Team1Score + 3
			elif Score == "d":
				Team1Score = Team1Score + 3
		if Team == "T2":
			if Score == "t":
				Team2Score = Team2Score + 5
			elif Score == "c": 
				Team2Score = Team2Score + 2
			elif Score == "p":
				Team2Score = Team2Score + 3
			elif Score == "d":
				Team2Score = Team2Score + 3

		i += 3
		FinalScore = str(Team1Score)+":"+str(Team2Score)
		inputfile.close()
		os.chdir(currentfile)
		outputfile = open(resultsfolder+filename, "w")
		outputfile.write (FinalScore)
		outputfile.close()
		