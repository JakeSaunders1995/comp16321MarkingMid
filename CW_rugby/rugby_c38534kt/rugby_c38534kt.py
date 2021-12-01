import sys
import contextlib
walk_dir=sys.argv[1]
dest_dir=sys.argv[2]
with open (walk_dir, "r") as f:
		data = f.read()

l=len((data))
first_team=0
second_team=0
mark=""
for i in range(0,l):
	if data[i]=='1':
		score=data[i+1]
		if score=='t':
			mark=5
		if score=='c':
			mark=2
		if score=='p':
			mark=3
		if score=='d':
			mark=3
		
		first_team += mark


	if data[i]=='2':
		score=data[i+1]
		if score=='t':
			mark=5
		if score=='c':
			mark=2
		if score=='p':
			mark=3
		if score=='d':
			mark=3
		
		second_team += mark
i=i+1
scoreboard= (str(first_team) +":" +str(second_team))
with open(dest_dir,"w") as o:
		 with contextlib.redirect_stdout(o):
		 	print(scoreboard)