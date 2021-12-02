import sys
import os

morseCode = ["a", ".-", "b", "-...", "c", "-.-.", "d", "-..", "e", ".", "f", "..-.", "g", "--.", "h", "....", "i", "..", "j", ".---", "k", "-.-", "l", ".-..", "m", "--", "n", "-.", "o", "---", "p", ".--.", "q", "--.-", "r", ".-.", "s", "...", "t", "-", "u", "..-", "v", "...-", "w", ".--", "x", "-..-", "y", "-.--", "z", "--.."]

for textFile in os.listdir(sys.argv[1]):
	filename = (sys.argv[1]+"/"+textFile)
	file = open(filename, "r")
	for line in file:
		ciphertext = line.strip()
		
		if ciphertext[0] == "M":
			ciphertext = ciphertext[(len(ciphertext) - 11) * (-1):]
			plaintext = ""
			morseChar = ""
			for i in range(len(ciphertext)):
				if ciphertext[i] == "." or ciphertext[i] == "-":
					morseChar += ciphertext[i]
				elif ciphertext[i] == " " and ciphertext[i - 1] != "/":
					for j in range(len(morseCode)):
						if morseCode[j] == morseChar:
							newChar = morseCode[j - 1]
					plaintext += newChar
					morseChar = ""
				elif ciphertext[i] == "/":
					plaintext += " "
				if (i + 1) == len(ciphertext):
					for j in range(len(morseCode)):
						if morseCode[j] == morseChar:
							newChar = morseCode[j - 1]
					plaintext += newChar
					morseChar = ""
			print(plaintext)
		
		elif ciphertext[0] == "C":
			ciphertext = ciphertext[(len(ciphertext) - 18) * (-1):]
			plaintext = ""
			for i in range(len(ciphertext)):
				if ciphertext[i] == " ":
					plaintext += " "
				elif ciphertext[i] == "a":
					plaintext += "x"
				elif ciphertext[i] == "b":
					plaintext += "y"
				elif ciphertext[i] == "c":
					plaintext += "z"
				else:
					plaintext += chr(ord(ciphertext[i]) - 3)
			plaintext = plaintext.lower()
			print(plaintext)
		
		elif ciphertext[0] == "H":
			ciphertext = ciphertext[(len(ciphertext) - 4) * (-1):]
			plaintext = bytearray.fromhex(ciphertext).decode()
			plaintext = plaintext.lower()
			print(plaintext)

		outputFile = textFile[:-4]
		outputFile += "_p35799ap.txt"
		outputFile = (sys.argv[2]+"/"+outputFile)
		#print(outputFile)
		# test_file1.txt --> ./output_folder/test_file1_p35799ap.txt
		writeFile = open(outputFile, "w")
		writeFile.write(plaintext)



# line = line.rstrip() # remove spaces from line
# guesses = "" # create empty string
# guess = input("Enter guess " + str(count) + " ") # next character to be added to string
# guesses += guess # update string with next character