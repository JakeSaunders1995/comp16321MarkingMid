import os,sys
path = sys.argv[1]
FileList = os.listdir(path)
for file in FileList:
	print(file[-9999:-4]+"_y59276ma.txt")
	OutputFile = sys.argv[2] +"/"+file[-999:-4]+"_y59276ma.txt"
	InputFile = sys.argv[1] + "/" +file
	Team1Score, Team2Score,Points  = 0, 0, 0
	ScoreSheet = open(InputFile,"rt")
	Team = ScoreSheet.read(2)
	while(Team != ""):
		if(Team == "T1"):
			Score = ScoreSheet.read(1)
			if(Score == "t"):
				Points = 5
			elif(Score == "c"):
				Points = 2
			elif(Score == "p"):
				Points = 3
			elif(Score == "d"):
				Points = 3
			Team1Score += Points
			Team = ScoreSheet.read(2)
		elif(Team == "T2"):
			Score = ScoreSheet.read(1)
			if(Score == "t"):
				Points = 5
			elif(Score == "c"):
				Points = 2
			elif(Score == "p"):
				Points = 3
			elif(Score == "d"):
				Points = 3
			Team2Score +=Points
			Team = ScoreSheet.read(2)
	ScoreSheet.close()
	if(Team1Score>Team2Score):
		print("Team 1 wins")
	elif(Team2Score>Team1Score):
		print("Team 2 Wins")
	else:
		print("It is a draw")
	Results = open(OutputFile,"x")
	Results.write(str(Team1Score)+":"+str(Team2Score))
	Results.close()
	Results = open(OutputFile,"r")
	print(Results.read())
	Results.close()