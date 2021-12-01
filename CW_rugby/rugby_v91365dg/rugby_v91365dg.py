import os
import sys

for File in os.listdir(sys.argv[1]):
	InputFile=open(os.path.join(sys.argv[1],File),"r")
	Scores=InputFile.read()
	Team1Score=0
	Team2Score=0
	for i in range(0,len(Scores),3):
		Score=0
		if(Scores[i+2]=="t"):
			Score=5
		elif(Scores[i+2]=="c"):
			Score=2
		elif(Scores[i+2]=="p"):
			Score=3
		elif(Scores[i+2]=="d"):
			Score=3
		if(Scores[i+1]=="1"):
			Team1Score+=Score
		else:
			Team2Score+=Score
	Output=open(os.path.join(sys.argv[2],File[0:len(File)-4]+'_v91365dg.txt'),"w")
	Output.write(str(Team1Score)+":"+str(Team2Score))
	Output.close()