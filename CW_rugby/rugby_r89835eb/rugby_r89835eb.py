import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_path")
parser.add_argument("output_path")

p = parser.parse_args()
# print(p.input_path)
# print(p.output_path)

import os


def get_score(char):
	if char == "t":
		return 5
	elif char == "c":
		return 2
	elif char == "p":
		return 3
	else:
		return 3

for index, filename in enumerate(os.listdir(p.input_path)):
	if filename.endswith(".txt"):
		input = open(os.path.join(p.input_path, filename), "r")
		team_1_score = 0
		team_2_score = 0

		scores = input.readline()

		for team in range(1,len(scores),3):
			if scores[team] == "1":
				team_1_score += get_score(scores[team+1])
			else:
				team_2_score += get_score(scores[team+1])

		output = open(os.path.join(p.output_path, "test_file{}_r89835eb.txt".format(os.path.join(p.input_path, filename)[-5])), "w")
		output.write("{}:{}".format(team_1_score, team_2_score))
		input.close()
		output.close()
				

	else:
		pass 
		




