import sys, os

input_directory = sys.argv[1]
file_list = os.listdir(input_directory)

n = 0
while n <= len(file_list)-1:

	T1_score = 0
	T2_score = 0

	test_file1 = open(input_directory+"/"+file_list[n], "r")

	scores = test_file1.read()
	test_file1.close()

	i = 0
	while i <= len(scores)-2:
		if scores[i] == "T" and scores[i+1] == "1":
			if scores[i+2] == "t":
				T1_score = T1_score+5
				i += 1
			elif scores[i+2] == "c":
				T1_score = T1_score+2
				i += 1
			elif scores[i+2] == "p" or scores[i+2] == "d":
				T1_score = T1_score+3
				i += 1
			else:
				i += 3
		if scores[i] == "T" and scores[i+1] == "2":
			if scores[i+2] == "t":
				T2_score = T2_score+5
				i += 1
			elif scores[i+2] == "c":
				T2_score = T2_score+2
				i += 1
			elif scores[i+2] == "p" or scores[i+2] == "d":
				T2_score = T2_score+3
				i += 1
			else:
				i += 3
		i+=1

	if T1_score > T2_score:
		#print("Team 1 won")
		winner = "Team 1 won"
	elif T1_score < T2_score:
		#print("Team 2 won")
		winner = "Team 2 won"
	else:
		#print("It was a draw")
		winner = "It was a draw"
	#print(winner)

	filename = str(file_list[n]).replace(".txt", "")
	ouput_directory = sys.argv[2]
	output_file = open(ouput_directory+"/"+filename+"_h78811cv.txt", "w")
	output_file.write(str(T1_score)+":"+str(T2_score))
	output_file.close()

	n += 1