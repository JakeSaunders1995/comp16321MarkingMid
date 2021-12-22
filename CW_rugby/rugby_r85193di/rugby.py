import argparse
t=5
c=2
p=3
d=3

parser = argparse.ArgumentParser()
parser.add_argument('testfile')
parser.add_argument('filetowrite')
args = parser.parse_args()


file=open(args.testfile, "r")
T1points = 0
T2points = 0
testword = ""

while True:
    w = file.read(1)
    if not w:
      break
    testword = testword + w

file.close()  

i=0

while i<(len(testword)-1):
	if testword[i] == "1":
		point = testword[i+1]
		if point == "t":
			T1points = T1points + 5
		elif point == "c":
			T1points = T1points + 2
		elif point == "p" or "d":
			T1points = T1points + 3

	if testword[i] == "2":
		point = testword[i+1]
		if point == "t":
			T2points = T2points + 5
		elif point == "c":
			T2points = T2points + 2
		elif point == "p" or "d":
			T2points = T2points + 3

	i+=1
'''
if T1points > T2points:
	print("team 1 won with a score of ", T1points, ":", T2points)
elif T1points < T2points:
	print("team 2 won with a score of ", T2points, ":", T1points)
else:
	print("its a draw ",T1points, ":", T2points)
'''
finalscore = str(T1points) + ":" + str(T2points)
outputfile = open(args.filetowrite, "w")
outputfile.write(finalscore)
outputfile.close()



