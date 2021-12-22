import argparse
import os
import re

Parser=argparse.ArgumentParser()
# Parser.add_argument('EnglishWords', type=argparse.FileType('r'))
Parser.add_argument("input",nargs="+")
args=Parser.parse_args()
# args.input[0]
x=os.listdir(args.input[1])
z=os.path.abspath(args.input[0])

for a in range(0,len(x)):
	text=args.input[1]+"/"+x[a]

	file=open(text, "r")
	words=file.read()

	numofnum=len(re.findall("\d",words))
	numofpunc=len(re.findall("[^\w\s]",words))
	numofUC=len(re.findall('([A-Z])',words))



	# numberofpunc = len(re.compile(u'[\u4E00-\u9FA5|\s\w]').findall(words))
	# words1 = re.sub('u[\u9FA5|\s\w]','',words)

	words1 = re.sub("\d", '', words)
	words2 = re.sub('[^\w\s]', '', words1)
	words3 = re.sub(' +', ' ', words2)

	
	l = words3.lower()
	n = l.split(" ")
	# print(n)

	file1=args.input[0]
	dic=open(file1, "r")
	o = dic.read()
	m = o.split("\n")
	

	incorrect=set(n)-set(m)


	r=args.input[2]+"/"+x[a]
	q0='g78196wl'
	q1=' Formatting ###################'
	q2="Number of upper case words transformed: "+str(numofUC)
	q3="Number of punctuation’s removed: "+str(numofpunc)
	q4="Number of numbers removed: "+str(numofnum)
	q5="Spellchecking ###################"
	q6="Number of words in file: "+str(len(n))
	q7="Number of correct words in file: "+str(len(n)-len(incorrect))
	q8="Number of incorrect words in file: "+str(len(incorrect))
	# result=print('g78196wl','\n',q1,'\n',q2,'\n',q3,'\n',q4,'\n',q5,'\n',q6,'\n',q7)
	u=r.replace(".", "_g78196wl.")
	f=open(u,'w')
	f.write(q0)
	f.write('\r\n')
	f.write(q1)
	f.write('\r\n')
	f.write(q2)
	f.write('\r\n')
	f.write(q3)
	f.write('\r\n')
	f.write(q4)
	f.write('\r\n')
	f.write(q5)
	f.write('\r\n')
	f.write(q6)
	f.write('\r\n')
	f.write(q7)
	f.write('\r\n')
	f.write(q8)


