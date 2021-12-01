import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()

def filelist(input_file):
	file_path_list = []
	for file in os.listdir(input_file):
		file_path = os.path.join(input_file,file)
		file_path_list.append(file_path)
	return(file_path_list)

l = filelist(args.input_file)
for name in l:
	f_input = open(name)
	result = f_input.read()
	count = 1
	T1 = 0
	T2 = 0
	while count < len(result):
		if result[count] == "1" and result[count+1] == "t":
			T1 += 5
		elif result[count] == "1" and result[count+1] == "c":
			T1 += 2
		elif result[count] == "1" and result[count+1] == "p":
			T1 += 3	
		elif result[count] == "1" and result[count+1] == "d":
			T1 += 3
		elif result[count] == "2" and result[count+1] == "t":
			T2 += 5
		elif result[count] == "2" and result[count+1] == "c":
			T2 += 2
		elif result[count] == "2" and result[count+1] == "p":
			T2 += 3
		elif result[count] == "2" and result[count+1] == "d":
			T2 += 3
		count += 3				
		pass
	f_input.close()
	basename = os.path.basename(name)
	filename = basename.split(".txt")
	filename.append("_v08387yx.txt")
	file_name = ''.join(filename)
	output_file_name = os.path.join(args.output_file,file_name)
	f_output = open(output_file_name,"w")
	f_output.write(str(T1)+":"+str(T2))
	f_output.close()	


