import os
import argparse

arg_parser = argparse.ArgumentParser(description="Spellchecking")
arg_parser.add_argument('english_words')
arg_parser.add_argument('input_folder')
arg_parser.add_argument('output_folder')
args = arg_parser.parse_args()

punctuation = "-–—−?!,:;(){}[]'\"." # doesnt include ... handled separately

with open(args.english_words, "r") as file:
	words = file.read().split('\n')

for file_name in os.listdir(args.input_folder):
	with open(args.input_folder + "/" + file_name, "r") as file:
		contents = file.read()

	numbers_removed = 0
	uppercase_transformed = 0
	punctuation_removed = 0

	incorrect_words = 0
	word_count = 0

	alphabet = "abcdefghijklmnopqrstuvwxyz"

	# ------ STRIPPING PROCESS --------
	stripped = ""

	i = 0

	while i < len(contents):

		char = contents[i]
		if char in "1234567890":
			# rm numbers
			numbers_removed += 1
		elif char in alphabet.upper():
			# uppercase
			uppercase_transformed += 1
			stripped += char.lower()
		elif char in punctuation:
			if char == '.':
				if i+2 < len(contents) and contents[i+1] == '.' and contents[i+2] == '.':
					# ellipsis
					punctuation_removed += 1
					i += 2 # will skip ahead 2 overall as incremented at the end too
				else:
					punctuation_removed += 1
			else:
				punctuation_removed += 1
		elif char in alphabet or char == ' ':
			# must be alphabetical
			stripped += char
		i += 1

	contents_words = list(filter(None, stripped.split(' ')))

	word_count = len(contents_words)

	for word in contents_words:
		if word not in words:
			incorrect_words += 1

	to_write = f'''h96407tf
Formatting ###################
Number of upper case letters changed: {uppercase_transformed}
Number of punctuations removed: {punctuation_removed}
Number of numbers removed: {numbers_removed}
Spellchecking ###################
Number of words: {word_count}
Number of correct words: {word_count - incorrect_words}
Number of incorrect words: {incorrect_words}
'''

	output_file = file_name.split('.')[0] + "_h96407tf.txt"

	with open(args.output_folder + "/" + output_file, "w") as file:
		file.write(to_write)