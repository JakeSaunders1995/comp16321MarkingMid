import sys
import os
import string

textInput = sys.argv[1]
folderInput = sys.argv[2]
folderOutput = sys.argv[3]




for folder in os.listdir(folderInput):
		files = os.path.join(folderInput, folder)
		if os.path.isfile(files):

			fileRead = open(files, 'r')

			fileName = os.path.basename(files)

			shortfileName = os.path.splitext(fileName)[0]

			
			# try:
			# 	os.mkdir(folderOutput)
			# except:
			# 	os.chdir(folderOutput)
			if os.path.isdir(folderOutput):
				dirName = os.path.join(folderOutput, shortfileName + '_m83653ns.txt')
				fileNew = open(dirName, 'a')
				data = fileRead.read()
				sepWords = data.split()
				capitalCount = 0
				punctuationCount = 0
				numberCount = 0
				wordCount = 0
				correctCount = 0
				incorrectCount = 0
				txtfile_Open = open(textInput, 'r')
				txtfile_Read = txtfile_Open.read()
				txtfile_Sep = txtfile_Read.split()
				data_strip = data.translate(str.maketrans('', '', string.punctuation))
				data_strip_split = data_strip.split()
				
				

				fileNew.write('_m83653ns')
				fileNew.write('\nFormatting ###################')
				
				for word in range(0, len(data)):
					if data[word].isupper():
						capitalCount += 1
					if data[word] in ('!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\'', ']', '^', '_', '`', '{', '|', '}', '~'):
						punctuationCount += 1
					if data[word].isnumeric():
						numberCount += 1
				fileNew.write("\nNumber of upper case letters changed: " + str(capitalCount))
				fileNew.write("\nNumber of punctuations removed: " + str(punctuationCount))
				fileNew.write("\nNumber of numbers removed: " + str(numberCount))

				fileNew.write("\nSpellchecking ###################")
				wordCount = len(sepWords) - numberCount
				fileNew.write("\nNumber of words: " + str(wordCount))

				for word in data_strip_split:
					wordLower = word.lower()
					if wordLower in txtfile_Read:
						correctCount += 1
					else:
						incorrectCount += 1
	

				fileNew.write("\nNumber of correct words: " + str(correctCount))
				fileNew.write("\nNumber of incorrect words: " + str(incorrectCount))
			else:
				os.mkdir(folderOutput)
				 






