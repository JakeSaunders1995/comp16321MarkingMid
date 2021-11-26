import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("english_words_path")
parser.add_argument("input_path")
parser.add_argument("output_path")

p = parser.parse_args()
spellingReference = open(p.english_words_path, "r")



def spellCheck(englishWordsList, lines):
	numberOfDigits = 0
	numberOfPunctuation = 0
	numberOfCapitalLetters = 0
	numberOfCorrectlySpelledWords = 0
	numberOfIncorrectlySpelledWords = 0

	punc = [".","?","!",",",":",";","‐","–","(",")","{","}","[","]","'","...",'"']
	newLines = []
	periodsInaRow = 0
	for word in lines:
		temp = ""
		for index,char in enumerate(word):
			# if not char.isdigit() and (not in punc) and not char.isupper():
			# 	temp+=char
			if char.isdigit():
				periodsInaRow = 0
				numberOfDigits += 1
				continue
			elif char in punc:
				if char == ".":
					periodsInaRow += 1
					if index == len(word) - 1 and periodsInaRow == 3:
						numberOfPunctuation -= 2
						periodsInaRow = 0
					elif periodsInaRow == 3 and word[index+1] != ".":
						numberOfPunctuation -= 2
						periodsInaRow = 0
				else:
					periodsInaRow = 0
				numberOfPunctuation += 1
				continue
			elif char.isupper():
				numberOfCapitalLetters += 1
				periodsInaRow = 0
				temp += char.lower()
				continue
			periodsInaRow = 0
			temp += char
		newLines.append(temp)
		numberOfPunctuation -= int(word.count('"') / 2)



	words = []
	for line in newLines:
		if " " not in line:
			if line[0] == '"':
				words.append(line[1:-1])
			else:
				words.append(line)
			continue
		start = 0
		end = 0
		firstSpace = True
		for index,char in enumerate(line):
			if char == " ":
				if firstSpace:
					start = 0
					firstSpace = False
				else:
					start = end + 1
				end = index
				if line[start:end] == "":
					continue
				if line[start:end][0] == '"':
					words.append(line[start+1: end - 1])
					numberOfPunctuation += 2
					continue
				words.append(line[start:end])
			if index == len(line) - 1:
				if line[start:end] == "":
					continue
				words.append(line[end+1:len(line)])


	for word in words:
		if word in englishWordsList:
			numberOfCorrectlySpelledWords +=1
		else:
			numberOfIncorrectlySpelledWords +=1

	if words[-1] == '':
		words.remove('')
		numberOfIncorrectlySpelledWords -= 1

	return numberOfCapitalLetters, numberOfPunctuation, numberOfDigits, len(words), numberOfCorrectlySpelledWords, numberOfIncorrectlySpelledWords



def removeNewLine(line):
	if line[-1] != "\n":
		return line
	return line[:-1]


englishWords = map(removeNewLine, spellingReference.readlines())

englishWordsList = []

for englishWord in englishWords:
	englishWordsList.append(englishWord)

for index, filename in enumerate(os.listdir(p.input_path)):
	if filename.endswith(".txt"):
		input = open(os.path.join(p.input_path, filename), "r")
		lines = map(removeNewLine, input.readlines())
		one, two, three, four, five, six = spellCheck(englishWordsList, lines)
		output = open(os.path.join(p.output_path, "test_file{}_r89835eb.txt".format(os.path.join(p.input_path, filename)[-5])), "w")
		toBeWritten = "r89835eb\nFormatting ###################\nNumber of upper case letters changed: {}\nNumber of punctuations removed: {}\nNumber of numbers removed: {}\nSpellchecking ###################\nNumber of words: {}\nNumber of correct words: {}\nNumber of incorrect words: {}".format(one,two,three,four,five,six)
		output.write(toBeWritten)
		input.close()
		output.close()
	else:
		pass

spellingReference.close()