

import argparse
import os


# Parsing input and output directories

parser = argparse.ArgumentParser()
parser.add_argument('inputdir')
parser.add_argument('outputdir')
args = parser.parse_args()


task = 0

# Score Points

t = 5		#Try
c = 2		#Goal kick
p = 3		#Penalty
d = 3		#Drop goal



# Team totals

# T1Total = 0
# T2Total = 0


# Opening directory and reading each file

input_directory = args.inputdir
for filename in os.listdir(input_directory):
	if filename.endswith(".txt"):
		f = os.path.join(input_directory, filename)
		readfile = open(f, "r")							
		results_in_file = readfile.readline()
		# print(results_in_file)


		input_list = []
		input_list.append(results_in_file)
		# print(input_list)	
		input_score_list = []
		

		n = 3
		for i in range (0, len(input_list[0]), n):
			input_score_list.append(input_list[0][i:i+n])
		print(input_score_list, "		for reference only")
		

		T1Total = 0
		T2Total = 0
		for i in input_score_list:
			# print(i)
			if i == "T1t":
				T1Total = T1Total + t 
			elif i == "T1c":
				T1Total = T1Total + c 
			elif i == "T1p":
				T1Total = T1Total + p 
			elif i == "T1d":
				T1Total = T1Total + d 
			elif i == "T2t":
				T2Total = T2Total + t 
			elif i == "T2c":
				T2Total = T2Total + c 
			elif i == "T2p":
				T2Total = T2Total + p 
			elif i == "T2d":
				T2Total = T2Total + d 


	print("T1 total: ", T1Total, "	(For reference only)")
	print("T2 Total: ", T2Total, "	(For reference only)")


	print(T1Total, ":", T2Total, "		(in the form T1:T2)		for reference only")
	# if T1Total > T2Total:
	# 	print(T1Total, ":", T2Total)
	# elif T1Total < T2Total:
	# 	print(T2Total, ":", T1Total)
	# elif T1Total == T2Total:
	# 	print(T1Total, ":", T2Total)



	

	# Write to an output directory	

	output_directory = args.outputdir
	
	
	writefile = open(output_directory + "/" + filename[:-3] + "_j80560hh.txt", "w")
	writefile.write(str(T1Total) + ":" + str(T2Total))



	# if T1Total > T2Total:
	# 	writefile.write(str(T1Total) + ":" + str(T2Total))
	# elif T1Total < T2Total:
	# 	writefile.write(str(T2Total) + ":" + str(T1Total))
	# elif T1Total == T2Total:
	# 	writefile.write(str(T1Total) + ":" + str(T2Total))
	



	# writefile.write("hello")












# for file in output_directory:
# 	f2 = os.path.join(output_directory, file)








	


























		# for i in results_in_file:
		# 	print(i)










	# 	continue
	# else:
	# 	continue

# print(results_in_file)
	




































	# # if filename.endswith(".txt"):
	# f = os.path.join(directory_name, filename)
	
	# openfile = open(f, "r")
	# readfile = openfile.readlines()
	# print(readfile)
	# 	# continue
	# # else:
	# 	# continue





# dir_path = os.path.dirname(f)



	
	# 	f = open(filename, "r")
	# 	print(f)
	# 	continue
	# else:
	# 	continue


# current_directory = os.listdir()
# print(current_directory)
# for filename in current_directory:
# 	if filename.endswith(".txt"):
# 		file = open(filename)
# 		lines = file.read()
# 		print(lines)
# 		continue
# 	else:
# 		continue

