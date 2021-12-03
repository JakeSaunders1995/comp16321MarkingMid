import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument("englishWord")
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()

def format_check():
	upper_changed, punc_rm, num_rm = 0, 0, 0
	format_result = {'upper':'', 'punctuation':'', 'number':''}
	letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	new_str = ""
	for i in x:
		if i in letter_list:
			if i in letter_list[0:26]: # upper letter
				j = 0
				while i != letter_list[j]:
					j += 1
				new_str += letter_list[j + 26] # change to lower letter
				upper_changed += 1
			else:                      # lower letter
				new_str += i
		elif i in number_list:
			num_rm += 1
		elif i == " ":
			new_str += i
		elif i == "\n":
			continue
		else: # others should be punctuations
			punc_rm += 1
	format_result['upper'] = str(upper_changed)
	format_result['punctuation'] = str(punc_rm)
	format_result['number'] = str(num_rm)
	return new_str, format_result

def spell_check():
	input_word_list = []
	spell_result = {'num_total':'', 'num_correct':'', 'num_incorrect':''}
	local_str = new_str + " "
	# ensure bottem of string has at least one space as trigger
	while local_str[0] == " ":
		local_str = local_str[1: len(local_str)]
	# ensure string starts with a letter not a space
	single_word = ""
	for i in range(0, len(local_str)):
		if local_str[i] != " ":
			single_word += local_str[i]
		elif local_str[i] == " ":
			if local_str[i - 1] != " ":
				input_word_list.append(single_word)
				single_word = ""
			else:
				continue
	spell_result['num_total'] = str(len(input_word_list))
	falseWord, trueWord = 0, 0
	for word in input_word_list:
		if not word in word_list:
			falseWord += 1
		else:
			trueWord += 1
	spell_result['num_correct'] = str(trueWord)
	spell_result['num_incorrect'] = str(falseWord)
	return spell_result	


englishWord = open(args.englishWord)
word_list = []
for line in englishWord:
	line = line.rstrip('\n')
	word_list.append(line)

for file in os.listdir(args.input):
	readInput = open(os.path.join(args.input, file))
	x = readInput.read()
	
	new_str, format_result = format_check()
	spell_result = spell_check()
	content = "w21706bc\nFormatting ###################\nNumber of upper case letters changed: " + format_result['upper'] + "\nNumber of punctuations removed: " + format_result['punctuation'] + "\nNumber of numbers removed: " + format_result['number'] + "\nSpellchecking ###################\nNumber of words: " + spell_result['num_total'] + "\nNumber of correct words: " + spell_result['num_correct'] + "\nNumber of incorrect words: " + spell_result['num_incorrect'] + "\n"

	newFileName = str(file[0:len(file)-4]) + "_w21706bc.txt"
	writeOutput = open(os.path.join(args.output, newFileName), "w")
	writeOutput.write(content)