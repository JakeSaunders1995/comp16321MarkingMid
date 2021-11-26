import argparse, os
parser = argparse.ArgumentParser()
parser.add_argument("a1", help="input file path")
parser.add_argument("a2", help="output file path")
args = parser.parse_args()
files = []
for file in os.listdir(args.a1):
	if file.endswith(".txt"):
		files.append(file)
for y in range (len(files)):
	f = open(files[y], "r")
	line = f.readline()
	f.close()
	T1Score = 0
	T2Score = 0
	for x in range(1,len(line),3):
		if line[x] == "1":
			if line[x+1] == "t":
				T1Score += 5
			elif line[x+1] == "c":
				T1Score += 2
			elif line[x+1] == "p":
				T1Score += 3
			elif line[x+1] == "d":
				T1Score += 3
		elif line[x] == "2":
			if line[x+1] == "t":
				T2Score += 5
			if line[x+1] == "c":
				T2Score += 2
			if line[x+1] == "p":
				T2Score += 3
			if line[x+1] == "d":
				T2Score += 3

	noExt = files[y][:-4]

	f = open(str(args.a2) + "/" + noExt + "_t92001cr.txt" , "w")
	f.write(str(T1Score) + ":" + str(T2Score))
	f.close()
