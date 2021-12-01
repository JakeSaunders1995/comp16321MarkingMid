import argparse, os

parser = argparse.ArgumentParser(description='Calculate rugby score')
parser.add_argument('input', help='Input file path')
parser.add_argument('output', help='Output file path')
args = parser.parse_args()

scoreDict = {'t':5, 'c':2, 'p':3, 'd':3}

for file in os.listdir(str(args.input)):

	team1Score = 0
	team2Score = 0

	if file.endswith(".txt"):
		inputFile = open(os.path.join(args.input, file))
	else:
		continue

	scoreString = inputFile.readline()

	while len(scoreString) > 0:
		if scoreString[0:2] == 'T1':
			team1Score += scoreDict[scoreString[2]]
		else:
			team2Score += scoreDict[scoreString[2]]
		scoreString = scoreString[3:]

	print(team1Score, ':', team2Score)

	if team1Score > team2Score:
		print("Team 1 wins")
	elif team2Score > team1Score:
		print("Team 2 wins")
	else:
		print("It's a draw")

	outputFile = open(os.path.join(args.output, file[0:-4] + '_m32784sh.txt'), 'x')
	outputFile.write(str(team1Score) + ':' + str(team2Score))