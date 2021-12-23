import sys,os
from pathlib import Path
import ntpath
import re

list1=[] 
file1=sys.argv[2]
file2=sys.argv[3]
for in_entry in os.scandir(file1):
	f1=open(in_entry.path, 'r')
	string=f1.readline().strip()
	f1.close()

	#string="My ! name Is 2 khawla $ a ab aba"
	nums=['0','1','2','3','4','5','6','7','8','9']
	punc='''!()-[]}{;:'",<>./?@#$%^&*_~''' 
	i=0
	num=0
	puncnum=0 
	upperCase=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

	while i<len(string):
		if string[i] in nums:
			num+=1
		i+=1

	newString=re.sub(r'[0-9]','',string)

	 
	newString2 = ""
	p=0
	for x in newString:
	   if x not in punc:
	       newString2 +=x
	   else:
	   	p+=1



	newString3= newString2.lower()
	upper=0
	y=0
	while y<len(newString2):
		if newString2[y] in upperCase:
			upper+=1
		y+=1

	newString4= newString3.split()
	lenght=len(newString4)

	file= open("./EnglishWords.txt")
	fileList=file.read()
	fileList=fileList.split()
	file.close()

	z=0 #correct lines
	k=0 #incorrect lines 
	

	for b in newString4:
		if b in fileList:
			z+=1
		else:
			k+=1

	#print("Formatting ################### ") 
	#print("Number of upper case words transformed:", upper)
	#print("Number of punctuation's removed:", p)
	#print("Number of numbers removed:", num)
	#print("Spellchecking ###################")
	#print("Number of words in file:", lenght)
	#print("Number of correct words in file:", z)
	#print("Number of incorrect words in file:", k)
	#print(newString4)


	f2=Path(in_entry).stem + "_e37076ka.txt"
	f2= os.path.join(file2, f2)
	f2out=open(f2, 'w+')
	f2out.write("Formatting" + " ################## \n")
	f2out.write("Number of upper case words transformed" + ":" + str(upper)+"\n")
	f2out.write("Number of punctuation's removed" + ":" + str(p)+"\n")
	f2out.write("Number of numbers removed:" + ":" + str(num)+"\n")
	f2out.write("Spellchecking ###################"+"\n")
	f2out.write("Number of words in file" + ":" + str(lenght)+"\n")
	f2out.write("Number of correct words in file" + ":" + str(z)+"\n")
	f2out.write("Number of incorrect words in file" + ":" + str(k))
	f2out.close()
 