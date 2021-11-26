import os
import sys 

# Add score function for every type of score
scores = {"t": 5, "c": 2, "p": 3, "d": 3}
def addScore(score_type):
	for type in scores:
		if score_type == type:
			return scores[type]

# Real program starts from here
for file in os.listdir(sys.argv[1]):			# Make a list of files inside input folder and iterate through each file
	t1, t2 = 0, 0
	f = open(os.path.join(sys.argv[1],file))	# Open each file on path: input_folder/file_name.txt
	length = int(len(f.read())/3)				# Find the length of the input file and how many iteration is needed
	f.seek(0)

	i = 0			
	while i < length:
		i += 1
		score = f.read(3)
		if score[1] == "1":
			t1 += addScore(score[-1])
		else:
			t2 += addScore(score[-1])
	f.close()

	# Output file
	outputFile = open(os.path.join(sys.argv[2], "".join(file.split(".")[0]) + '_j49970fa.txt'), "w")
	outputFile.write((str(t1) + ":" + str(t2)))
	outputFile.close()