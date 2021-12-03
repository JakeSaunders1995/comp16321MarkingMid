import re
import sys
import os
import argparse


inputPath = sys.argv[1]  
outputPath = sys.argv[2]
print(inputPath)
print(outputPath)


inputFiles = os.listdir(inputPath)



count = 0
for files in inputFiles:
	

	


	os.chdir(inputPath)


	with open (inputFiles[count], "r") as readFile:
		teamScores = readFile.readline()

	


	T1total = 0
	T2total = 0

	T1Scores = re.findall("T1t|T1c|T1p|T1d", teamScores)
	

	for score in T1Scores:
		if (score == "T1t"):
			T1total += 5
		elif (score == "T1c"):
			T1total += 2
		elif (score == "T1p"):
			T1total += 3
		elif (score == "T1d"):
			T1total += 3			

	

	T2Scores = re.findall("T2t|T2c|T2p|T2d", teamScores)
	
	for score in T2Scores:
		if (score == "T2t"):
			T2total += 5
		elif (score == "T2c"):
			T2total += 2
		elif (score == "T2p"):
			T2total += 3
		elif (score == "T2d"):
			T2total += 3		

	print(T2total)
	if (T1total > T2total):
		print("Team 1 has won this game")

	elif (T2total > T1total):
		print("Team 2 has won this game")	#

	else:
		print("It's a draw")	


	result = str(T1total) + ":" + str(T2total)
	
	readFile.close()

	
	os.chdir("..")
	os.chdir(outputPath)

	x = re.split(".txt", inputFiles[count], 1)
	print(x[0])
	fileWriter = open(x[0] + "_j11865sr.txt", "w")
	fileWriter.write(result)
	fileWriter.close

	os.chdir("..")
	count += 1





