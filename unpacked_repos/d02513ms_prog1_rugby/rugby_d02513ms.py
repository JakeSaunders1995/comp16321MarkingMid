import sys
import os
for file in os.listdir(sys.argv[1]):
	with open(sys.argv[1] + '/' + file, 'r') as f:
		contents = f.read().rstrip()
		score=""
		t1=0
		t2=0
		add1=0
		add2=0
		for character in contents:
			if(add1==1):
				if(character=='t'):
					t1+=5
				if(character=='c'):
					t1+=2
				if(character=='p'):
					t1+=3
				if(character=='d'):
					t1+=3
			if(add2==1):
				if(character=='t'):
					t2+=5
				if(character=='c'):
					t2+=2
				if(character=='p'):
					t2+=3
				if(character=='d'):
					t2+=3
			if(character=='1'):
				add1=1
			else:
				add1=0
			if(character=='2'):
				add2=1
			else:
				add2=0
	score+=str(t1)
	score+=":"
	score+=str(t2)
	Output_folder = sys.argv[2]
	file = file.replace(".txt","")
	file += "_d02513ms.txt"
	output_file=open(Output_folder+"/" + file,"w")
	output_file.write(score)
