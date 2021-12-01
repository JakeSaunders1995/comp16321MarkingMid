import sys
import os
folder  = os.listdir(sys.argv[1])
base= os.getcwd()
for file in folder:
	os.chdir(sys.argv[1])
	with open(file, 'r') as f:
		contents = f.read()
	team1=0
	team2=0
	x = 1
	while x < len(contents):
		score=0
		if contents[x+1]=='t':
			score=5
		elif contents[x+1]=='c':
			score=2
		elif contents[x+1]=='p':
			score=3
		elif contents[x+1]=='d':
			score=3
		if contents[x]=='1':
			team1 += score
		elif contents[x]=='2':
			team2 += score
		x += 3
	new_file = sys.argv[2] + "/" + file[:-4] +"_w65214ka.txt"
	os.chdir(base)
	text_file = open(new_file, 'w')
	text_file.write(str(team1) + ":" + str(team2))
	text_file.close()