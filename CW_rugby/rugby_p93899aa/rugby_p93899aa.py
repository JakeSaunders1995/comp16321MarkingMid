import sys
import os

if (len(sys.argv) != 3):
	print("check the number of arguments\nprogram will exit")
	sys.exit(0)


for file in os.listdir(sys.argv[1]):
	file = sys.argv[1] +"/"+ file
#	print(file)
	counter = file[-5]
	fileIn = open(file)
	line = fileIn.read()

	T1 = 0
	T2 = 0
	i = 0
	points = 0

	while (i < len(line)):

		# determine the points for each letter
		if (line[i+2] == 't'):
			points = 5
		elif (line[i+2] == 'c'):
			points = 2
		else:
			points = 3

		# giving the scores to the team
		if (line[i+1] == '1'):
			T1 += points
		else:
			T2 += points

		i += 3

	results = str(T1) + ":" + str(T2)
	fileOutPath = sys.argv[2] + "/test_file" + str(counter) + "_p93899aa.txt"
	#print(fileOutPath)
	fileOut = open(fileOutPath,'w')
	fileOut.write(results)