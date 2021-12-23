import re

Dictionary = open("EnglishWords.txt" , "r")
Wordlist = []
for line in Dictionary:
	line.strip()
	Wordlist.append(line)

theWords = []
for space in Wordlist:
	theWords.append(space.replace("\n", ""))


exportedSentence = ""	
with open("test_file1.txt") as file: # input a new file here
	exportedSentence = file.readlines()

def listToSentence(s):
	strings = ""
	for words in s:
		strings += words
		return strings

def separatedLists(l):
	list = l.split()
	return list

sentence = listToSentence(exportedSentence)
upperAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerAlphabet = "abcdefghijklmnopqrstuvwxyz"
punctuations = ['...', '\"', "\'", '@', '?', '.', ',' ,'#', '!', '[', ']', '(' , ')', ';', ':']
numbers = "1234567890"

uppercase = 0
punctuationNumber = 0
misplacedNumbers = 0
correctSentence = ""

for st in range(len(sentence)):
	if(sentence[st: st + 3] == punctuations[0]):
		punctuationNumber += 1
		sentence = re.sub("[\.][\.][\.]", "", sentence)


for s in sentence:
	correctSentence += s
	for c in range(len(upperAlphabet)):
		if(s == upperAlphabet[c]):
			uppercase += 1
			correctSentence += lowerAlphabet[c]
			correctSentence = correctSentence.replace(upperAlphabet[c], "")

	for p in range(len(punctuations)):
		if(s == punctuations[p]):
			punctuationNumber += 1
			correctSentence = correctSentence.replace(punctuations[p], "")
					
	for n in range(len(numbers)):
		if(s == numbers[n]):
			misplacedNumbers += 1
			correctSentence = correctSentence.replace(numbers[n], "")

SentenceList = correctSentence.split()

textPosition = 0
correctWords = 0


for i in range(len(SentenceList)):
	totalwords = i + 1
	for word in theWords:
		if(SentenceList[i] == word):
			correctWords += 1
			break


incorrectWords = totalwords - correctWords

f = open("test_file1_f11711jy.txt", "w") #exported file
f.write("f11711jy\n")
f.write("Formatting ###################\n") 
f.write("Number of upper case words changed: " + str(uppercase) + "\n")
f.write("Number of punctuations removed: "  + str(punctuationNumber) + "\n")
f.write("Number of numbers removed: " + str(misplacedNumbers) + "\n")
f.write("Spellchecking ###################\n")
f.write("Number of words: " + str(totalwords) + "\n")
f.write("Number of correct words: " + str(correctWords) + "\n")
f.write("Number of incorrect words: " + str(incorrectWords) + "\n")
f.close()


	    





