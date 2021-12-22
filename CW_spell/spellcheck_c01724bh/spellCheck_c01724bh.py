import argparse
import re
import os

obj = argparse.ArgumentParser()

obj.add_argument("english_words", type=str, metavar='path')
obj.add_argument("input_folder", type=str, metavar='path')
obj.add_argument("output_folder", type=str, metavar='path')

args = obj.parse_args()


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4' ,'5', '6', '7', '8', '9', '0']


for filename in os.listdir(args.input_folder):
	
	new_file = args.input_folder + '/' + filename
	file = open(new_file, 'r')

	line = file.readline()
	file.close()
	sentence_array = line.split()
	punctuation_count = 0
	uppercase_count = 0
	number_count = 0
	words = 0
	correct_words = 0
	incorrect_words = 0
	filtered_list = []
	filtered_sentence = []
	li = []


	for i in range(len(line)):

		if line[i] in numbers:
			number_count += 1

		elif line[i].isupper():
			uppercase_count += 1
			li.append(line[i].lower())

		elif line[i] not in letters and line[i] not in numbers and line[i] != ' ':
			punctuation_count += 1

		elif line[i] == ' ':
			li.append(' ')

		elif line[i] in letters: 
			li.append(line[i])


	filtered_sentence = ''.join(li)

	filtered_sentence = filtered_sentence.replace('  ', ' ')

	filtered_list = filtered_sentence.split()

	file = open(args.english_words, 'r')

	line = file.read()

	file.close()

	words = len(filtered_list)

	for i in range(len(filtered_list)):
		if re.search(r'\b({0})\b'.format(filtered_list[i]), line, flags=re.IGNORECASE):
			correct_words += 1
		else:
			incorrect_words += 1

	new_output_file = filename.replace('.', '_c01724bh.')
	new_file = args.output_folder + '/' + new_output_file


	file = open(new_file, 'w')
	
	file.write('c01724bh\n')
	file.write('Formatting ###################\n')
	file.write('Number of upper case words changed: ' + str(uppercase_count) + '\n')
	file.write('Number of punctuations removed: ' + str(punctuation_count) + '\n')
	file.write('Number of numbers removed: ' + str(number_count) + '\n')
	file.write('Spellchecking ################### \n')
	file.write('Number of words: ' + str(words) + '\n')
	file.write('Number of correct words: ' + str(correct_words) + '\n')
	file.write('Number of incorrect words: ' + str(incorrect_words))


	file.close()








	
