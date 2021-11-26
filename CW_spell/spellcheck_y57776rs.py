import sys
import os
import string
argumentlist = sys.argv
words = str(argumentlist[1])
inputfolder = str(argumentlist[2])
outputfolder = str(argumentlist[3])
file_name = "_y57776rs.txt"

def numbers(sentances):
	count = 0
	for i in sentances:
		if (i == "0") or (i == "1") or (i == '2') or (i == '3') or (i == '4') or (i == '5') or (i == '6') or (i == '7') or (i == '8') or (i == '9'):
			count = count + 1
	return(count)

def removenumbers(sentances):
	sentances = sentances.replace("0", '')
	sentances = sentances.replace("1", '')
	sentances = sentances.replace("2", '')
	sentances = sentances.replace("3", '')
	sentances = sentances.replace("4", '')
	sentances = sentances.replace("5", '')
	sentances = sentances.replace("6", '')
	sentances = sentances.replace("7", '')
	sentances = sentances.replace("8", '')
	sentances = sentances.replace("9", '')
	return(sentances)

def punctuation(sentances):
	count = 0
	for i in sentances:
		if (i == ".") or (i == "?") or (i == '!') or (i == ',') or (i == ':') or (i == ';') or (i == '-') or (i == '(') or (i == ')') or (i == '{') or (i == '}') or (i == '"') or (i == "'") or (i == "[") or (i == "]") or (i == "@") or (i == "#"):
			count = count + 1
	return(count)

def removepunctuation(sentances):
	sentances = sentances.replace(".", '')
	sentances = sentances.replace("?", '')
	sentances = sentances.replace("!", '')
	sentances = sentances.replace(",", '')
	sentances = sentances.replace(":", '')
	sentances = sentances.replace("-", '')
	sentances = sentances.replace("(", '')
	sentances = sentances.replace(")", '')
	sentances = sentances.replace("{", '')
	sentances = sentances.replace("}", '')
	sentances = sentances.replace('"', '')
	sentances = sentances.replace("'", '')
	sentances = sentances.replace("[", '')
	sentances = sentances.replace("]", '')
	sentances = sentances.replace("@", '')
	sentances = sentances.replace("#", '')
	return(sentances)

def numofwords(sentances):
	word_list = sentances. split()
	number_of_words = len(word_list)
	return(number_of_words)

def correctwords(sentances, wordlist):
	count = 0
	word_list = sentances.split()
	correctwordlist = wordlist.split()
	for i in word_list:
		if i in correctwordlist:
			count = count + 1
	return(count)
	

basepath = inputfolder + "/"
with os.scandir(basepath) as entries:
       for entry in entries:
                if entry.is_file():
                        filename = entry.path
                        name = os.path.basename(filename).split('.')[0]
                        newname = name + file_name
                        completeName = os.path.join(outputfolder, newname)
                        f = open(str(filename), "r")
                        file = str(f.read())
                        y = open(words, "r")
                        x = open(completeName, "a")
                        wordfile = str(y.read())
                        print(name)
                        print("y57776rs")
                        x.write("y57776rs")
                        x.write('\n')
                        print("Formatting ###################")
                        x.write("Formatting ###################")
                        x.write('\n')
                        uppercase = sum(1 for c in file if c.isupper())
                        print("Number of upper case words changed: " + str(uppercase))
                        x.write("Number of upper case words changed: " + str(uppercase))
                        x.write('\n')
                        file = file.lower()
                        print("Number of punctuations removed: " + str(punctuation(file)))
                        x.write("Number of punctuations removed: " + str(punctuation(file)))
                        x.write('\n')
                        file = removepunctuation(file)
                        print("Number of numbers removed: " + str(numbers(file)))
                        x.write("Number of numbers removed: " + str(numbers(file)))
                        x.write('\n')
                        file = removenumbers(file)
                        print("Spellchecking ###################")
                        x.write("Spellchecking ###################")
                        x.write('\n')
                        number = numofwords(file)
                        print("Number of words: " + str(number))
                        x.write("Number of words: " + str(number))
                        x.write('\n')
                        numofcwords = correctwords(file, wordfile)
                        print("Number of correct words: " + str(numofcwords))
                        x.write("Number of correct words: " + str(numofcwords))
                        x.write('\n')
                        incorrectwords = number - numofcwords
                        print("Number of incorrect words: " + str(incorrectwords))
                        x.write("Number of incorrect words: " + str(incorrectwords))
                        x.close()
                        f.close()
                        y.close()
