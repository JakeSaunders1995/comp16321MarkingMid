import argparse
import os

obj = argparse.ArgumentParser()
obj.add_argument("input_folder", type=str, metavar='path')
obj.add_argument("output_folder", type=str, metavar='path')

args = obj.parse_args()



for filename in os.listdir(args.input_folder):
	
	new_file = args.input_folder + '/' + filename
	file = open(new_file, 'r')

	score_1 = []
	score_2 = []

	count_1 = 0
	count_2 = 0

	line = file.readline()

	file.close()

	for i in range(len(line)):
		if line[i] == '1':
			if line[i+1] == 't':
				count_1 += 5
			elif line[i+1] == 'c':
				count_1 += 2
			elif line[i+1] == 'p':
				count_1 += 3
			elif line[i+1] == 'd':
				count_1 += 3

		if line[i] == '2':
			if line[i+1] == 't':
				count_2 += 5
			elif line[i+1] == 'c':
				count_2 += 2
			elif line[i+1] == 'p':
				count_2 += 3
			elif line[i+1] == 'd':
				count_2 += 3


	result = str(count_1) + ':' + str(count_2)

	new_output_file = filename.replace('.', '_c01724bh.')
	new_file = args.output_folder + '/' + new_output_file

	file = open(new_file, 'w')
	file.write(result)
	file.close()