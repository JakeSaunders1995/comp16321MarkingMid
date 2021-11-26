import sys
import os

scoreOne = 0
scoreTwo = 0

def GetResultsFromFiles():
	results = []

	txtFiles = os.listdir(sys.argv[1])
	txtFiles.sort()

	for i in range(len(txtFiles)):
		file = open(sys.argv[1] + "/" + txtFiles[i])
		results.append(file.read())

	return results

def ReturnResults(i, scoreOne, scoreTwo):
	i+=1
	file = open(sys.argv[2] + "/" + "test_file" + str(i) + "_k47680dm.txt", "w")
	file.write(str(scoreOne) + ":" + str(scoreTwo))
	file.close()

allResults = GetResultsFromFiles()

for j in range(len(allResults)):

	results = allResults[j]

	for i in range(int(len(results) / 3)):
		team = results[(i * 3):((i*3) + 2):1]
		event = results[((i * 3) + 2):((i*3) + 3):1]
		if team == "T1":
			if event == "t":
				scoreOne += 5
			elif event == "c":
				scoreOne += 2
			elif event == "p":
				scoreOne += 3
			elif event == "d":
				scoreOne += 3

		elif team == "T2":
			if event == "t":
				scoreTwo += 5
			elif event == "c":
				scoreTwo += 2
			elif event == "p":
				scoreTwo += 3
			elif event == "d":
				scoreTwo += 3

	
	ReturnResults(j, scoreOne, scoreTwo)

	scoreTwo = 0
	scoreOne = 0
