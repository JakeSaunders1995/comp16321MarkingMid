import os
import sys


def ScoringTeam1(FileIn):
	T1Score = 0
	for x in range(int(len(FileIn)/3)):
		teamsScore = FileIn[(3*x)+2]
		if FileIn[3*x+1] == "1":
			if teamsScore == "p":
				T1Score = T1Score + 3
			elif teamsScore == "d":
				T1Score = T1Score + 3
			elif teamsScore == "c":
				T1Score = T1Score + 2
			elif teamsScore =="t":
				T1Score = T1Score + 5
	return(str(T1Score))

def ScoringTeam2(FileIn):
	T2Score = 0
	for x in range(int(len(FileIn)/3)):
		teamsScore = FileIn[(3*x)+2]
		if FileIn[3*x+1] == "2":
			if teamsScore == "p":
				T2Score = T2Score + 3
			elif teamsScore == "d":
				T2Score = T2Score + 3
			elif teamsScore == "c":
				T2Score = T2Score + 2
			elif teamsScore =="t":
				T2Score = T2Score + 5
	return(str(T2Score))


directory = sys.argv[1]
dest = sys.argv[2]

for filename in os.listdir(directory):
	print
	with open(os.path.join(directory, filename), "r") as file:
		FileIn = file.readline()
		with open(os.path.join(dest, os.path.basename(filename)[:-4] + "_y59426ra.txt"), "w+") as file:
			FileOut= file.write(ScoringTeam1(FileIn)+":"+ScoringTeam2(FileIn))
			

#if T2Score > T1Score:
#	print("Team Two wins!")
#elif T1Score > T2Score:
#	print("Team One wins!")
#elif T1Score == T2Score:
	#print("It's a draw!")


#print(T1Score,":",T2Score)


#path in: /home/csimage/COMP16321/coursework/16321_python_coursework_y59426ra/midterm/Program1/Example_inputs_program1/test_file1.txt
#path out:
