import os 
import sys


#Assigning the inputs 
input_Folder = sys.argv[1]
output_Folder = sys.argv[2]


#checks if output_folder exists, otherwise makes one n
if not os.path.isdir(output_Folder):
	os.mkdir(output_Folder)


#iterate over files in input_folder
for file in os.listdir(input_Folder):

	with open(os.path.join(input_Folder, file)) as file_in:
		score = file_in.read().split("T")

	count1 = 0
	count2 = 0 
	points = {'t':5, 'c':2, 'p':3, 'd':3}
	score.remove("")


	#loops through score/ increments scores 
	for i in range (len(score)):
		if int(score[i][0]) == 1: 
			count1 += points.get(score[i][1])
		
		else:
			count2 += points.get(score[i][1])


	#adds resutls in a file in the output folder 
	with open(os.path.join(output_Folder, os.path.basename(file)[:-4] + "_f54617sa.txt") , "w") as file_out:
		file_out.write(str(count1) +  ":" + str(count2))
