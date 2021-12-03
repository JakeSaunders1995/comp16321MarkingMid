import re
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("echo")
parser.add_argument("output")
args = parser.parse_args()
directory_in = args.echo
directory_out = args.output


for file in os.listdir(directory_in):
	T1 = 0
	T2 = 0
	x = os.path.join(directory_in, file)
	f = open(x)
	lines = f.read()
	char = len(lines)
	for i in range(char):
		if lines[i] == "1":
			if lines[i+1] == 't':
				T1 += 5
			elif lines[i+1] == 'c':
				T1 += 2
			elif lines[i+1] == 'p':
				T1 += 3
			elif lines[i+1] == 'd':
				T1 += 3
		elif lines[i] == "2":
			if lines[i+1] == 't':
				T2 += 5
			elif lines[i+1] == 'c':
				T2 += 2
			elif lines[i+1] == 'p':
				T2 += 3
			elif lines[i+1] == 'd':
				T2 += 3
	

	file_name = re.split('.txt', file)
	file_out_name = file_name[0]
	file_out_path = directory_out + "/" + file_out_name + "_" + "v14799cc.txt"
	g = open(file_out_path, "w")
	g.write(str(T1) + ":" + str(T2))

	




	


	
