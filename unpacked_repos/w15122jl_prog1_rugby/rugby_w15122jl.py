import os
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output')
args=parser.parse_args()
Input=args.input
Output=args.output
info=os.listdir(Input)
oufo=os.listdir(Output)
t=[]
test=''
team1=0
team2=0
num=0
a=0
info.sort()
for file in info:
	f=open(Input+'/'+file)
	iter_f=iter(f);
	i=''
	for line in iter_f:
		i+=line
	t.append(i)
	while num < len(t):
		test=t[num]
		num+=1
		for a in range(0,len(test)):
			if test[a]=='1':
				if test[a+1]=='t':
					team1+=5
				if test[a+1]=='c':
					team1+=2
				if test[a+1]=='p':
					team1+=3
				if test[a+1]=='d':
					team1+=3
			elif test[a]=='2':
				if test[a+1]=='t':
					team2+=5
				if test[a+1]=='c':
					team2+=2
				if test[a+1]=='p':
					team2+=3
				if test[a+1]=='d':
					team2+=3		
		o=open(Output+'/'+file[0:-4]+'_w15122jl.txt','w')		
		o.write(str(team1)+':'+str(team2))
		team1=0
		team2=0
		o.close()