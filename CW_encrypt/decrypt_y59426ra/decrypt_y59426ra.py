import sys, os, string

#the followings are the functions for decodeing each type

def hexDecryption (TextInFile):

	textH= TextInFile[5:]

	#print("This is a hex encrption")

	DecodedTextHEX = bytes.fromhex(textH)
	DecodedTextHEX = DecodedTextHEX.decode("ascii")

	return DecodedTextHEX.lower()

def Ceaser3Decryption(TextInFile):

	#print("this is a Ceaser encryption")

	textV= TextInFile[18:].lower()

	alphabet = string.ascii_lowercase
	DecodedC3 = ""

	for i in textV:

		if i in alphabet:
			position = alphabet.find(i)
			new_position = (position - 3) % 26
			new_charcter = alphabet[new_position]
			DecodedC3 += new_charcter
		else:
			DecodedC3 += i
	return DecodedC3.lower()

def MorseDecryption(TextInFile):

	MorseDecryption = str()

	#textV = TextInFile[11:]
	#print("this is a Morse encryption")

	MORSE_CODE_DICT = {'....' : 'h', 
	'.-' : 'a', '-...' : 'b', '-.-.' : 'c', 
	'-..' : 'd', '.' : 'e', '..-.' : 'f', 
	'--.' : 'g', '..' : 'i', '.---' : 'j', 
	'-.-' : 'k', '.-..' : 'l', '--' : 'm', 
	'-.' : 'n', '---' : 'o', '.--.' : 'p', 
	'--.-' : 'q', '.-.' : 'r', '...' : 's', 
	'-' : 't', '..-' : 'u', '...-' : 'v', 
	'.--' : 'w', '-..-' : 'x', '-.--' : 
	'y', '--..' : 'z', '.-.-.-' : '.', 
	'..--..' : '?', '--..--' : ',', '/' : ' ',
	'-----':'0', '.----':'1', '..---':'2', '...--':'3', '....-':'4',
    '.....':'5', '-....':'6', '--...': '7', '---..':'8', '----.':'9'
}

	encryptedText = TextInFile.split(":")
	encryptedWords = encryptedText[1].split(" ")

	for x in encryptedWords:
		encryptedWords = MORSE_CODE_DICT.get(x)
		MorseDecryption += str(encryptedWords)
	return(MorseDecryption.lower())




pathFileIn = sys.argv[1]
pathFileOut = sys.argv[2]

for filename in os.listdir(pathFileIn):
	print
	with open(os.path.join(pathFileIn, filename), "r") as file:
		FileIn = file.read()
		with open(os.path.join(pathFileOut, os.path.basename(filename)[:-4] + "_y59426ra.txt"), "w+") as file:
			TextInFile=FileIn
			value = TextInFile[0]
			if value == "H":
				#print("the decrypted text is: ",hexDecryption (TextInFile))
				#fOut = pathFileOut + "/" + filename[0:-4] + "_" + "y59426ra" + ".txt"
				file.write(hexDecryption(TextInFile))

			elif value == "C":
				#print("the decrypted text is: ",Ceaser3Decryption(TextInFile))
				#fOut = pathFileOut + "/" + filename[0:-4] + "_" + "y59426ra" + ".txt"
				file.write(Ceaser3Decryption(TextInFile))

			elif value == "M":
				#print("the decrypted text is: ",MorseDecryption(TextInFile))
				#fOut = pathFileOut + "/" + filename[0:-4] + "_" + "y59426ra" + ".txt"
				file.write(MorseDecryption(TextInFile))
			
#pathin: /home/csimage/COMP16321/coursework/16321_python_coursework_y59426ra/midterm/Program2/Example_inputs_program2
#pathout: /home/csimage/COMP16321/coursework/16321_python_coursework_y59426ra/midterm/Program2/Example_outputs_program2