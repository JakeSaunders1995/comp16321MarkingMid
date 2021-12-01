import os
import sys

input_folder = sys.argv[1]
output_folder = sys.argv[2]
dir_list = os.listdir(input_folder)




i = 0
j=2 
for i in range (i, len(dir_list),1):
	file = open(input_folder +"/"+ dir_list[i])
	list1=file.readline()
	print(list1)
	sum1 = 0
	sum2 = 0
	for j in range (j, len(list1), 3):
		if (list1[j-1]) == '1':
			if (list1[j])=='t':
				sum1 = sum1 + 5
			elif (list1[j])=='c':
				sum1 = sum1 + 2
			elif (list1[j])=='p':
				sum1 = sum1 + 3
			elif (list1[j]) =='d':
				sum1 = sum1 + 3
		elif (list1[j-1])== '2':
			if (list1[j])=='t':
				sum2 = sum2 + 5
			elif (list1[j])=='c':
				sum2 = sum2 + 2
			elif (list1[j])=='p':
				sum2 = sum2 + 3
			elif (list1[j]) =='d':
				sum2 = sum2 + 3
	j=2

	print ( sum1, ":", sum2)
	if (sum1>sum2):
		print ("T1 is the winner")
	elif (sum2>sum1):
		print ("T2 is the winner")
	else:
		print ("Equal score")
	output_file = dir_list[i].replace("txt","_p01679ma.txt")
	output_file=output_folder+"/"+output_file
	with open (output_file, "a")as file:
		file.write(f'{sum1}:{sum2}')



