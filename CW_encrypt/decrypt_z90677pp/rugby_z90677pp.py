#create function to find the scores of given file
def findScores(txtFile):
	#read from score file
	with open(txtFile, 'r') as scoreFile:
		scores = scoreFile.read()
		scoreFile.close()

	#seperate scores and put into array
	scoreList = []
	i = 0
	while i < (len(scores)-1):
		currentScore = scores[i] + scores[i+1] + scores[i+2]
		scoreList.append(currentScore)
		i = i+3

	#add points to team totals
	total1 = 0
	total2 = 0
	for i in scoreList:
		if i[1] == '1':
			if i[2] == 't':
				total1 += 5
			elif i[2] == 'c':
				total1 += 2
			elif i[2] == 'p':
				total1 += 3
			elif i[2] == 'd':
				total1 += 3
			else:
				print('there is an input that the program does not understand. please ensure scores are of the type: t, c, p or d')
				sys.exit()
		elif i[1] == '2':
			if i[2] == 't':
				total2 += 5
			elif i[2] == 'c':
				total2 += 2
			elif i[2] == 'p':
				total2 += 3
			elif i[2] == 'd':
				total2 += 3
			else:
				print('there is an input that the program does not understand. please ensure scores are of the type: t, c, p or d')
				sys.exit()
		else:
			print('there is an input that the program does not understand. please ensure there are only teams 1 and 2')
			sys.exit()

	#concatonate scores into correct format for output
	outputScores = str(total1) + ':' + str(total2)

	return(outputScores)


#main program
import os, sys, shutil
inFolder = sys.argv[1]
outFolder = sys.argv[2]
#seperate input folder into list of .txt files
with os.scandir(inFolder) as files:
    for file in files:
    	length = len(file.name)
    	#for each .txt file run function to find scores
    	if file.name[(length-3) : (length)] == 'txt':
    	 	scores = findScores(file)
    	 	#write scores to a new file
    	 	newFile = file.name[0 : (length-4)] + '_z90677pp.txt'
    	 	with open(newFile, 'w') as f:
    	 		f.write(scores)
    	 		f.close()
    	 	#move file to output folder
    	 	shutil.move(newFile, outFolder)