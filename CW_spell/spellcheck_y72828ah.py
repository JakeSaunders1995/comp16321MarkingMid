import os
import sys
import re
textfile = sys.argv[1]
inputf = sys.argv[2]
outputf = sys.argv[3]

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = ["0","1","2","3","4","5","6","7","8","9"]
capital_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
allwords = open(textfile)
for x in os.listdir(inputf):
	
	numbercount = 0
	punctuation_count = 0
	uppercase = 0
	nowords = 0
	nocorrectwords = 0
	f = os.path.join(inputf,x)
	text = open(f)
	line = text.readline()
	filename = os.path.basename(x)
	for i in line:
		if i in capital_letters:
			uppercase +=1

	line = line.lower()
	
	lettersl = []
	for i in line:
		if i in number:
			numbercount += 1
		elif i not in alphabet and i not in number and i != " " and i != "\n" and i!= "#" and i!= "@":
			punctuation_count +=1
			

	for i in line:
		if i in alphabet or i == " ":
			lettersl.append(i)
	letters = ''.join([str(item) for item in lettersl])
	words = letters.split(" ")
	while "" in words:
		words.remove("")
	for x in words:
		allwords = open(textfile)
		nowords+=1
		if "\n" + x +"\n" in allwords.read() or x == "a":
			nocorrectwords += 1
	filename = filename.replace(".txt","")
	outputname = outputf + "/" + filename+"_y72828ah.txt"
	outputfile = open(outputname, "w")
	outputfile.write("y72828ah\n")
	outputfile.write("Formatting ###################\n")
	outputfile.write("Number of upper case letters changed: " +str(uppercase)+"\n")
	outputfile.write("Number of punctuations removed: " + str(punctuation_count)+"\n")
	outputfile.write("Number of numbers removed: " + str(numbercount) + "\n")
	outputfile.write("Spellchecking ###################\n")
	outputfile.write("Number of words: "+str(nowords)+"\n")
	outputfile.write("Number of correct words: "+str(nocorrectwords)+"\n")
	outputfile.write("Number of incorrect words: "+str(nowords - nocorrectwords)+"\n")
	outputfile.close()
