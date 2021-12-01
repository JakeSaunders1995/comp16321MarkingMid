import sys
import os

numArgs = len(sys.argv)
print(numArgs)
if numArgs == 3:
	inputFile = sys.argv[1]
	outputFile = sys.argv[2]

	if os.path.isdir(inputFile):
		if not os.listdir(inputFile):
			print("Input directory is empty")
		else:
			# print("Input directory is not empty")
			allFiles = os.listdir(inputFile)
			for file in allFiles:
				fileName = file[:-4]
				with open(inputFile + '/' + file) as f:
					fileData = f.read()				
				# print(fileData)				
				# print(file)
				numIterations = len(fileData) / 3
				# print(numIterations)

				currentTextIndex = 0
				team1Score = 0
				team2Score = 0

				for i in range(int(numIterations)):
					teamThatScored = fileData[currentTextIndex + 1]
					scoreType = fileData[currentTextIndex + 2]
					# print("Team " + teamThatScored)
					# print("Score Type: ", scoreType)

					scoreToGive = 0
					if (scoreType == "t"):
						scoreToGive = 5
					elif (scoreType == "c"):
						scoreToGive = 2
					elif (scoreType == "p"):
						scoreToGive = 3
					elif (scoreType == "d"):
						scoreToGive = 3
					else:
						print("There is an error in the finding amount of points to give")

					# print("Score to give: ", scoreToGive)

					# print(teamThatScored)

					if teamThatScored == "1":
						team1Score += scoreToGive
					elif teamThatScored == "2":
						team2Score += scoreToGive
					else:
						print("There is an error in the finding team to give point to")

					# print("Current Team 1 Score: ", team1Score)
					# print("Current Team 2 Score: ", team2Score)
					currentTextIndex += 3

				print("Final Scoring Team1:Team2 = ", team1Score, ":", team2Score)
				if (team1Score == team2Score):
					print("Teams have drawed this match!")
				elif (team1Score > team2Score):
					print("Team 1 has won this match!")
				else:
					print("Team 2 has won this match!")

				# print("Saving scores to file output...")
				outputFileName = outputFile + "/" + fileName + "_g62512ww.txt"
				# print(outputFileName)
				textToWrite = str(team1Score) + ":" + str(team2Score)
				with open(outputFileName, "x") as f:
					f.write(textToWrite)

	else:
		print("Input directory does not exist")

