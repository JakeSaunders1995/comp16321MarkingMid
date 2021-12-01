import os
import sys
directory = sys.argv[1]
outputDirectory = sys.argv[2]
for filename in os.listdir(directory):
		filepath = directory + "/" + filename
		text_file = open(filepath, "r")
		scoreCard = text_file.read()
		

		
		T1 = 0
		T2 = 0

		teamScore = []
		for index in range(0, len(scoreCard), 3):
			teamScore.append(scoreCard[index : index + 3]) # This seperates the scorecard into indivdual scores
		

	   
		for item in teamScore:  #Calculates the team scores
			if item == "T1t":
				T1 = T1 + 5
			elif item == "T1c":
				T1 = T1 + 2
			elif item == "T1p":
				T1 = T1 + 3
			elif item == "T1d":
				T1 = T1 + 3
			elif item == "T2t":
				T2 = T2 + 5
			elif item == "T2c":
				T2 = T2 + 2
			elif item == "T2p":
				T2 = T2 + 3
			elif item == "T2d":
				T2 = T2 + 3


		print(str(T1) + ":" + str(T2))
		text_file.close()

		outputFile = outputDirectory + "/" + filename[0:-4] + "_" + "f37609ak" + ".txt"

		f = open(outputFile, "w")
		f.write(str(T1) + ":" + str(T2))
		f.close



	