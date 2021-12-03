import os
import argparse

def commandSystem(state):
	parser = argparse.ArgumentParser(description='Path of the Input and Output')
	parser.add_argument('inputFolder', type=str, help='Input Folder Path')
	parser.add_argument('outputFolder', type=str, help='Output Folder Path')
	args = parser.parse_args()

	folderIput = args.inputFolder
	dirsIput = os.listdir(folderIput)
	
	if state == 1:
		for file1 in dirsIput:	
			filePath = os.path.join(folderIput, file1)
			fileCotent = open(filePath, "rt")
			content = fileCotent.read()
			fileCotent.close()
			content_lis.append(content)
		return content_lis

	if state == 0:
		folderOput = args.outputFolder
		for file1 in dirsIput:
			file2 = file1[:-4] + "_c29824zl.txt"
			outputPath = os.path.join(folderOput, file2)
			path_lis.append(outputPath)
		return path_lis



def scoreSystem():
	if inputCotent[i+1] == "t":
		score = 5
	elif inputCotent[i+1] == "c": 
		score = 2
	elif inputCotent[i+1] == "p": 
		score = 3
	elif inputCotent[i+1] == "d": 
		score = 3
	theScore = score
	return theScore

def compareSystem():
	winner = ()
	if (T1 != T2):
		if (T1 > T2):
			winner = "T1"
		else:
			winner = "T2"
		print(winner + " is the winner!")
	else:
		print("Two teams draw.")


count = 0
content_lis = []
path_lis = []
commandSystem(1)
commandSystem(0)
while count < len(content_lis):
	inputCotent = content_lis[count]
	print (inputCotent)
	i = 1
	T1 = 0
	T2 = 0
	while i < (len(inputCotent) - 1):
		if inputCotent[i] == "1":		
			theScore = scoreSystem()
			T1 += theScore
			#print ("Team1 has scored " + str(T1))
		else:
			theScore = scoreSystem()
			T2 += theScore
			#print ("Team2 has scored " + str(T2))
		i += 3
	compareSystem()
	f = open(path_lis[count], "w")
	f.write(str(T1) + ":" + str(T2))
	f.close()
	count += 1


