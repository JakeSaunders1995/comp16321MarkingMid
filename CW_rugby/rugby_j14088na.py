import argparse, re, os

def defArguments():
	global args
	ap = argparse.ArgumentParser()
	ap.add_argument("inputFolder", help="input folder")
	ap.add_argument("outputFolder", help="out folder")
	args = ap.parse_args()
def GenerateFileList():
	fileList=[]
	for file in os.listdir(args.inputFolder):
	    if file.endswith(".txt"): 
	         fileList.append(os.path.join(args.inputFolder, file))
	return fileList
def accessFile(f):
	inFile  = open(f)
	txt = inFile.read().strip()
	inFile.close()
	return txt
def generateOutput(f):
	t1raw =reduce(f, "T1")
	t2raw =reduce(f, "T2")
	t1score = calculatePoints(t1raw)
	t2score = calculatePoints(t2raw)
	return "%s:%s" % (t1score, t2score)
def reduce(f,team):
	txt = accessFile(f)
	scoreList = re.findall(team + ".", txt)
	for i in range(len(scoreList)):
		scoreList[i] = scoreList[i][2]
	return scoreList
def calculatePoints(pointList):
	points= 0
	for i in pointList:
		if i == "t":
			points +=5
		elif i == "c":
			points +=2
		elif i == "p" or i == "d":
			points +=3
	return points
def writeOutput():
	if not os.path.exists(args.outputFolder):
		os.makedirs(args.outputFolder)
	for f in GenerateFileList():
		filename=re.sub((".+/"), "", f)
		filename=re.sub((".txt"), "_j14088na.txt", filename)
		outFile = open(os.path.join(args.outputFolder, filename), "w")
		outFile.write(generateOutput(f))
		outFile.close()
def determineWinners():
	for file in GenerateFileList():
		filename = re.sub(".txt", "", file)
		filename = re.sub(".+/", "", filename)
		txt = generateOutput(file)
		list= re.split(":", txt)
		if int(list[0]) > int(list[1]):
			print("Winner of %s is team 1" % filename)
		elif int(list[0]) < int(list[1]):
			print("Winner of %s is team 2" % filename)
		else:
			print("Match of %s is a draw" % filename)

defArguments()
writeOutput()
determineWinners()