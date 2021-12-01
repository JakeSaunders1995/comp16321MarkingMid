import sys, os
from pathlib import Path
import ntpath

InFile = sys.argv[1]
OutFile = sys.argv[2]

for in_entry in os.scandir(InFile):
	FileIn = open(in_entry,"r")
	result = FileIn.readline().strip()
	FileIn.close()

	Team1scores = []
	Team2scores = []

	x = 0
	T1 = 0
	T2 = 0

	while x < len(result):
		if result[x+1] == "1":
			Team1scores.append(result[x+2])
		elif result[x+1] == "2":
			Team2scores.append(result[x+2])
		x += 3

	for a in Team1scores:
		if a == "t":
			T1 = T1 + 5
		elif a == "c":
			T1 = T1 + 2
		elif a == "p":
			T1 = T1 + 3
		elif a == "d":
			T1 = T1 + 3

	for b in Team2scores:
		if b == "t":
			T2 = T2 + 5 
		elif b == "c":
			T2 = T2 + 2
		elif b == "p":
			T2 = T2 + 3
		elif b == "d":
			T2 = T2 + 3

	File2 = Path(in_entry).stem + "_x43881he.txt"
	File2 = os.path.join(OutFile, File2)
	FileOut = open(File2, 'w+')
	FileOut.write(str(T1) + ":" + str(T2))
	FileOut.close()
