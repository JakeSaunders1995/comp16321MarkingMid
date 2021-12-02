import argparse
import os
def upcase(wordContent):
	count_u=0
	content=""
	for i in wordContent:
		if 65<=int(ord(i))<=90:
			count_u+=1
			content+=i.lower()
		else:
			content+=i
	f1.write("e54842zt\nFormatting ###################\nNumber of upper case letters changed: " + str(count_u))
	return content

def punctuation(wordContent):
	count_p=0
	content=""
	for i in wordContent:
		if i in ".,'\":;?!/[]{}()":
			count_p+=1
		else:
			content+=i
	f1.write("\nNumber of punctuations removed: " + str(count_p))
	return content

def number(wordContent):
	count_n=0
	content=""
	for i in wordContent:
		if i in "0123456789":
			count_n+=1
		else:
			content+=i
	f1.write("\nNumber of numbers removed: " + str(count_n))
	return content

def num_word(wordContent):
	f1.write("\nSpellchecking ###################\nNumber of words: " + str(len(wordContent)))
	return int(len(wordContent))
def num_correct(wordContent):
	count_C=0
	for i in wordContent:
		if i +"\n" in EnglishWord:
			count_C+=1
	f1.write("\nNumber of correct words: " + str(count_C))
	return count_C
def num_incorrect(WORD,CORRECT):
	count_i=WORD-CORRECT
	f1.write("\nNumber of incorrect words: " +str(count_i))

my_parser = argparse.ArgumentParser()
my_parser.add_argument('Englishword_file', help="input")
my_parser.add_argument('input_file', help="input")
my_parser.add_argument('output_file', help="output")
args = my_parser.parse_args()
Englishword_path=args.Englishword_file
input_folder_path=args.input_file
output_folder_path=args.output_file

EnglishWord="" 
with open(Englishword_path, "r") as f:
	EnglishWord=f.readlines()
	f.close()
os.chdir(input_folder_path)
files= os.listdir(input_folder_path)
files.sort()
file_count =1

for file in files:
	with open(file, "r+") as f:
		wordContent= f.read()
		f.close()
	file_name= file.replace(".txt","_e54842zt.txt")
	f1=open(output_folder_path+"/"+file_name, "w")
	wordContent=upcase(wordContent)
	wordContent=punctuation(wordContent)
	wordContent=number(wordContent)
	wordContent=wordContent.split()
	WORD=num_word(wordContent)
	CORRECT=num_correct(wordContent)
	num_incorrect(WORD,CORRECT)