import sys
import os


word_list = sys.argv[1]
folder_inputs = sys.argv[2]
folder_outputs = sys.argv[3]


for filename in os.listdir(folder_inputs):
	with open(os.path.join(folder_inputs,filename), 'r') as file:

		output_file = filename.split('.')[0] + "_n03227rm.txt"

		punctuations_list = ['.', '?', '!', ',', ':', ';', '_', '-', '[', ']', '{', '}', '(', ')', '\'', '\"', '...']

		updated_line = ""
		removed_numbers = [] 
		removed_punctuations = []

		count_upper = 0

		line = file.read()


		for char in line:
			if char.isupper():
				new_char = char.lower()
				updated_line = updated_line + new_char
				count_upper += 1

			elif char == " ":
				updated_line += char

			elif char.isdigit():
				removed_numbers.append(char)

			elif char in punctuations_list:
				removed_punctuations.append(char)

			else:
				updated_line += char

		count_punct = len(removed_punctuations)
		count_numbers = len(removed_numbers)

		words = updated_line.split()


		correct_word = []
		incorrect_word = []


		with open(word_list, 'r') as wl:
			words_list = wl.read().split()
				
		for word in words:
			if word in words_list:
				correct_word.append(word)
		else:
			incorrect_word.append(word)

	with open(os.path.join(folder_outputs, output_file), 'w') as op:

		outputList = ['n03227rm', '\n'
						'Formatting ###################', '\n'
						'Number of upper case letters changed: ', str(count_upper), "\n" 
						'Number of punctuations removed: ', str(count_punct), "\n"
						'Number of numbers removed: ' , str(count_numbers), "\n"
						"Spellchecking ###################", "\n"
					    "Number of words: " , str(len(words)), "\n"
					    "Number of correct words: " , str(len(correct_word)), "\n"
					    "Number of incorrect words: " , str(len(incorrect_word)), "\n"]

		op.writelines(outputList)








