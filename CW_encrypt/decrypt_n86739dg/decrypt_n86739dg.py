import os, argparse, re
import sys

morseDic ={
    '....' : 'h', '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' '
}
#arrayOfOutputFiles = []

# handle input arguments
if len(sys.argv) == 3:

	inputDirectory = sys.argv[1]
	outputDirectory = sys.argv[2]

	#print(inputDirectory)
	for currentFileName in os.listdir(inputDirectory):
		#print(currentFileName)
		with open(inputDirectory + "/" + currentFileName, 'r') as f:
            
			# step 1 - READ CURRENT FILE
			currentFileContents = f.read()
			print(currentFileContents)
			f.close()

			# step 2 - DO LOGIC
			encryptedmessage = ""
			encryptedmessage = currentFileContents
			encryptedmessage = encryptedmessage.strip() #THE .STRIP IS TAKING OUT FINAL /n OF ALL ENCRYPTEDMESSAGE

			CurrentContentConverted = ""


            #IF MORSE....

			#OUR DICTIONARY MORSEDIC IS ALREADY IN LOWER CASE, NO NEED TO TRANSFORM IT 
			
			if encryptedmessage.startswith("Morse Code:"):
				currentMorse = ""
				accumulatevariable = ""
				i = 0
				encryptedmessage = encryptedmessage.lstrip("Morse Code:") #lstrip REMOVES "Morse Code" FROM THE START
				for character in encryptedmessage: 
					if character != ' ':
						currentMorse += character #ADDS EVERY LETTER IN CIPHERTEXT INTO A STRING UNTIL IT FINDS A SPACE
						i += 1
						#print(morseDic[currentMorse]) THIS PRINTS THE LETTER OF EACH CURRENT MORSE, dont need to accumulate here
						#print(currentMorse)
					elif character == '/':
						print(morseDic[currentMorse], end=' ') #ENDS THE OUTPUT WITH A SPACE 
						#print(currentMorse)
						i = 0
					else: #WHEN SPACE -
						print(morseDic[currentMorse], end='') #NOT ADDING SPACES 
						#print(morseDic[currentMorse]) THIS IS THE ONE THAT ACCUMULATES
						accumulatevariable += morseDic[currentMorse]
						#print(accumulatevariable)
						currentMorse = "" 
						#print(currentMorse)
						i = 0


				if i > 0: #FOR THE LAST CHARACTER WHICH STAYS STORED AT CURRENTMORSE
					print(morseDic[currentMorse])
					accumulatevariable += morseDic[currentMorse]

				CurrentContentConverted = accumulatevariable

			#IF CAESAR +3
			if encryptedmessage.startswith("Caesar Cipher(+3):"):
				encryptedmessage = encryptedmessage[18:]
				length = len(encryptedmessage)
				encryptedmessagePos = 0 
				plainText = ""
				while (encryptedmessagePos < length):  
					for i in encryptedmessage.lower():
						if (i == ' '): #WE NEED THIS IF FOR SPACES
							plainText += ' '
						else:
							encryptedmessageChr = encryptedmessage[encryptedmessagePos] 
							ASCIIValue = ord(encryptedmessageChr)
							ASCIIValue -= 3  #AS IT IS +3 WE -3 TO DECRYPT 
							if ASCIIValue < 97:
								ASCIIValue += 26


							plainText = plainText + chr(ASCIIValue)
							#print(plainText)
						
						encryptedmessagePos += 1

					print(plainText)

					CurrentContentConverted = plainText

			#IF HEX
			if encryptedmessage.startswith("Hex:"):
				encryptedmessage = encryptedmessage.lstrip("Hex:")
				encryptedmessage = encryptedmessage.replace(" ", "") #THIS WILL REMOVE ALL THE WHITESPACES FROM THE STRING 

				def convertHexToString(hexString):
					return chr(int(hexString, 16))   #THIS FUNCTION CONVERTS HEX TO STRING


				string = ""

				if len(encryptedmessage) % 2 == 0: #ENCRYPTED MESSAGE TIENE QUE SER PAR PARA PODER HACER PAREJAS
					for i in range(0,len(encryptedmessage),2): #WE WANT TO GRAB PAIRS OF NUMBERS 
						pairOfNumbers = encryptedmessage[i] + encryptedmessage[i+1] #A CHARACTER IN NORMAL TEXT IS PAIR OF NUMBERS IN HEXADECIMAL
						#print(pairOfNumbers)
						string += convertHexToString(pairOfNumbers) #WE ACCUMULATE EACH CHARACTER TO THE VARIABLE string UNTIL RANGE FINISHES
						#print(string)
				print(string.lower())

				CurrentContentConverted = string.lower()

			# step 3 - CREATING OUTPUT FILEPATH AND FILENAME
			fileSplitArray = os.path.splitext(currentFileName)
			currentOutputFileName = outputDirectory + "/" + fileSplitArray[0] + "_n86729dg" + fileSplitArray[1]
			#print(currentOutputFileName)

			# step 4 - WRITE CONTENTS ON OUTPUT FILE
			currentFileWriter = open(currentOutputFileName, "w")
			currentFileWriter.write(CurrentContentConverted)
			currentFileWriter.close()
else:
	print("Invalid parameters error. Expected: python3 decrypt_n86739dg.py ./[input folder] ./[output folder]")







