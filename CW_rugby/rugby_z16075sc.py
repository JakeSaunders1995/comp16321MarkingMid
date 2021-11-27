import sys
import argparse
import os

def file_name(file_dir):
	files=os.listdir(file_dir)

	return files

parser = argparse.ArgumentParser()
parser.add_argument("read_space", help="display a name of a table")
parser.add_argument("write_space", help="display a name of a space")
args = parser.parse_args()

x=file_name(args.read_space)

for i in x:
	a=[]
	word=""
	wordlist=[]
	for h in i:
		wordlist.append(h)
	list2=wordlist[:-4]
	for g in list2:
		word+=g
	with open(args.read_space+"/"+i,'r') as f:
		g=(f.read())
		a.append(g)


	lingard={'T1':0,'T2':0}

	for i in range(len(a[0])):
		if a[0][i] == "t":
			if a[0][i-1] == "1":
				lingard['T1']+=5
			if a[0][i-1]=="2":
				lingard['T2']+=5
		if a[0][i] == "c":
			if a[0][i-1] == "1":
				lingard['T1']+=2
			if a[0][i-1]=="2":
				lingard['T2']+=2
		if a[0][i] == "p":
			if a[0][i-1] == "1":
				lingard['T1']+=3
			if a[0][i-1]=="2":
				lingard['T2']+=3
		if a[0][i] == "d":
			if a[0][i-1] == "1":
				lingard['T1']+=3
			if a[0][i-1]=="2":
				lingard['T2']+=3
		fs = open(args.write_space+"/"+word+"_z16075sc.txt",'w')
		fs.write(str(lingard['T1'])+":"+str(lingard['T2']))
