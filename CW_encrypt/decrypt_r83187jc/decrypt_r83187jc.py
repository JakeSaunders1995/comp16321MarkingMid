import argparse, os

parser = argparse.ArgumentParser()

parser.add_argument("inputFolder")
parser.add_argument("outputFolder")
args = parser.parse_args()

inputFolderName = args.inputFolder
outputFolderName = args.outputFolder

filesList = os.listdir(inputFolderName)

morseDict = {".-":"a", "-...":"b", "-.-.": "c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h",
"..":"i", ".---":"j", "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o", ".--.":"p", "--.-":"q",
".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y",
"--..":"z", ".-...":"&", ".----.":"'", ".--.-.":"@", "-.--.-":")", "-.--.":"(", "---...":":",
"--..--":",", "-...-":"=", "-.-.--":"!", ".-.-.-":".", "-....-":"-", "-----..-.----":"%", ".-.-.":"+",
'.-..-.':'"', "..--..":"?", "-..-.":"/", "/":" "}

for fileName in filesList:
	inputDirectory = inputFolderName + '/' + fileName

	f = open(inputDirectory, "r")
	inputContent = f.read()
	f.close()

	mode = ""
	inputList = list(inputContent)

	codeStart = inputList.index(":") + 1

	dotIndex = fileName.find(".")
	outputFileName = fileName[:dotIndex] + "_r83187jc" + fileName[dotIndex:]
	outputDirectory = outputFolderName + '/' + outputFileName
	f = open(outputDirectory, "w")

	if inputList[0] == "M":
		#Morse code
		tempWord = []
		tempChar = []
		sentence = ""
		inputList.append(" ")
		for i in range(codeStart, len(inputList)):
			#Separating into words and letters.
			if inputList[i] != " ":
				tempChar.append(inputList[i])
			else:
				if tempChar == ["/"]:
					sentence = sentence + ("".join(tempWord))
					tempWord = []
				
				
				tempWord.append(morseDict.get("".join(tempChar)))
				tempChar = []
		sentence = sentence + ("".join(tempWord))
		f.write(sentence)

	elif inputList[0] == "C":
		#caesar cipher
		charArray = []
		for i in range(codeStart, len(inputContent)):
			if inputList[i] != " ":
				asciiVal = ord(inputList[i])
				asciiVal -= 3
				charArray.append(chr(asciiVal))
			else:
				charArray.append(" ")
		f.write("".join(charArray))
		
	elif inputList[0] == "H":
		#Hex
		hexArray = []
		for i in range(codeStart, len(inputList), 3):
			hexArray.append(inputList[i]+inputList[i+1])
		#Now in the format [53, 6f, ...]
		charArray = []
		for i in range(0, len(hexArray)):
			#Converts hex to a character
			charArray.append(chr(int(hexArray[i], 16)).lower())
		f.write("".join(charArray))

	f.close()
