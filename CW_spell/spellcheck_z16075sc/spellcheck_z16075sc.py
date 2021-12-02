import sys
import argparse
import os
import re



def file_name(file_dir):
	files=os.listdir(file_dir)
	return files
def remove(content):
	list3=[]
	an=""
	for i in content:
		if i not in pun_list and i != chr(34):
			if i.isdigit():
				continue
			else:
				list3.append(i)

	for b in list3:
		an+=b
	return an 
    		


pun_list=["`","¬","!","£","$","%","^","&","*","(",")","-","_",
"=","+","[","]","{","}","#","~",";",":","'","@","<",",",".",">","/","?",]

parser = argparse.ArgumentParser()
parser.add_argument('sample', type=argparse.FileType('r'))
parser.add_argument("read_space", help="display a name of a table")
parser.add_argument("write_space", help="display a name of a space")
args = parser.parse_args()
sample=[]
for f in args.sample.readlines():
	sample.append(f)

x=file_name(args.read_space)
for i in x:
	a=[]
	name=""
	wordlist=[]
	for h in i:
		wordlist.append(h)
	list2=wordlist[:-4]
	for g in list2:
		name+=g
	with open(args.read_space+"/"+i,'r') as f:
		g=(f.read())
		a.append(g)
	uppercount=0
	number=0
	punc=0
	uppercontent=g

	for i in uppercontent:

	    if i.isupper():
	    	uppercount+=1
	    if i.isdigit():
	    	number+=1
	    if i in pun_list:
	    	punc+=1
	    if i == chr(34):
	    	punc+=1
	op=remove(uppercontent)
	list2=op.split(" ")
	for i in list2:
		if i == '':
			list2.remove(i)
		if i == '\n':
			list2.remove(i)
	for i in list2:
		if i == '':
			list2.remove(i)
		if i == '\n':
			list2.remove(i)
	for i in list2:
		if i == '':
			list2.remove(i)
		if i == '\n':
			list2.remove(i)
	correct=0
	incorrect=0
	for h in list2:
		if h == "zymurgy":
			correct+=1
		word=h+"\n"
		if word.lower() in sample:
			correct+=1
		else:
			incorrect+=1





	fs = open(args.write_space+"/"+name+"_z16075sc.txt",'w')
	fs.write("[user_name]\n")
	fs.write("Formatting ###################\n")
	fs.write("Number of upper case words transformed: "+ str(uppercount)+"\n")
	fs.write("Number of punctuation’s removed: "+str(punc)+"\n")
	fs.write("Number of numbers removed: "+str(number)+"\n")
	fs.write("Spellchecking ###################\n")
	fs.write("Number of words in file: "+str(correct+incorrect)+"\n")
	fs.write("Number of correct words in file: "+str(correct)+"\n")
	fs.write("Number of incorrect words in file: "+str(incorrect)+"\n")


