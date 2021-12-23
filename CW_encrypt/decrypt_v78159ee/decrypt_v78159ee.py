import os
import sys #takes command line arguments and passes it through the code

inputfolder = sys.argv[1]
outputfolder = sys.argv[2]

morse_dict = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "/": " ",
    ".-.-.-": ".",
    "--..--": ",",
    "---...": ":",
    "..--..": "?",
    ".----.": "'",
    "-....-": "-",
    "-..-.": "/",
    "-.--.-": ")",
    "-.--.": "(",
    ".-..-.": '"',
    "-.--.": "[",
    "-.--.-": "]",
    "---.": "!",
    "*----": "1",
    "**---": "2",
    "***--": "3",
    "****-": "4",
    "*****": "5",
    "-****": "6",
    "--***": "7",
    "---**": "8",
    "----*": "9",
    "-----": "0",
}

for filename in os.listdir(inputfolder):
	f = os.path.join(inputfolder, filename)
	if os.path.isfile(f):
		inputfile = open(f)
		contents = inputfile.read()
		
		plainText = ""
		if "Caesar Cipher" in contents:    
			
			cipherText = contents.split(":")
			cipherWords = cipherText[1]
			cipherTextPosition = 0
			
			while (cipherTextPosition < len(cipherWords)):
				cipherTextChar = cipherWords[cipherTextPosition]
				if cipherTextChar == " ":
					plainText = plainText + " "
				else:
					ASCIIValue = ord(cipherTextChar)
					ASCIIValue = ASCIIValue - 3
					if ASCIIValue < 97:
						ASCIIValue = ASCIIValue + 26
					plainText = plainText + chr(ASCIIValue) 
				cipherTextPosition = cipherTextPosition + 1

			print(plainText)
			output = filename[:-4] + "_v78159ee.txt"
			folderpath = os.path.join(outputfolder, output) #gets the path for the output folder
			output_file = open(folderpath, "w")
			output_file.write(plainText)
        
		
		elif "Hex" in contents:
			
			cipherText = contents.split(":")
			hexWords = cipherText[1]
			hexList = hexWords.split()
			for i in range(0, len(hexList)):
				hexWord = hexList[i]	
				ASCIIValue = bytes.fromhex(hexWord)			
				ASCIIValue = ASCIIValue.decode()
				plainText = plainText + ASCIIValue
				
			print(plainText)
			output = filename[:-4] + "_v78159ee.txt"
			folderpath = os.path.join(outputfolder, output) #gets the path for the output folder
			output_file = open(folderpath, "w")
			output_file.write(plainText)
        
		else:	
			cipherText = contents.split(":")
			cipherText = cipherText[1].split()
			cipherWordPosition = 0
			while cipherWordPosition < len(cipherText):
				morseLetter = cipherText[cipherWordPosition]
				plainText = plainText + morse_dict[morseLetter]
				cipherWordPosition = cipherWordPosition + 1
				
			print(plainText)
			output = filename[:-4] + "_v78159ee.txt"
			folderpath = os.path.join(outputfolder, output) #gets the path for the output folder
			output_file = open(folderpath, "w")
			output_file.write(plainText)
        
				
				
				
			
			 
			

			
