import sys
import os

n = len(sys.argv) #total arguments
print("Total arguments passed:", n)

print("\nName of Python script:", sys.argv[0]) #printing the python script

input_directory = sys.argv[1]
output_directory = sys.argv[2]

for filename in os.listdir(input_directory):
	if filename.endswith(".txt"):

		input_file = open(os.path.join(input_directory,filename),"r") #Opening The required file for input

		score_T1=0 #assigning the initial score 0 for team 1
		score_T2=0 #assigning the initial score 0 for team 2

		while True:
			text = input_file.read(2)          #reading team name
			if text == "T1":                   #checking if team is T1
				readscore = input_file.read(1) #updating team score
				if readscore == "t":
					score_T1 += 5
				elif readscore == "c":
					score_T1 += 2
				elif readscore == "p":
					score_T1 += 3
				elif readscore == "d":
					score_T1 += 3
				else:
					print('Wrong Scoring type', readscore) #Givng error if the score is not one of t/c/p/d


			elif text == "T2":                 #checking if team is T2        
				readscore = input_file.read(1) #updating team score
				if readscore == "t":
					score_T2 += 5
				elif readscore == "c":
					score_T2 += 2
				elif readscore == "p":
					score_T2 += 3
				elif readscore == "d":
					score_T2 += 3
				else:
					print('Wrong Scoring type', readscore) ##Givng error if the score is not one of t/c/p/d

			else:
				print('End Of File')
				if score_T1 > score_T2:
					print('Team 1 won the game')
				elif score_T1 == score_T2:
					print('Match ended in a tie')
				else:
					print('Team 2 won the game')
				break

		input_file.close() #Closing the input file

		x=filename
		x = x.replace(".txt", "_j34330vk.txt")

		output_file = open(os.path.join(output_directory, x), 'w') #Creating the required file for output

		score_T1=str(score_T1) #converting team 1 score to str
		score_T2=str(score_T2) #converting team 2 score to str

		line=score_T1 +':'+ score_T2 #concatenating strings to from one string

		output_file.write(line) #writing the output in the required file
		output_file.close()     #Closing the output file
	else:
		continue
