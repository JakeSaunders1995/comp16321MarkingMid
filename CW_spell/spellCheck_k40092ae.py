import os
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('eng_word_file')
parser.add_argument('input_folder_path')
parser.add_argument('output_folder_path')

args = parser.parse_args()

engfilpath = (args.eng_word_file)
inputfolpath = (args.input_folder_path)
outputfolpath = (args.output_folder_path)

englishwords = []

wordfile = open(engfilpath,"r")
for lines in wordfile:
	lines = lines.strip()
	englishwords.append(lines)

#print (englishwords)

wordfile.close()
for filename in os.listdir(inputfolpath):
	inputfile = open(inputfolpath + "/" + filename,"r")
	inputline = inputfile.readline()
	temp = filename.split(".")
	username = 'k40092ae'
	
	output_file_name = temp[0] +"_"+ username + "." + temp[1]
	inputcharacterlist = list(inputline)

	capchanged = 0
	puncremoved = 0
	numremoved = 0
	alphabetlow = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	alphabetcap = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	punctuation = ['.',',','?',';','!',':',"'","(",")","[","]",'"',"…","-","–","/","{","}"]
	numbers = ['1','2','3','4','5','6','7','8','9','0']
	adjustedcharacterstring = ""
	periodrow = 0
	for count in range(len(inputcharacterlist)):
		if inputcharacterlist[count] in alphabetcap:
			adjustedcharacterstring = adjustedcharacterstring + alphabetlow[alphabetcap.index(inputcharacterlist[count])]
			capchanged = capchanged + 1
			periodrow = 0
		elif inputcharacterlist[count] in punctuation:
			puncremoved = puncremoved + 1
			if inputcharacterlist[count] == ".":
				periodrow = periodrow + 1
				if periodrow == 3:
					periodrow = 0
					puncremoved = puncremoved - 2
			else:
				periodrow = 0
		elif inputcharacterlist[count] in numbers:
			numremoved = numremoved + 1
			periodrow = 0
		elif inputcharacterlist[count] == "\n":
			pass
			periodrow = 0
		else:
			adjustedcharacterstring = adjustedcharacterstring + inputcharacterlist[count]
			periodrow = 0



	wordsapart = adjustedcharacterstring.split(" ")
	#print (wordsapart)
	temporarystorage = []

	for count1 in range(len(wordsapart)):
		if wordsapart[count1] != "":
			temporarystorage.append(wordsapart[count1])

	wordsapart = []
	for count2 in range(len(temporarystorage)):
		wordsapart.append(temporarystorage[count2])
	totalwords = len(wordsapart)
	incorrectwords = 0
	#print (wordsapart)
	for i in range(len(wordsapart)):
		if wordsapart[i] not in englishwords:
			incorrectwords = incorrectwords + 1

	correctwords = totalwords - incorrectwords

	inputfile.close()


	outputfile = open(outputfolpath+ "/" + output_file_name,"w")
	outputfile.write("k40092ae\n")
	outputfile.write("Formatting ###################\n")
	outputfile.write("Number of upper case letters changed: "+str(capchanged)+"\n")
	outputfile.write("Number of punctuations removed: "+str(puncremoved)+"\n")
	outputfile.write("Number of numbers removed: " + str(numremoved)+"\n")
	outputfile.write("Spellchecking ###################\n")
	outputfile.write("Number of words: "+ str(totalwords)+"\n")
	outputfile.write("Number of correct words: "+ str(correctwords)+"\n")
	outputfile.write("Number of incorrect words: "+ str(incorrectwords)+"\n")
	outputfile.close()
