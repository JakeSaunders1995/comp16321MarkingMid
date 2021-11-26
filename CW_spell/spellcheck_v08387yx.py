import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('EnglishWords')
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()

def filelist(input_file):
	file_path_list = []
	for file in os.listdir(input_file):
		file_path = os.path.join(input_file,file)
		file_path_list.append(file_path)
	return(file_path_list)

l = filelist(args.input_file)
d = open(args.EnglishWords,"r")
dictionary = []
for line in d:
	line = line.rstrip()
	dictionary.append(line)

num = "1234567890"
punctuation = [".", "?", "!", ",", ":", ";", "—", "-", "[", "]", "{", "}", "(", ")", "'", '"', "..."]
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

for name in l:
	f_input = open(name)
	text = f_input.read()
	checklist = []
	word_list = text.split(" ")
	numberCount = 0
	punctuationCount = 0
	uppercaseCount = 0
	correctCount = 0
	wrongCount = 0
	Position = 0
	numberWords = 0
	for Word in word_list:
		temp = ""
		wordPosition = 0
		while wordPosition < len(Word):
			if Word[wordPosition] in num:
				numberCount += 1
			elif Word[wordPosition] in punctuation:
				punctuationCount += 1
			elif Word[wordPosition] in uppercase:
				uppercaseCount += 1
				lc = Word[wordPosition].lower()
				temp = temp + lc
			elif Word[wordPosition] in lowercase:
				temp = temp + Word[wordPosition]
			wordPosition += 1
		if temp != "":
			checklist.append(temp)
	for w in checklist:
		if w in dictionary:
			correctCount += 1
		else:
			wrongCount += 1
	numberWords = len(checklist)
	wrongCount = numberWords - correctCount
	result = "v08387yx\nFormatting ##################\nNumber of upper case letters changed:" + str(uppercaseCount) + "\nNumber of punctuations removed:" + str(punctuationCount) + "\nNumber of numbers removed:" + str(numberCount) + "\nSpellchecking ###################\nNumber of words:" + str(numberWords) + "\nNumber of correct words:" + str(correctCount) + "\nNumber of incorrect words:" + str(wrongCount)
	f_input.close()
	basename = os.path.basename(name)
	filename = basename.split(".txt")
	filename.append("_v08387yx.txt")
	file_name = ''.join(filename)
	output_file_name = os.path.join(args.output_file,file_name)
	f_output = open(output_file_name,"w")
	f_output.write(result)
	f_output.close()