import sys, os

def checkScore(goal):
	if goal == 't':
		return 5
	elif goal == 'c':
		return 2
	elif goal == 'p' or goal == 'd':
		return 3


cwd = os.getcwd()
os.chdir(sys.argv[1])

outputList = []

for file in os.listdir():
	inputFile = open(file, 'r')
	line = inputFile.read()

	scores = []
	for a in range(len(line)):
		if line[a] == 'T':
			scores.append(str(line[a] + line[a+1] + line[a+2]))

	inputFile.close()

	t1Score, t2Score = 0, 0

	for element in scores:
		if element[1] == '1':
			t1Score += checkScore(element[2])
		elif element[1] == '2':
			t2Score += checkScore(element[2])

	outputList.append([(file.split('.'))[0], t1Score, t2Score])

os.chdir(cwd)

outputDirectory = sys.argv[2]
os.mkdir(outputDirectory)
os.chdir(outputDirectory)

for element in outputList:
	newFile = open(element[0] + '_b95211hc.txt', 'w')
	newFile.write(str(element[1]) + ':' + str(element[2]))
	newFile.close()