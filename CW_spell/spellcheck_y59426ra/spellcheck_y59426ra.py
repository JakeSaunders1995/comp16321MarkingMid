#path in: /home/csimage/COMP16321/coursework/16321_python_coursework_y59426ra/midterm/Program3/Example_inputs_program3
#path out: /home/csimage/COMP16321/coursework/16321_python_coursework_y59426ra/midterm/Program3/Example_outputs_program3

import sys, os, re, string

EngFilePath = sys.argv[1]
directory = sys.argv[2]
dest = sys.argv[3]

Eng_list = []
EngFile = open(EngFilePath, "r")
for line in EngFile:
	stripped_line = line.strip()
	#line_list = stripped_line.split()
	Eng_list.append(stripped_line)
EngFile.close()


#for filename in os.listdir(directory):


def Upper_cases(FileIn):
	numberUpperCase =len(re.findall(r'[A-Z]', FileIn))
	return str(numberUpperCase)

def Punctioations(FileIn):
	NumberPunc = int()
	global NoPunct
	NoPunct = ""
	for i in FileIn.lower():
		if i in string.punctuation:
			NumberPunc = NumberPunc + 1
		elif i not in string.punctuation:
			NoPunct = NoPunct + i
	return str(NumberPunc)

def	Number_of_Numbers():
	Num="1234567890"
	NumNum = 0
	global NoNum
	NoNum = ""
	for i in NoPunct:
		if i in Num:
			NumNum = NumNum + 1
		elif i not in Num:
			NoNum = NoNum + i
	return str(NumNum)

#print("Spellchecking ##############")

def Count_of_words():
	global Words
	Words= NoNum.split()
	Numwords = len(Words)
	return str(Numwords)

def Count_of_Correct():
	CorrectWords = 0
	for i in Words:
		if i in Eng_list:
			CorrectWords += 1
	return str(CorrectWords)
		

def Incorrect_words():
	IncorrectWords = 0
	for i in Words:
		if i not in Eng_list:
			IncorrectWords += 1
	return str(IncorrectWords)


for filename in os.listdir(directory):
	with open(os.path.join(directory, filename), "r") as file:
		FileIn = file.readline()
	with open(os.path.join(dest, os.path.basename(filename)[:-4] + "_y59426ra.txt"), "w+") as file:
		FileOut = file.write("y59426ra\n")
		FileOut = file.write("Formatting ###############\n")
		FileOut = file.write("Number of upper case words changed: "+Upper_cases(FileIn)+"\n")
		FileOut = file.write("Number of Punctioations removed: "+ Punctioations(FileIn)+"\n")
		FileOut = file.write("Number of numbers removed: " + Number_of_Numbers()+"\n")
		FileOut = file.write("Formatting ###############\n")
		FileOut = file.write("Number of Words: " + Count_of_words() + "\n")
		FileOut = file.write("Number of Correct Words: " + Count_of_Correct() + "\n")
		FileOut = file.write("Number of incorrect words: " + Incorrect_words())