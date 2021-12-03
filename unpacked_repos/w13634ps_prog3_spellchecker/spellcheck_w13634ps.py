import re
import os
import sys


def output(uppercase_changed, punctuation_removed, numbers_removed, total_words, total_correct_words, total_incorrect_words, path):
	username = "w13634ps" + "\n"
	formatting = "Formatting ###################" + "\n"
	spellcheckking  = "Spellchecking ###################" + "\n"
	ouput_directory = sys.argv[3]
	if ".txt" in path:
		output_path = path.replace(".txt", "_w13634ps.txt")
	else:
		output_path = path + "_w13634ps.txt"


	full_output_path = os.path.join(ouput_directory, output_path)
	create_file = open(full_output_path, "w")
	create_file.write(username)
	create_file.write(formatting)
	create_file.write(uppercase_changed)
	create_file.write(punctuation_removed)
	create_file.write(numbers_removed)
	create_file.write(spellcheckking)
	create_file.write(total_words)
	create_file.write(total_correct_words)
	create_file.write(total_incorrect_words)





file2 = sys.argv[2]
filelist = str(file2)
for path in sorted(os.listdir(file2)):
	##This is basically getting the directory you given and turned to string and adding the directory of the file
	full_path = os.path.join(filelist, path)
	f = open(full_path, "r")
	caps_count = 0
	number_count = 0
	special_count = 0
	correct_words_count = 0	
	incorrect_words_count = 0
	wordsinfile = 0
	for contents in f:
		numbers = "0123456789"
		punctuation = """.?!,:;-–[]""}{''()"""
		punctuation_and_numbers = """0123456789.?!,:;-–[]""}{''()"""
		newline = "\n"
		for letter in contents:
			if letter.isupper():
				caps_count = caps_count + 1	
			if letter in numbers:
				number_count = number_count + 1
			if letter in punctuation:
				special_count = special_count + 1
		elipses_count = contents.count("...")
		special_count = special_count - (elipses_count * 2)		


		uppercase_changed = "Number of upper case letters changed: " + str(caps_count) + "\n"
		punctuation_removed = "Number of punctuations removed: " + str(special_count) + "\n"
		numbers_removed = "Number of numbers removed: " + str(number_count) + "\n"

		contents = contents.strip("\n")
		contents = contents.lower()
		clearedcontent = ""
		for eachletter in contents:
			if eachletter not in punctuation_and_numbers:
				clearedcontent = clearedcontent + eachletter
			else:
				clearedcontent = clearedcontent	
		clearedcontent = clearedcontent.split(" ")
		while "" in clearedcontent:
			clearedcontent.remove("")		


		file1 = sys.argv[1]
		correct_words = open(file1, "r")
		alist = []
		for each_correct_word in correct_words:
			each_correct_word = each_correct_word.strip("\n")
			alist.append(each_correct_word)	
		for eachword in clearedcontent:
			if eachword in alist:
				correct_words_count = correct_words_count + 1
				wordsinfile = wordsinfile + 1
			else:
				incorrect_words_count = incorrect_words_count + 1
				wordsinfile = wordsinfile + 1
		

		total_words = "Number of words: " + str(wordsinfile) + "\n"
		total_correct_words = "Number of correct words: " + str(correct_words_count) + "\n"
		total_incorrect_words = "Number of incorrect words: " + str(incorrect_words_count) + "\n"

		output(uppercase_changed, punctuation_removed, numbers_removed, total_words, total_correct_words, total_incorrect_words, path)	





