import sys
import os
import string


EngWordPath = str(sys.argv[1])
FolderIN = str(sys.argv[2])
FolderOUT = str(sys.argv[3])
fEng = open (EngWordPath,"r")
Dict = (fEng.read()).strip()
fEng.close() 
WordList = Dict.split("\n")
punctuations = [".","?","!",",",":",";","–","-","[","]","{","}","(",")","'",'"',"…"]

for files in os.listdir(FolderIN):
	filename = str(files)
	InFilePath = os.path.join(FolderIN,filename)


	with open(InFilePath) as f:
		content = f.read()
	f.close()
	
	Upletters = 0
	Punct = 0
	Num = 0
	NoWords = 0
	NoCWords = 0
	NoIWords = 0

	if "..." in content:
		content = content.replace("...","…")

	if ". . ." in content:
		content = content.replace(". . .","…")

	for character in content:
		if character.isupper():
			Upletters += 1
			content = content.replace(character,character.lower())
		if character.isdigit():
			Num += 1
			content = content.replace(character,"")
			content = " ".join(content.split())

		#if character in string.punctuation:
		if character in punctuations:
			Punct += 1
			content = content.replace(character,"")
			content = " ".join(content.split())

	words = content.split(" ")

	for word in words:
		if word != " " and word != "\n" and word != "":
			NoWords += 1
			if word in WordList:
				NoCWords += 1
			else:
				NoIWords += 1


	FPos = filename.index(".")
	outFilename = filename[:FPos] + "_y28244lw.txt"
	OutFilePath = os.path.join(FolderOUT,outFilename)

	fout = open(OutFilePath,"w")
	fout.write("y28244lw\nFormatting ###################\nNumber of upper case letters changed: " + str(Upletters) + "\nNumbers of punctuations removed: " + str(Punct) + "\nNumber of numbers removed: " + str(Num) + "\nSpellchecking ###################\nNumber of words: " + str(NoWords) + "\nNumber of correct words: " + str(NoCWords) + "\nNumber of incorrect words: " + str(NoIWords))
	fout.close()
