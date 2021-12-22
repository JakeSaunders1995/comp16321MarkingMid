import argparse

# argparse
parser = argparse.ArgumentParser(description="Spellchecker")
parser.add_argument('dictionary', type=str, help='Input English Word file')
parser.add_argument('CheckerIndir', type=str, help='Input dir for checker')
parser.add_argument('CheckerOutdir', type=str, help='Output dir for checker')

args = parser.parse_args()

# read dictionary file strip space
dictionaryWords = []
dictionaryFile = open(args.dictionary, 'r')
for line in dictionaryFile:
	word = line.strip()
	dictionaryWords.append(word)
dictionaryFile.close()
# print(dictionaryWords)

dictionaryStr = ','.join([str(elem) for elem in dictionaryWords])
# print(dictionaryStr)

initialPunc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# read file and remove punctuation
with open(args.CheckerIndir, 'r') as f:
	inputFile = f.read()
removedPunc = []
for line in inputFile:
	wordsOnline = line.strip().split()	
	for word in wordsOnline:
		if word in initialPunc:
			inputFile = inputFile.replace(word, "")
			removedPunc.append(word)
#print(inputFile)

# remove number in text
removedNum = ''.join((item for item in inputFile if item.isdigit()))
textOnlyfile = ''.join((item for item in inputFile if not item.isdigit()))
# print(textOnlyfile)

# convert upper to Lower case
upperCase = sum(1 for elem in textOnlyfile if elem.isupper())
formattedFile = textOnlyfile.lower().split()
# print(formattedFile)

# compare text to dictionary
incorrect = []
for i in formattedFile:
	if i not in dictionaryStr:
		incorrect.append(i)
# print(len(incorrect))

print("y67506st")
print("Formatting ###################")
print("Number of upper case words transformed: " + str(upperCase))
print("Number of punctuation’s removed: " + str(len(removedPunc)))
print("Number of numbers removed: " + str(len(removedNum)))
print("Spellchecking ###################")
print("Number of words in file: " + str(len(formattedFile)))
print("Number of correct words in file: " + str(len(formattedFile) - len(incorrect)))
print("Number of incorrect words in file: " + str(len(incorrect)))