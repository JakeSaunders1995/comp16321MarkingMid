import os.path
# import argparse
import sys
# parser = argparse.ArgumentParser()
# parser.add_Argument("txt", help = "the folder name", type= txt)
# file = parser.parse_args()
x=0
inputfolder = sys.argv[1]
for filename in os.listdir(inputfolder):
	fpath = inputfolder + "/" + filename
	filetxt= open(fpath, "r")
	file = filetxt.read()
	x+=1
	i = 0 
	t1 = 0
	t2 = 0	
	while i != len(file):
		if file[i] == "1":
			i+=1
			if file[i] == "t":
				t1 += 5
			elif file[i] == "c":
				t1 += 2
			elif file[i] == "p":
				t1 += 3
			elif file[i] == "d":
				t1 += 3
			else:
				print("error: no score")
		elif file[i] == "2":
			i+=1
			if file[i] == "t":
				t2 += 5
			elif file[i] == "c":
				t2 += 2
			elif file[i] == "p":
				t2 += 3
			elif file[i] == "d":
				t2 += 3
			else:
				print("error: no score")
		else:
			i+=1
	output = sys.argv[2]
	outfile = output + "/" + "test_file"+ str(x) +"_f01643ka" + ".txt"
	tempout = open(outfile, "w")
	tempout.write(str(t1)+":"+str(t2))
	tempout.close()
	
