import os 
import sys

#Declaring variables

folderIn = sys.argv[1]
folderOut = sys.argv[2]
scores_list = []
file_number = 0
current_file = 0

#Inputting the folder with stored results

for file in sorted(os.listdir(folderIn)):
	file_number += 1
	with open(os.path.join(folderIn, file), 'r') as f:
		all_scores = f.read().rstrip()
		scores_list.append(all_scores)

#Calculating the scores and the winner for each file

for string in scores_list:
	t1 = 0
	t2 = 0
	i = 0
	current_file += 1
	for character in string: 
		if character == "1":
			if string[i + 1] == "t":
				t1 += 5
			elif string[i + 1] == "p":
				t1 += 3
			elif string[i + 1] == "d":
				t1 += 3
			elif string[i + 1] == "c":
				t1 += 2
		
		elif character == "2":
			if string[i + 1] == "t":
				t2 += 5
			elif string[i + 1] == "p":
				t2 += 3
			elif string[i + 1] == "d":
				t2 += 3
			elif string[i + 1] == "c":
				t2 += 2
		i += 1

	#Comparing the scores to determine a winner

	if t1 > t2:
		print("Team 1 wins")
	elif t2 > t1:
		print("Team 2 wins")
	else:
		print("Draw")

#Outputting final scores

	output_name = "test_file" + str(current_file) + "_b16225mz"
	output = open(folderOut+"/"+output_name+".txt", "w")
	final_score = (str(t1) + ":" + str(t2))
	output.write(final_score)

