import sys
import os
inDir = sys.argv[1] + "/"
outDir = sys.argv[2] + "/"

for file in os.listdir(inDir):
	inFile = open(inDir + file, "r")
	message = inFile.readline().rstrip("\n")
	inFile.close()


	algo_ci = message.split(":")
	if algo_ci[0] == "Hex":
		decryptedText = bytearray.fromhex(algo_ci[1]).decode()

	elif algo_ci[0] == "Caesar Cipher(+3)":
		decryptedText = ""
		
		for letter in algo_ci[1]:
			if letter.isalpha():
				ordValue = ord(letter)
				if ordValue < 100:
					decryptedText += chr(ordValue + 23)
				else:
					decryptedText += chr(ordValue - 3)
			else:
				decryptedText += letter

	elif algo_ci[0] == "Morse Code":
		morse = {".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e",
		"..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j",
		"-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o",
		".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t",
		"..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y",
		"--..":"z", ".----":"1", "..---":"2", "...--":"3", "....-":"4",
		".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9",
		"-----":"0", "..--..":"?", "-.-.--":"!", ".-.-.-":".", "--..--":",",
		"-.-.-.":";", "---...":":", ".-.-.":"+", "-....-":"-", "-..-.":"/",
		"-...-":"=", ".----.":"'", "-.--.":"(", "-.--.-":")", ".-...":"&",
		"..--.-":"_", "...-..-":"$", ".--.-.":"@", ".-..-.":"\"", "":""}

		decryptedText = ""
		words = algo_ci[1].split("/")

		for word in words:
			letters = word.split(" ")
			for letter in letters:
				decryptedText += morse.get(letter)
			decryptedText += " "
		decryptedText = decryptedText[:-1]


	outputFileName = file[:-4] + "_r88993ia" + file[-4:]

	outFile = open(outDir + outputFileName, "w")
	outFile.write(decryptedText)
	outFile.close()