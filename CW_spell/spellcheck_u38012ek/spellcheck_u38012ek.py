import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("englishwords_path")
parser.add_argument("input_path")
parser.add_argument("output_path")
args = parser.parse_args()

for file in os.listdir(args.input_path):
	input_destination = args.input_path + "/" + file
	input_file = open(input_destination)
	input = input_file.read()
	input_file.close()

	englishwords_file = open(args.englishwords_path)
	allwords = []
	for line in englishwords_file:
		line = line.rstrip()
		allwords.append(line)
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrtsuvwxyz"
	numbers = "0123456789"

	text = ""
	text1 = ""
	text2 = ""

	numberofpunctuation = 0
	numberofnumbers = 0
	numberchangedtocapitals = 0

	skip = False
	skipcounter = 0
	for i in range(0,len(input)):
		if skip == True:
			skipcounter += 1
			if skipcounter == 2:
				skip = False
				skipcounter = 0
			continue
		alpha = False
		num = False
		space = False
		for j in alphabet:
			if input[i] == j:
				alpha = True
		for k in numbers:
			if input[i] == k:
				num = True
		if input[i] == " ":
			space = True
		if alpha == True or num == True or space == True:
			text += input[i]
		elif input[i] != "\n":
			numberofpunctuation += 1
			if (i + 2) < len(input):
				if input[i] == "." and input[i+1] == "." and input[i+2] == ".":
					skip = True
	
	for i in text:
		alpha = False
		space = False
		for j in alphabet:
			if i == j:
				alpha = True
		if i == " ":
			space = True
		if alpha == True or space == True:
			text1 += i
		else:
			numberofnumbers += 1

	text2 = text1.lower()
	
	for i in range(0,len(text1)):
		if text2[i] != text1[i]:
			numberchangedtocapitals += 1

	listofwords = text2.split()
	numberofwords = len(listofwords)
	
	numberspeltcorrect = 0
	for i in listofwords:
		for j in allwords:
			if i == j:
				numberspeltcorrect += 1

	numberspeltincorrect = len(listofwords) - numberspeltcorrect

	output_destination = args.output_path + "/" + file[0:-4] + "_u38012ek.txt"
	output_file = open(output_destination, "w")
	output_file.write("u38012ek")
	output_file.write("\nFormatting ###################")
	output_file.write("\nNumber of upper case letters changed: " + str(numberchangedtocapitals))
	output_file.write("\nNumber of punctuations removed: " + str(numberofpunctuation))
	output_file.write("\nNumber of numbers removed: " + str(numberofnumbers))
	output_file.write("\nSpellchecking ###################")
	output_file.write("\nNumber of words: " + str(numberofwords))
	output_file.write("\nNumber of correct words: " + str(numberspeltcorrect))
	output_file.write("\nNumber of incorrect words: " + str(numberspeltincorrect))
	output_file.close()
