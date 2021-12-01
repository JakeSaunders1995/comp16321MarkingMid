import sys
import os


folder_inputs = sys.argv[1]
folder_outputs = sys.argv[2]



for filename in os.listdir(folder_inputs):

	output_file = filename.split('.')[0] + "_n03227rm.txt"

	with open(os.path.join(folder_inputs, filename), 'r') as file:
		l = []
		score_string = file.read()
		for i in range(len(score_string)):
			if score_string[i].isupper():
				l.append(score_string[i] + score_string[i+1] + score_string[i+2])


		T1_score = []
		T2_score = []

		for i in l:
			if "T1" in i:
				T1_score.append(i)
			else:
				T2_score.append(i)



		t = 5 
		c = 2  
		p = 3 
		d = 3


		finalScoreT1 = 0
		finalScoreT2 = 0

		for i in T1_score:
			if 't' in i:
				finalScoreT1 += 5
			elif "p" in i:
				finalScoreT1 += 3
			elif "d" in i:
				finalScoreT1 += 3
			elif "c" in i:
				finalScoreT1 += 2

		for i in T2_score:
			if 't' in i:
				finalScoreT2 += 5
			elif "p" in i:
				finalScoreT2 += 3
			elif "d" in i:
				finalScoreT2 += 3
			elif "c" in i:
				finalScoreT2 += 2
			

		with open(os.path.join(folder_outputs, output_file), 'w') as op:
			op.write(str(finalScoreT1) + ":" + str(finalScoreT2))
			

