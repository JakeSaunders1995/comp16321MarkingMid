import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('wordsfile')
parser.add_argument('inputfile')
parser.add_argument('outputfile')
args = parser.parse_args()

wordspath = args.wordsfile
filepath = args.inputfile
outfilepath = args.outputfile


file = open(wordspath, 'r')
words = file.read().split()
file.close()

for file in os.listdir(filepath):
	with open(filepath + "/" + file) as f:
		inp = f.readlines()

	inp = ' '.join(i for i in inp)
	print(inp)
	up = 0
	punc = 0
	num = 0

	for i in inp:
		if i.isdigit():
			num += 1
	inp = ''.join([i for i in inp if not i.isdigit()])
#	for i in inp:
#		if not (i.isalpha() or i == " " or i == "\n" or i == "#" or i == "@"):
#			punc += 1

#ellipsis stuff:
	count = 0
	end = len(inp)
	inp += " a b c"
	while count <= end:
		if not (inp[count].isalpha() or inp[count] == " " or inp[count] == "\n" or inp[count] == "#" or inp[count] == "@"):
			if inp[count] == "." and inp[count + 1] == "." and inp[count + 2] == ".":
				punc += 1
				count += 3
			else:
				punc += 1
				count += 1
		else:
			count += 1
	inp = inp[:-6]
	inp = ''.join(i for i in inp if i.isalpha() or i == " ")
	for i in inp:
		if i != " " and i == i.upper():
			up += 1
	inp = inp.lower()

	inp = inp.split()
	numWords = len(inp)
	correct = 0
	incorrect = 0

	for word in inp:
		if word in words:
			correct += 1
		else:
			incorrect += 1

	print(inp)
	print("up:",up)
	print("punc", punc)
	print("num", num)
	print("len", numWords)
	print("correct", correct)
	print("incorrect", incorrect)

	newfilepath = outfilepath + "/" + file[:-4] + "_q78216ae.txt"
	file = open(newfilepath, 'w')
	file.write("q78216ae\nFormatting " + "###################\nNumber of upper case letters changed: " + str(up))
	file.write("\nNumber of punctuations removed: " + str(punc) + "\nNumber of numbers removed: " + str(num))
	file.write("\nSpellchecking " + "###################\nNumber of words: " + str(numWords))
	file.write("\nNumber of correct words: " + str(correct) + "\nNumber of incorrect words: " + str(incorrect))
	file.close()
