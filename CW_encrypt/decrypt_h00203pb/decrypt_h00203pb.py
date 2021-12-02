import argparse
import os

parserVariable = argparse.ArgumentParser()
parserVariable.add_argument("inputFolderPath", type = str)
parserVariable.add_argument("outputFolderPath", type = str)
arguments = parserVariable.parse_args()

files = os.listdir(arguments.inputFolderPath)
files.sort()
for file in files :
	if len(file) >= 4 :
		if file[-4 :] == ".txt" :

			inputFilePath = (arguments.inputFolderPath + "/" + file)
			inputFile = open(inputFilePath)
			inputString = inputFile.read()
			inputFile.close()

			for x in range(len(inputString)) :
				if inputString[x] == ":" :
					encryptedText = inputString[x + 1 : len(inputString) + 1]
					break;


			def shiftWord(word, plaintext) :
				for p in word :
					number = ord(p)
					number = number - 3
					if number < 97 :
						number = number + 26
					plaintext += str(chr(number))
				return plaintext


			def caesarDecrypt(ciphertext) :
				plaintext = ""
				word = ""
				counter = 0

				for a in ciphertext :
					counter += 1		

					if a.isalpha() :

						if a.isupper() :
							word += a.lower()
						else :
							word += a

						if counter == len(ciphertext) :
							plaintext = shiftWord(word, plaintext)

					else :
						plaintext = shiftWord(word, plaintext)
						plaintext += a
						word = ""

				return plaintext


			def morseDecrypt(ciphertext) :
				morseCode = {".-" : "a", "-..." : "b", "-.-." : "c", "-.." : "d", "." : "e", "..-." : "f", "--." : "g", "...." : "h", ".." : "i", ".---" : "j", "-.-" : "k", ".-.." : "l", "--" : "m",
				 "-." : "n", "---" : "o", ".--." : "p", "--.-" : "q", ".-." : "r", "..." : "s", "-" : "t", "..-" : "u", "...-" : "v", ".--" : "w", "-..-" : "x", "-.--" : "y", "--.." : "z", ".----" : "1",
				 "..---" : "2", "...--" : "3", "....-" : "4", "....." : "5", "-...." : "6", "--..." : "7", "---.." : "8", "----." : "9", "-----" : "0", ".-.-.-" : ".",  "..--.." : "?", "-.-.--" : "!",
				 "--..--" : ",", "---..." : ":", "-.-.-." : ";", "-....-" : "-", "-.--." : "(", "-.--.-" : ")", ".----." : "'", ".-..-." : '"'}
				
				plaintext = ""
				encryptedLetter = ""
				ciphertext = ciphertext + " "

				for m in range(len(ciphertext)) :

					if ciphertext[m] == " ":

						if encryptedLetter == "/" :
							plaintext = plaintext + " "
						else :
							plaintext = plaintext + morseCode.get(encryptedLetter)
						encryptedLetter = ""

					else :
						encryptedLetter = encryptedLetter + ciphertext[m]
				return plaintext


			decryptedText = ""
			if inputString[0] == "H" or inputString[0] == "h" :
				decryptedText = bytes.fromhex(encryptedText).decode("utf-8")
			elif inputString[0] == "C" or inputString[0] == "c" :
				decryptedText = caesarDecrypt(encryptedText)
			elif inputString[0] == "M" or inputString[0] == "m" :
				decryptedText = morseDecrypt(encryptedText)

			outputFilePath = arguments.outputFolderPath + "/" + file[0 : len(file) - 4] + "_h00203pb.txt"
			outputFile = open(outputFilePath, "w")
			outputFile.write(decryptedText)
			outputFile.close()


