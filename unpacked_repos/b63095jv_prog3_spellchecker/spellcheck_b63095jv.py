import sys
import os


punctuation = [".", "?", "!", ",", ":", ";", "-", "—", "(", ")", "{", "}", "[", "]", "'", "\"", "..."]

file = open(sys.argv[1])
dictionary = file.read() # EnglishWords.txt
dictionary = dictionary.split("\n")
file.close()

in_directory = sys.argv[2]
files = os.listdir(in_directory)
for file in files:
	input_path = os.path.join(in_directory, file)
	input_file = open(input_path)
	text = input_file.read()
	input_file.close()

	num_of_upper = 0
	num_of_nums = 0
	num_of_punc = 0

	# format text
	text = text.replace("\n", " ")
	text2 = ""
	c = 0
	while c < len(text):
		character = text[c]
		if ord(character) >= 97 and ord(character) <= 122 or character == " ": # 97 - 122 lower case ASCII
			text2 += character
			c += 1
		elif ord(character) >= 65 and ord(character) <= 90: # 65 - 90 caps ASCII
			num_of_upper += 1
			text2 += character
			c += 1
		elif ord(character) >= 48 and ord(character) <= 57: # 48 - 57 numbers ASCII
			num_of_nums += 1
			c += 1
		elif character == "." and c <= len(text)-3:
			if text[c+1] == "." and text[c+2] == ".":
				num_of_punc += 1
				c += 3
			else:
				num_of_punc += 1
				c += 1
		elif character in punctuation: # punctuation
			num_of_punc += 1
			c += 1

	text2 = text2.lower() # upper case to lower case

	# spellchecking
	text2 = text2.strip()
	words = text2.split()

	num_of_words = len(words)
	num_of_correct = 0
	num_of_wrong = 0

	for x in words:
		if x in dictionary:
			num_of_correct += 1
		else:
			num_of_wrong += 1


	out_directory = sys.argv[3]
	index = file.find(".txt")
	output_path = os.path.join(out_directory, file[:index] + "_b63095jv" + file[index:])
	output_file = open(output_path, "w")
	output_file.write("b63095jv\nFormatting ###################\nNumber of upper case letters changed: " + str(num_of_upper) + "\nNumber of punctuations removed: " + str(num_of_punc) + "\nNumber of numbers removed: " + str(num_of_nums) + "\nSpellchecking ###################\nNumber of words: " + str(num_of_words) + "\nNumber of correct words: " + str(num_of_correct) + "\nNumber of incorrect words: " + str(num_of_wrong))
	output_file.close()

