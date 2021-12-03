import os

import sys
inputf = sys.argv[1]
outputf = sys.argv[2]
def score(type):
	if type == "t":
		return 5
	elif type == "c":
		return 2
	elif type == "p":
		return 3
	elif type == "d":
		return 3
for x in os.listdir(inputf):
   team1 = 0
   team2 = 0
   f = os.path.join(inputf,x)
   text = open(f)
   line = text.readline()
   filename = os.path.basename(x)
   seperate = [line[i:i+3] for i in range(0, len(line), 3)]
   
   for i in seperate:
   	if i[1] == "1":
   		team1+= score(i[2])
   	elif i[1] == "2":
   		team2+= score(i[2])
   ratio = str(team1) + ":"+str(team2)
   if (team1 > team2):
   	print("Team 1 has won in " + filename)
   elif (team2>team1):
   	print("Team 2 has won in " + filename)
   else:
   	print("The teams have tied in "+filename)
   filename = filename.replace(".txt","")
   outputname = outputf + "/" + filename+"_y72828ah.txt"
   outputfile = open(outputname, "w")
   outputfile.write(ratio)
   outputfile.close()

   

