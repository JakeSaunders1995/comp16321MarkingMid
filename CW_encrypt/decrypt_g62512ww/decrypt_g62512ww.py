import sys
import os
def outputDecryptedAsFile(textToWrite, outputFileNameLocation):
	with open(outputFileName, "x") as f:
		f.write(textToWrite)
morseDictionary = {	"/": " ",".-": "a","-...": "b","-.-.": "c","-..": "d",".": "e","..-.": "f","--.": "g","....": "h","..": "i",".---": "j","-.-": "k",".-..": "l","--": "m","-.": "n","---": "o",".--.": "p","--.-": "q",".-.": "r","...": "s","-": "t","..-": "u","...-": "v",".--": "w","-..-": "x","-.--": "y","--..": "z" }
numArgs = len(sys.argv)
if numArgs == 3:
	inputFile = sys.argv[1]
	outputFile = sys.argv[2]
	if os.path.isdir(inputFile):
		if not os.listdir(inputFile):
			print("Directory is empty")	
		else:
			allFiles = os.listdir(inputFile)
			for file in allFiles:
				fileName = file[:-4]
				outputFileName = outputFile + "/" + fileName + "_g62512ww.txt"
				with open(inputFile + '/' + file) as f:
					fileData = f.read()	
				fullyDecrypted = ""
				if (fileData[0] == "M"):
					fileData = fileData[11:]
					toDecryptMorse = fileData.split()
					for word in toDecryptMorse:
						decryptedWord = morseDictionary[word]
						fullyDecrypted += decryptedWord
					outputDecryptedAsFile(fullyDecrypted, outputFileName)
				elif (fileData[0] == "C"):
					fileData = fileData[18:]
					alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
					for char in fileData:
						if (char == " "):
							fullyDecrypted += char
						else:
							charPos = 3
							while char != alphabet[charPos]:
								charPos += 1
							charPos -= 3
							fullyDecrypted += alphabet[charPos]
					outputDecryptedAsFile(fullyDecrypted, outputFileName)
				elif (fileData[0] == "H"):
					fileData = fileData[4:]
					toDecryptHex = fileData.split()
					for word in toDecryptHex:
						fullyDecrypted += chr(int(word, 16)).lower()
					outputDecryptedAsFile(fullyDecrypted, outputFileName)						
				else:
					print("There has been an error with the file: ", inputFile + "/" + file)			
	else:
		print("Input directory does not exist")