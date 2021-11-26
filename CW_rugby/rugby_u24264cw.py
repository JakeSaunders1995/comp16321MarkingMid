import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("inputfolderpath")
parser.add_argument("outputfolderpath")

args = parser.parse_args()

#creating list to store input file paths
inputfilelist = []
for filename in os.scandir(args.inputfolderpath):
	if filename.path.endswith(".txt") and filename.is_file():
		inputfilelist.append(filename.path)

for files in inputfilelist:
	inputfile = open(files)
	scores = inputfile.read()

	inputlist = []

	i=0
	j=3

	t1score = 0
	t2score = 0

	for char in scores:
		inputlist.append(scores[i:j])
		i += 3
		j += 3

	for elements in inputlist:
		if elements[0:2] == "T1":
			if elements[2:3] == "t":
				t1score += 5
			elif elements[2:3] == "c":
				t1score += 2
			elif elements[2:3] == "p":
				t1score += 3
			elif elements[2:3] == "d":
				t1score += 3

		elif elements[0:2] == "T2":
			if elements[2:3] == "t":
				t2score += 5
			elif elements[2:3] == "c":
				t2score += 2
			elif elements[2:3] == "p":
				t2score += 3
			elif elements[2:3] == "d":
				t2score += 3

	print(t1score)
	print(t2score)

	if t1score > t2score:
		print("Team 1 is the winner!")
	elif t2score > t1score:
		print("Team 2 is the winner!")
	else:
		print("Result is a Draw.")

	finalscore = str(t1score) + ":" + str(t2score)

	#creating complete output file path 
	inputfilename = os.path.basename(files)
	outputfilename = inputfilename[0:(len(inputfilename)-4)] + '_u24264cw'
	completefilepath = os.path.join(args.outputfolderpath, outputfilename + ".txt")

	outputfile = open(completefilepath, "w")

	outputfile.write(finalscore)

	outputfile.close()
inputfile.close()