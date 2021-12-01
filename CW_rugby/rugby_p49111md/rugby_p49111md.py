import os
import sys
path=sys.argv[1]
path2=sys.argv[2]

dirs=os.listdir(path)
for x in dirs:
	test=open(path+'/'+x,'r')
	temp=test.read()
	test.close()

	length = len(temp)

	team1=0
	team2=0

	for i in range(length):
		if temp[i]=='1':
			if temp[i+1]=='t':
				team1=team1+5
				#print('T1: ',team1)
				#print('T2: ',team2)
			elif temp[i+1]=='c':
				team1=team1+2
				#print('T1: ',team1)
				#print('T2: ',team2)
			elif temp[i+1]=='p' or temp[i+1]=='d':
				team1=team1+3
				#print('T1: ',team1)
				#print('T2: ',team2)

		if temp[i]=='2':
			if temp[i+1]=='t':
				team2= team2+ 5
				#print('T1: ',team1)
				#print('T2: ',team2)
			elif temp[i+1]=='c':
				team2=team2+2
				#print('T1: ',team1)
				#print('T2: ',team2)
			elif temp[i+1]=='p' or temp[i+1]=='d':
				team2=team2+3
				#print('T1: ',team1)
				#print('T2: ',team2)
		i=i+3		

	if team1>team2:
		print('T1 Wins')
	elif team2>team1:
		print('T2 Wins')
	else:
		print("It's a draw")

	
	print(str(team1)+':'+str(team2))
	
	a=x[:-4]
	
	myfile=open(path2+'/'+a+'_p49111md.txt','w')
	myfile.write(str(team1))
	myfile.write(':')
	myfile.write(str(team2))
