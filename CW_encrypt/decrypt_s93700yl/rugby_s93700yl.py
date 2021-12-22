import sys
import os


input_Folder = sys.argv[1]
output_Folder = sys.argv[2]
fileList = os.listdir(input_Folder)
for filename in fileList:
	score_file = open(input_Folder + "/" + filename)
	teamAndScore = score_file.read()
	score_file.close()
	def scoreCalculator():
		emptyString = ""
		scoreCalculator.x = 0
		scoreCalculator.y = 0
		for i in range(len(teamAndScore)):
			emptyString += teamAndScore[i]
			if len(emptyString) % 3 == 0:
				if emptyString[len(emptyString) - 3 : len(emptyString) - 1] == "T1":
					if emptyString[len(emptyString) - 1] == "t":
						scoreCalculator.x += 5
					elif emptyString[len(emptyString) - 1] == "c":
						scoreCalculator.x += 2
					elif emptyString[len(emptyString) - 1] == "p" or emptyString[len(emptyString) - 1] == "d":
						scoreCalculator.x += 3
				elif emptyString[len(emptyString) - 3 : len(emptyString) - 1] == "T2":
					if emptyString[len(emptyString) - 1] == "t":
						scoreCalculator.y += 5
					elif emptyString[len(emptyString) - 1] == "c":
						scoreCalculator.y += 2
					elif emptyString[len(emptyString) - 1] == "p" or emptyString[len(emptyString) - 1] == "d":
						scoreCalculator.y += 3
	scoreCalculator()
	calculatedScore_file = open(output_Folder + "/" + filename[0:len(filename) - 4] + "_s93700yl.txt", "w")
	calculatedScore_file.write(str(scoreCalculator.x) + ":" + str(scoreCalculator.y))
	calculatedScore_file.close()





