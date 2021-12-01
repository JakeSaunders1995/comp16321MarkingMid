import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input_path")
parser.add_argument("output_path")
args = parser.parse_args()

for file in os.listdir(args.input_path):
	input_destination = args.input_path + "/" + file
	input_file = open(input_destination)
	input = input_file.read()
	input_file.close()

	current_team = ""
	team1_score = 0
	team2_score = 0
	for i in range(0, len(input)):
		score = 0
		if input[i] == "T":
			current_team = input[i+1]
			if input[i+2] == "t":
				score = 5
			elif input[i+2] == "c":
				score = 2
			elif input[i+2] == "p" or input[i+2] == "d":
				score = 3
			if current_team == "1":
				team1_score += score
			elif current_team == "2":
				team2_score += score

	output_destination = args.output_path + "/" + file[0:-4] + "_u38012ek.txt"
	output_file = open(output_destination, "w")
	output_file.write("%s:%s" % (team1_score, team2_score))
	output_file.close()



