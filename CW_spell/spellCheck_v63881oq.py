import argparse,os,re

def get_filepaths(): # Gets filepath arguments from command line
	parser = argparse.ArgumentParser(description="I/O Filepaths")
	parser.add_argument("englishWordsFilepath", type=str, help="English Words Filepath")
	parser.add_argument("input_folder", type=str, help="Input Folder Path")
	parser.add_argument("output_folder", type=str, help="Output Folder Path")
	return parser.parse_args()

def ammend_string(string):
	upperAmmended = 0
	puncRemoved = 0
	numsRemoved = 0
	charIndex = 0
	while True:
		try:
			charCode = ord(string[charIndex])
		except IndexError:
			break

		if (33 <= charCode <= 47) or (58 <= charCode <= 64) or (91 <= charCode <= 96) or (123 <= charCode <= 127):
			string = string[:charIndex] + string[(charIndex+1):] 
			puncRemoved += 1
			print(string)
		elif (48 <= charCode <= 57):
			string = string[:charIndex] + string[(charIndex+1):]
			numsRemoved += 1
			print(string)
		elif (65 <= charCode <= 90):
			string = string[:charIndex] + string[charIndex].lower() + string[(charIndex+1):]
			upperAmmended += 1
			charIndex += 1
		else:
			charIndex += 1
	return string, upperAmmended, puncRemoved, numsRemoved

def spell_check(word,englishWords,charIndex,string,incorrectWordCount,correctWordCount):
	if (re.search("^"+word+"\n|\n"+word+"\n|\n"+word+"$",englishWords) == None):
		incorrectWordCount += 1
	else:
		correctWordCount += 1
	print(word)
	
	while True:
		try:
			if (string[charIndex+1] == " " or string[charIndex+1] == "\n"):
				charIndex += 1
			else:
				break
		except IndexError:
			break
	return incorrectWordCount, correctWordCount

def check_string(string, englishWords):
	wordCount = 0
	correctWordCount = 0
	incorrectWordCount = 0
	word = ""
	charIndex = 0
	while True:
		try:
			character = string[charIndex]
		except IndexError:
			break
		if (character != " " and character != "\n" and character != ""):
			word += character
			if (charIndex == len(string) - 1):
				wordCount += 1
				incorrectWordCount, correctWordCount = spell_check(word,englishWords,charIndex,string,incorrectWordCount,correctWordCount)
		else:
			if word != "":
				wordCount += 1
				incorrectWordCount, correctWordCount = spell_check(word,englishWords,charIndex,string,incorrectWordCount,correctWordCount)
			word = ""
		charIndex += 1
	return wordCount, correctWordCount, incorrectWordCount

folderPathArgs = get_filepaths()

for fileName in os.listdir(folderPathArgs.input_folder):

	with open(folderPathArgs.input_folder+"/"+fileName,"r") as file:
		inputString = file.read()

	inputString, upperAmmended, puncRemoved, numsRemoved = ammend_string(inputString)

	with open(folderPathArgs.englishWordsFilepath) as file:
		englishWords = file.read()

	wordCount, correctWordCount, incorrectWordCount = check_string(inputString,englishWords)

	outputString = "v63881oq\nFormatting ###################\nNumber of upper case words changed: %s\nNumber of punctuations removed: %s\nNumber of numbers removed: %s\nSpellchecking ###################\nNumber of words: %s\nNumber of correct words: %s\nNumber of incorrect words: %s\n"%(upperAmmended,puncRemoved,numsRemoved,wordCount,correctWordCount,incorrectWordCount)

	with open(folderPathArgs.output_folder+"/"+fileName[:-4]+"_v63881oq.txt","w") as file:
		file.write(outputString)



