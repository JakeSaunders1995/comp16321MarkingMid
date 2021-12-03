import sys
import os

inFolder = sys.argv[1]
outFolder = sys.argv[2]  

for inFile in os.scandir(inFolder):

	fileName = inFile.name

	with open (inFile) as file:
		cText = file.read()

		if (cText[0] == "M"  or cText[0] == "m"):
			morse_code = {
  			  '....' : 'h', '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '-.-.--' : '!' , '---...' : ':' , '-.-.-.' : ';' , '-....-' : '-' , '-.--.' : '(' , '-.--.-' : ')' , '.----.' : '\'' , '.-..-.' : '\"' , 


 			  '/' : ' '
			}	

			cText = cText + " /"
			

			letter = ""
			word = ""
			plaintext = ""

			for i in cText:
				if i == "." or i == "-":

					letter = letter + i

				elif i == " ":
					if letter == "":
						pass
					else:
						completeLetter = morse_code[letter]
						word = word + completeLetter
						letter = ""

				elif i == "/":
					plaintext = plaintext + word + " "
					
					word = ""

				else:
					pass

			

		

			

		elif (cText[0] == "C"  or cText[0] == "c"):

			cText = cText.replace("Caesar Cipher(+3):", "")

			plaintext = ""
			cipherTextPosition = 0
			while (cipherTextPosition < len(cText)):
				cipherTextChar = cText[cipherTextPosition]
				if cipherTextChar == " ":
					plaintext = plaintext + " "

				else:
					ASCIIValue = ord(cipherTextChar)
					ASCIIValue = ASCIIValue - 3
					plaintext = plaintext + chr(ASCIIValue)
					
				cipherTextPosition = cipherTextPosition + 1

			
			

		elif (cText[0] == "H"  or cText[0] == "h"):

			cText = cText.replace("Hex:", "")
			hexText = cText.split(" ")

			x = 0
			plaintext = ""

			while x < len(hexText):
			
		 		i = hexText[x]
		 		a = int(i,16)
		 		
		 		b = chr(a)
		 		
		 		x = x+1
		 		plaintext = plaintext + b


		
			



		else:
			pass 


	outFile = fileName.replace(".txt", "_g33966si.txt")
	completeName = os.path.join(outFolder, outFile)
	fileX = open(completeName, "w")
	fileX.write( plaintext.lower())
	fileX.close()

			




