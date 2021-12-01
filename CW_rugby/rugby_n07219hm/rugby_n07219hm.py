from sys import argv
from os import listdir
global input_folder_path
input_folder_path = argv[1]
global output_folder_path
output_folder_path = argv[2]
global username
username = "n07219hm"


# Function will read input file and split each set of 3 characters (one scoring event) into a list and return this list
def read_input_file(file):
	score_list = []

	input_file = open(file,"r")
	score_string = input_file.read()
	input_file.close()

	
	i = 0
	

	while True:
		#The try and except block is to find the end of the line and deal with blankspace at the end of the line or a new line
		try:
			if score_string[3*i] == " " or score_string[3*i] =="\n":
				break
		except IndexError:
			break


		score_list.append(score_string[(3*i):(3+3*i)])
		i += 1
		
	return(score_list)	

# Function will calcuate the appropriate number of points to add to each team using the list returned by read_input_file(). Returns final score in "x:y" format
def calculate_score(scores):
	T1_score = 0
	T2_score = 0
	
	for i in range(0,len(scores)):
		
		
		if scores[i][1] == "1":
			if scores[i][2] == "p" or scores[i][2] == "d":
				T1_score += 3

			if scores[i][2] == "t":
				T1_score += 5
			if scores[i][2] == "c":
				T1_score += 2


		if scores[i][1] == "2":
			if scores[i][2] == "p" or scores[i][2] == "d":
				T2_score += 3
			if scores[i][2] == "t":
				T2_score += 5
			if scores[i][2] == "c":
				T2_score += 2
	#calculates winner or if it is a draw

	if T2_score > T1_score:
		result = "Team 2 Won"
	if T2_score == T1_score:
		result = "Draw"
	else:
		result = "Team 1 Won"

	return str(T1_score) + ":" + str(T2_score)

# Fuction takes output_file_path from the user and the final score returned by calculate_score() and will write the final score to the text file. Returns Nothing.
def write_to_output_file(file,final_score):
	output_file = open(file,"w")
	output_file.write(final_score)
	output_file.close()



#loops through files in directory
file_list = listdir(input_folder_path)
output_file_list = []
for file in file_list:
	output_file_list.append(file[:-4] + "_" + username + ".txt")

for i in range(0,len(file_list)):
	output_file_path = output_folder_path + output_file_list[i] 
	write_to_output_file(output_file_path,calculate_score(read_input_file(input_folder_path + str(file_list[i]))))
