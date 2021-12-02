import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("english_words_file", type=str)
parser.add_argument("input_dir", type=str)
parser.add_argument("output_dir", type=str)
args = parser.parse_args()

if args.input_dir[:-1] != "/":
	args.input_dir += "/"
	
if args.output_dir[:-1] != "/":
	args.output_dir += "/"


def change_upper(text_list):
	amount_changed = 0
	
	for i in range(len(text_list)):
		if not text_list[i].islower() and text_list[i].isalpha():
			text_list[i] = text_list[i].lower()
			amount_changed += 1
	
	return amount_changed, text_list


def remove_punct(text_list):
	amount_removed = 0
	
	for i in range(len(text_list)):
		#The '#' and '@' characters are not classed as punctuation according to the midterm test pdf
		if not text_list[i-amount_removed].isalnum() and text_list[i-amount_removed] != " " and text_list[i-amount_removed] != "#" and text_list[i-amount_removed] != "@":	
			text_list.remove(text_list[i-amount_removed])
			amount_removed += 1

	return amount_removed, text_list


def remove_nums(text_list):
	amount_removed = 0
	
	for i in range(len(text_list)):
		if text_list[i-amount_removed].isnumeric():
			text_list.remove(text_list[i-amount_removed])
			amount_removed += 1
	
	return amount_removed, text_list


def check_spelling(text_list):
	dictionary = []
	with open(args.english_words_file) as f:
		for line in f:
			line = line.rstrip()
			dictionary.append(line)
		
	correct_words = 0
	for word in text_list:
		if word in dictionary:
			correct_words += 1
	
	return correct_words


def spell_check(text):
	#Formatting
	output = "y99614zh\nFormatting ###################\n"
	
	text = text.replace("\n", "")
	
	char_list = []
	for i, char in enumerate(text):
		char_list.append(char)
		
	temp = change_upper(char_list)
	word_list = temp[1]
	output += "Number of upper case letters changed: " + str(temp[0]) + "\n"
		
	temp = remove_punct(char_list)
	char_list = temp[1]
	output += "Number of punctuations removed: " + str(temp[0]) + "\n"
	
	temp = remove_nums(char_list)
	char_list = temp[1]
	output += "Number of numbers removed: " + str(temp[0]) + "\n"
	
	text = ""
	for char in char_list:
		text += char
	
	word_list = text.split(" ")
	while "" in word_list:
		word_list.remove("")
	
	#Spellchecking
	output += "Spellchecking ###################\n"
	
	output += "Number of words: " + str(len(word_list)) + "\n"
	
	temp = check_spelling(word_list)
	output += "Number of correct words: " + str(temp) + "\n"
	output += "Number of incorrect words: " + str(len(word_list)-temp)
	
	return output
	

if not os.path.isdir(args.output_dir):
	os.makedirs(args.output_dir)

file_list = os.listdir(args.input_dir)

for x in file_list:
	if x[-4:] == ".txt":
		with open(args.input_dir + x) as f:
			result = spell_check(f.read())
			with open(args.output_dir + x[:-4] + "_y99614zh.txt", "w") as g:
				g.write(result)



