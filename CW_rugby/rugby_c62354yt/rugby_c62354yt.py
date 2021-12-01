import sys
import os

txt=""
s1=0
s2=0
filepath=""
outputpath=""
outputname=""

folder=sys.argv[1]
if folder[0]=="." and folder[1]=="/":
	folder=folder.replace("./","",1)
outputpath=sys.argv[2]
if outputpath[0]=="." and outputpath[1]=="/":
	outputpath=outputpath.replace("./","",1)
filelist=os.listdir(folder)
for i in range (len(filelist)):
	check=filelist[i]
	if check.endswith(".txt"):
		filepath=str(folder)+"/"+str(filelist[i])
		file=open(filepath, "r")
		txt=file.read()

		x=len(txt)
		for g in range (0,x):
			if txt[g]=="1":
				if txt[g+1]=="t":
					s1=s1+5
				if txt[g+1]=="c":
					s1=s1+2
				if txt[g+1]=="p":
					s1=s1+3
				if txt[g+1]=="d":
					s1=s1+3
			elif txt[g]=="2":
				if txt[g+1]=="t":
					s2=s2+5
				if txt[g+1]=="c":
					s2=s2+2
				if txt[g+1]=="p":
					s2=s2+3
				if txt[g+1]=="d":
					s2=s2+3

		if s1>s2:
			ptext="Team 1 is the winner!"
		elif s2>s1:
			ptext="Team 2 is the winner!"
		else:
			ptext="The match is a draw!"

		print(filelist[i], ": ", ptext)
		finalscore=str(s1)+":"+str(s2)
		outputname=str(outputpath)+"/"+str(check.replace(".txt","_c62354yt.txt"))
		output=open(outputname, "w")
		output.write(finalscore)
		output.close()
		s1=0
		s2=0