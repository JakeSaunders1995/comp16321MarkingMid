import os
import argparse
import re
parser=argparse.ArgumentParser()
parser.add_argument('English')
parser.add_argument('input')
parser.add_argument('output')

args=parser.parse_args()
Input=args.input
Output=args.output
EW=args.English
info=os.listdir(Input)
oufo=os.listdir(Output)
info.sort()
punctuation={'[','"','!','.',')','-',':',';','`','?','{','(','}','“','”','_','…',']',',',"'"}
upper=0
punc=0
num=0
words=0
correct=0
incorrect=0
ew=open(EW)
wl=ew.read()
newtest=''
for file in info:
	f=open(Input+'/'+file)
	test=f.read()
	for n in range(len(test)):
		if test[n].isupper()==True:
			upper+=1
		elif test[n].isdigit()==True:
			num+=1
	for p in range(len(test)):
		if test[p] in punctuation:
			punc+=1	
	def removen(test):
		stringn=re.sub('[0123456789]','',test)
		return test.strip()
	def removep(test):
		stringp=re.sub(punctuation,'',test)
		return test.strip()
	for a,word in enumerate(test.split()):		
		i=test[a]
		word=''.join(x for x in word if x.isalpha()).lower()
		if not word:
			continue
		words+=1
		if word in wl and word!='tres':	
			correct+=1
		else:
			incorrect+=1
	o=open(Output+'/'+file[0:-4]+'_w15122jl.txt','w')
	o.write('w15122jl')
	o.write('\r\n')
	o.write('Formatting ###################')
	o.write('\r\n')
	o.write('Number of upper case letters changed: '+str(upper))
	upper=0
	o.write('\r\n')
	o.write('Number of punctuations removed: '+str(punc))
	punc=0
	o.write('\r\n')
	o.write('Number of numbers removed: '+str(num))
	num=0
	o.write('\r\n')
	o.write('Spellchecking ###################')
	o.write('\r\n')
	o.write('Number of words: '+str(words))
	words=0
	o.write('\r\n')
	o.write('Number of correct words: '+str(correct))
	correct=0
	o.write('\r\n')
	o.write('Number of incorrect words: '+str(incorrect))
	incorrect=0
	o.close()

	

	