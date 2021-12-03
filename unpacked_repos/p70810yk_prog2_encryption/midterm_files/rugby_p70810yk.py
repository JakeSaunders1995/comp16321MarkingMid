import sys
import os.path
import os
filenumber = ""
inputpath = sys.argv[1]
filelist = os.listdir(inputpath)
for file in filelist:
	for x in file:
		if x.isdigit():
			filenumber +=str(x)
	f = open(inputpath+"/"+file)
	scoreline = f.readline()
	f.close()

	Team1Score = 0
	Team2Score = 0


	for x in range(int(len(scoreline)/3)):
		score_type = scoreline[(3*x)+2]
		if scoreline[3*x+1] == "1":
			if score_type == "t":
				Team1Score +=5
			elif score_type == "c":
				Team1Score +=2
			elif score_type == "p":
				Team1Score +=3
			elif score_type == "d":
				Team1Score +=3  
		if scoreline[3*x+1] == "2":
			if score_type == "t":
				Team2Score +=5
			elif score_type == "c":
				Team2Score +=2
			elif score_type == "p":
				Team2Score +=3
			elif score_type == "d":
				Team2Score +=3

	outputpath = sys.argv[2]
	output = open(outputpath+"/"+"Output_File"+str(filenumber)+"_p70810yk.txt","x")
	output.write(str(Team1Score)+":"+str(Team2Score))
	filenumber = ""

