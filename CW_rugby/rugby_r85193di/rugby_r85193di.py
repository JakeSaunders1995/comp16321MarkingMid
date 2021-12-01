import argparse, os
#point values
t=5
c=2
p=3
d=3
T1 = 0
T2 = 0

parser = argparse.ArgumentParser()
parser.add_argument('dirctry')
parser.add_argument('filestowrite')
args = parser.parse_args()
strfile = os.listdir(args.dirctry)#opening directory and adding all files from in directory into a list
writefile = os.listdir(args.filestowrite)
q=0

while q<len(strfile):#looping through each file in directory to open
	
	file = args.dirctry+"/"+strfile[q]
	filescore = open(file, "r")#opening each file in directory, one at a time
	

	#initialising variables
	T1points = 0
	T2points = 0
	testword = ""

	while True:#adding each character to a new variable to search from
	    w = filescore.read(1)
	    if not w:
	      break
	    testword = testword + w

	filescore.close()  

	i=0

	while i<(len(testword)-1):#scanning through each character
		if testword[i] == "1":#if its team 1 add points to team 1 total
			point = testword[i+1]
			if point == "t":
				T1points = T1points + t#if its t, add t points
			elif point == "c":
				T1points = T1points + c#if its c, add c points
			elif point == "p" or "d":
				T1points = T1points + p#if its p/d, add p/d points

		if testword[i] == "2":#if its team 2 add points to team 2 total
			point = testword[i+1]
			if point == "t":
				T2points = T2points + t#if its t, add t points
			elif point == "c":
				T2points = T2points + c#if its c, add c points
			elif point == "p" or "d":
				T2points = T2points + p#if its p/d, add p/d points

		i+=1

	finalscore = str(T1points) + ":" + str(T2points)#put points in ratio form
	'''
	if T1points > T2points:
		T1 += 1
	elif T2points > T1points:
		T2 += 1
	'''
	T1 = T1 + T1points
	T2 = T2 + T2points

	renamefile = strfile[q]
	renamed = renamefile[0:len(renamefile)-4]+"_r85193di.txt"# take name of input file, get rid of the ".txt" at the end and add username.txt

	outputfile = open(renamed, "w")#open file
	outputfile.write(str(finalscore))#add points to file
	outputfile.close()
	
	q+=1

if T1 > T2:#comparing all overall scores to find an overall winner
	winner = "The overall winning team is Team 1, having scored a total of "+ str(T1) +" points and only conceded "+ str(T2) +" points from Team 2."
elif T2 > T1:
	winner = "The overall winning team is Team 2, having scored a total of "+ str(T2) +" points and only conceded "+ str(T1) +" points from Team 1."
else:
	winner = "The overall score is a draw, where Team 1 scored "+ str(T1) + " points and Team 2 scored "+ str(T2) +" points."
print(winner)