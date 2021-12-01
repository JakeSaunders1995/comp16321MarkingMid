Sequence = ""	
with open("test_file4.txt") as file:
	Sequence = file.readlines()

def listtoString(s):
	string = ""
	for l in s:
		string += l
	return string

scoreSequence = listtoString(Sequence)

Try = 5
goalKick = 2
penalty = 3
dropGoal = 3


def T1scoring():
	global T1pts
	T1pts = 0
	for i in range(len(scoreSequence)):
		
		if(scoreSequence[i:i+3] == "T1t"):
			T1pts += Try
			
		elif(scoreSequence[i:i+3] == "T1c"):
			T1pts += goalKick
			
		elif(scoreSequence[i:i+3] == "T1p"):
			T1pts += penalty
			
		elif(scoreSequence[i:i+3] == "T1d"):
			T1pts += dropGoal
			

def T2scoring():
	global T2pts
	T2pts = 0
	for i in range(len(scoreSequence)):
		if(scoreSequence[i:i+3] == "T2t"):
			T2pts += Try
			
		elif(scoreSequence[i:i+3] == "T2c"):
			T2pts += goalKick
			
		elif(scoreSequence[i:i+3] == "T2p"):
			T2pts += penalty
			
		elif(scoreSequence[i:i+3] == "T2d"):
			T2pts += dropGoal
			
		



T1scoring()
T2scoring()

f = open("test_file4_f11711jy.txt", "w")
f.write(str(T1pts) + ":" + str(T2pts))
	

