import argparse
import os

arg_parser = argparse.ArgumentParser(description="Rugby Score Program")
arg_parser.add_argument('input_folder')
arg_parser.add_argument('output_folder')
args = arg_parser.parse_args()


scoring = {
	't': 5,
	'c': 2,
	'p': 3,
	'd': 3
}

for file_path in os.listdir(args.input_folder):
	t1_score = 0
	t2_score = 0

	with open(args.input_folder + "/" + file_path, "r") as file:
		contents = file.read()

		i = 0

		while i < len(contents):
			if contents[i] == 'T':
				if contents[i+1] == '1':
					t1_score += scoring[contents[i+2]]
				elif contents[i+1] == '2':
					t2_score += scoring[contents[i+2]]
				i += 3

		output_file = file_path.split('.')[0] # get name of file without extension

	output_file += "_h96407tf.txt"
	with open(args.output_folder + "/" + output_file, "w") as file:
		file.write(f"{t1_score}:{t2_score}")