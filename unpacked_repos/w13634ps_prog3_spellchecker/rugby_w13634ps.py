import sys
import os


def end(Team1, Team2, path):
	#This is doing very siilar to begining of code but instead its creating a new file instead of reading existing ones
	output = sys.argv[2]
	if ".txt" in path:
		output_path = path.replace(".txt", "_w13634ps.txt")
	else:
		output_path = path + "_w13634ps.txt"	
	full_path_output = os.path.join(output, output_path)
	createfile = open(full_path_output, "w")
	createfile.write(str(Team1) + ":" + str(Team2))




Team1 = 0
Team2 = 0

#giving directory in cmd prompt
file = sys.argv[1]
#turning into string for join
filelist = str(file)
#for each file in that directory 
for path in sorted(os.listdir(file)):
	##This is basically getting the directory you given and turned to string and adding the directory of the file
	full_path = os.path.join(filelist, path)
	f = open(full_path, "r")
	for index in f:
		sep = index.split("T")
		Team1 = 0
		Team2 = 0
		for i in sep:
			if "1" in i:
				if i == "1t":
					Team1 = Team1 + 5
				if i == "1c":
					Team1 = Team1 + 2
				if i == "1p":
					Team1 = Team1 + 3
				if i == "1d":
					Team1 = Team1 + 3
			elif "2" in i:
				if i == "2t":
					Team2 = Team2 + 5
				if i ==	"2c":
					Team2 = Team2 + 2
				if i == "2p":
					Team2 = Team2 + 3
				if i == "2d":
					Team2 = Team2 + 3
		print("Team 1 total score was "+ str(Team1))
		print("Team 2 total score was "+ str(Team2))			
		if Team1 > Team2:
			print("Team 1 won")
			end(Team1,Team2, path)
		elif Team1 < Team2:
			print("Team 2 won")
			end(Team1, Team2, path)
		elif Team1 == Team2:
			print("It was a draw")
			end(Team1, Team2, path)			


		









