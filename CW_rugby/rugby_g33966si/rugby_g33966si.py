import sys
import os

inFolder = sys.argv[1]
outFolder = sys.argv[2]  

team1 = 0
team2 = 0

for inFile in os.scandir(inFolder):

	fileName = inFile.name

	with open (inFile) as file:
		scores = file.read()
		scores2 = scores.split("T")
		
		
		x = 1
		while x < len(scores2):
			
			i = scores2[x]


			if (i[0] == "1"):
				if (i[1] == "t"):
					team1 += 5
				elif (i[1] == "c"):
					team1 += 2
				elif (i[1] == "p"):
					team1 += 3
				elif (i[1] == "d"):
					team1 += 3
				else:
					pass

			elif (i[0] == "2"):
				if (i[1] == "t"):
					team2 += 5
				elif (i[1] == "c"):
					team2 += 2
				elif (i[1] == "p"):
					team2 += 3
				elif (i[1] == "d"):
					team2 += 3
				else:
					pass

			else:
				pass

			
			x = x + 1
			
	
	if team1 > team2:
		winner = "The winner is Team1"

	elif team1 < team2:
		winner = "The winner is Team2"

	else:
		winner = "Draw"


	outFile = fileName.replace(".txt", "_g33966si.txt")
	completeName = os.path.join(outFolder, outFile)
	fileX = open(completeName, "w")
	fileX.write( str(team1) + ":" + str(team2))
	fileX.close()

	team1 = 0
	team2 = 0
	










