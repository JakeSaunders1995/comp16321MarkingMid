import os, sys

input_folder = sys.argv[1]
output_folder = sys.argv[2]
dir_list = os.listdir(input_folder)
print(dir_list)



x = 0
y = 2 

for x in range (x, len(dir_list),1):
	file = open(input_folder +"/"+ dir_list[x])
	mylist=file.readline()
	print(mylist)
	Team1Total = 0
	Team2Total = 0
	while (y <= len(mylist)):
		if (mylist[y-1]) == '1':
			if (mylist[y])=='t':
				Team1Total += 5
			elif (mylist[y])=='c':
				Team1Total += 2
			elif (mylist[y])=='p':
				Team1Total += 3
			elif (mylist[y]) =='d':
				Team1Total += 3
		elif (mylist[y-1])== '2':
			if (mylist[y])=='t':
				Team2Total += 5
			elif (mylist[y])=='c':
				Team2Total += 2
			elif (mylist[y])=='p':
				Team2Total += 3
			elif (mylist[y]) =='d':
				Team2Total += 3
		y += 3
	y=2
	print (Team1Total, ":", Team2Total)
	if Team1Total > Team2Total:
		print("Team 1 is the winner")
	elif Team1Total < Team2Total:
		print("Team 2 is the winner")
	else:
		print("DRAW SCORE!")

	output_file = dir_list[x].replace("txt","_m65670fa.txt")
	output_file=output_folder+"/"+output_file
	with open (output_file, "a")as file:
		file.write(f'{Team1Total}:{Team2Total}')



	


	

