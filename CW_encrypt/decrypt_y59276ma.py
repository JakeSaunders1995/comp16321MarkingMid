import os,sys
#Functions
def CaesarCipher(character):
	Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	index = 0
	if (character in Alphabet):
		while(character != Alphabet[index]):
			index += 1
		NewCharIndex = (index - 3 ) % 26
		return Alphabet[NewCharIndex]
	else:
		return " "
def MorseCodeToText(Morse):
	Decrypted = ""
	MorseTextDict = {".-":"a","-...":"b","-.-.":"c","-..":"d",
	".":"e","..-.":"f","--.":"g","....":"h","..":"i",".---":"j",
	"-.-":"k",".-..":"l","--":"m","-.":"n","---":"o",".--.":"p",
	"--.-":"q",".-.":"r","...":"s","-":"t","..-":"u","...-":"v",
	".--":"w","-..-":"x","-.--":"y","--..":"z",".----":"1",
	"..---":"2","...--":"3","....-":"4",".....":"5","-....":"6",
	"--...":"7","---..":"8","----.":"9","-----":"0"}
	for item in Morse:
		if(item !='/'):
			Decrypted = Decrypted + MorseTextDict[item]
		else:
			Decrypted = Decrypted + " "
	return Decrypted

#Main program
path = sys.argv[1]
FileList = os.listdir(path)
for file in FileList:
	print(file[-9999:-4]+"_y59276ma.txt")
	OutputFile = sys.argv[2] +"/"+file[-999:-4]+"_y59276ma.txt"
	InputFile = sys.argv[1] + "/" +file

	DecryptedText = ""
	FileInfo = list()

	EncryptedFile = open(InputFile,"r")
	EncryptionType = EncryptedFile.read(1)
	#Conversion of Hex to Text
	if(EncryptionType == "H" or EncryptionType == "h"):
		FileInfo = EncryptedFile.readline()
		EncryptedFile.close()
		StringSplit = FileInfo.split(":",1)
		EncryptedInfo = StringSplit[1]
		Hex = EncryptedInfo.split()
		for item in Hex:
			Conversion = int(item,16)
			DecryptedText = DecryptedText + chr(Conversion)
		print(DecryptedText.lower())
		print("Hex Encryption")
	#Conversion Of MorseCode to Text
	elif(EncryptionType == "M" or EncryptionType == "m"):
		FileInfo = EncryptedFile.read()
		EncryptedFile.close()
		StringSplit = FileInfo.split(":",1)
		EncryptedInfo = StringSplit[1]
		MorseCode = EncryptedInfo.split()
		DecryptedText = MorseCodeToText(MorseCode)
		print(DecryptedText)
		print("Morse Code Encryption")
	#Conversion of Caesar Cipher Text to PlainText
	elif(EncryptionType == "C" or EncryptionType == "c"):
		FileInfo = EncryptedFile.readline()
		EncryptedFile.close()
		StringSplit = FileInfo.split(":",1)
		EncryptedInfo = StringSplit[1]
		for c in EncryptedInfo:
			DecryptedText = DecryptedText + CaesarCipher(c)
		print(DecryptedText.lower())
		print("Caesar Cipher Encryption")
	DecryptedFile = open(OutputFile,"x")
	DecryptedFile.write(DecryptedText.lower())
	DecryptedFile.close()
	# Results = open(OutputFile,"r")
	# print(Results.read())
	# Results.close()