import sys,argparse,os

def decryptCaesar3():
	finalString=""
	for i in range(len(encryptedString)):
		char=encryptedString[i]
		if char!= " ":
			ASCIIvalue=ord(char)
			ASCIIvalue-=3
			finalString+=chr(ASCIIvalue)
		else:
			finalString+=" "
	return finalString.lower()

def decryptMorse(encryptedString):
	finalString=""
	subString=""
	morseDict={
		'a':'.-', 'b':'-...','c':'-.-.', 'd':'-..', 'e':'.',
	    'f':'..-.', 'g':'--.', 'h':'....','i':'..', 'j':'.---', 'k':'-.-',
	    'l':'.-..', 'm':'--', 'n':'-.','o':'---', 'p':'.--.', 'q':'--.-',
	    'r':'.-.', 's':'...', 't':'-','u':'..-', 'v':'...-', 'w':'.--',
	    'x':'-..-', 'y':'-.--', 'z':'--..','1':'.----', '2':'..---', '3':'...--',
	    '4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
	    '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', 
	    '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-','!':'-.-.--',':':'---...',
	    ';':'-.-.-.','"':'.-..-.'
	}
	encryptedString+=" "

	for character in encryptedString:
		if character==" ":
			if subString!="":
				finalString+=list(morseDict.keys())[list(morseDict.values()).index(subString)]
				subString=""
		elif character=="/":
			finalString+=" "
		else:
			subString+=character
	return finalString

inputFolder=sys.argv[1]
outputFolder=sys.argv[2]
if not os.path.exists(outputFolder):
	os.mkdir(outputFolder)
inFolderList=os.listdir(inputFolder)

for file in inFolderList:
	if file.endswith('.txt'):
		inputFile=open(inputFolder + '/' + file)
		fileContent=inputFile.read()
		inputFile.close()
		splitString=fileContent.split(":")
		encryptedString=splitString[1]

		if splitString[0] in ["Hex","hex","Hexadecimal","hexadecimal"]:
			byteArray=bytearray.fromhex(encryptedString)
			decryptedString=byteArray.decode().lower()
		elif splitString[0] in ["Caesar Cipher(+3)","caesar +3","Caesar +3", "caesar cipher(+3)"]:
			decryptedString=decryptCaesar3()
		elif splitString[0] in ["morseCode","morse code","Morse Code"]:
			decryptedString=decryptMorse(encryptedString)

		newFile=file[:-4]
		outputFile=open(outputFolder + '/' + newFile + "_h01895cg.txt","w")
		outputFile.write(decryptedString)
