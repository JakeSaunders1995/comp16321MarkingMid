import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()

def count_score():
	scoreType = x[teamNumber + 1]
	if scoreType == "t":
		return 5
	elif scoreType == "c":
		return 2
	elif scoreType == "p":
		return 3
	elif scoreType == "d":
		return 3


for file in os.listdir(args.input):
	readInput = open(os.path.join(args.input, file))
	x = readInput.read()
	T1Score = 0
	T2Score = 0
	for teamNumber in range(1, len(x), 3):
		if x[teamNumber] == str(1):
			T1Score = T1Score + count_score()
		elif x[teamNumber] == str(2):
			T2Score = T2Score + count_score()
	newFileName = str(file[0:len(file)-4]) + "_w21706bc.txt"
	writeOutput = open(os.path.join(args.output, newFileName), "w")
	content = str(T1Score) + ":" + str(T2Score)
	writeOutput.write(content)