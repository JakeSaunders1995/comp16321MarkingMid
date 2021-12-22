import sys
import os
def score_worth(score_type):
	if score_type == "t":
		return 5
	elif score_type == "c":
		return 2
	elif score_type == "p" or score_type == "d":
		return 3

def calculate_scores(filename):
	input_file = input_folder + "/" + filename
	input_file = open(input_file,"r")
	output_file = filename[:-4]
	output_file = output_file+"_V55941np.txt"
	new_output_file = output_folder + "/" + output_file
	output_file = open(new_output_file,"w+")
	data = input_file.readlines()
	data = data[0]
	T1_score = 0
	T2_score = 0
	for i in range(0,len(data)-2,3): #checks every 3 characters and works out the team and the points earned
		score = score_worth(data[i+2])
		if data[i:i+2] == "T1":
			T1_score += score
		elif data[i:i+2] == "T2":
			T2_score += score
		
	output_file.write(str(T1_score)+":"+str(T2_score))

input_folder = sys.argv[1]
output_folder = sys.argv[2]
try: #creates a folder if there isn't one
	os.mkdir(output_folder)
except OSError as error:
	pass

arr = os.listdir(input_folder)
for i in range(0,len(arr)):
	calculate_scores(arr[i])

#command i used to test ignore
#python3 rugby_V55941np.py ~/PythonStuff/Python_Midterm/midterm_files/Example_inputs/Example_inputs_program1 ~/PythonStuff/Python_Midterm/midterm_files/program1_outputs
#python3 rugby_V55941np.py ./midterm_files/Example_inputs/Example_inputs_program1 ./midterm_files/program1_outputs