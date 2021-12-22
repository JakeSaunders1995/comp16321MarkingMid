import sys
import os
import os.path

input1 = sys.argv[1]
output1 = sys.argv[2]

for filename in os.listdir(input1):
	file = open(input1 + '/' + filename,'r')
	input = file.read()
	outputfname = filename[:-4]

	start = 0
	end = 0

	# print(input)

	Team1score=0
	Team2score=0
	while end < len(input):
		end = end + 3
		scoring = input[start:end]
		# print(scoring)
		if scoring == "T1t":
			Team1score += 5
		elif scoring == "T1c":
			Team1score += 2
		elif scoring == "T1p" or scoring == "T1d" :
			Team1score += 3
		elif scoring == "T2t":
			Team2score += 5
		elif scoring == "T2c": 
			Team2score += 2
		elif scoring == "T2p" or scoring == "T2d" :
			Team2score += 3
		start = end
		# print(Team1score)
		# print(Team2score)

	FinalScore = str(Team1score) + ':' + str(Team2score)

	path = output1 + '/' + filename[0:-4] + '_' + 'p37429am.txt'
	with open(path, 'w+') as output:	
		output.write(FinalScore)


# /home/csimage/Documents/PythonStuff/COMP16321-Labs_p37429am/Program1/inputs
#/home/csimage/Documents/PythonStuff/COMP16321-Labs_p37429am/Program1/outputfolder