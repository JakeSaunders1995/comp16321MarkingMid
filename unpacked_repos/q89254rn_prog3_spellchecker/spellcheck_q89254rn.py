import sys
import re
import string
import os

dictionary_words= sys.argv[1]
folder_input = sys.argv[2]
folder_output= sys.argv[3]

def spell_check(parameter):
	punctuation_list= '''.?!,:;-{}[]()'"'''
	inside_files=parameter.read()
	uppercase_turned=0
	punc_removed=0
	numbers_removed=0
	elipses_replaced=inside_files.replace("...",".")

	num_words=0
	words_correct=0
	words_incorrect=0

	

	for x in inside_files:
		if (x.isupper()) == True:
			uppercase_turned+=1


		if x.isnumeric():
			numbers_removed+=1

	for g in elipses_replaced:
		if g in string.punctuation:
			punc_removed+=1
	
	removing_punctuation = re.sub( r'[^\w\s]', '', inside_files)
	removing_uppercases = removing_punctuation.lower()
	removing_numbers = re.sub(r'[0-9]', '', removing_uppercases)
	after_removed=removing_numbers.split()
	num_words=len(after_removed)

	
	
	file_dict = open(dictionary_words, 'r')
	words_inside = []
	for z in file_dict:
		words_inside.append(z.replace('\n', ''))

	for word in after_removed:
		if word not in words_inside:
			words_incorrect+=1
		else:
			words_correct+=1

    
	my_username="q89254rn"

	
   

	with open(filesoutput_name, 'w') as o:
		print(my_username, "Formatting ###################", "Number of upper case letters changed: " + str(uppercase_turned), "Number of punctuations removed: " + str(punc_removed), "Number of numbers removed:" + str(numbers_removed), "Spellchecking ###################", "Number of words: " +  str(num_words), "Numbers of correct words: " + str(words_correct), "Number of incorrect words: " + 	str(words_incorrect), sep="\n", file=o)
        

        



for filename in os.listdir(folder_input):
	if filename.endswith('.txt'):
		files_input=os.path.join(folder_input, filename)
		filesoutput_name=str(folder_output + "/" + filename[:10] + "_q89254rn" + filename[10:])
		print(files_input)
		with open(files_input, 'r') as i:
			files=i
			spell_check(files)
