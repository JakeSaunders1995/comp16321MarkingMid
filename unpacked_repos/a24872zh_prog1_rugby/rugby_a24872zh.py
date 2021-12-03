import argparse, os

def split_string(input_file):
	scores = open(input_file, "r")
	scores_as_string = scores.read()
	split = scores_as_string.split("T")
	split.pop(0)
	scores.close()
	return calculate_scores(split)

def calculate_scores(split):
	team1 = 0
	team2 = 0
	for item in split:
		if item[1] == "t":
			if item[0] == "1":
				team1 += 5
			else:
				team2 += 5
		elif item[1] == "c":
			if item[0] == "1":
				team1 += 2
			else:
				team2 += 2
		elif item[1] == "p":
			if item[0] == "1":
				team1 += 3
			else:
				team2 += 3
		elif item[1] == "d":
			if item[0] == "1":
				team1 += 3
			else:
				team2 += 3
	result = [team1, team2]
	return result

def output_results(score, output_path, input_name):
	toPrint = (str(score[0]) + ":" + str(score[1]))
	nameOfOutput = input_name[:-4]
	nameOfOutput += "_a24872zh.txt"
	output_to = open(output_path + "/" + nameOfOutput, "w")
	output_to.write(toPrint)
	output_to.close()

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()

input_path = args.input_file
output_path = args.output_file
listOfTextFiles = os.listdir(input_path)
listToOutput = []

for item in listOfTextFiles:
	listToOutput.append(split_string(input_path + "/" + item))

for i in range(len(listToOutput)):
	output_results(listToOutput[i], output_path, listOfTextFiles[i])





