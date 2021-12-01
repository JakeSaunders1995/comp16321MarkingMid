import sys, os 
from pathlib import Path
import ntpath

inputfile = sys.argv[1] 
outputfile = sys.argv[2]

for in_entry in os.scandir(inputfile):
	file1 = open(in_entry.path, 'r')
	scores = file1.readline().strip()
	file1.close()

	T1Points = []
	T2Points = []
	vp = 1
	while vp < len(scores):
		if scores[vp] == "1":
			T1Points.append (scores[vp+1])
		elif scores[vp] == "2":
			T2Points.append (scores[vp+1])
		vp = vp + 3

	T1 = 0
	T2 = 0

	for s in T1Points:
		if s == "t":
			T1 = T1 + 5
		elif s =="c":
			T1 = T1 + 2
		elif s =="p":
			T1 = T1 + 3
		elif s =="d":
			T1 = T1 + 3

	for n in T2Points:
		if n == "t":
			T2 = T2 + 5
		elif n =="c":
			T2 = T2 + 2
		elif n =="p":
			T2 = T2 + 3
		elif n =="d":
			T2 = T2 + 3

	file2name = Path(in_entry).stem + "_n79777aa.txt"
	file2name = os.path.join(outputfile, file2name)
	outputfilefinal = open(file2name, 'w+')
	outputfilefinal.write(str(T1) + ":" + str(T2))
	outputfilefinal.close()