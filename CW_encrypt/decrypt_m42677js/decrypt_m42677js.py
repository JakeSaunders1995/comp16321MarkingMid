import re, argparse

parser = argparse.ArgumentParser(description="Decrption")
parser.add_argument('input', type=argparse.FileType('r'), help="input text file")
parser.add_argument('o', type=argparse.FileType('w'), help="output the decrypted text to a file")
args = parser.parse_args()

encryptedFile = ()
file = args.input.read()
encryptedFile = file
print(encryptedFile)

lower = "xyzabcdefghijklmnopqrstuvwxyzabc"
decryptedText = ""
answer = ""
textPosition = 0

if (encryptedFile[0] == "H"):
	decryptedText = ""
	lower = "xyzabcdefghijklmnopqrstuvwxyzabc"
	hexText = ""
	pattern = re.compile(r'\d[a-z\d]')
	matches = pattern.finditer(encryptedFile)	
	for match in matches:
		hexValue = match.group()
		bytes_object = bytes.fromhex(hexValue)
		ascii_string = bytes_object.decode("ASCII")
		decryptedText = decryptedText + ascii_string
		answer = decryptedText.lower()

elif(encryptedFile[0] == "C"):
	hexTextwithPunc = ""
	hexText = ""
	pattern1 = re.compile(r':.+')
	matches1 = pattern1.finditer(encryptedFile)

	for match in matches1:
	    character = match.group()
	    hexTextwithPunc = hexTextwithPunc + character

	encryptedFile = hexTextwithPunc
	pattern0 = re.compile(r'[a-z]+.')
	matches0 = pattern0.finditer(encryptedFile)

	for match in matches0:
	    character1 = match.group()
	    hexText = hexText + character1

	while textPosition < len(hexText):
		textChar = hexText[textPosition]
		lowerPosition = 3
		if textChar not in lower:
			textPosition += 1
			decryptedText = decryptedText + textChar
			continue
		elif textChar in lower:
			while textChar != lower[lowerPosition]:
				lowerPosition += 1
				if textChar == lower[lowerPosition]:
					break
			lowerPosition -= 3
			decryptedText = decryptedText + lower[lowerPosition]
			textPosition += 1
	answer = answer + decryptedText

elif(encryptedFile[0] == "M"):
	morseText = ""
	pattern2 = re.compile(r'[^:a-zA-Z]')
	matches2 = pattern2.finditer(encryptedFile)	
	for match in matches2:
		morseValue = match.group()
		morseText = morseText + morseValue
		character = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9', ' ']
		code = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.', '/']
		morse_dict = {}
		zipped_code_char = zip(code,character)
		morse_dict = dict(list(zipped_code_char))
		while True:
			input_message = []
			outputDecryptedCode = []
			input_message.append(morseText)
			morseCodeList = morseText.split( )

			for value in range (0,len(morseCodeList)):
				if morseCodeList[value] in (morse_dict.keys()):
					outputDecryptedCode.append(morse_dict[morseCodeList[value]])
			answer = ''.join(outputDecryptedCode)
			break
			
else:
	print("Please state the type of decryption by setting your first character H for Hex decryption, C for Caesor Cipher and M for Morse Code")



print(answer)

file = args.o.write("%s" %answer)