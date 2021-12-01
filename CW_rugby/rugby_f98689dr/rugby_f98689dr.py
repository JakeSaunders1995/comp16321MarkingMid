import argparse
import os

#read terminal
cmdline = argparse.ArgumentParser()
cmdline.add_argument("input")
cmdline.add_argument("output")
inp = cmdline.parse_args()
out = cmdline.parse_args()
inputFolderName = str(inp.input)
outputFolderName = str(out.output)
ls = os.listdir(inputFolderName)
loop = 0
for i in ls:
	#read file
	file = inputFolderName+"/"+ls[loop]
	inputFile = open(file,"r")
	scores = inputFile.read()
	scoresList = scores.split("T")
	inputFile.close()
	scoresList.remove("")

	#determining scores
	t1=0
	t2=0
	for i in scoresList:
		if i[0]=="1":
			if i[1]=="t":
				t1+=5
			elif i[1]=="c":
				t1+=2
			elif i[1]=="p":
				t1+=3
			elif i[1] =="d":
				t1+=3
		elif i[0]=="2":
			if i[1]=="t":
				t2+=5
			elif i[1]=="c":
				t2+=2
			elif i[1]=="p":
				t2+=3
			elif i[1] =="d":
				t2+=3

	#output score
	temp = ls[loop]
	outputFile = open(outputFolderName+"/"+temp[:-4]+"_f98689dr.txt","w")
	outputFile.write(str(t1)+":"+str(t2))
	outputFile.close()
	loop += 1