import os
import sys
import re
import contextlib
import string

file1 = sys.argv[1]
file2 = sys.argv[2]

with open("EnglishWords.txt", "r") as lib:
	dic=lib.read()

with open(file1, "r") as fin:
	data = fin.read()
	dataLowercase=data.lower() #convert upper to lower
	uppercase=0
	digitcount=0
	punctcount=0
	for i in data:
		if(i.isupper()): #check if char is uppercase
			uppercase=uppercase+1 #add to count
		if(i.isdigit()): #check if char is digit
			digitcount=digitcount+1 #add to count
		if i in string.punctuation: #check if char is punc
			punctcount=punctcount+1 #add to count
	listtoremove=string.punctuation + string.digits
	table_ = str.maketrans('', '', listtoremove)
	newdata = dataLowercase.translate(table_)
	countWords = len(re.findall(r'\w+',newdata))
	datax =newdata.split()
	countcorrect=0
	countwrong=0
	posi=0
	for i in datax:
		sc=dic[posi]
		if i in dic:
			countcorrect+=1
			posi+=1
		if i not in dic:
			countwrong+=1
			posi+=1
	
	
with open(file2, "w") as fout:
	with contextlib.redirect_stdout(fout):
		print(datax)
		print('\n')
		print("x32001nm")
		print("Formatting ##############")
		print("Number of upper case letters changed: ",uppercase)
		print("Number of punctuations removed: ", punctcount)
		print("Number of numbers remove: ",digitcount)
		print("Spellchecking #############")
		print("Number of words: ",countWords)
		print("Number of correct words: ", countcorrect)
		print("Number of incorrect words: ", countwrong)
