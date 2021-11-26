import os
import argparse


def parse_scores(scores):
	scoring_map = {
		"t": 5,
		"c": 2,
		"p": 3,
		"d": 3
	}

	T1 = 0
	T2 = 0

	for i in range(0, len(scores), 3):
		if scores[i:i + 2] == "T1":
			T1 += scoring_map[scores[i + 2: i + 3]]
		else:
			T2 += scoring_map[scores[i + 2: i + 3]]

	return {
		"T1": T1,
		"T2": T2
	}


def main():
	parser = argparse.ArgumentParser()

	parser.add_argument("input")
	parser.add_argument("output")

	args = parser.parse_args()

	for f in os.listdir(args.input):
		input_file = open(os.path.join(args.input, f))
		scores = input_file.read()
		input_file.close()

		scores = parse_scores(scores)

		output_file = open(os.path.join(args.output, f"{os.path.splitext(f)[0]}_c48306ah.txt"), "w")
		output_file.write(f"{scores['T1']}:{scores['T2']}")
		output_file.close()

main()