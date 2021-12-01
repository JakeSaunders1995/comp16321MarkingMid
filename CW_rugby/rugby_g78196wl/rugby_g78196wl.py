import argparse
import os
import re

Parser=argparse.ArgumentParser()
Parser.add_argument("input",nargs="+")
args=Parser.parse_args()
# args.input[0]
x=os.listdir(args.input[0])

# y=args.input[0]+"/"+x

for a in range(0,len(x)):
	y=args.input[0]+"/"+x[a]

	T1=0
	T2=0
	mark=open(y,"r")
	score=mark.read()
	for b in range(0,len(score)):
		if score[b]=="t":
			if score[b-1]=="1":
				T1=T1+5
			elif score[b-1]=="2":
				T2=T2+5
		if score[b]=="c":
			if score[b-1]=="1":
				T1=T1+2
			elif score[b-1]=="2":
				T2=T2+2
		if score[b]=="p":
			if score[b-1]=="1":
				T1=T1+3
			elif score[b-1]=="2":
				T2=T2+3
		if score[b]=="d":
			if score[b-1]=="1":
				T1=T1+3
			elif score[b-1]=="2":
				T2=T2+3
				

		
	r=args.input[1]+"/"+x[a]
	result=str(T1)+":"+str(T2)
	o=r.replace(".", "_g78196wl.")
	f=open(o,'w')
	f.write(result)

