import sys, os


#txtFile = "Caesar Cipher(+3):exw fdhvdu lv d olwwoh pruh gliilfxow"
#txtFile = "Morse Code:.... --- .-- . ...- . .-. / ... --- .-.. ...- .. -. --. / -- --- .-. ... . / -.-. --- -.. . / -- .- -.-- / -... . / - .... . / -- --- ... - / -.. .. ..-. ..-. .. -.-. ..- .-.. -"
#txtFile = "Hex:53 6f 6c 76 69 6e 67 20 68 65 78 20 69 73 20 76 65 72 79 20 65 61 73 79 20 69 6e 20 70 79 74 68 6f 6e"
inputdDirName = sys.argv[1]
outputDirName = sys.argv[2]

files = os.listdir(inputdDirName)

for file in files:
	baseFileName = os.path.splitext(file)[0]
	fullFileName = inputdDirName + "/" + file

	txtFiles = open(fullFileName, "r")
	txtFile = txtFiles.read()
	txtFiles.close()
	txtFile = txtFile.strip()

	outputFullFileName = outputDirName + "/" + baseFileName + "_e40494op.txt"
	translation = open(outputFullFileName, "w")

	if txtFile[0] == "H":
		for i in range(len(txtFile)):
			if txtFile[i] == ":":
				cut = i + 1
				newFile = txtFile[cut:len(txtFile)]
				newFile = newFile.strip()
				
		hexTranslation = bytes.fromhex(newFile).decode("utf-8")
		hexTranslation = hexTranslation.lower()
		
		translation.write(hexTranslation)

	elif txtFile[0] == "C":

		
		for i in range(len(txtFile)):
			if txtFile[i] == ":":
				cut = i + 1
				newFile = txtFile[cut:len(txtFile)]
				newFile = newFile.strip()
		
		cipherTxt = ""
		wordPosition = 0
		while wordPosition < len(newFile):
	 		letter = newFile[wordPosition]
	 		asciiValue = ord(letter)
	 		if asciiValue == 32:
	 			cipherTxt = cipherTxt + " "
	 			#wordPosition = wordPosition + 1
	 		elif asciiValue == 97:
	 			cipherTxt = cipherTxt + "x"
	 		elif asciiValue == 98:
	 			cipherTxt = cipherTxt + "y"
	 		elif asciiValue == 99:
	 			cipherTxt = cipherTxt + "z"

	 		else:
	 			asciiValue = asciiValue - 3
	 			cipherTxt = cipherTxt + chr(asciiValue)
	 		wordPosition = wordPosition + 1
		
		
		translation.write(cipherTxt)




	elif txtFile[0] == "M":
	 	for i in range(len(txtFile)):
				if txtFile[i] == ":":
	 				cut = i + 1
	 				newFile = txtFile[cut:len(txtFile)]
	 				newFile = newFile.strip()


	 	ssplit = newFile.split()
	 	cypherText = ""
	 	for code in ssplit:
	 		if code == ".-":
	 			cypherText = cypherText + "a"
	 		if code == "-...":
	 		    cypherText = cypherText + "b"	
	 		if code == "-.-.":
	 			cypherText = cypherText + "c"
	 		if code == "-..":
	 			cypherText = cypherText + "d"
	 		if code == ".":
	 			cypherText = cypherText + "e"
	 		if code == "..-.":
	 			cypherText = cypherText + "f"
	 		if code == "--.":
			   cypherText = cypherText + "g"
	 		if code == "....":
	 			cypherText = cypherText + "h"
	 		if code == "..":
	 			cypherText = cypherText + "i"
	 		if code == ".---":
	 			cypherText = cypherText + "j"
	 		if code == "-.-":
	 			cypherText = cypherText + "k"
	 		if code == ".-..":
	 			cypherText = cypherText + "l"
	 		if code == "--":
	 			cypherText = cypherText + "m"
	 		if code == "-.":
	 			cypherText = cypherText + "n"
	 		if code == "---":
	 			cypherText = cypherText + "o"
	 		if code == ".--.":
	 			cypherText = cypherText + "p"
	 		if code == "--.-":
	 			cypherText = cypherText + "q"
	 		if code == ".-.":
	 			cypherText = cypherText + "r"
	 		if code == "...":
			    cypherText = cypherText + "s"
	 		if code == "-":
	 			cypherText = cypherText + "t"
	 		if code == "..-":
	 			cypherText = cypherText + "u"
	 		if code == "...-":
	 			cypherText = cypherText + "v"
	 		if code == ".--":
	 			cypherText = cypherText + "w"
	 		if code == "-..-":
	 			cypherText = cypherText + "x"
	 		if code == "-.--":
	 			cypherText = cypherText + "y"
	 		if code == "--..":
	 			cypherText = cypherText + "z"
	 		if code == "/":
	 			cypherText = cypherText + " "
	 		
	 	translation.write(cypherText)
 		
