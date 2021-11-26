import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument("pathIn")
parser.add_argument("pathOut")
inputpaths = parser.parse_args()
filelist = os.listdir(inputpaths.pathIn)

#pointsdict = {"c":2, "d":3, "t":5, "p":3}
#print(filelist)

for x in range(len(filelist)):
	T1_score = 0
	T2_score = 0	
	filename = filelist[x]
	input_file = open(inputpaths.pathIn+"/"+filename,"r")
	firstline = input_file.readline()
	text = []
	for n in range(0,len(firstline),3):
		text.append(firstline[n:n+3])
		#print(firstline)
		#print(text)

	for i in range(len(text)):
		if text[i][1] == "1":
			if text[i][2] == "t":
				T1_score += 5
			elif text[i][2] == "c":
				T1_score += 2
			else:
				T1_score += 3
		else:
			if text[i][2] == "t":
				T2_score += 5
			elif text[i][2] == "c":
				T2_score += 2
			else:
				T2_score += 3

	#print(T1_score,T2_score)
	input_file.close()
	name = filename[0:-4]
	outputfilePath = os.path.join(inputpaths.pathOut,name+"_r46739lt.txt")
	#print(outputfilePath)
	file = open(outputfilePath,"w")
	file.write(str(T1_score)+":"+str(T2_score))
	file.close()
