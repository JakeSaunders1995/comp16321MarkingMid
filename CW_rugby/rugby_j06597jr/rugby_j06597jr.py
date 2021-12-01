import re, os, argparse

def readfile(path):
	with open(path, "r", encoding="utf-8-sig") as f:
		scores = f.read()
		f.close()
	return scores

def writefile(path):
		with open(path, "w", encoding="utf-8-sig") as f:
			result = f.write(str(T1) + ":" + str(T2))
			f.close()
		return result

parser = argparse.ArgumentParser(description="input and output files for testing rugby scores")
parser.add_argument("input", type=str, help="input file folder")
parser.add_argument("output", type=str, help="output file folder")
args = parser.parse_args()
inputFolder = args.input
outputFolder = args.output
inputFiles = os.listdir(inputFolder)
inputPath = os.listdir(inputFolder)
os.chdir(inputFolder)

for y in range(0,len(inputFiles)):
	inputFiles[y] = inputFiles[y][:-4]

count = 0
for z in range(0,len(inputPath)):
	os.chdir(inputFolder)
	inputPath[z] = inputFolder+"/"+inputPath[z]
	scores = readfile(inputPath[z])
	T1 = 0
	T2 = 0


	matchT1 = re.findall(r"T1[tcpd]", scores)
	for x in matchT1:
		if x == "T1t":
			T1 += 5
		elif x == "T1c":
			T1 += 2
		elif x == "T1p":
			T1 += 3
		elif x == "T1d":
			T1 += 3


	matchT2 = re.findall(r"T2[tcpd]", scores)
	for x in matchT2:
		if x == "T2t":
			T2 += 5
		elif x == "T2c":
			T2 += 2
		elif x == "T2p":
			T2 += 3
		elif x == "T2d":
			T2 += 3

	os.chdir(outputFolder)
	outputPath = outputFolder +"/" + inputFiles[count]+"_j06597jr.txt"
	count += 1
	result = writefile(outputPath)




	
