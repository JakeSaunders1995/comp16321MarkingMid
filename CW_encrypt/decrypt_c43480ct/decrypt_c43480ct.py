import argparse
import os
import re
import sys

inputFolder = sys.argv[-2]
outputFolder = sys.argv[-1]

def decryption(inputFile):

	inputAlgorithm = inputFile

	def hexToDec(hexToDecrypt):
		return chr(int(hexToDecrypt, 16))

	alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc" 
	decryptedCaesar = ""
	caesarPosition = 0

	morseCode = { '/':' ', '.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-.':'f', '--.':'g', '....':'h',
	                    '..':'i', '.---':'j', '-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o', '.--.':'p', '--.-':'q',
	                    '.-.':'r', '...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x', '-.--':'y', '--..':'z',
	                    '.----':'1', '..---':'2', '...--':'3', '....-':'4', '.....':'5', '-....':'6', '--...':'7', '---..':'8', '----.':'9',
	                    '-----':'0', '--..--':', ', '.-.-.-':'.', '..--..':'?', '-..-.':'/', '-....-':'-', '-.--.':'(', '-.--.-':')',
	                    '.-..-.':'"', '---...':':', '-.-.--':'!', '.--...':'[', '-..---':']', '..--.':'{', '--..-':'}', '-....-':';',
	                    '--.---':"'",}
	decrypted = ""

	if 		inputAlgorithm[0] == "H" :
				inputHex = inputAlgorithm.split(":")

				hexString = inputHex[1]

				hexString = re.sub(" ", "", hexString)
				decryptedHex = ""

				if len(hexString) % 2 == 0:
					for i in range(0,len(hexString),2):
						subString = hexString[i] + hexString[i+1]
						decryptedHex += hexToDec(subString)
						decryptedHex = decryptedHex.lower()
				#print(decryptedHex) #Testing
				decrypted = decryptedHex

	elif	inputAlgorithm[0] == "C" :
				inputCaesar = inputAlgorithm.split(":")

				caesarToDecrypt = inputCaesar[1]

				while caesarPosition < len(caesarToDecrypt):
					plaintextChar = caesarToDecrypt[caesarPosition]
					if plaintextChar == " ":
						decryptedCaesar=decryptedCaesar+" "
						caesarPosition = caesarPosition + 1
					else:
						alphabetPosition = 3
						while plaintextChar != alphabet[alphabetPosition]:
							alphabetPosition += 1
						alphabetPosition = alphabetPosition - 3
						decryptedCaesar = decryptedCaesar + alphabet[alphabetPosition]
						caesarPosition = caesarPosition + 1
				#print (decryptedCaesar) #Testing
				decrypted = decryptedCaesar

	elif	inputAlgorithm[0] == "M" :
				inputMorse = inputAlgorithm.split(":")

				morseToDecrypt = inputMorse[1]

				sepWord = morseToDecrypt.split("/")
				sepLetter = []
				for i in sepWord:
					sepLetter.append(i.split())
				decryptedMorse = ""
				for i in sepLetter:
					for j in i:
						decryptedMorse = decryptedMorse + morseCode.get(j)
					decryptedMorse = decryptedMorse + " "
				#print(decryptedMorse) #Tesing
				decrypted = decryptedMorse

	return decrypted				

for inputFile in os.listdir(inputFolder):
	with open (os.path.join(inputFolder, inputFile), "r") as file:
		file = file.read()
		decrypted = decryption(file)

		outputFileTemp = inputFile.rstrip(".txt")
		outputFile = outputFileTemp + "_c43480ct.txt"

		with open(os.path.join(outputFolder, outputFile), "w+") as file:
			file.write(decrypted)
