import string
import argparse
import os
import sys
import codecs
import glob


def count(string):
	return len(string)

def count_num(string):
	i=0;
	for ch in string:
		if ch.isdigit():
			i+=1
	return i
def rev_num(string):
	no_num=""
	for ch in string:
		if ch.isdigit():
			continue
		no_num+=ch
	return no_num


def count_pun(string):
	s='''/.,:;'(){}"[]?-!<>~_'''
	i=0
	for ch in string:

		for c in s:
			if(ch==c):
				i+=1
	return i
def remove_pun(remov_pun):
	removed="".join(u for u in remov_pun if u not in ("?","'",".", ";", ":", "!","/",",","{","}","[","]","-","~","(",")",">","<","..."))	
	return removed.strip("\n")	
if __name__=="__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument('eng_dic')
	parser.add_argument('input')
	parser.add_argument('output')
	args = parser.parse_args()
	eng_words=str(args.eng_dic)
	st=str(args.input)
	st_out=str(args.output)
	l=os.listdir(st)
	l.sort()
	for filepath in l:
		f= os.path.join(st,filepath)
		pos_t=filepath.find(".txt")
		out_fname=filepath[0:pos_t]
		dic=[]
		# with open(eng_words,'r') as fdic:
		# 	dic=fdic.read()
		# 	for ch in dic:
		# 		if(ch=="tres"):
		# 			print(ch)
		with codecs.open(f, 'r', encoding='utf-8',errors='ignore') as fdata:
			  string=fdata.read()
			  num_count=count_num(string)
			  string=rev_num(string)
			  count_dots=0
			  for ch in string:
			  	if ch=="...":
			  		count_dots+=1
			  count_ellipses=0
			  if count_dots%3==0 :
			  	count_ellipses=count_dots/3
			  pun_count=count_pun(string)
			  string=remove_pun(string.replace('\u2026',''))
			  lword=""
			  j=0
			  string=string.replace("  "," ")
			  string=string.replace(" \n","")
			  length=len(string)
			  # print(length)
			  upcase_count=0
			  while j<length:
			  	ch=string[j]
			  	if ch.isupper():
			  		upcase_count+=1
			  		lword+=ch.lower()
			  	else:
			  		lword+=ch
			  	j+=1
			  string=lword
			  lister=[]
			  i=0
			  string_word=""
			  for ch in string:
			  	if(ch==" "):
			  		lister.append(string_word)
			  		i+=1
			  		string_word=""
			  	string_word+=ch
			  	# print(string_word)
			  lister.append(string_word)
			  # print(lister)
			  i=0
			  countwords=0
			  correct=0
			  incorrect=0
		
			  for word in lister:
			  	if word==" " or word=="\n":
			  		lister.remove(word)
			  for word in lister:
			  	countwords+=1
			  	lister2=[]
			  	for wordin in lister:
			  		lister2.append(wordin.strip())
			  	with open(eng_words,'r') as fdic:
			  		# print(word.lstrip())
			  		if (word.lstrip()) in fdic.read().split():
			  			correct+=1
			  			# print("correct: " + (word.strip()).strip("\n"))
			  		elif (word.lstrip()) not  in fdic.read():
			  		# else:
			  			# print("incorrect: " + word.lstrip())
			  			incorrect+=1			
			  # print(lister2)
			  with open(os.path.join(st_out,f'{out_fname}_z35437sk.txt'),"w") as file_writer:
			       # print(st_out)
			       file_writer.write("\nz35437sk")
			       file_writer.write("\nFormatting ###################")
			       file_writer.write("\nNumber of upper case letters changed: "+str(upcase_count))
			       file_writer.write("\nNumber of punctuations removed: "+str(pun_count))
			       file_writer.write("\nNumber of numbers removed: "+str(num_count))
			       file_writer.write("\nSpellchecking ###################")
			       file_writer.write("\nNumber of words in file: "+str(countwords))
			       file_writer.write("\nNumber of correct words in file: "+str(correct))
			       file_writer.write("\nNumber of incorrect words in file: "+str(incorrect))
			       file_writer.close()
