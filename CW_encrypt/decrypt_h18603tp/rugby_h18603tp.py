import argparse	
import os



parser = argparse.ArgumentParser()
parser.add_argument("first")
parser.add_argument("last")
args = parser.parse_args()

files = os.scandir(args.first) 

if not os.path.isdir(args.last):
	os.mkdir(args.last)


for element in files:

	with open(element.path, 'r') as myfile:
	    list1 = myfile.read()

	
	T1 = 0
	T2 = 0

	x = 3
	list2 = [list1[i:i+x] for i in range(0, len(list1), x)]
	
	if list2[-1] == "\n":
		del list2[-1]

	for x in list2:
		if x[1:3] == "1t":
			T1 += 5
		elif x[1:3] == "1c":
			T1 += 2
		elif x[1:3] == "1p":
			T1 += 3
		elif x[1:3] == "1d":
			T1 += 3
		elif x[1:3] == "2t":
			T2 += 5
		elif x[1:3] == "2c":
			T2 += 2
		elif x[1:3] == "2p":
			T2 += 3
		elif x[1:3] == "2d":
			T2 += 3

	output_name = element.name.split(".")[0]
	output_name = output_name + "_h18603tp.txt"

	os.path.join(args.last, output_name)
	with open(os.path.join(args.last, output_name), 'w+') as myfile:
		myfile.write(str(T1) + ":" + str(T2))
	   