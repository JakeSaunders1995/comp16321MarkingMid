import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input_dir", type=str)
parser.add_argument("output_dir", type=str)
args = parser.parse_args()

if args.input_dir[:-1] != "/":
	args.input_dir += "/"
	
if args.output_dir[:-1] != "/":
	args.output_dir += "/"


def calculate_scores(scores):
	points = {
		"t" : 5,
		"c" : 2,
		"p" : 3,
		"d" : 3
	}
			
	scores = scores.split("T")

	team_1_score = 0
	team_2_score = 0

	for score in scores:
		if len(score) == 2:
			if score[0] == "1":
				if score[1] in ["t","c","p","d"]:
					team_1_score += points.get(score[1])
			elif score[0] == "2":
				if score[1] in ["t","c","p","d"]:
					team_2_score += points.get(score[1])
			
	output = str(team_1_score) + ":" + str(team_2_score)
	
	return output


if not os.path.isdir(args.output_dir):
	os.makedirs(args.output_dir)

file_list = os.listdir(args.input_dir)

for x in file_list:
	if x[-4:] == ".txt":
		with open(args.input_dir + x) as f:
			result = calculate_scores(f.read().replace("\n",""))
			with open(args.output_dir + x[:-4] + "_y99614zh.txt", "w") as g:
				g.write(result)



