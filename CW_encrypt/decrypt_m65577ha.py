import os, re, argparse

def slice(input):
    return [char for char in input]

parser = argparse.ArgumentParser()
parser.add_argument("path")
parser.add_argument("path2")

startDir = os.getcwd()
inputPath = parser.parse_args()
dir_list = os.listdir(inputPath.path)
os.chdir(inputPath.path)

for file in dir_list:
	if file.endswith(".txt"):
		os.chdir(startDir)
		os.chdir(inputPath.path)
		inputFile = open(file)
		input = inputFile.read()
		slicedInput = slice(input)
		cipherText = ""
		print(os.linesep + "For the " + file + " code: ")


		# Caeser cipher code
		if slicedInput[0] == "C":
			print("This cipher is encrypted using Caeser +3.")
			alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
			currentPosition = 18
			alphabetPosition = 0
			input = input.lower()
			inputLength = len(input)
			slicedInput = slice(input)
			slicedAlphabet = slice(alphabet)
			currentAlphabetLetter = slicedAlphabet[alphabetPosition]
			currentLetter = slicedInput[currentPosition]
			while currentPosition != (inputLength - 1):
				currentLetter = slicedInput[currentPosition]
				alphabetPosition = 3
				currentAlphabetLetter = slicedAlphabet[alphabetPosition]
				while currentLetter != currentAlphabetLetter:
					if currentLetter == " ":
						currentPosition = currentPosition + 1
						currentLetter = slicedInput[currentPosition]
						cipherText = cipherText + " "
					else:
						alphabetPosition = alphabetPosition + 1
						currentAlphabetLetter = slicedAlphabet[alphabetPosition]
				alphabetPosition = alphabetPosition -3
				currentAlphabetLetter = slicedAlphabet[alphabetPosition]
				cipherText = cipherText + currentAlphabetLetter
				currentPosition = currentPosition + 1
			print("This message reads: " + cipherText)


		# Hex cipher code
		if slicedInput[0] == "H":
			print("This cipher is encrypted using Hexadecimal.")
			alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 "
			hexAlphabet = "41 42 43 44 45 46 47 48 49 4a 4b 4c 4d 4e 4f 50 51 52 53 54 55 56 57 58 59 5a 61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76 77 78 79 7a 30 31 32 33 34 35 36 37 38 39 20"
			currentPosition = 1
			alphabetPosition = 0
			HexAlphabetPosition = 0
			slicedHexInput = re.findall("\w{1,3}", input)
			slicedAlphabet = slice(alphabet)
			slicedHexAlphabet = re.findall("\w{1,3}", hexAlphabet)
			inputHexLength = len(slicedHexInput)
			currentHexLetter = slicedHexInput[currentPosition]
			while currentPosition != (inputHexLength):
				currentHexLetter = slicedHexInput[currentPosition]
				currentHexAlphabetLetter = slicedHexAlphabet[HexAlphabetPosition]
				while currentHexLetter != currentHexAlphabetLetter:
					HexAlphabetPosition = HexAlphabetPosition + 1
					currentHexAlphabetLetter = slicedHexAlphabet[HexAlphabetPosition]
				currentHexAlphabetLetter = slicedHexAlphabet[HexAlphabetPosition]
				alphabetPosition = HexAlphabetPosition
				currentAlphabetLetter = slicedAlphabet[alphabetPosition]
				cipherText = cipherText + currentAlphabetLetter
				HexAlphabetPosition = 0
				currentPosition = currentPosition + 1
			cipherText = cipherText.lower()
			print("This message reads: " + cipherText)

		# Morse cipher code
		if slicedInput[0] == "M":
			print("This cipher is encrypted using Morse Code.")
			alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 "
			MorseAlphabet = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. ----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----. /"
			currentPosition = 2
			alphabetPosition = 0
			MorseAlphabetPosition = 0
			slicedMorseInput = re.findall("\S{1,5}", input)
			slicedAlphabet = slice(alphabet)
			slicedMorseAlphabet = re.findall("\S{1,5}", MorseAlphabet)
			inputMorseLength = len(slicedMorseInput)
			while currentPosition != (inputMorseLength):
				currentMorseLetter = slicedMorseInput[currentPosition]
				currentMorseAlphabetLetter = slicedMorseAlphabet[MorseAlphabetPosition]
				while currentMorseLetter != currentMorseAlphabetLetter:
					MorseAlphabetPosition = MorseAlphabetPosition + 1
					currentMorseAlphabetLetter = slicedMorseAlphabet[MorseAlphabetPosition]
				currentMorseAlphabetLetter = slicedMorseAlphabet[MorseAlphabetPosition]
				alphabetPosition = MorseAlphabetPosition
				currentAlphabetLetter = slicedAlphabet[alphabetPosition]
				cipherText = cipherText + currentAlphabetLetter
				MorseAlphabetPosition = 0
				currentPosition = currentPosition + 1
			cipherText = cipherText.lower()
			print("This message reads: " + cipherText)

		os.chdir(startDir)
		os.chdir(inputPath.path2)
		filename = file.replace(".txt", "_m65577ha.txt")
		outputFile = open(filename, "w")
		outputFile.write(cipherText)
		inputFile.close()
	else:
		print("Error: No .txt files in input folder.")
