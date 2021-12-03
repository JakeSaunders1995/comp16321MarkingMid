
import argparse
import os 

parser = argparse.ArgumentParser()
parser.add_argument("inputFolder", type = str)
parser.add_argument("outputFolder", type = str)

args = parser.parse_args()

inputDirectory = args.inputFolder


counterInput = 0

for inputPath in os.listdir(inputDirectory):
	if os.path.isfile(os.path.join(inputDirectory, inputPath)):
		counterInput = counterInput + 1
		
		
counterOutput = 0

outputDirectory = args.outputFolder

for outputPath in os.listdir(inputDirectory):
	if os.path.isfile(os.path.join(outputDirectory, outputPath)):
		counterOutput = counterOutput + 1
		
for nameInput in os.scandir(inputDirectory):
	
	if nameInput.is_file():
	

		with open(nameInput) as input_file:
			line = input_file.readline()
	
		code = line.split(":")[1]

		#Hexadecimal decryption

		if line[0] == "H" or line[0] == "h":

			hexString = code
			bytesObject= bytes.fromhex(code)

			asciiString = bytesObject.decode("ASCII")

			decyphered = asciiString.lower()





			#Caesar decryption

		elif line[0] == "C" or line[0] == "c":

			cipherText= code
			plaintext = ""
			ciphertextPosition = 0
			while ciphertextPosition < len(cipherText):
				ciphertextChar = cipherText[ciphertextPosition]
				if ciphertextChar == " ":
					plaintext = plaintext + " "
				elif ciphertextChar == "@":
					plaintext = plaintext + "@"
				elif ciphertextChar == "#":
					plaintext = plaintext + "#"
				elif ciphertextChar == "1":
					plaintext = plaintext + "1"
				elif ciphertextChar == "2":
					plaintext = plaintext + "2"
				elif ciphertextChar == "3":
					plaintext = plaintext + "3"
				elif ciphertextChar == "4":
					plaintext = plaintext + "4"
				elif ciphertextChar == "5":
					plaintext = plaintext + "5"
				elif ciphertextChar == "6":
					plaintext = plaintext + "6"
				elif ciphertextChar == "7":
					plaintext = plaintext + "7"
				elif ciphertextChar == "8":
					plaintext = plaintext + "8"
				elif ciphertextChar == "9":
					plaintext = plaintext + "9"
				elif ciphertextChar == "0":
					plaintext = plaintext + "0"
				
				ASCIIValue = ord(ciphertextChar)
				ASCIIValue = ASCIIValue - 3
				if ASCIIValue < 97 and ASCIIValue > 58:
					ASCIIValue += 26
				plaintext = plaintext + chr(ASCIIValue)
				ciphertextPosition = ciphertextPosition +1

			decyphered = plaintext.lower()

			#Morse decryption

		elif line[0] == "M" or line[0] == "m":

			MorseDictionary = { "a":".-", "b":"-...",
								"c":"-.-.", "d":"-..", "e":".",
								"f":"..-.", "g":"--.", "h":"....",
								"i":"..", "j":".---", "k":"-.-",
								"l":".-..", "m":"--", "n":"-.",
								"o":"---", "p":".--.", "q":"--.-",
								"r":".-.", "s":"...", "t":"-",
								"u":"..-", "v":"...-", "w":".--",
								"x":"-..-", "y":"-.--", "z":"--..",
								"1":".----", "2":"..---", "3":"...--",
								"4":"....-", "5":".....", "6":"-....",
								"7":"--...", "8":"---..", "9":"----.",
								"0":"-----", ", ":"--..--", ".":".-.-.-",
								"?":"..--..", "/":"-..-.", "-":"-....-",
								"(":"-.--.", ")":"-.--.-"}
					
					

			MorseText = code

			decyphered = ""

			numberOfWords = len(MorseText.split("/"))
									  
			character = MorseText.split(" ")
			characterPosition = 0                              

			dictionaryPosition = 0
			alphabetLetter=""

			numberOfCharacters = len(character)



			while characterPosition < numberOfCharacters:
	
				letter = character[characterPosition]
	
				if letter in MorseDictionary.values():
					alphabetLetter = list(MorseDictionary.keys())[list(MorseDictionary.values()).index(letter)]
		
				elif letter == "/":
					alphabetLetter = " "
		
				characterPosition += 1 
	
				decyphered = decyphered + alphabetLetter
				
				decyphered = decyphered.lower()
	   
			
	
		outputDiretory = args.outputFolder
		checker = os.scandir(outputDirectory)
		filename = nameInput.name.split(".")
	
		if counterOutput < counterInput:
			for count in range(counterInput):
				outputFile = filename[0] + "_e58876ch.txt"
				newFile = args.outputFolder + "/" + outputFile
				
			
				newPath = open(newFile, "x") 
				break
		checker = os.scandir(outputDirectory)
		for writtenText in checker:
			write = writtenText.name.split("_")
			concatenation = write[0] + "_" + write[1]
		
			if filename[0] == concatenation:
				finalFile = open(writtenText, "w")
				finalFile.write(decyphered)
			else:
				continue
					
				
				
			


