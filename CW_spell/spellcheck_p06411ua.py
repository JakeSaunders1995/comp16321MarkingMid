import argparse
import os
import string
input_files = []
output_files = []
parser = argparse.ArgumentParser()
parser.add_argument("English_words", type = argparse.FileType('r'))
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()
symbols = [".", "?", "!", ",", ":", ";", "–", "-", "(", ")", "{", "}", "[", "]", "'", "\"", "…"]
numbers = string.digits
uppercase = string.ascii_uppercase
format_text = "Formatting ###################"
spellchecking = "Spellchecking ###################"
username = "p06411ua"
correct_spelling_array = []
correct_spelling = args.English_words.read()
h = 0
temp = ""
for h in range (0, len(correct_spelling)):
	if correct_spelling[h] != "\n":
		temp += correct_spelling[h]
	else:
		correct_spelling_array.append(temp)
		temp = ""
object = os.scandir(path = args.input)
h = 0
for h in object :
	if h.is_file():
		input_files.append(h.name)
i = 0
for i in range (0, len(input_files)):
	temp = ""
	number_of_symbols = 0
	number_of_numbers = 0
	number_of_uppercase = 0
	incorrect_spelling = 0
	count = 0
	words_array = []
	text_list = []
	input_text_file = open (args.input + input_files[i], "r")
	input_text = input_text_file.read()
	j = 0
	for j in range (0, len(input_text)):
		changes = 0
		k = 0
		for k in range (0, len(symbols)):
			if input_text[j] == symbols[k]:
				number_of_symbols += 1
				changes += 1
				if input_text[j] == input_text[j-1] == input_text[j-2] == ".":
					number_of_symbols -= 2
		k = 0
		for k in range (0, len(numbers)):
			if input_text[j] == numbers[k]:
				number_of_numbers += 1
				changes += 1
		k = 0
		for k in range (0, len(uppercase)):
			if input_text[j] == uppercase[k]:
				number_of_uppercase += 1
				changes += 1
				temp += uppercase[k].lower()
		if changes == 0:
			temp += input_text[j]
	print (temp)
	temp_2 = ""
	j = 0
	for j in range (0, len(temp)):
		count = 0
		if temp[j] != " " and temp[j] != "\n":
			temp_2 += temp[j]
		else:
			k = 0
			for k in range (0, len(correct_spelling_array)):
					if temp_2 == correct_spelling_array[k]:
						count += 1
			if temp_2 != "":
				words_array.append(temp_2)
				if count == 0:
					incorrect_spelling += 1
			temp_2 = ""
	k = 0
	for k in range (0, len(correct_spelling_array)):
			if temp_2 == correct_spelling_array[k]:
				count += 1
	if temp_2 != "":
		words_array.append(temp_2)
		if count == 0 and temp[j] != " " and temp[j] != "\n":
			incorrect_spelling += 1
	correct_spelling_number = len(words_array) - incorrect_spelling 
	j = 0
	temp = ""
	while input_files[i][j] != ".":
		temp += input_files[i][j]
		j += 1
	spell_check_file = open (args.output + temp + "_" + username +".txt", "w")
	spell_check_file.write(username + "\n" + format_text + "\nNumber of upper case letters changed: " + str(number_of_uppercase) + "\nNumber of punctuations removed: " + str(number_of_symbols) + "\nNumber of numbers removed: " + str(number_of_numbers) + "\n" + spellchecking + "\nNumber of words: " + str(len(words_array)) + "\nNumber of correct words: " + str(correct_spelling_number) + "\nNumber of incorrect words: " + str(incorrect_spelling))		
