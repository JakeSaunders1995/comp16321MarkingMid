import argparse
import os

def outputResult():
	file_name= i.replace(".txt","_e54842zt.txt")
	output_file=open(output_folder_path+"/"+file_name, "w")
	output_file.write(result)
def indir():
	inputDir = sorted(os.listdir(args.inputfolder))
	return inputDir
my_parser = argparse.ArgumentParser()
my_parser.add_argument('inputfolder', help="input")
my_parser.add_argument('outputfolder', help="output")
args = my_parser.parse_args()
input_folder_path=args.inputfolder
output_folder_path=args.outputfolder

x = indir()

for i in x:
	file = open(input_folder_path+"/"+i, "r")
	first_file = file.read()

	count_1=0
	count_2=0
	position=0

	while position<len(first_file):
		character=first_file[position]
		if character == "1":
			if first_file[position+1] == "t":
				count_1+=5
			elif first_file[position+1] == "c":
				count_1+=2
			elif first_file[position+1] == "p":
				count_1+=3
			elif first_file[position+1] == "d":
				count_1+=3
		elif character == "2":
			if first_file[position+1] == "t":
				count_2+=5
			elif first_file[position+1] == "c":
				count_2+=2
			elif first_file[position+1] == "p":
				count_2+=3
			elif first_file[position+1] == "d":
				count_2+=3
		position+=1
	result=str(count_1)+ ":"+ str(count_2)
	outputResult()
