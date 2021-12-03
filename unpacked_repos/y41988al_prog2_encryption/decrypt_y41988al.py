inputFileName = input("Please enter the input file name including the extension: ")
cipherText = 0
inputFile = open(inputFileName, "r")
for line in inputFile:
	cipherText = line.lower()
	print(cipherText)
inputFile.close()

if (cipherText[:5] == "morse"):
	print("It's Morse code!")
	cipherText = cipherText.lower()
	cipherList = cipherText.split(':', 1)
	cipher = cipherList[1]
	morseCodeDictionary = { '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
		'--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l','--':'m','-.':'n','---':'o',
		'.--.':'p','--.-':'q','.-.':'r','...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
		'-.--':'y','--..':'z','-----':'0','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5',
		'-....':'6','--...':'7','---..':'8','----.':'9','.-.-.-':'.','--..--':',','..--..':'?',
		'.----.':"'",'-.-.--':'!','-..-.':'/','-.--.':'(','-.--.-':')','-....-':'-','.-..-.':'"',
		'---...':':','-.-.-.':';','-...-':'=','.-.-.':'+','.--.-.':'@','..--.-':'_','...-..-':'$', '/':' '}
	cipherWords = cipher.split('/')
	element = ""
	plaintext = ""
	for i in range(0, len(cipherWords)):
		value = cipherWords[i].split()
		for element in range(0, len(value)):
			char = morseCodeDictionary.get(value[element])
			plaintext = str(plaintext) + str(char)
		plaintext = str(plaintext) + str(" ")
	print("Plaintext: "+plaintext)
#COMPLETE


elif (cipherText[:3] == "cae"):
	print("It's a caesar shift to the right by 3!")
	cipherText = cipherText.lower()
	print(cipherText)
	cipherList = cipherText.split(':', 1)
	cipher = cipherList[1]
	plaintext = ""
	alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
	cipherPosition = 0

	while(cipherPosition < len(cipher)):
		cipherChar = cipher[cipherPosition]
		ASCIIValue = ord(cipherChar)
		ASCIIValue = ASCIIValue - 3
		plaintext = plaintext + chr(ASCIIValue)
		cipherPosition = cipherPosition + 1
		continue 
	print("Plaintext: " + plaintext)
#ADD SPACES TO PLAINTEXT


elif (cipherText[:3] == "hex"):
	print("It's hexadecimal!")
	cipherText = cipherText.lower()
	print(cipherText)
	cipherText = cipherText.replace(" ", "")
	cipherList = cipherText.split(':', 1)
	print(cipherList)
	cipher = cipherList[1]
	print(cipher)
	plaintext = ""
	cipherElement = bytes.fromhex(cipher)
	plaintext = cipherElement.decode("ASCII")
	plaintext = plaintext.lower()
	print("Plaintext: "+plaintext)
#COMPLETE
else:
	print("Not a known method of encryption.")

outputFileName = input("Please enter the output file name including the extension: ")
outputFile = open(outputFileName, "w")
outputFile.write(plaintext)
outputFile.close()

