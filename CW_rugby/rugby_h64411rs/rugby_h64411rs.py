import sys 
import os 

inputFolder = sys.argv[1]
outputFolder = sys.argv[2]

if os.path.exists(outputFolder) == False:
	os.makedirs(outputFolder)

for input_file in os.listdir(inputFolder):
	file = open(os.path.join(inputFolder,input_file), "r")
	tally = file.readline()
	file.close()

	length = len(tally)
	t1_score = 0 
	t2_score = 0

	for x in range(0, length, 3):
		team = tally[x:x+2]
		scoring_type = tally[x+2]

		if scoring_type == "t":
			score = 5
		elif scoring_type == "c":
			score = 2 
		elif scoring_type == "p":
			score = 3
		else:
			score = 3 

		if team == "T1":
			t1_score = t1_score + score
		else:
			t2_score = t2_score + score 

	name, ext = os.path.splitext(input_file)
	output_file = name + "_h64411rs" + ext 

	file = open(os.path.join(outputFolder, output_file), "w")
	file.write(str(t1_score) + ":" + str(t2_score))
	file.close()
