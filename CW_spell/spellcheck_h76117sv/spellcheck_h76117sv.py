import argparse
import string
import os

def get_output_file_name(filename, username):
	before_txt = filename.split('.')[0]
	return before_txt + '_' + username + '.txt'

if __name__=="__main__":

	parser=argparse.ArgumentParser()
	parser.add_argument('input')
	parser.add_argument('english')
	parser.add_argument('output')
	args=parser.parse_args()
var = str(args.input)
out=str(args.output)
eng=str(args.english)
m=os.scandir(var)
for filepath in m:
	f=os.path.join(var,filepath)
	string=open(filepath, 'r') 
	string=string.read()

	word=string
	numberscount=0
	length=len(string)
	nonum=""
	i=0
	while i<length :
		charac=string[i]
		if charac=='1':
			numberscount=numberscount+1
		elif charac=='2':
			numberscount=numberscount+1
		elif charac=='3':
			numberscount=numberscount+1
		elif charac=='4':
			numberscount=numberscount+1
		elif charac=='5':
			numberscount=numberscount+1
		elif charac=='6':
			numberscount=numberscount+1
		elif charac=='7':
			numberscount=numberscount+1
		elif charac=='8':
			numberscount=numberscount+1
		elif charac=='9':
			numberscount=numberscount+1
		elif charac=='0':
			numberscount=numberscount+1
		else :
			nonum=nonum+charac
		i=i+1
	string=nonum
	j=0
	uppercase=0
	lowerword=""
	length=len(string)
	while j<length:
		chars=string[j]
		if chars.isupper():
			uppercase=uppercase+1
			lowerword=lowerword+chars.lower()
		else:
			lowerword=lowerword+chars

		j=j+1

	string=lowerword
	punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	punctr=0
	nopunc=""
	for elements in string:
		if elements in punc:
			punctr=punctr+1
		else:
			nopunc=nopunc+elements
		
	string=nopunc
	length=len(string)
	newstr=""
	i=0
	while i<length:
		charac=string[i]
		i=i+1
		if charac!='.' and charac!='':
			newstr=newstr+charac

	string=newstr
	string=string.lower()
	string=string+" "
	length=len(string)
	i=0
	pos=0
	sub=""
	words=[]
	while i<length :
		character=string[i]
		if character==" ":
			sub=string[pos:i]
			pos=i+1
			words.append(sub)
		i=i+1



	for elements in words:
		if elements=='':
			words.remove(elements)


	countcorrect=0
	countwrong=0
	countwords=0
	for element in words:
			countwords=countwords+1
			with open(eng, 'r') as file:
				if element in file.read():
					countcorrect=countcorrect+1
				else:
					countwrong=countwrong+1

	output_file = os.path.join(args.output, get_output_file_name(filepath.name, 'h76117sv'))
	with open(output_file,'w+') as file:
		file.write("h76117sv")
		file.write("\nFormatting ###################")
		file.write("\nNumber of uppercase words changed :"+str(uppercase))
		file.write("\nNumber of punctuations removed:"+str(punctr))
		file.write("\nNumber of numbers removed:"+str(numberscount))
		file.write("\nSpellchecking ###################")
		file.write("\nNumber of words:"+str(countwords))
		file.write("\nNumber of correct words:"+str(countcorrect))
		file.write("\nNumber of incorrect words:"+str(countwrong))