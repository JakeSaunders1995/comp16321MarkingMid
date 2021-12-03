import sys
import re
wordsChanged = 0
punctuationsRemoved = 0
numbersRemoved = 0
print(sys.argv)
test = open(sys.argv[2] , "r")
text = test.readline()
print(text)
cleanText = re.sub('[^A-Za-z]', ' ', text)
cleanBigChar = re.sub('[^A-Z]', '', text)
print(cleanBigChar)
wordsChanged = len(cleanBigChar)
cleanNumbers = re.sub('[^0-9]','', text)
if cleanNumbers != '':
	numbersRemoved = len(cleanNumbers)
print(len(text), "-", len(cleanText),"+", numbersRemoved)

count2 = text.count('.')
count3 = text.count('?')
count4 = text.count('!')
count5 = text.count(',')
count6 = text.count(':')
count7 = text.count(';')
count8 = text.count('–')
count9 = text.count('-')
count10 = text.count('[')
count11 = text.count('{')
count12 = text.count('(')
count13 = text.count('"')
count14 = text.count("'")
count15 = text.count(']')
count16 = text.count('}')
count17 = text.count(')')


countSum = count2 +count3 +count4 +count5 +count6 +count7 +count8 +count9 +count10 +count11 +count12 +count13 +count14 +count15 +count16 +count17 

if "..." in text :
	countSum-=2



cleanText = cleanText.lower()

print(cleanText)
words = cleanText.split()
for word in words:
	if len(word) <= 1 and word != "a" and word != "an":
		words.remove(word)
print(words)
correctWords = 0
with open(sys.argv[1]) as file: 
	for line in file:
		line = str(line[:-1])
		for word in words:
			if line == word:
				correctWords += 1
incorrectWords = len(words) - correctWords
f = open(sys.argv[3],"a")
f.write("d62825cd\n")
f.write("Formatting ###################\n")
f.write("Number of upper case words changed: {}\n".format(wordsChanged))
f.write("Number of punctuations removed: {}\n".format(countSum)) 
f.write("Number of numbers removed: {}\n".format(numbersRemoved))
f.write("Spellchecking ###################\n")
f.write("Number of words: {}\n".format(len(words)))
f.write("Number of correct words: {}\n".format(correctWords))
f.write("Number of incorrect words: {}\n".format(incorrectWords))

f.close()