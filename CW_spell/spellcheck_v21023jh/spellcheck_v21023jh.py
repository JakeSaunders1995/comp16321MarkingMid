import os
import os.path
import sys
inputDir = sys.argv[1]  
inputDir2 = sys.argv[2]
outputDir = sys.argv[3]
englishWords = open(inputDir , 'r')
dictionary = englishWords.read()
dictionaryLst = dictionary.split()
for filename in os.listdir(inputDir2):
	file = open(inputDir2+"/"+filename, 'r')
	string = file.read()
	outputfname = filename[:-4]
	path= outputDir
	punctuationCount = 0
	digitCount = 0
	upperCount = 0 
	wordCount = 0
	correctWords = 0
	incorrectWords = 0



	text = ''
	numbers = ["1","2","3","4","5","6","7","8","9","0"]
	punctuation = ['.','?' ,'!' ,',', ':' , ';' , '-' , '(' , ')' ,'{','}','[',']',"'",'"','...'] 
	for element in string:
		for characters in element:
			if characters not in numbers and characters not in punctuation:
				text += characters.lower()
			if characters in numbers:
				digitCount += 1
			if characters in punctuation:
				punctuationCount += 1
			if characters.isupper():
				upperCount += 1

	
	textList = text.split()
	wordCount = len(textList)

	for word in textList:
		if word in dictionaryLst:
			correctWords += 1
		else:
			incorrectWords += 1

	finalOutput = ''
	finalOutput += '21023jh\n'
	finalOutput += 'Formatting ###################\n'
	finalOutput += 'Number of upper case letter changed:' + str(upperCount) + '\n'
	finalOutput += 'Number of punctuation’s removed:'+ str(punctuationCount) + '\n'
	finalOutput +='Number of numbers removed:' + str(digitCount) + '\n'
	finalOutput +='Spellchecking ###################\n'
	finalOutput +='Number of words:' + str(wordCount) + '\n'
	finalOutput +='Number of correct words:'+ str(correctWords) + '\n'
	finalOutput += 'Number of incorrect words:' + str(incorrectWords) 

	if not os.path.exists(path):
		os.makedirs(path)
	outputF = outputDir + '/' + filename[0:-4] + '_' + 'v21023jh.txt'   
	output = open(outputF,'w')
	output.write(finalOutput)
	output.close()


    # /home/csimage/Documents/PythonStuff/16321_python_coursework_v21023jh/program3/inputF
    # /home/csimage/Documents/PythonStuff/16321_python_coursework_v21023jh/program3/outputF