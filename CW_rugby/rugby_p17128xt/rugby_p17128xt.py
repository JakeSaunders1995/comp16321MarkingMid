import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("dir", nargs = "+")
args = parser.parse_args()

a = os.listdir(args.dir[0])


for x in range (0,len(a)):
	b = args.dir[0] + "/" + a[x]

	team1score = 0
	team2score = 0

	scoring = open(b,"r")
	score = scoring.read()
	for y in range (len(score)):
		if score[y] == "t" and score[y-1] == str(1):
			team1score += 5
		if score[y] == "c" and score[y-1] == str(1):
			team1score += 2
		if score[y] == "p" and score[y-1] == str(1):
			team1score += 3
		if score[y] == "d" and score[y-1] == str(1):
			team1score += 3

		if score[y] == "t" and score[y-1] == str(2):
			team2score += 5
		if score[y] == "c" and score[y-1] == str(2):
			team2score += 2
		if score[y] == "p" and score[y-1] == str(2):
			team2score += 3
		if score[y] == "d" and score[y-1] == str(2):
			team2score += 3


	
	c = args.dir[1] + "/" + a[x]
	d = c.replace(".", "_p17128xt.")
	f = open(d,'w')
	result = str(team1score) + ":" + str(team2score)
	f.write(result)
	f.close