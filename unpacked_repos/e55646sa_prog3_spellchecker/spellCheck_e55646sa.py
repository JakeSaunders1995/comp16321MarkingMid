import argparse
import os

#Entire bulk of code here to decrypt. Made it into the function since it needed to get called multiple times due to the file path input ambiguity.
def spellCheck(textPath):
	#Opens the file to work with the string inside and sets up some variables for the formatting counters and to make the while loop possible.
	unfiltext = open(textPath, "r").read()
	text = ''
	upperRemoved = 0
	puncRemoved = 0
	numRemoved = 0
	wordList = ['']
	wordListIndex = 0
	wordsRight = 0

	#First removes puncuation, then removes numbers and skips spaces. At last, if the character still isn't alphabetic, then it will just be removed, but it won't count towards any counter.
	i = 0
	while i < len(unfiltext):
		if unfiltext[i] in ".?!,:;-–[]{{}}()'\"…":
			unfiltext = unfiltext.replace(unfiltext[i], '', 1)
			puncRemoved += 1
			continue
		elif unfiltext[i].isnumeric():
			unfiltext = unfiltext.replace(unfiltext[i], '', 1)
			numRemoved += 1
			continue
		elif unfiltext[i] == ' ':
			i += 1
			continue
		elif not unfiltext[i].isalpha():
			unfiltext = unfiltext.replace(unfiltext[i], '', 1)
			continue
		i += 1

	#Sets every letter to lower case. The counter is for every letter changed, even though the outputs all say words. A typo I'm assuming since my outputs are identical to the test outputs.
	i = 0
	while i < len(unfiltext):
		if unfiltext[i].isupper(): upperRemoved += 1
		text += unfiltext[i].lower()
		i += 1

	#This is the manual version of .split(). I did it this way because it gave me more control if I wished for it.
	i = 0
	while i < len(text):
		if text[i].isalpha():
			wordList[wordListIndex] += text[i]
		elif text[i] == ' ':
			wordList.append('')
			wordListIndex += 1
		i += 1

	#This both removed any empty words in the previous list, which can happen if there were two spaces next to each other. It then checked if it was in the english language.
	i = 0
	while i < len(wordList):
		if wordList[i] == '':
			wordList.pop(i)
			continue
		elif wordList[i] in englishWords:
			wordsRight += 1
		i += 1

	#This just set up the file path of the output file, using the inputted folder path, and changing the name as per specifications.
	output = open(args.Output_Path + '\\' + os.path.splitext(os.path.basename(textPath))[0] + "_e55646sa.txt", 'w')

	#Just writing the information into the file per instructions.
	output.write('e55646sa\n')
	output.write('Formatting ###################\n')
	output.write('Number of upper case words transformed: ' + str(upperRemoved) + '\n')
	output.write('Number of punctuation’s removed: ' + str(puncRemoved) + '\n')
	output.write('Number of numbers removed: ' + str(numRemoved) + '\n')
	output.write('Spellchecking ###################\n')
	output.write('Number of words in file: ' + str(len(wordList)) + '\n')
	output.write('Number of correct words in file: ' + str(wordsRight) + '\n')
	output.write('Number of incorrect words in file: ' + str(len(wordList) - wordsRight))

my_parser = argparse.ArgumentParser(description='Spell Checker')

my_parser.add_argument(
	'language',
    metavar='path',
    type=str,
    help='the english language in a text file')

my_parser.add_argument(
	'Input_Path',
    metavar='path',
    type=str,
    help='the path to the input file')

my_parser.add_argument(
	'Output_Path',
    metavar='path',
    type=str,
    help='the path to output directory')

args = my_parser.parse_args()

inputFolder = args.Input_Path


#Sets up a list with every english word in the english.txt
englishWords = []
for line in open(args.language, 'r'):
	line = line.rstrip()
	englishWords.append(line)


#Checks whether the input file path is a folder, then it would iterate through that folder and calculate for all text files in the folder.
if os.path.isdir(inputFolder):
	for entry in os.scandir(inputFolder):
	    if entry.path.endswith(".txt") and entry.is_file():
	        spellCheck(entry.path)
else:
	print("Please input a text file or an existing folder/directory")