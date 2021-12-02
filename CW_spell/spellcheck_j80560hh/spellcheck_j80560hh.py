# Spell Checker


import argparse
import os
import re 



# Parsing input and output directories 

parser = argparse.ArgumentParser()
parser.add_argument('dictionary')
parser.add_argument('inputdir')
parser.add_argument('outputdir')
args = parser.parse_args()






number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
punctuation = ['.', '?', '!', ',', ':', ';', '-', '(', ')', '[', ']', '{', '}', "'", '"', '...']
caps_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Reading dictionary 

english_words_file = args.dictionary
fPath = os.path.join(english_words_file)
readF = open(fPath, "r")
english_dictionary_read = readF.readlines()
# print(english_dictionary_read)
# eng_dics = english_dictionary_read.split("\n")
english_dictionary = []
for word in english_dictionary_read:
	# print(word)
	word1 = word.replace("\n", "")	
	english_dictionary.append(word1)
# for word in english_dictionary:
# 	print(word)




# Reading input files from input directory

input_directory = args.inputdir
for filename in os.listdir(input_directory):
	if filename.endswith(".txt"):
		f = os.path.join(input_directory, filename)
		readfile = open(f, "r")
		results_in_file = readfile.readline()
		# print(results_in_file)

		word_section = re.split(' ', results_in_file) 
		# print(word_section)
		numcheck = 0
		puncscheck = 0
		capscheck = 0
		wordsnum = 0
		correctwordsnum = 0
		incorrectwordsnum = 0
		words_only = []


		for word in word_section:
			word0 = word.replace("\n", "")
			# print(word)

			for char in word0:
				if char in number:
					word0 = word0.replace(char, "")
					numcheck += 1
				if char in punctuation:
					word0 = word0.replace(char, "")
					puncscheck += 1
				if char in caps_letter:
					word0 = word0.replace(char, char.swapcase())
					capscheck += 1
			# print(word0)
			words_only.append(word0)

		
		# for dicsword in english_dictionary:
		# 	print(dicsword)

		for word1 in words_only:			
			# print(word1)
			if word1 == "":
				continue
			else:
				# print(word1)
				wordsnum += 1
				if word1 in english_dictionary:
					# print(word1 + ": correct")
					correctwordsnum += 1
				else:
					# print(word1 + ": incorrect")
					incorrectwordsnum += 1
		
		print("j80560hh")
		print("Formatting ###################")
		print("Number of upper case letters changed: " + str(capscheck))
		print("Number of punctuations removed: " + str(puncscheck))
		print("Number of numbers removed: " + str(numcheck))
		print("Spellchecking ###################")
		print("Number of words: " + str(wordsnum))
		print("Number of correct words: " + str(correctwordsnum))
		print("Number of incorrect words: " + str(incorrectwordsnum))

		
		output_directory = args.outputdir
		write_file_open = open(output_directory + "/" + filename[:-4] + "_j80560hh.txt", "w")
		write_file_open.write("j80560hh")
		write_file_open.write("\nFormatting ###################")
		write_file_open.write("\nNumber of upper case letters changed: " + str(capscheck))
		write_file_open.write("\nNumber of punctuations removed: " + str(puncscheck))
		write_file_open.write("\nNumber of numbers removed: " + str(numcheck))
		write_file_open.write("\nSpellchecking ###################")
		write_file_open.write("\nNumber of words: " + str(wordsnum))
		write_file_open.write("\nNumber of correct words: " + str(correctwordsnum))
		write_file_open.write("\nNumber of incorrect words: " + str(incorrectwordsnum))





































		# print(words_only)

		# print(english_dictionary)




		# for i in english_dictionary:
		# 	print(i)

			




			# print(word1)
			# wordsnum += 1
			# for dicsword in english_dictionary:
			# 	if word1 == dicsword:
			# 		print(word1)
			# 	else:
			# 		print(word1)
			# for dicsword in english_dictionary:
			# 	if word in dicsword:
			# 		if word == dicsword:
			# 			print(word)
			# 		elif word != dicsword:
			# 			print(dicsword)



			






			# 		print(word)



			# for dicsword in english_dictionary:
			# 	if word in dicsword:
			# 		print(word)
			# 		correctwordsnum += 1
				

				
			# 	elif word in dicsword and word != dicsword:
			# 		print(dicsword)
			# 		incorrectwordsnum += 1



		



		


		# print(*words_only)

		# for i in words_only:
		# 	print(i)





		#correctwords = 0
		#capscheck = 0
		#puncscheck = 0
		#numcheck = 0
		#wordsinfile = 0
		#incorrectwords = 0

		# for word in word_section:
			# print(word)
			#if punctuation in word, remove punctution 
			#if number in word, remove number
			#if caps letter, change to lowercase letter

			#word_section2 = word without punctuation, numbers, caps letters
			# for word in englishfiles.txt:
				# for word2 in word_section_2:
					#if word2 in englishfiles.txt and word2 == word in englishfiles.txt:
						#correctwords += 1
					#elif word2 in englishfiles.txt and word2 != word in englishfiles.txt:
						#spell check += 1, incorrectwords += 1




		

		







