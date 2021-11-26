import sys
import os

def add_points_func(score, score_type):
	score += score_types[score_type]
	return score


score_types = {"t": 5, "c": 2, "p": 3, "d": 3}

in_directory = sys.argv[1]
files = os.listdir(in_directory)
for file in files:
	input_path = os.path.join(in_directory, file)
	input_file = open(input_path)
	scores = input_file.read()
	input_file.close()

	score_t1 = 0
	score_t2 = 0

	for i in range(0, len(scores), 3):
		game = scores[i:i+3]
		if game[1] == "1":
			score_t1 = add_points_func(score_t1, game[2])
		else:
			score_t2 = add_points_func(score_t2, game[2])

	if score_t1 > score_t2:
		status = "T1 is the winner"
	elif score_t2 > score_t1:
		status = "T2 is the winner"
	else:
		status = "It's a draw"

	out_directory = sys.argv[2]
	index = file.find(".txt")
	output_path = os.path.join(out_directory, file[:index] + "_b63095jv" + file[index:])
	output_file = open(output_path, "w")
	output_file.write(str(score_t1) + ":" + str(score_t2))
	output_file.close()





