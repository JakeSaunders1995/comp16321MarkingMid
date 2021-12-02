import sys
import os 

dictionaryFile =sys.argv[1]
input_directory = sys.argv[2]
file_list = os.listdir(input_directory)
output_directory = sys.argv[3]

n=0

while n<= len(file_list)-1:
	test_file1= open(input_directory +"/" +file_list[n],"r")
	def readDictionaryFile(dictionaryFilename):
		dictionaryWords= []
		inputFile =open(dictionaryFilename, "r")
		for line in inputFile:
			word =line.strip()
			dictionaryWords.append(word)
		inputFile.close()
		return dictionaryWords


	def readTextFile(textFilename):
		words =[]
		inputFile = open(input_directory +"/" +file_list[n],"r")
		for line in inputFile:
			wordsOnLine =line.strip().split()
			for word in wordsOnLine:
				words.append(word.strip(".,!\":@';?/123456789").lower())
		inputFile.close()
		return words


	def findErrors(dictionaryWords, textWords):
		missspelledWords = []
		for word in textWords:
			if word not in dictionaryWords:
				missspelledWords.append(word)
		return missspelledWords


	def printErrors(errorList):
		for word in errorList:
			print(len(word))


	def main():
		test_file1= open(input_directory +"/" +file_list[n],"r")
		textFile=test_file1
		dictionaryList =readDictionaryFile(dictionaryFile)
		textList =readTextFile(textFile)
		errorList =findErrors(dictionaryList, textList)
		L= list(filter(None,errorList))
		number_of_inccorect_words= len(L)
		correctword= textList.copy()
		correctword = filter(None, correctword)
		correctword = filter(bool, correctword)
		correctword = filter(len, correctword)
		correctword = filter(lambda item: item, correctword)
		correctword = list(filter(None, correctword))
		num_of_words=len(correctword)
		Lcorrectword = num_of_words - number_of_inccorect_words
		filename =str(file_list[n]).replace(".txt", "")
		output_file =open(output_directory +"/"+filename+"a86442gs.txt", "w")
		output_file.write("a86442gs""\n")
		output_file.write ("Formatting ###################\n")
		output_file.write ("Number of upper case letters changed :" + str(Total_uppercase) +"\n") 
		output_file.write ("Number of punctuations removed :" +str(Total_Punctuation_in_document) +"\n")
		output_file.write ("Number of numbers removed :" + str(Total_numbers_in_document) + "\n") 
		output_file.write ("Spellchecking ###################""\n")
		output_file.write ("Number of words:" + str(num_of_words) +"\n")
		output_file.write ("Number of correct words:" + str(Lcorrectword)+"\n")
		output_file.write ("Number of incorrect words:" + str(number_of_inccorect_words) +"\n")
		output_file.close()
		return textFile


	data=open(input_directory +"/" +file_list[n],"r").read()

	Letter1 =data.count("A")
	Letter2 =data.count("B")
	Letter3 =data.count("C")
	Letter4 =data.count("D")
	Letter5 =data.count("E")
	Letter6 =data.count("F")
	Letter7 =data.count("G")
	Letter8 =data.count("H")
	Letter9 =data.count("I")
	Letter10 =data.count("J")
	Letter11 =data.count("K")
	Letter12 =data.count("L")
	Letter13 =data.count("M")
	Letter14 =data.count("N")
	Letter15 =data.count("O")
	Letter16 =data.count("P")
	Letter17 =data.count("Q")
	Letter18 =data.count("R")
	Letter19 =data.count("S")
	Letter20 =data.count("T")
	Letter21 =data.count("U")
	Letter22 =data.count("V")
	Letter23 =data.count("W")
	Letter24 =data.count("X")
	Letter25 =data.count("Y")
	Letter26 =data.count("Z")

	Total_uppercase= (Letter1 +Letter2 +Letter3 +Letter4 +Letter5 +Letter6 +Letter7 +Letter8 +Letter9 +Letter10 +Letter11 +Letter12 +Letter13 +Letter14 +Letter15 +Letter16 +Letter17 +Letter18 +Letter19 +Letter20 +Letter21 +Letter22 +Letter23 +Letter24 +Letter25 +Letter26)

	#print("Total Upper case words:" + str(Total_uppercase))


	Punctuation1 = data.count(".")
	Punctuation2 = data.count("?")
	Punctuation3 = data.count("!")
	Punctuation4 = data.count(",")
	Punctuation5 = data.count(":")
	Punctuation6 = data.count(";")
	Punctuation7 = data.count("-")
	Punctuation8 = (data.count("["))*2
	Punctuation9 = (data.count("{"))*2
	Punctuation10 = (data.count("("))*2
	Punctuation11 = (data.count("'"))
	Punctuation12 = data.count("\"")
	Punctuation13 = data.count("...")

	


	Total_Punctuation_in_document = (Punctuation1 +Punctuation2 +Punctuation3 + Punctuation4 + Punctuation5 + Punctuation6 +Punctuation7 +Punctuation8 +Punctuation9 + Punctuation10 + Punctuation11 + Punctuation12 +Punctuation13) 

	#print("Punctuation in Document:" + str(Total_Punctuation_in_document))

	number0 = data.count("0")
	number1 = data.count("1")
	number2 = data.count("2")
	number3 = data.count("3")
	number4 = data.count("4")
	number5 = data.count("5")
	number6 = data.count("6")
	number7 = data.count("7")
	number8 = data.count("8")
	number9 = data.count("9")
	number10 =data.count("10")


	Total_numbers_in_document = (number0 + number1 + number2 + number3 + number4 + number5 + number6 + number7 + number8 + number9) 

	
	main()
	#print((input_directory +"/" +file_list[n],"r"))
	#filename =str(file_list[n]).replace(".txt", "")
	#output_file =open(output_directory +"/"+filename+"a86442gs.txt", "w")

	#output_file.write("a86442gs""\n")
	#output_file.write ("Formatting ###################\n")
	#output_file.write ("Number of upper case words transformed :" + str(Total_uppercase) +"\n") 
	#output_file.write ("Number of punctuation's removed :" +str(Total_Punctuation_in_document) +"\n")
	#output_file.write ("Number of numbers removed :" + str(Total_numbers_in_document) + "\n") 
	#output_file.write ("Spellchecking ###################""\n")
	#output_file.write ("Number of words:" + str(num_of_words) +"\n")
	#output_file.write ("Number of correct words in file:" + str(Lcorrectword)+"\n")
	#output_file.write ("Number of incorrect words in file:" + str(number_of_inccorect_words) +"\n")
	#output_file.close()
	n+=1