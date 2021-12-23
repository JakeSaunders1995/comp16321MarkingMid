import os
import sys

path=sys.argv[2]
path2=sys.argv[3]
path3=sys.argv[1]

EnglishWords=open(path3+'/EnglishWords.txt','r')
Words=EnglishWords.read()
EnglishWords.close()

dirs=os.listdir(path)
for x in dirs:
	file=open(path+'/'+x,'r')
	text=file.read()
	file.close()
	
	num=['1','2','3','4','5','6','7','8','9','0']
	punc=['!','"','(',')',',','.','/',':',';','?','[',']','{','}','~','...','-',"'"]
	upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	num_count=0
	punc_count=0
	upper_count=0
	correct=0
	incorrect=0
	newtext=''

	for i in range (len(text)):
		if text[i] in num:
			num_count+=1
			
		elif text[i] in punc:
			punc_count+=1
			
		elif text[i] in upper:
			upper_count+=1
			temp=text[i]
			temp2=temp.lower()
			newtext+=temp2
		else:
			newtext+=text[i]
		
	list_of_words=newtext.split()
	
	num_words=len(list_of_words)
	
	for s in range (len(list_of_words)):
		temp=list_of_words[s]
		if temp not in Words:
			incorrect+=1
		else:
			correct+=1

	a=x[:-4]

	myfile=open(path2+'/'+a+'_p49111md.txt','w')
	myfile.write('p49111md\n')
	myfile.write('Formatting ###################\n')
	myfile.write('Number of upper case letters changed: ')
	myfile.write(str(upper_count))
	myfile.write('\n')
	myfile.write('Number of punctionation removed: ')
	myfile.write(str(punc_count))
	myfile.write('\n')
	myfile.write('Number of numbers removed: ')
	myfile.write(str(num_count))
	myfile.write('\n')
	myfile.write('Spellchecking ###################\n')
	myfile.write('Number of words: ')
	myfile.write(str(num_words))
	myfile.write('\n')
	myfile.write('Number of correct words: ')
	myfile.write(str(correct))
	myfile.write('\n')
	myfile.write('Number of incorrect words: ')
	myfile.write(str(incorrect))
	myfile.write('\n')
