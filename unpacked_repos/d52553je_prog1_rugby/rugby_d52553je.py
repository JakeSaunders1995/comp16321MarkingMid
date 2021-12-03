import sys
import os

#must get rid of () in arguments because bash shell doesnt accept
#eg. input1 = "/home/csimage/www/midterm_files"(5)"/midterm_files/Example_inputs/Example_inputs_program1"
# eg. output1 = "/home/csimage/www/midterm_files"(5)"/midterm_files/Example_outputs/Example_outputs_program1"

input1 = sys.argv[1]
output1 = sys.argv[2]
#output folder already created by autobot
dir_list = os.listdir(input1)
#print(dir_list)
cwd = os.getcwd()
input1 = input1.replace(cwd+"/","")
output1 = output1.replace(cwd+"/","")

def Count_Scores(scorecard_from_file):
 	T1_Count = 0
 	T2_Count = 0
 	for x in range(0,len(scorecard),3):
 		if scorecard[x+2] == "t" and scorecard[x+1] == "1":#try and T1
 			T1_Count += 5
 		if scorecard[x+2] == "t" and scorecard[x+1] == "2":#try and T2
 			T2_Count += 5
 		if scorecard[x+2] == "c" and scorecard[x+1] == "1":#coversion and T1
 			T1_Count += 2
 		if scorecard[x+2] == "c" and scorecard[x+1] == "2":#conversion and T2
 			T2_Count += 2
 		if scorecard[x+2] == "p" and scorecard[x+1] == "1":
 			T1_Count += 3
 		if scorecard[x+2] == "p" and scorecard[x+1] == "2":
 			T2_Count += 3
 		if scorecard[x+2] == "d" and scorecard[x+1] == "1":
 			T1_Count += 3
 		if scorecard[x+2] == "d" and scorecard[x+1] == "2":
 			T2_Count += 3
 	score = str(T1_Count)+":"+str(T2_Count)
 	if T1_Count < T2_Count:
 		print("Team 2 Won")
 	if T2_Count < T1_Count:
 		print("Team 1 Won")
 	if T1_Count == T2_Count:
 		print("Was a draw")
 	return score

for files in range(len(dir_list)):
 	file_to_check = input1+"/"+dir_list[files]
 	file = open(file_to_check)
 	scorecard = file.read()
 	file.close()
 	final_score = Count_Scores(scorecard)
 	#print(final_score)
 	output_file = dir_list[files].replace(".txt","_d52553je")
 	output_file = output_file+".txt"
 	file_to_write = output1+"/"+output_file
 	file = open(file_to_write, "w")
 	file.write(final_score)
 	file.close()






