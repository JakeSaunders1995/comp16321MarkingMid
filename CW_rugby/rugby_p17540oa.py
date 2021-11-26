import sys
import os.path
import os

inputpath = sys.argv[1]   # input file.
filelist = os.listdir(inputpath)  #want directory list of input file
for file in filelist:
	output_file_name = file[:-4]
	f = open(inputpath+"/"+file,)  
	scores = f.readline()
			
	T1_points = 0
	T2_points = 0
			
	for x in range(int(len(scores)/3)):   #loops thru
		score_type = scores[(3*x)+2]
		if scores[3*x+1] == "1":
			if "t" in score_type:
				T1_points += 5
			elif "c" in score_type:
				T1_points += 2
			elif "p" in score_type:
				T1_points += 3
			elif "d" in score_type:
				T1_points += 3
				
		if scores[3*x+1] == "2":
			if "t" in score_type:
				T2_points += 5
			elif "c" in score_type:
				T2_points += 2
			elif "p" in score_type:
				T2_points += 3
			elif "d" in score_type:
				T2_points += 3

	outputpath = sys.argv[2]
	#outputfile = outputpath.split(".") #divides to list,. values in resultant list are separated based on a separator char
	#output = open(file, "x")
	path = outputpath
	if not os.path.exists(path):
		os.makedirs(path)
	outputfile = (outputpath+'/'+file[:-4])
	output = open((outputfile+"_p17540oa.txt"),"x")
	output.write(str(T1_points) + ":" + str(T2_points))
	f.close()
	output.close()
			