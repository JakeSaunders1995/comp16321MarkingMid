

file= open('test_file1.txt','r')
for line in file:
	   a1=line.count('T1t')
	   a=5*a1

	   b1=line.count('T1c')
	   b=2*b1

	   c1=line.count('T1p')
	   c=3*c1

	   d1=line.count('T1d')
	   d=3*d1 

	   e1=line.count('T2t')
	   e=5*e1

	   f1=line.count('T2c')
	   f=2*f1

	   g1=line.count('T2p')
	   g=3*g1

	   h1=line.count('T2d')
	   h=3*h1



	   


team1=a+b+c+d
team2=e+f+g+h

if team1>team2:
   print('team 1 is the winner')
elif team1<team2:
   print('team 2 is the winner')
else:
   print('draw')


f=open('test_file1_p50391tc.txt','w')
f.write(str(team1)+':'+str(team2))

