import os, argparse


def getUserInput():
	parser = argparse.ArgumentParser()
	parser.add_argument('input_folder', type=str)
	parser.add_argument('output_folder', type=str)
	args = parser.parse_args()

	if not os.path.exists(args.output_folder):
	    os.makedirs(args.output_folder)

	return args.input_folder, args.output_folder


def calculateScores(input_string):
	score1, score2 = 0, 0
	for i in range(0, len(input_string), 3):
		s = input_string[i:i+3]
		team = s[1]
		typ = s[2]
		if team == "1":
			score1 += points_dict[typ]
		else:
			score2 += points_dict[typ]

	return str(score1) + ":" + str(score2)


points_dict = {"t": 5, "c": 2, "p": 3, "d": 3}
input_folder, output_folder = getUserInput()
filenames = os.listdir(input_folder)
for file in filenames:
	try:
		if not file.endswith(".txt"):
			continue
		with open(input_folder + "/" + file, "r") as f:
			input_string = f.read()
		out = calculateScores(input_string)
	except Exception as e:
		out = ""
		print(repr(e))

	output_location = output_folder + "/" + file[:-4] + "_d50341jc.txt"
	with open(output_location, "w") as f:
		f.write(out)
