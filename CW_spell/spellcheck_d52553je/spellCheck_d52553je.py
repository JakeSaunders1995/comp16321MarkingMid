import sys
import os

#eg. input1 = "/home/csimage/www/midterm_files"(5)"/midterm_files/Example_inputs/Example_inputs_program3"
#eg. output1 = "/home/csimage/www/midterm_files"(5)"/midterm_files/Example_outputs/Example_outputs_program3"
#eg. dictionary_input = "/home/csimage/www/midterm_files"(5)"/midterm_files/EnglishWords.txt"

dictionary_input = sys.argv[1]
input1 = sys.argv[2]
output1 = sys.argv[3]

dir_list = os.listdir(input1)
cwd = os.getcwd()
input1 = input1.replace(cwd+"/","")
output1 = output1.replace(cwd+"/","")
dictionary_input = dictionary_input.replace(cwd+"/","")
file_dictionary = open(dictionary_input)
dictionary = file_dictionary.read()
file_dictionary.close()
dictionary_array = dictionary.split("\n")

def spellChecker(essay, dictionary_file):
	#removed # and @ cause that what it says
	#removed <,>,$,&,%,^,*,~,_ because not regarded as punctuation
	punctuation = '''!()[]-\,{};:,"\n",."./?...'''
	numbers = "0123456789"
	punctuation_count = 0
	numbers_count = 0
	uppercase_count = 0

	#counting and replacing numbers
	for num in essay:
	    if num in numbers:
	        essay = essay.replace(num, "")
	        numbers_count += 1
	#counting and replacing punctuation
	for punc in essay:
	    if punc in punctuation:
	        essay = essay.replace(punc, "")
	        punctuation_count += 1
	#counting uppercase
	for upper in range(len(essay)):
		if essay[upper].isupper():
			uppercase_count += 1
	#making lower case and printing  essay array
	essay_array = essay.split(" ")
	for z in range(len(essay_array)):
		essay_array[z] = essay_array[z].lower()
	#print(essay_array)

	#COUNTING WORDS
	word_count = len(essay_array)
	#print(word_count)
	for a in range(len(essay_array)):
		if essay_array[a] == "":
			word_count -= 1
	#counting correct words
	correct_word_count = 0
	for x in range(len(essay_array)):
		for y in range(len(dictionary_array)):
			if essay_array[x] == dictionary_array[y]:
				correct_word_count += 1
	incorrect_word_count = word_count - correct_word_count

	return uppercase_count,punctuation_count,numbers_count,word_count,correct_word_count,incorrect_word_count

def output_to_file():
	return("d52553je\nFormatting ###################\nNumber of upper case letters changed: "+str(Checked_spelling[0])+"\nNumber of punctuations removed: "+str(Checked_spelling[1])+"\nNumber of numbers removed: "+str(Checked_spelling[2])+"\nSpellchecking ###################\nNumber of words: "+str(Checked_spelling[3])+"\nNumber of correct words: "+str(Checked_spelling[4])+"\nNumber of incorrect words: "+str(Checked_spelling[5]))

for files in range(len(dir_list)):
 	file_to_check = input1+"/"+dir_list[files]
 	file = open(file_to_check)
 	essay = file.read()
 	file.close()
 	#print(essay)
 	Checked_spelling = spellChecker(essay,dictionary_array)
 	SpellCheck = output_to_file()
 	output_file = dir_list[files].replace(".txt","_d52553je")
 	output_file = output_file+".txt"
 	file_to_write = output1+"/"+output_file
 	file = open(file_to_write, "w")
 	file.write(SpellCheck)
 	file.close()
