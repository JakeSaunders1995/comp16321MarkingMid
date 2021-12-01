import sys
import os

inputfile = sys.argv[1]
outputfile = sys.argv[2]
# input_file = os.listdir(inputfile)
# for p in input_file:
	# file = open(inputfile + "/" + p,'r')
	# text = file.readline()
# inputfile= sys.argv[1]
# outputfile= sys.argv[2]
# input_file = os.listdir(inputfile)
# for x in input_file:
file = open( inputfile,'r')
text = file.readline()
t1score = 0
t2score = 0

for x in range(1,(len(text)), 3):
	if (text[x]) == "1":
		scoringteam = "t1"
	else:
		scoringteam = "t2"	
	if (text[x+1]) == "t":
		if scoringteam == "t1":
			t1score += 5
		else:
			t2score += 5
	elif (text[x+1]) == "c":
		if scoringteam == "t1":
			t1score += 2
		else:
			t2score += 2
	elif (text[x+1]) == "p":
		if scoringteam == "t1":
			t1score += 3
		else:
			t2score += 3
	elif (text[x+1]) == "d":
		if scoringteam == "t1":
			t1score += 3
		else:
			t2score += 3

print(str(t1score) + ":" + str(t2score))
file= open(outputfile,"w")
# outputfile = open(outputfile + "/" + p.replace(".txt","",'w')
# # outputfile = open(outputfile,'w')
file.write(str(t1score) + ":" + str(t2score)) 






			


							
