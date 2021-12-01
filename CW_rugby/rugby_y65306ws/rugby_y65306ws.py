import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()
inputFile = args.input
outputFile = args.output
file = open(inputFile, "r")
for line in file:
    score = line
teamOne = True
teamOneScore = 0
teamTwoScore = 0
for x in range(len(score)):
	add = 0
	if score[x] == "1":
		teamOne = True
	elif score[x] == "2":
		teamOne = False
	elif score[x] == "t":
		add = 5
	elif score[x] == "c":
		add = 2
	elif score[x] == "p":
		add = 3
	elif score[x] == "d":
		add = 3

	if teamOne == True:
		teamOneScore += add
	elif teamOne == False:
		teamTwoScore += add
score = (str(teamOneScore) + ":" + str(teamTwoScore))
file = open(outputFile, "w")
file.write(score)