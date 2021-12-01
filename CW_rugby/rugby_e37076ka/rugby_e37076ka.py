import sys,os
from pathlib import Path
import ntpath

file1=sys.argv[1]
file2=sys.argv[2]

for in_entry in os.scandir(file1):
	f1=open(in_entry.path, 'r')
	string=f1.readline().strip()
	f1.close()
	T1=[]
	T2=[]
	sum1=0
	sum2=0
	i=1
	while i<len(string):
		if string[i]=="1":
			T1.append(string[i+1])		
		elif string[i]=="2":
			T2.append(string[i+1])
		i+=3

	for x in T1:
		if x=="t":
			sum1+=5
		elif x=="c":
			sum1+=2
		elif x=="p":
			sum1+=3
		elif x=="d":
			sum1+=3
			
	for y in T2:
		if y=="t":
			sum2+=5
		elif y=="c":
			sum2+=2
		elif y=="p":
			sum2+=3
		elif y=="d":
			sum2+=3
		

	f2=Path(in_entry).stem + "_e37076ka.txt"
	f2= os.path.join(file2, f2)
	f2out=open(f2, 'w+')
	f2out.write(str(sum1)+":"+str(sum2))
	f2out.close()
	





