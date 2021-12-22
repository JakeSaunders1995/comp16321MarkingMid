import os
import sys

i = sys.argv[1]
o = sys.argv[2]

ifile = open(i, "r")
ofile = open(o, "w")

inputfile = (ifile.read())



team1_score= 0
team2_score= 0

for j in range (len(inputfile)):
	if inputfile[j]=='1':
		if inputfile[j+1] == 't':
			team1_score = team1_score + 5
		elif inputfile[j+1] == 'c':
			team1_score = team1_score + 2
		elif inputfile[j+1] == 'p':
			team1_score = team1_score + 3
		elif inputfile[j+1] == 'd':
			team1_score = team1_score + 3
	if inputfile[j]=='2':
		if inputfile[j+1] == 't':
			team2_score = team2_score + 5
		elif inputfile[j+1] == 'c':
			team2_score = team2_score + 2
		elif inputfile[j+1] == 'p':
			team2_score = team2_score + 3
		elif inputfile[j+1] == 'd':
			team2_score = team2_score + 3

if team1_score>team2_score:
	print("Team 1 won.")
elif team1_score<team2_score:
	print("Team 2 won.")
else:
	print("It was a draw")

ofile.write (str(team1_score) + ":" + str(team2_score))
