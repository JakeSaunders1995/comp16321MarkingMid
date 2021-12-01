import argparse, os
	
parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()

f_input = os.listdir(args.input)

for i in range(len(f_input)):
	
	with open (args.input + "/" + f_input[i], "r") as file:

		scores = file.readline()

	file.close()

	team1_score = 0
	team2_score = 0

	while scores != "":
		
		sub_score = scores[0:3]


		if sub_score[0:2] == "T1":

			if sub_score[2] == "t": team1_score += 5
			elif sub_score[2] == "c": team1_score += 2
			elif sub_score[2] == "p": team1_score += 3
			elif sub_score[2] == "d": team1_score += 3

		elif sub_score[0:2] == "T2":

			if sub_score[2] == "t": team2_score += 5
			elif sub_score[2] == "c": team2_score += 2
			elif sub_score[2] == "p": team2_score += 3
			elif sub_score[2] == "d": team2_score += 3

		scores = scores[3:]

	game_score = str(team1_score) + ":" + str(team2_score)

	f_output = f_input[i][:-4] + "_p23525lg.txt"

	with open (args.output + "/" + f_output, "w") as file:

		file.write(game_score)

	file.close()
