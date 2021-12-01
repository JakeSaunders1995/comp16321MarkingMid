import sys
import os
inputpath = sys.argv[1]
outputpath = sys.argv[2]
ipathfile = open(inputpath, "r")
opathfile = open(outputpath, "w")

inputfile = ipathfile.read()


score_string= "T1tT2pT2pT1pT1d"
import score_string
l = []
for i in range(len(score_string)):
	if score_string[i].isupper():
		l.append(score_string[i] + score_string[i+1] + score_string[i+2])
lst.append(line[i]+line[i+1]+line[i+2])

T1Score, T2Score= [],[]

for score in l:
 if"T1" in score:
    T1Score.append(score[-1])
 elif"T2" in score:
    T2Score.append(score[-1])

T1=0
T2=0

for letter in T1Score:
	if letter == "t":
		T1 += 5
	elif letter == "c":
	    T1 += 2
	elif letter == "p":
		T1 += 3
	elif letter == "d":
	    T1 += 3

for letter in  T2Score:
    if letter == "t":
        T2 += 5	 
    elif letter == "c":
	    T2 += 2
	elif letter == "d":
	    T2 += 3   

with open(outputpath, "w") as op:
    op.write(str(T1) + ":" + str(T2))	    

