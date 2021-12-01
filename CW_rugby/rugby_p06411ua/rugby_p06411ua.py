import argparse
import os
input_files = []
output_files = []
parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()
object = os.scandir(path = args.input)
h = 0
for h in object :
	if h.is_file():
		input_files.append(h.name)
username = "p06411ua"
j = 0
for j in range (0, len(input_files)):
	T1_score = []
	T2_score = []
	temp = ""
	T1_points = 0
	T2_points = 0
	input_scores_file = open (args.input + input_files[j], "r")
	input_scores = input_scores_file.read()
	i = 0
	for i in range (0, len(input_scores)):
		temp += input_scores[i]
		if len(temp) == 3:
			if temp[1] == "1":
				T1_score.append(temp)
				temp = ""
			else:
				T2_score.append(temp)
				temp = ""
				i += 1
	i = 0
	for i in range (0, len(T1_score)):
		temp = T1_score[i]
		if temp[2] == "t":
			T1_points += 5
		elif temp[2] == "c":
			T1_points += 2
		elif temp[2] == "p":
			T1_points += 3
		elif temp[2] == "d":
			T1_points += 3

	for i in range (0, len(T2_score)):
		temp = T2_score[i]
		if temp[2] == "t":
			T2_points += 5
		elif temp[2] == "c":
			T2_points += 2
		elif temp[2] == "p":
			T2_points += 3
		elif temp[2] == "d":
			T2_points += 3
	final_score = str(T1_points)+ ":"+ str(T2_points)
	i = 0
	temp = ""
	while input_files[j][i] != ".":
		temp += input_files[j][i]
		i += 1
	final_scores_file = open (args.output + temp + "_" + username +".txt", "w")
	final_scores_file.write(final_score)
	if T1_points > T2_points:
		print ("T1 won. The final score was:")
	elif T1_points < T2_points:
		print ("T2 won. The final score was:")
	else:
		print ("The teams drew. The final score was:")
	print (final_score)
	final_score = ""
