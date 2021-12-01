import sys
inputfile = sys.argv[1]
outputfile= sys.argv[2]

def getScore():
	file = open(inputfile)
	score = file.readline()
	file.close()
	return score

def calc_score(points):
	score = 0
	for i in range(0,len(points)):
		if points[i] ==  't':
			score +=5
		elif points[i] == 'c':
			score +=2
		else:
			score+=3

	return score

def output_score(ouput):
	file = open(outputfile,"a")
	file.write(output + "\n")


scoreline = getScore()
scoreline = scoreline.replace("T","")


team1_points = []
team2_points = []

for i in range (0, len(scoreline)-1):
	if scoreline[i] == "1":
		team1_points.append(scoreline[i+1])
	elif scoreline[i] =="2":
		team2_points.append(scoreline[i+1])


team1_score = calc_score(team1_points)
team2_score = calc_score(team2_points)
output = f"{team1_score}:{team2_score}"
print(output)
output_score(output)