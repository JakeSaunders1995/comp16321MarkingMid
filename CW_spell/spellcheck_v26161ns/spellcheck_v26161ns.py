import sys
import os

LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_CASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
PUNCTUATION = ".?!,:;--(){'}[]\""
WORDS = []

english_words = sys.argv[1]
folder_path_input = sys.argv[2]
folder_path_output = sys.argv[3]
list_of_files = os.listdir(folder_path_input)


for file_name in list_of_files:
	x = file_name.find(".")
	output_file_name = file_name[:x] + "_v26161ns" + file_name[x:] 
	full_path_input = os.path.abspath(os.path.join(folder_path_input, file_name))
	full_path_output = os.path.abspath(os.path.join(folder_path_output, output_file_name))


	with open(full_path_input, "r") as essay_file:
		essay = essay_file.read()
		essay_splitted = essay.split()

	#READING WORD LIST
	with open(english_words , "r") as WordList:
		for line in WordList:
			line = line.rstrip()
			WORDS.append(line)


	punctuation_counter = 0
	upper_case_counter = 0
	number_counter = 0
	wrong_word_counter = 0
	num_words = 0
	ellipsis_tracker = 0
	character_counter = 0

	for word in essay_splitted:
		character_counter = 0
		temp = ""
		if word == "...":
			punctuation_counter += 1
			continue
		alpha_numeric_word = ''.join(filter(str.isalnum, word))
		alpha_numeric_word = alpha_numeric_word.lower()
		try:
			alpha_word = int(alpha_numeric_word)
		except ValueError:
			if alpha_numeric_word != "":
				num_words += 1
				alpha_word = "".join(i for i in alpha_numeric_word if not i.isdigit())
				if alpha_word not in WORDS:
					wrong_word_counter += 1

		for letter in word:
			# if character_counter == 0:
			# 	pass

			if letter in LOWER_CASE_LETTERS:
				continue

			elif letter == "." and temp == ".":
				ellipsis_tracker += 1
				if ellipsis_tracker == 2:
					punctuation_counter +=1
					ellipsis_tracker = 0

			else:
				if letter in UPPER_CASE_LETTERS:
					upper_case_counter += 1
				elif letter in NUMBERS:
					number_counter += 1
				elif letter in PUNCTUATION:
					punctuation_counter += 1
				else:
					pass

			temp = letter

	with open(full_path_output, "w") as wf:    
		wf.write("v26161ns \n")
		wf.write("Formatting ################### \n")
		wf.write("Number of upper case words changed: " + str(upper_case_counter) + "\n")
		wf.write("Number of punctuations removed: " + str(punctuation_counter) + "\n")
		wf.write("Number of numbers removed: " + str(number_counter) + "\n")
		wf.write("Spellchecking ################### \n")
		wf.write("Number of words: " + str(num_words) + "\n")
		wf.write("Number of correct words: " + str(num_words - wrong_word_counter) + "\n")
		wf.write("Number of incorrect words: " + str(wrong_word_counter) + "\n")
