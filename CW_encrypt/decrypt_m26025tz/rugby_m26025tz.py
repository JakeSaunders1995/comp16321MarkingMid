import sys
import os

input_folder = sys.argv[1]
output_folder = sys.argv[2]
input_files = os.listdir(input_folder)
for input_file in input_files:
	position = input_folder +"//" + input_file

	T1score = 0
	T2score = 0

	with open(position) as f:
		contents = f.read()
	def score(y, x):
		if y == 't': x += 5
		elif y == 'c': x += 2
		elif y == 'p': x += 3
		elif y == 'd': x += 3
		return x
	for i in range(len(contents)):

		if contents[i] == '1':
			T1score = score(contents[i + 1], T1score )			
		elif contents[i] == '2':
			T2score = score(contents[i + 1], T2score)

	output = (str(T1score) + ":" + str(T2score))
	output_file = output_folder + "//" + input_file[:-4] +"_m26025tz.txt"
	with open(output_file, "w") as f:
		f.write(output)