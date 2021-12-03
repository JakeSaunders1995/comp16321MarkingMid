import argparse

parser = argparse.ArgumentParser(description = "SpellChecking")
parser.add_argument('inputpath')
parser.add_argument('onputpath')
path = parser.parse_args()
inputPath = path.inputpath
outputPath = path.onputpath
inputStream = open(inputPath, "r")
inputContent = inputStream.read()

alphabet = open('..\\EnglishWords.txt', "r").read().split('\n')

upperNum = 0
punNum = 0
numberNum = 0
tmpContent = ''
for i in inputContent:
	if 48 <= ord(i) <= 57:
		numberNum += 1
	elif 65 <= ord(i) <= 90:
		upperNum += 1
		tmpContent += chr(ord(i) + 32)
	elif (97 <= ord(i) <= 122) or (i == ' '):
		tmpContent += i
	else:
		punNum += 1

wordsList = tmpContent.split(' ')
wordsList.remove('')
wordNum = len(wordsList)
incorrectNum = 0
for i in wordsList:
	if i in alphabet:
		pass
	else: 
		incorrectNum += 1

user_name = "c87452cd"
outputContent = user_name + '\n'
outputContent = "Formatting ###################\n"
outputContent += "Number of upper case words transformed: "
outputContent += str(upperNum)
outputContent += "\nNumber of punctuation's removed: "
outputContent += str(punNum)
outputContent += "\nNumber of numbers removed: "
outputContent += str(numberNum)
outputContent += "\nSpellchecking ###################\nNumber of words in file: "
outputContent += str(wordNum)
outputContent += "\nNumber of correct words in file: "
outputContent += str(wordNum - incorrectNum)
outputContent += "\nNumber of incorrect words in file: "
outputContent += str(incorrectNum)

print(outputContent)

outputStream = open(outputPath, "w")
outputStream.write(outputContent)
