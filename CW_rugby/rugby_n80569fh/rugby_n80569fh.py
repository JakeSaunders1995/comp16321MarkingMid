import sys
import os
import re

path = os.getcwd()
try:
	os.chdir(sys.argv[1])
	true_input = sys.argv[1]
	os.chdir(sys.argv[2])
	true_ouput = sys.argv[2]
except:
	arg1 = (sys.argv[1])[2:]
	arg2 = (sys.argv[2])[2:]
	true_input = path + "/" + arg1
	true_ouput = path + "/" + arg2
os.chdir(true_input)
input_folder = os.listdir(true_input)
for file in input_folder:
	if  file.endswith(".txt"):
		with open(file,"r") as f:
			sugma = (f.read()).strip()
			print(sugma)
			pos = 0
			posplus = pos + 3
			t1points = 0
			t2points = 0
			while (pos<len(sugma)):
				checker = sugma[pos:posplus]
				if checker == "T1t":		
					t1points = t1points + 5
				elif checker == "T1c":
					t1points = t1points + 2
				elif checker == "T1p":
					t1points = t1points + 3
				elif checker == "T1d":
					t1points = t1points + 3
				elif checker == "T2t":
					t2points = t2points + 5
				elif checker == "T2c":
					t2points = t2points + 2
				elif checker == "T2p":
					t2points = t2points + 3
				elif checker == "T2d":
					t2points = t2points + 3	
				pos = pos + 3
				posplus = pos + 3
			print (str(t1points) + ":" + str(t2points))
		os.chdir(true_ouput)
		output_file = file[:-4] + "_n80569fh.txt"
		print (output_file)
		with open(output_file,"w") as o:
			o.write(str(t1points) + ":" + str(t2points))
		os.chdir(true_input)


