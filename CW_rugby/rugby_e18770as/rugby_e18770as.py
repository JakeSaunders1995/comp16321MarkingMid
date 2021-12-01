import sys
import os
list_input=sys.argv
input_directory= sys.argv[1]
output_directory= sys.argv[2]
filenames=[]
outputpaths=[]
paths=[]
for entry in os.listdir(input_directory):
    if (entry.endswith(".txt")):
        path1=(os.path.join(input_directory,entry))
        paths.append(path1)
        filename= entry.split(".")[0]
        outputfilename=filename+"_e18770as.txt"
        outputpath=(os.path.join(output_directory,outputfilename))
        outputpaths.append(outputpath)
        filenames.append(filename)

length=len(filenames)

for i in range(length):
	input_file=paths[i]
	output_file=outputpaths[i]
	fin= open(input_file, "r")
	fout=open(output_file,"w")
	contents= fin.read()
	length_of_file= len(contents)
	list1=[]
	list2=[]
	for i in range(len(contents)):
	    if contents[i]=="T":
	    	if contents[i+1]=="1":
	    		list1.append(contents[i+2])
	    	elif contents[i+1]=="2":
	    		list2.append(contents[i+2])
	    else:
	    	pass

	score1=0
	score2=0

	for i in (list1):
	    if i=="t":
	        score1+=5
	    elif i=="c":
	        score1+=2
	    elif i=="p":
	        score1+=3
	    elif i=="d":
	        score1+=3

	for i in (list2):
	    if i=="t":
	        score2+=5
	    elif i=="c":
	        score2+=2
	    elif i=="p":
	        score2+=3
	    elif i=="d":
	        score2+=3
	if score1>score2:
		winner= "Team 1"
	elif score1==score2:
		winner="Draw"
	else:
		winner= "Team 2"
	final_Score=str(score1)+ ":" + str(score2)
	fout.write(final_Score)

	fin.close()
	fout.close()