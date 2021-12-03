numbers = "1234567890"

morse = ",-/"


Extracted = ""	
with open("test_file3.txt") as file:
	Extracted = file.readlines()

def listToSentence(s):
	strings = ""
	for words in s:
		strings += words
		return strings

def convertToList(string):
	Li = list(string.strip(" "))
	return Li

hiddenMessage = listToSentence(Extracted)

hexTranslator = {
'a': '61',
'b': '62',
'c': '63', 
'd': '64',
'e': '65',
'f': '66',
'g': '67',
'h': '68',
'i': '69',
'j': '6a',
'k': '6b',
'l': '6c',
'm': '6d',
'n': '6e',
'o': '6f',
'p': '70',
'q': '71',
'r': '72',
's': '73',
't': '74',
'u': '75',
'v': '76',
'w': '77',
'x': '78',
'y': '79',
'z': '7a',
' ': '20',

'0': '30',
'1': '31',
'2': '32',
'3': '33',
'4': '34',
'5': '35',
'6': '36',
'7': '37',
'8': '38',
'9': '39' 
}
morseTranslator = {
'a': '.-',
'b': '-...',
'c': '-.-.', 
'd': '-..',
'e': '.',
'f': '..-.',
'g': '--.',
'h': '....',
'i': '..',
'j': '.---',
'k': '-.-',
'l': '.-..',
'm': '--',
'n': '-.',
'o': '---',
'p': '.--.',
'q': '--.-',
'r': '.-.',
's': '...',
't': '-',
'u': '..-',
'v': '...-',
'w': '.--',
'x': '-..-',
'y': '-.--',
'z': '--..',

'0': '-----',
'1': '.----',
'2': '..---',
'3': '...--',
'4': '....-',
'5': '.....',
'6': '-....',
'7': '--...',
'8': '---..',
'9': '----.' 
}


if (hiddenMessage[0:3] == "Hex"):
	hexLength = len(hiddenMessage)
	hexCode = hiddenMessage[4:hexLength]
	hexCode = hexCode.split(" ")
	hexList = []
	for newline in hexCode:
		hexList.append(newline.replace("\n", ""))
	plainText = ""
	for h in hexList:
		for t in hexTranslator:
			if(h == hexTranslator[t]):
				plainText += t
	f = open("test_file1_f11711jy.txt", "w")
	f.write(plainText)
	
	


elif(hiddenMessage[0:3] == "Cae"):
	alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
	caeserLength = len(hiddenMessage)
	caeserCode = hiddenMessage[18:caeserLength]
	textPosition = 0
	plainText = ""
	while(textPosition < len(caeserCode)): 
		textChar = caeserCode[textPosition]
		alphabetPosition = 3
		if(textChar == " "):
			plainText += " "
			textPosition += 1
			continue
		while(textChar != alphabet[alphabetPosition]):
			alphabetPosition += 1
			if(textChar == alphabet[alphabetPosition]):
				break;
		alphabetPosition = alphabetPosition - 3
		plainText = plainText + alphabet[alphabetPosition]
		textPosition += 1
	f = open("test_file2_f11711jy.txt", "w")
	f.write(plainText)

		

elif(hiddenMessage[0:3] == "Mor"):
	morseLength = len(hiddenMessage)
	morseCode = hiddenMessage[11:morseLength]
	morseCode = morseCode.split(" ")
	plainText = ""
	for m in morseCode:
		for d in morseTranslator:
			if(m == '/'):
				plainText += " "
				break
			if(m == morseTranslator[d]):
				plainText += d

	f = open("test_file3_f11711jy.txt", "w")
	f.write(plainText)