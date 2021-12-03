import sys, os 
from pathlib import Path
import ntpath

inputfile = sys.argv[1] 
outputfile = sys.argv[2]

for in_entry in os.scandir(inputfile):
	file1 = open(in_entry.path, 'r')
	cipherText = file1.readline().strip()
	file1.close()
	file2name = Path(in_entry).stem + "_n79777aa.txt"
	file2name = os.path.join(outputfile, file2name)
	outputfilefinal = open(file2name, 'w+')

	if cipherText[0] == 'C':
		EnglishWords = ""
		codePosition = 18
		while codePosition < len(cipherText):
			if cipherText[codePosition] == " ":
				EnglishWords = EnglishWords + " "
				codePosition = codePosition + 1
			else:
				codeChar = cipherText[codePosition]
				ASCII = ord(codeChar)
				ASCII = ASCII - 3
				EnglishWords = EnglishWords + chr(ASCII) 
				codePosition = codePosition + 1
		Message1 = EnglishWords.lower()
		outputfilefinal.write(str(Message1))


	if cipherText[0] == 'M':
	    Alphabet ={
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
	        '9': '----.',
		    ' ' : '/'	   
	        }

	    Message2 = ""
	    morse_dyc = {a : b for b,a in Alphabet.items()}
	    cipherTextShort = cipherText[11:]
	    cipherText = cipherTextShort.split()
	    for d in cipherText:
	   		EnglishText = morse_dyc.get(d)
	   		Message2 = str(Message2) + str(EnglishText)
	    outputfilefinal.write(str(Message2))
	

	if cipherText[0] == 'H':
		hexcode = cipherText[4:]
		hexcode2 = bytes.fromhex(hexcode)
		hexcode3 = hexcode2.decode("ascii")
		Message3 = hexcode3.lower()
		outputfilefinal.write(str(Message3))
	
outputfilefinal.close()
