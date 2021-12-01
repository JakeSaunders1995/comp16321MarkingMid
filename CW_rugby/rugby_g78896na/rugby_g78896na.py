#This program takes the input from a file which contains the scores of Rugby teams T1 and T2
import os
import argparse

#input_file_name = "test_file5.txt"
#file_handle = open(input_file_name, "r")
#file_line = file_handle.read()
#print(file_line)

#Input file closed to save resources
#file_handle.close()

#Error handling of the input line from the file

#Main program starts here
#Processing command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("input_file_path", type = str)
parser.add_argument("output_file_path", type = str)
args = parser.parse_args()
input_file_arr = os.listdir(args.input_file_path)
print(input_file_arr)

number_of_files = len(input_file_arr)
count = 0

while count < number_of_files:
	file_handle = open((args.input_file_path + "./" + input_file_arr[count]), "r")
	file_line = file_handle.read()
	file_handle.close()
	T1_score = 0
	T2_score = 0
	tried = 5 #t in the input line
	goal_kick = 2 #c in the input line
	penalty = 3 # p in the input line
	drop_goal = 3 #d in the input line
	print(file_line[0] )
	print(len(file_line))
	#for x in file_line:
	#	print(x)
	#	if x == 'T':
	#		print("yes")
	length = len(file_line)
	line_count = 0
	T1_count = 0
	T2_count = 0

	#Starting while
	while line_count < length :
		if file_line[line_count] == 'T':
			if file_line[line_count + 1] == '1':
				print("the character is : " + file_line[line_count + 1])
				T1_count = T1_count + 1
				if file_line[line_count + 2] == 'c':
					T1_score = T1_score + goal_kick
					print("line_count + 2" + file_line[line_count + 2])
				if file_line[line_count + 2] == 'p':
					T1_score = T1_score + penalty
					print("line_count + 2" + file_line[line_count + 2])
				if file_line[line_count + 2]	== 't':
					T1_score = T1_score + tried
					print("line_count + 2" + file_line[line_count + 2])
				if file_line[line_count + 2] == 'd':
					T1_score = T1_score + drop_goal

			if file_line[line_count + 1] == '2':
				print("the character is : " + file_line[line_count + 1])
				T2_count = T2_count + 1
				if file_line[line_count + 2] == 'c':
					T2_score = T2_score + goal_kick
				if file_line[line_count + 2] == 'p':
					T2_score = T2_score + penalty
				if file_line[line_count + 2]	== 't':
					T2_score = T2_score + tried
				if file_line[line_count + 2] == 'd':
					T2_score = T2_score + drop_goal
		line_count = line_count + 1
	#Ending while
	file_handle = open((args.output_file_path + "/" + str(input_file_arr[count]).replace(".txt", "") + "_g78896na.txt"), "w")
	file_handle.write(str(T1_score) + ":" + str(T2_score))
	file_handle.close()

	count = count + 1

print("Number of T1's : " + str(T1_count))
	
print("T1's score: " + str(T1_score))

print("Number of T2's : " + str(T2_count))
	
print("T2's score: " + str(T2_score))

if T1_score == T2_score:
	print("The match is a draw")
elif T1_score > T2_score:
	print("The winner is T1")
elif T1_score < T2_score:
	print("The winner is T2")

print(str(T1_score) + ":" + str(T2_score))

outputFile_handle = open("outputFile.txt", "w")
outputFile_handle.write(str(T1_score) + ":" + str(T2_score))

















