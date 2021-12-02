import os, argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('englishFile')
	parser.add_argument('input')
	parser.add_argument('output')
	args = parser.parse_args()
	for file in os.listdir(args.input):
		filepath = os.path.join(args.input, file)
		text = extractData(filepath)
		punctuation = ['.', '?', '!', ',', ':', ';', '-', '—', '–', '[', ']', '<', '>', '(', ')', '{', '}', '\'', '"', '...']
		list = []
		for i in range(len(text)):
			list.append(text[i])
		# end for
		cleanText = ''
		upperCase = 0
		punctuationRemoved = 0
		numbers = 0
		for i in range(len(list)):
			if list[i] in punctuation:
##				list.remove(list[i])
				punctuationRemoved += 1
			elif list[i].isdigit():
##				list.remove(list[i])
				numbers += 1
			elif ord(list[i]) >= 65 and ord(list[i]) <= 90:
				cleanText += chr(ord(list[i]) + 32)
				upperCase += 1
			else:
				cleanText += list[i]
			# end if
		# end for
		letterCounter = ''
		words = []
		for i in range(len(cleanText)):
			if cleanText[i] == ' ':
				if letterCounter == '': continue
				words.append(letterCounter)
				letterCounter = ''
			else:
				letterCounter += cleanText[i]
			# end if
		# end for
		if letterCounter not in ['\n', '']:
			words.append(letterCounter)
		# end if
		if '\n' in words:
			words.remove('\n')
		# end if
		'''
		if '@' in words:
			words.remove('@')
		# end if
		if '#' in words:
			words.remove('#')
		# end if
		'''
##		print(words)
		correctSpellings = 0
		incorrectSpellings = 0
		wordCount = 0
		dictionary = extractData(args.englishFile)
		for word in words:
			if word in dictionary:
				correctSpellings += 1
			else:
				incorrectSpellings += 1
			# end if
			wordCount += 1
		# end for
##		print(cleanText)
		result = outputName(file)
		result = os.path.join(args.output, result)
		f = open(result, 'w')
		f.write("n66033ai")
		f.write("\nFormatting ###################")
		f.write("\nNumber of upper case letters changed: " + str(upperCase))
		f.write("\nNumber of punctuations removed: " + str(punctuationRemoved))
		f.write("\nNumber of numbers removed: " + str(numbers))
		f.write("\nSpellchecking ###################")
		f.write("\nNumber of words: " + str(wordCount))
		f.write("\nNumber of correct words: " + str(correctSpellings))
		f.write("\nNumber of incorrect words: " + str(incorrectSpellings))
		f.close()
	# end for
# end def

def extractData(file):
	f = open(file, 'r')
	code = f.read()
	f.close()
	return code
# end def

def outputName(file):
	firstHalf = file[:-4]
	output = firstHalf + "_n66033ai.txt"
	return output
# end def

main()