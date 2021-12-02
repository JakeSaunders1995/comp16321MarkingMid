import os, argparse, re

args = None
textfile_pattern = None
dictionary = []
# creates global variables for each of the conditions
upper_count = 0
punctuation_count = 0
number_count = 0
word_count = 0
correct_count = 0
incorrect_count = 0


# gets command line arguments and validates their format
def get_args():
	# take arguments from command line
	global args, textfile_pattern
	parser = argparse.ArgumentParser(description='Formats and checks spelling for text documents')
	parser.add_argument('wordspath',help='file path to EnglishWords.txt containing a list of valid english words')
	parser.add_argument('inpath',help='directory containing only .txt files to read input from')
	parser.add_argument('outpath',help='directory to write .txt output files to')
	args = parser.parse_args()
	
	# prints an error and quits if the input folder doesn't exist, creates the output folder if it doesn't exist
	if not os.access(args.inpath,os.F_OK):
		print("Error: Input folder doesn't exist")
		raise SystemExit
	if not os.access(args.outpath,os.F_OK):
		os.mkdir(args.outpath)

	# prints an error and quits if the words path doesn't end with EnglishWords.txt
	if not re.search('[a-zA-Z0-9_/~]+EnglishWords.txt',args.wordspath):
		print("Error: Words path should be a complete file path to EnglishWords.txt (i.e. including EnglishWords.txt")
		raise SystemExit

	# tries to open EnglishWords.txt. Prints an error and quits if the file doesn't exist or the path is wrong in some way
	try:
		words_file = open(args.wordspath)
	except FileNotFoundError:
		print("Error: Words file not found at the given path")
		raise SystemExit

	# reads the words file line by line, removes the '/n' and appends to the list of words
	for line in words_file:
		dictionary.append(line[:-1])
	words_file.close()

	textfile_pattern = re.compile('^[a-zA-Z0-9_/~]+.txt$')

	# starts loop
	loop_files()


# loops through files in the given directory and performs the spell check on each one
def loop_files():
	global args, textfile_pattern, upper_count, punctuation_count, number_count, word_count,correct_count,incorrect_count
	# loops through files in the provided directory
	for file in os.listdir(args.inpath):
		# skips to the next file if the current file is not .txt
		if not textfile_pattern.search(file):
			continue
		
		with open(f'{args.inpath}/{file}') as f:
			file_lines = f.readlines()

		# replaces upper case, punctuation and number, and counts each one
		upper_count = 0
		punctuation_count = 0
		number_count = 0
		file_lines = format_text(file_lines)
			
		# counts the number of words and how many are/aren't in the dictionary
		word_count = 0
		correct_count = 0
		incorrect_count = 0
		spell_check(file_lines)

		# writes the results to the output file in the desired format
		write_output(file)


# for every line in the list passed to this method, removes all characters that are not a letter or space, and lowers all upper case letters
def format_text(file_lines):
	global upper_count, punctuation_count, number_count
	new_lines = []
	for line in file_lines:
		# checks for ellipses or any other punctuation character (makes sure ... is only counted as +1)
		punctuation_count += len(re.findall('\.\.\.|['+re.escape('.?!,:;-(){}[]"')+'\']',line))
		number_count += len(re.findall('[0-9]',line))
		upper_count += len(re.findall('[A-Z]',line))
		# removes all non-letter characters and lowers
		line = re.sub('[^a-zA-Z ]','',line).lower()
		new_lines.append(line)
	return new_lines



# splits each line by space and then loops through words, tallying how many are/aren't in the dictionary 
def spell_check(file_lines):
	global word_count, correct_count, incorrect_count
	for line in file_lines:
		line = line.split(' ')
		for word in line:
			# ignores the case of 2 consecutive spaces, which is possible after removing all numbers and punctuation
			if word == '':
				continue
			word_count += 1

			if word in dictionary:
				correct_count += 1
			else:
				incorrect_count += 1


def write_output(file):
	with open(f'{args.outpath}/{file[:-4]}_w16910dg.txt','w') as f:
		f.write('w16910dg\n')
		f.write('Formatting ###################\n')
		f.write(f'Number of upper case letters changed: {upper_count}\n')
		f.write(f'Number of punctuations removed: {punctuation_count}\n')
		f.write(f'Number of numbers removed: {number_count}\n')
		f.write(f'Spellchecking ###################\n')
		f.write(f'Number of words: {word_count}\n')
		f.write(f'Number of correct words: {correct_count}\n')
		f.write(f'Number of incorrect words: {incorrect_count}\n')



get_args()
