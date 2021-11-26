import sys 
import os
inputpath = sys.argv[1]
outputpath = sys.argv[2]
ipathfile = open(inputpath,"r")
opathfile = open(outputpath, "w")

inputfile = (ipathfile.read())

team1 = 0
team2 = 0
for x in range (len(inputfile)):
	if inputfile[x] == '1':
		if inputfile[x+1] == 't':
			team1= team1 + 5
		elif inputfile[x+1] == 'c':
			team1= team1 + 2
		elif inputfile[x+1] == 'p':
			team1= team1 + 3
		elif inputfile[x+1] == 'd':
			team1= team1+ 3
	if inputfile[x]  == '2':
		if inputfile[x+1] == 't':
			team2= team2 + 5
		elif inputfile[x+1] == 'c':
			team2= team2+ 2
		elif inputfile[x+1] == 'p':
			team2 = team2 + 3
		elif inputfile[x+1] == 'd':
			team2 = team2 + 3

opathfile.write(str(team1) + ":" + str(team2))

