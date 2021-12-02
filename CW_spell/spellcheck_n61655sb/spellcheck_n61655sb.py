# - Imports -
import sys
from os import listdir
from os.path import isfile, join

# - Global variables and inputs -
ponctuation = ['.', '?', '!', ',', ':', ';', '/', '-', '_', '[', ']', '{', '}', '(', ')', '\'', '\"', '...']
english_words = open(sys.argv[1]).read().splitlines()
input_folder = sys.argv[2]
test_files = [file for file in listdir(input_folder) if isfile(join(input_folder, file)) and file[0] != '.']



# - Main functions -
def count(text):
	return {'ponctuation': sum(text.count(e) for e in ponctuation) - 3*text.count('...'), 
			'number': sum(text.count(e) for e in [str(i) for i in range(10)]), 
			'upper cases': sum(1 for character in text if character.isupper()) }

def is_allowed(character):
	return character in [" "] + [chr(i) for i in range(ord('a'),ord('z')+1)]

def simplify(text):
	return "".join([charac.lower() for charac in text if is_allowed(charac.lower())])

def seperate_words(simplified_text):
	return simplified_text.split()

def check(list_of_word):
	checking_states = {'correct': [], 'incorrect': []}
	for word in list_of_word:
		if word in english_words:
			checking_states['correct'].append(word)
		else: checking_states['incorrect'].append(word)
	return {"correct": len(checking_states['correct']), "incorrect": len(checking_states['incorrect'])}

def print_answer(texts):
	username = 'n61655sb'
	# ----
	counts = {'ponctuation': 0, 'number': 0, 'upper cases': 0}
	for text in texts:
		for i in counts:
			counts[i] += count(text)[i]
	nb_ponctuation = counts['ponctuation']
	nb_number = counts['number']
	nb_uppercase = counts['upper cases']
	# ----
	simplified_text = ''
	for text in texts:
		simplified_text += simplify(text)
	sperated_words = seperate_words(simplified_text)
	nb_total_words = len(sperated_words)
	nb_correct_words = check(sperated_words)['correct']
	nb_incorrect_words = check(sperated_words)['incorrect']
	# -------
	return f"{username}\nFormatting ###################\nNumber of upper case letters changed: {nb_uppercase}\nNumber of punctuations removed: {nb_ponctuation}\nNumber of numbers removed: {nb_number}\nSpellchecking ###################\nNumber of words: {nb_total_words}\nNumber of correct words: {nb_correct_words}\nNumber of incorrect words: {nb_incorrect_words}"



# - Outputs -
for file in test_files:
	input_file = open(f"{input_folder}/{file}")
	
	text = [i.replace('\n', ' ') for i in input_file.readlines()]
	answer = print_answer(text)

	output_folder = sys.argv[3]
	output_file = open(f"{output_folder}/{file[:-4]}_n61655sb.txt", "w")
	output_file.write(answer)

	input_file.close()
	output_file.close()

