import sys 
import os


dirIn	 = sys.argv[1]
dirOut   = sys.argv[2]

for filename in os.listdir(dirIn):
	f = os.path.join(dirIn, filename)
	if os.path.isfile(f):
		file_in = open(f)
		data	= file_in.read()

		scoreT1  = 0
		scoreT2  = 0

		finalT1score = 0
		finalT2score = 0

		x = len(data)
		i = 0


		for i in range(0,x):
			if data[i] == "1":
				scoretype = data[i + 1]
				if scoretype == "t":
					scoreT1 = scoreT1 + 5
				elif scoretype == "c":
					scoreT1 = scoreT1 + 2
				elif scoretype == "p":
					scoreT1 = scoreT1 + 3
				else:
					scoreT1 = scoreT1 + 3
			elif data[i] == "2":
				scoretype = data[i + 1]
				if scoretype == "t":
					scoreT2 = scoreT2 + 5
				elif scoretype == "c":
					scoreT2 = scoreT2 + 2
				elif scoretype == "p":
					scoreT2 = scoreT2 + 3
				else:
					scoreT2 = scoreT2 + 3
				
			

		finalT1score = finalT1score + scoreT1
		finalT2score = finalT2score + scoreT2

		# if finalT1score == finalT2score:
		# 	print("This match results in a draw.")
		# elif finalT1score > finalT2score:
		# 	print("T1 has won this match!")
		# else:
		# 	print("T2 has won this match!")

		output = str(finalT1score) + str(":") + str(finalT2score)
		#print(output)


		outFileName = filename[:-4] + "_p91607ma.txt"
		pathToFile = os.path.join(dirOut, outFileName)
		outFile = open(pathToFile, "a")
		outFile.write(output)
	






