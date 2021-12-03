import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("inPath", type=str)
parser.add_argument("outPath", type=str)
args = parser.parse_args()

#Calculates the score total given a list of scores
def calcTotal(scoreList):
	outTotal = 0
	for i in scoreList:
		if(i=="t"):
			outTotal += 5
		elif(i=="c"):
			outTotal += 2
		elif((i=="p") or (i=="d")):
			outTotal += 3
	return outTotal

def scoreCount(inText):
	team1 = []
	team2 = []
	for i in range(len(inText)):
		if(inText[i]=="1"):
			team1.append(inText[i+1])
		elif(inText[i]=="2"):
			team2.append(inText[i+1])
	t1total = calcTotal(team1)
	t2total = calcTotal(team2)
	return (str(t1total) + ":" + str(t2total))

def main():
    files =	os.listdir(args.inPath)
    for i in files:
    	file1 = open(args.inPath + i, "r")
    	inText = file1.read()
    	file1.close()

    	outText = scoreCount(inText)
    	fileName = i.split(".")[0] + "_z83313gg.txt"
    	file2 = open(args.outPath + fileName, "w")
    	file2.write(outText)
    	file2.close()

main()