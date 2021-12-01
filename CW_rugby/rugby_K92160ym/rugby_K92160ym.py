import os,argparse,re

parser=argparse.ArgumentParser(description="Calculate and display the score of the Rugby game")
parser.add_argument("enterVariable",nargs="+")
args = parser.parse_args()
storedfile=os.listdir(args.enterVariable[0])
for i in range (0,len(storedfile)):
	name=storedfile[i].replace(".txt","")
	name_file=args.enterVariable[0]+"/"+storedfile[i]
	result_file=open(name_file,"r")
	score=result_file.read()
	tm1=[]
	tm2=[]
	r=score.split("T")
	for i in range(len(r)):      
	  if "1" in r[i]:
	    tm1.append(r[i])
	  if "2" in r[i]:
	    tm2.append(r[i])
	 
	def count (y):
		sc = 0
		for j in range(len(y)):
			if "t" in y[j]:
			  	sc += 5
			elif "c" in y[j]:
			  	sc += 2
			elif "p" in y[j]:
				sc += 3
			elif "d" in y[j]:
				sc +=3
		return sc
	team1=count(tm1)
	team2=count(tm2)

	if team1>team2:
		print("team1 is the winner")
	elif team2>team1:
		print("team2 is the winner")
	else:
		print("It is a draw")
	
	appearfile=str(args.enterVariable[1])+"/"+ name + "_K92160ym.txt"
	write_f=open(appearfile,"w")
	output=str(team1)+":"+str(team2)
	write_f.write(output) 