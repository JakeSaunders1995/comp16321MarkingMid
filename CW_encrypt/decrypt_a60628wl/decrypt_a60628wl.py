import sys

InputFolder = sys.argv[1] + "/test_file2.txt"
OutputFolder = sys.argv[2] + "/decryptOutput.txt"

readFile = open(InputFolder, "r")

fileTextRaw = readFile.readlines()
fileText = ""
for a in fileTextRaw:
	fileText = fileText + a
pass

Hex = "Hex"
CaesarCipher = "Caesar"
Morse = "Morse"

if Hex in fileText:
	hexCoded = fileText[4:]
	hexDecoded = "" 
	hexDecoded = bytearray.fromhex(hexCoded).decode()
	newFileHex = open(OutputFolder, "w")
	newFileHex.write(str(hexDecoded))
	newFileHex.close()


if CaesarCipher in fileText:
	caesarCoded = fileText[18:]
	for b in caesarCoded:
		caesarInteger = ((ord(b) - 3 - 97)%26 +97)
		caesarText = (chr(caesarInteger))
		if "k" in caesarText:
			caesarText = " "
		print(caesarText, end = "")
	newFileCaesar = open(OutputFolder, "w")
	newFileCaesar.write(str(caesarText))
	newFileCaesar.close()





morseDictionary = { "a": ".-", "b": "-...", "c": "-.-.",
					"d": "-..", "e": ".", "f": "..-.", 
					"g": "--.", "h": "....", "i": "..",
					"j": ".---", "k": "-.-", "l": ".-..", 
					"m": "--", "n": "-.", "o": "---", 
					"p": ".--.", "q": "--.-", "r": ".-.", 
					"s": "...", "t": "-", "u": "..-", 
					"v": "...-", "w": ".--", "x": "-..-", 
					"y": "-.--", "z": "--..", "1": ".----", 
					"2": "..---", "3": "...--", "4": "....-", 
					"5": ".....", "6": "-....", "7": "--...",
					"8": "---..", "9": "----.", "0": "-----", 
					",": "--..--", ".": ".-.-.-", "?": "..--..", 
					"/": "-..-.", "-": "-....-", "(": "-.--.", 
					")": "-.--.-", " ": "/"}

morseDictionaryReverse = {v: k for k,v in morseDictionary.items()}


if Morse in fileText:
	morseCoded = fileText[11:]
	morseDecoded = ''
	for c in morseCoded:
		if c != ' ':
			morseDecoded = morseDecoded + c
		elif c == '/':
			print(morseDictionaryReverse[morseDecoded], end=" ")
		else:
			print(morseDictionaryReverse[morseDecoded], end="")
			morseDecoded = ""
			newFileMorse = open(OutputFolder, "w")
			newFileMorse.write(str(morseDecoded))
			newFileMorse.close()


