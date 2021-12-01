import argparse
import os

input_dir=[]# input files list
global T1
global T2

T1=0
T2=0

def ChangePath(path):# add /
	if path[-1]!="\\" or path[-1]!="/":
		path+="/"
	return path

def Mark1(pointType):
	global T1
	if pointType[position+2]=="t":
		T1+=5

	elif pointType[position+2]=="c":
		T1+=2
		
	elif pointType[position+2]=="p":
		T1+=3

	else:
		T1+=3

def Mark2(pointType):
	global T2
	if pointType[position+2]=="t":
		T2+=5

	elif pointType[position+2]=="c":
		T2+=2
		
	elif pointType[position+2]=="p":
		T2+=3

	else:
		T2+=3



parser=argparse.ArgumentParser()
parser.add_argument('inputFile', type=str)
parser.add_argument('outputFile', type=str)
args=parser.parse_args()

input_folder=ChangePath(args.inputFile)
output_folder=ChangePath(args.outputFile)

input_dir = os.listdir(input_folder)

#os.chdir(input_folder)# change to that path

for file in input_dir:
	mark_file= open(input_folder+file, "r")
	content=mark_file.read()
	T1=0
	T2=0

	for position in range(len(content)):
		if content[position:position+2]=="T1":
			Mark1(content)

		elif content[position:position+2]=="T2":
			Mark2(content)

	mark_file.close()

	result=open(output_folder+file[0:-4]+"_j59004hl.txt", "w")
	result.write(str(T1)+":"+str(T2))
	if T1>T2:
		print("T1 wins!")
		print("T1:T2---->"+str(T1)+":"+str(T2))
	elif T1<T2:
		print("T2 wins!")
		print("T1:T2---->"+str(T1)+":"+str(T2))
	else:
		print("No one lose!")
		print("T1:T2---->"+str(T1)+":"+str(T2))
	result.close()