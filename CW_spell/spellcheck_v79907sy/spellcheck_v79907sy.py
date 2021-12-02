import argparse
import os

def format(wordContent):
	f1.write("v79907sy")
	f1.write("\nFormatting ###################")
	wordContent = upperCase(wordContent)
	wordContent = punctuation(wordContent)
	wordContent = numbers(wordContent)
	elements = ""
	for i in wordContent:
		elements += i
	return elements

def upperCase(wordContent):
	count = 0
	place = 0
	for i in wordContent:
		if 65<=ord(i)<=90:
			wordContent[place] = chr(ord(i) + 32)
			count += 1
		place += 1
	f1.write("\nNumber of upper case words changed: " + str(count))
	return wordContent

def numbers(wordContent):
	count = 0
	place = 0
	for index in wordContent:
		if index.isdigit() == True:
			wordContent[place] = ""
			count += 1
		place += 1
	f1.write("\nNumber of numbers removed: " + str(count))
	return wordContent

def punctuation(wordContent):
	count = 0
	w = ""
	for i in wordContent:
		w += i
	time = w.count(". . .")
	count = 0
	place = 0
	for index in wordContent:
		if 33<=ord(index)<=34:
			wordContent[place] = ""
			count += 1
		elif 36<=ord(index)<=47:
			wordContent[place] = ""
			count += 1
		elif 123<=ord(index)<=126:
			wordContent[place] = ""
			count += 1
		elif 91<=ord(index)<=95:
			wordContent[place] = ""
			count += 1
		elif 58<=ord(index)<=64:
			wordContent[place] = ""
			count += 1
		place += 1
	count -= time*2
	f1.write("\nNumber of punctuations removed: " + str(count))
	return wordContent

def SpellCheck(wordContent,Englishword_Content):
	f1.write("\nSpellchecking ###################")
	wordNumber(wordContent)
	wordCheck(wordContent,Englishword_Content)
	return wordContent

def wordNumber(wordContent):
	count = len(wordContent)
	f1.write("\nNumber of words in file: " + str(count))

def wordCheck(wordContent,Englishword_Content):
	correctWord_count = 0
	incorrectWord_count = 0

	for index in wordContent:
		result = Englishword_Content.count(index)
		if result == 0:
			incorrectWord_count += 1
		else:
			correctWord_count += 1

	f1.write("\nNumber of correct words in file: " + str(correctWord_count))
	f1.write("\nNumber of incorrect words in file: " + str(incorrectWord_count))

parser = argparse.ArgumentParser(description='input the txt files')
parser.add_argument("Englishword_file",type=str)
parser.add_argument("input_file",type=str)
parser.add_argument("output_file",type=str)
args = parser.parse_args()
Englishword_path = args.Englishword_file
input_path = args.input_file
output_path = args.output_file

with open(Englishword_path,"r") as f:
	EnglishWord = f.readlines()
	f.close()
Englishword_Content = [word.strip() for word in EnglishWord if word.strip()!='']

os.chdir(input_path)
files = os.listdir(input_path)
files.sort()
file_count = 1
for file in files:
	with open(file,"r+") as f:
		content = f.readlines()
		f.close()
	wordsContent = content[0]
	wordContent = []
	for i in wordsContent:
		wordContent.append(i)

	os.chdir(output_path)
	file_name = "test_file" + str(file_count) +"_v79907sy.txt"
	with open(file_name, "w") as f1:
		wordContents = format(wordContent)
		wordContent = wordContents.split()
		SpellCheck(wordContent, Englishword_Content)
		f1.close()
	file_count += 1
	os.chdir(input_path)

