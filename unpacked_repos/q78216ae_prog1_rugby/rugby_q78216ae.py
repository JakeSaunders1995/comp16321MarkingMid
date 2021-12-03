import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('inputfile')
parser.add_argument('outputfile')
args = parser.parse_args()

filepath = args.inputfile
outfilepath = args.outputfile


for file in os.listdir(filepath):
	with open(filepath + "/" + file) as f:
		inp=f.readlines()

	count = 2
	T1 = 0
	T2 = 0

	while (count) < len(inp[0]):
		if inp[0][count] == "t":
			if inp[0][count-1] == "1":
				T1 += 5
			else:
				T2 += 5
		elif inp[0][count] == "c":
			if inp[0][count-1] == "1":
				T1 += 2
			else:
				T2 += 2
		else:
			if inp[0][count-1] == "1":
				T1 += 3
			else:
				T2 += 3
		count += 3

	print("The score is " + str(T1) + ":" + str(T2))
	if T1 > T2:
		print("Team 1 wins")
	elif T1 < T2:
		print("Team 2 wins")
	else:
		print("It's a draw")

	newfilepath = outfilepath + "/" + file[:-4] + "_q78216ae.txt"
	print(newfilepath)
	file = open(newfilepath,'w')
	message = str(T1) + ":" + str(T2)
	file.write(message)
	file.close()
