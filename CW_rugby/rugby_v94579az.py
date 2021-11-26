import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument("input", help = "input folder")
parser.add_argument("output", help = "output folder")
args = parser.parse_args()
files = os.listdir(str(args.input))


def PointsCalc(scoresheet):
	team1Points = 0
	team2Points = 0
	count = 0
	for y in scoresheet:
			if y == "T":
				Teamscorecard = sheet[count + 1 : count + 3]
				if (Teamscorecard == "1t"):
					team1Points += 5
				elif (Teamscorecard == "1c"):
					team1Points += 2
				elif (Teamscorecard == "1p"):
					team1Points += 3
				elif (Teamscorecard == "1d"):
					team1Points += 3

				elif (Teamscorecard == "2t"):
					team2Points += 5
				elif (Teamscorecard == "2c"):
					team2Points += 2
				elif (Teamscorecard == "2p"):
					team2Points += 3
				elif (Teamscorecard == "2d"):
					team2Points += 3


				count += 3

			else:
				pass

	with open(outputPath, 'w') as o:
		o.write(str(team1Points) + ":" + str(team2Points))

	if (team1Points > team2Points):
		print("Team 1 is the winner")
	elif (team1Points < team2Points):
		print("Team 2 is the winner")
	elif (team1Points == team2Points):
		print("It was a draw")



	


for x in files:
	path = str(args.input + "/" + x)
	outputPath = str(args.output + "/" + x[:10] + "_v94579az" + x[10:])
	with open(path, 'r') as f:
		sheet = str(f.readline())

		PointsCalc(sheet)

		
		
			
		




    

	



