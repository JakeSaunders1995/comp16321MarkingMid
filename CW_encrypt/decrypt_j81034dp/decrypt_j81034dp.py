# Program 2 - Encryption

import sys
import os

InputFolder = sys.argv[1]
InputFolderList = os.listdir(InputFolder)
InputFolderList.sort()
OutputFolder = sys.argv[2]
OutputFolderList = os.listdir(OutputFolder)

for folder in InputFolderList:
	files = open(os.path.join(InputFolder, folder))
	content = files.read()
	folderstring = folder.replace(".txt","_j81034dp.txt")

	morse = { 'A':'.-', 'B':'-...',
	                    'C':'-.-.', 'D':'-..', 'E':'.',
	                    'F':'..-.', 'G':'--.', 'H':'....',
	                    'I':'..', 'J':'.---', 'K':'-.-',
	                    'L':'.-..', 'M':'--', 'N':'-.',
	                    'O':'---', 'P':'.--.', 'Q':'--.-',
	                    'R':'.-.', 'S':'...', 'T':'-',
	                    'U':'..-', 'V':'...-', 'W':'.--',
	                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
	                    '1':'.----', '2':'..---', '3':'...--',
	                    '4':'....-', '5':'.....', '6':'-....',
	                    '7':'--...', '8':'---..', '9':'----.',
	                    '0':'-----', ' ':'/'}
	 

	# Example: .... --- .-- . ...- . .-. / ... --- .-.. ...- .. -. --. / -- --- .-. ... . / -.-. --- -.. . / -- .- -.-- / -... . / - .... . / -- --- ... - / -.. .. ..-. ..-. .. -.-. ..- .-.. -
	def decrypt(Word):
		Word = Word.replace('\n','')
		Word += " "
		EnglishTrans = ""
		englishtomorse = ""
		for character in Word:
			if (character != " "):
				i = 0
				englishtomorse+= character
			else:
				i += 1
				if i == 2:
					EnglishTrans += " "
				else:
					EnglishTrans += list(morse.keys())[list(morse.values()).index(englishtomorse)]
					englishtomorse = ""
		return (EnglishTrans.lower())


	def Caesar(Wordlower):
		decrypted = ""
		for i in Wordlower:
			if i.islower():
				index = ord(i) - ord("a")
				originalpos = ((index - 3) % 26 ) + ord("a")
				original = chr(originalpos)
				decrypted = decrypted + original
			elif i.isdigit():
				original = (int(i) -3) % 10
				decrypted = decrypted + str(original)
			else:
				decrypted = decrypted + i
		return decrypted

	if content[0] == "H" or content[0] == "h":
		Word = content[4:]
		Word = bytes.fromhex(Word)
		Word = Word.decode("ascii")
		Word = Word.lower()

	elif content[0] == "C" or content[0] == "c":
		Word = content[18:]
		Wordlower = Word.lower()
		Word = Caesar(Wordlower)

	elif content[0] == "M" or content[0] == "m":
		Word = content[11:]
		Word = decrypt(Word)

	for folders in OutputFolder:
		outputFile = open(os.path.join(OutputFolder, folderstring), 'w')
		outputFile.writelines(Word)
