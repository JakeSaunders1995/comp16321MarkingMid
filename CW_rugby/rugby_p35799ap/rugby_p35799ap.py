import sys
import os

for textFile in os.listdir(sys.argv[1]):
	filename = (sys.argv[1]+"/"+textFile)
	file = open(filename, "r")
	for line in file:
		exampleInput = line

		team1Score = 0
		team2Score = 0

		for i in range(len(exampleInput)):
			if exampleInput[i] == "1":
				if exampleInput[i + 1] == "t":
					team1Score += 5
				elif exampleInput[i + 1] == "c":
					team1Score += 2
				elif exampleInput[i + 1] == "p" or exampleInput[i + 1] == "d":
					team1Score += 3
			elif exampleInput[i] == "2":
				if exampleInput[i + 1] == "t":
					team2Score += 5
				elif exampleInput[i + 1] == "c":
					team2Score += 2
				elif exampleInput[i + 1] == "p" or exampleInput[i + 1] == "d":
					team2Score += 3

		result = str(team1Score)+":"+str(team2Score)
		#print(result)

		outputFile = textFile[:-4]
		outputFile += "_p35799ap.txt"
		outputFile = (sys.argv[2]+"/"+outputFile)
		#print(outputFile)
		# test_file1.txt --> ./output_folder/test_file1_p35799ap.txt
		writeFile = open(outputFile, "w")
		writeFile.write(result)



# sys.argv = ['rugby_p35799ap.py', './Example_inputs_program1', './[output_folder]']
# os.listdir(sys.argv[1]) = ['test_file2.txt', 'test_file3.txt', 'test_file1.txt']