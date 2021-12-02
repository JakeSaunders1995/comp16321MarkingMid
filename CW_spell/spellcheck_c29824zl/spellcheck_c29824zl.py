import os, argparse

#to get the input information.
def commandSystem(state):
    parser = argparse.ArgumentParser(description='Path of the Input and Output')
    parser.add_argument('englishWords', type=str, help='EnglishWordsList')
    parser.add_argument('inputFolder', type=str, help='Input Folder Path')
    parser.add_argument('outputFolder', type=str, help='Output Folder Path')
    args = parser.parse_args()

    folderIput = args.inputFolder
    dirsIput = os.listdir(folderIput)
    dictIput = args.englishWords 	

    if state == 1:
        for file1 in dirsIput:  
            filePath = os.path.join(folderIput, file1)
            fileCotent = open(filePath, "rt")
            content = fileCotent.read()
            fileCotent.close()
            content_lis.append(content)
        return content_lis

    if state == 0:
        folderOput = args.outputFolder
        for file1 in dirsIput:
            file2 = file1[:-4] + "_c29824zl.txt"
            outputPath = os.path.join(folderOput, file2)
            path_lis.append(outputPath)
        return path_lis

    if state == 2:
    	dictionary = list()
    	with open(dictIput) as file:
    		dictionary = file.readlines()

    	dictionary = [line.rstrip('\n') for line in open(dictIput)]
    	file.close()
    	return dictionary

def removeNum(target):
	lis = []
	i = 0
	for item in target:
		if item in "0123456789":
			i += 1
		else:
			lis.append(item)
	content = ("".join(lis))
	return content,i

def removePunctuation(target):
	lis = list(target.split(' '))
	lis_content = []
	i = 0
	lis_punc = [".", "?", "!", ",", ":", ";", "-", "_", "'", '"', "(", ")", "{", "}", "[", "]", "—", "..."]

	for ii in lis:
		for j in lis_punc:
			if j in ii:
				if j == "...":
					i += 1
					singleletter = []
					singleletter1 = []
					singleletter.append(ii)
					lis.remove(ii)
					singlestr = ("".join(singleletter))
					for item in singlestr:
						if item != ".":
							singleletter1.append(item)
							part_content = ("".join(singleletter1))
					lis.append(part_content)
	
	content = (" ".join(lis))
	for item in content:
		if item in lis_punc:
			i += 1
		else:
			lis_content.append(item)
	content = ("".join(lis_content))
	return content,i

def changeUpper(target):
	lis_word = list(target.split(' '))
	#print(lis_word)
	i = 0
	count = 0
	content = ""
	while i < len(lis_word):
		word = ""
		for item in lis_word[i]:
			if 65 <= ord(item) <= 90:
				upperNum = ord(item) + 32
				lowerLetter = chr(upperNum)
				count += 1
			else:
				lowerLetter = item
			
			word += lowerLetter
		word += " "
		content += word	
		i += 1
	return content,count

def spellCheck(target, dictList):
	lis_input = list(target.split(' '))
	
	#remover the space
	lis_word = []
	for item in lis_input:
		if item != '':
			if item != '\n':	
				lis_word.append(item)
	count = 0
	wordList = []
	while count < len(lis_word):
		word = ""
		for item in lis_word[count]:
			if item != '\n':
				word += item
		wordList.append(word)
		count += 1
	
	word = len(wordList)
	i = 0
	correctWord = 0
	incorrectWord = 0
	while i < len(wordList):
		if wordList[i] in dictList:
			correctWord += 1
		else:
			incorrectWord += 1
		i += 1

	return word, correctWord, incorrectWord

def textEdit(path, upperCase, punct, num, word, correct, incorrect):
	f = open(path, "w")
	f.write("c29824zl\n")
	f.write("Formatting ###################\n")
	f.write("Number of upper case letters changed: " + str(upperCase) + "\n")
	f.write("Number of punctuations removed: " + str(punct) + "\n")
	f.write("Number of numbers removed: " + str(num) + "\n")
	f.write("Spellchecking ###################\n")
	f.write("Number of words: " + str(word) + "\n")
	f.write("Number of correct words: " + str(correct) + "\n")
	f.write("Number of incorrect words: " + str(incorrect) + "\n")
	f.close()


#Actual program start here.
content_lis = []
path_lis = []
i = 0
commandSystem(1)
commandSystem(0)
dictList = commandSystem(2)
while i < len(content_lis):
	singleText = content_lis[i]
	content1 = removeNum(singleText)[0]
	count1 = removeNum(singleText)[1]
	content2 = removePunctuation(content1)[0]
	count2 = removePunctuation(content1)[1]
	content3 = changeUpper(content2)[0]
	count3 = changeUpper(content2)[1]
	word = spellCheck(content3, dictList)[0]
	correct = spellCheck(content3, dictList)[1]
	incorrect = spellCheck(content3, dictList)[2]
	textEdit(path_lis[i], count3, count2, count1, word, correct, incorrect)
	i += 1