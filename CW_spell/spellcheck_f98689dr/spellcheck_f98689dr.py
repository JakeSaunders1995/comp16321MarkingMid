import argparse
import re
import os

#read terminal
cmdline = argparse.ArgumentParser()
cmdline.add_argument("words")
cmdline.add_argument("input")
cmdline.add_argument("output")
wrd = cmdline.parse_args()
inp = cmdline.parse_args()
out = cmdline.parse_args()
inputFolderName = str(inp.input)
outputFolderName = str(out.output)
wordFile = str(wrd.words)
ls = os.listdir(inputFolderName)
loop = 0
for i in ls:
	#read file
	file = inputFolderName+"/"+ls[loop]
	inputFile = open(file,"r")
	content = inputFile.read()
	rempunc = re.sub("[^A-Za-z0-9 ]+","",content)
	puncrem = len(content)-len(rempunc)
	remnum = re.sub("[^A-Za-z ]+","",content)
	numrem = len(content)-len(remnum)-puncrem
	cap = len(re.findall(r'[A-Z]',content))
	content = re.sub("[^A-Za-z ]+","",content)
	content = content.lower()
	string = content.split(" ")
	for w in string:
		if w == "":
			string.remove(w)
	inputFile.close()
	#open english words
	dictionary = open(wordFile,"r")
	engWords = dictionary.read()
	checker = engWords.split("\n")

	#check words
	inc = 0 
	cor = 0
	for i in string:
		if i not in checker:
			inc += 1
		else:
			cor += 1

	#output
	temp = ls[loop]
	outputFile = open(outputFolderName+"/"+temp[:-4]+"_f98689dr.txt","w")
	outputFile.write("f98689dr\n")
	outputFile.write("Formatting ###################\n")
	outputFile.write("Number of upper case words transformed: "+ str(cap)+"\n")
	outputFile.write("Number of punctuation’s removed: "+ str(puncrem)+"\n")
	outputFile.write("Number of numbers removed: "+ str(numrem)+"\n")
	outputFile.write("Spellchecking ###################\n")
	outputFile.write("Number of words in file: "+ str(len(string))+"\n")
	outputFile.write("Number of correct words in file: "+ str(cor)+"\n")
	outputFile.write("Number of incorrect words in file: "+ str(inc))
	outputFile.close()
	loop += 1