import argparse
import os

##start funct

def decrypt(fileToRead):

	fileText = fileToRead.read()
	fileToRead.close()

	sections = fileText.split(':')

	algorithm = sections[0]
	ciphertext = sections[1]

	# HEX SEXION #

	def hexadecimal():
		hexDict = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
		letters = ciphertext.split(" ")
		plaintext = ""
		for l in letters:
			newAscii = (hexDict[l[0]]*16) + hexDict[l[1]]
			newChar = chr(newAscii)
			plaintext = plaintext + newChar
		return plaintext

	# CIPHER SECHER #

	def caeserCipher():
		plaintext = ""
		for i in ciphertext:
			if i == " ":
				plaintext += i
			else:
				newAscii = ord(i) -3
				newChar = chr(newAscii)
				plaintext += newChar
		return plaintext

	# MORSE COURSE #

	def morseCode():
		morseDict = {'....' : 'h', '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' ', '-----' : '0', '.----' : '1', '..---' : '2', '...--' : '3', '....-' : '4', '.....' : '5', '-....' : '6', '--...' : '7', '---..' : '8', '----.' : '9'}
		words = ciphertext.split('/')
		plaintext = ""
		plainword = ""
		for w in words:
			letters = w.split(' ')
			letters.remove('')
			allLetters = ""
			for l in letters:
				if l == '':
					letters.remove(l)
				else:
					decodedLetter = morseDict[l]
					allLetters = allLetters + decodedLetter
			plainword = allLetters
			plaintext += plainword + " "
		return plaintext

	# ALGO SECT #

	if algorithm == "Hex":
		print(hexadecimal())
	elif algorithm == "Caesar Cipher(+3)":
		print(caeserCipher())
	elif algorithm == "Morse Code":
		print(morseCode())

arg = argparse.ArgumentParser()

arg.add_argument("inFolderPath")
arg.add_argument("outFolderPath")

File = arg.parse_args()

direct = os.scandir(File.inFolderPath)

for f in direct:
	print(f.name)
	folderInput = File.inFolderPath + "/" + f.name
	fileToRead = open(folderInput, "r")
	decrypt(fileToRead)
	folderOutput = File.outFolderPath + "/" + f.name
	folderOutput = folderOutput.replace(".txt", "_a07230cc.txt")

	fileToSave = open(folderOutput, "w")

	fileToSave.write("encryption is fun!")
	fileToSave.close()