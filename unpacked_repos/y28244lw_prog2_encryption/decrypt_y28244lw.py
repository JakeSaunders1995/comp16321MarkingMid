import sys
import os
import string


FolderIN = str(sys.argv[1])
FolderOUT = str(sys.argv[2])

for files in os.listdir(FolderIN):
	filename = str(files)
	InFilePath = os.path.join(FolderIN,filename)


	with open(InFilePath) as f:
		line = f.readlines()
	f.close()

	line = line[0]
	pos = 0
	message = ""


	for i in range(0,len(line)):
		if line[i] == ":":
			pos = i

	algorithm = line[0:pos]
	code = line[pos+1:]


	if algorithm[0].lower() == "h": #for hex
		message = bytearray.fromhex(code).decode()

	elif algorithm[0].lower() == "c": #for caesar
		alphabet = "abcdefghijklmnopqrstuvwxyzabc"
		words = code.split(" ")
		for c in range(len(words)):
			NWord = ""
			for i in range(len(words[c])):
				character = words[c][i].lower()
				CPos = 0

				if character.isalpha() == False:
					NWord += character
				else:

					for j in range(0,len(alphabet)):
						if character == alphabet[j] and j-3 >=0:
							NWord += alphabet[j - 3]
							break
			if c < len(words):
				message += NWord + " "

		
	elif algorithm[0].lower() == "m": #for morse
		words = code.split("/")
		for word in words:
			MChar = word.split(" ")
			DWord = ""
			for character in MChar:
				DChar = ""
				#letters
				if character == ".-":
					DChar = "a"
				elif character == "-...":
					DChar = "b"
				elif character == "-.-.":
					DChar = "c"
				elif character == "-..":
					DChar = "d"
				elif character == ".":
					DChar = "e"
				elif character == "..-.":
					DChar = "f"
				elif character == "--.":
					DChar = "g"
				elif character == "....":
					DChar = "h"
				elif character == "..":
					DChar = "i"
				elif character == ".---":
					DChar = "j"
				elif character == "-.-":
					DChar = "k"
				elif character == ".-..":
					DChar = "l"
				elif character == "--":
					DChar = "m"
				elif character == "-.":
					DChar = "n"
				elif character == "---":
					DChar = "o"
				elif character == ".--.":
					DChar = "p"
				elif character == "--.-":
					DChar = "q"
				elif character == ".-.":
					DChar = "r"
				elif character == "...":
					DChar = "s"
				elif character == "-":
					DChar = "t"
				elif character == "..-":
					DChar = "u"
				elif character == "...-":
					DChar = "v"
				elif character == ".--":
					DChar = "w"
				elif character == "-..-":
					DChar = "x"
				elif character == "-.--":
					DChar = "y"
				elif character == "--..":
					DChar = "z"

				#numbers
				elif character == "-----":
					DChar = "0"
				elif character == ".----":
					DChar = "1"
				elif character == "..---":
					DChar = "2"
				elif character == "...--":
					DChar = "3"
				elif character == "....-":
					DChar = "4"
				elif character == ".....":
					DChar = "5"
				elif character == "-....":
					DChar = "6"
				elif character == "--...":
					DChar = "7"
				elif character == "---..":
					DChar = "8"
				elif character == "----.":
					DChar = "9"

				#Punctuations
				elif character == ".-.-.-":
					DChar = "."
				elif character == "..--..":
					DChar = "?"
				elif character == "-.-.--":
					DChar = "!"
				elif character == "--..--":
					DChar = ","
				elif character == "---...":
					DChar = ":"
				elif character == "-.-.-.": 
					DChar = ";"
				elif character == "-....-":
					DChar = "-"
				elif character == "-.--.-":
					DChar = "("
				elif character == "	-.--.":
					DChar = ")"
				elif character == ".----.":
					DChar = "'"
				elif character == ".-..-.":
					DChar = '"'
				else:
					DChar = character

				DWord += DChar
			message += DWord + " "

	message = message.lower()

	FPos = filename.index(".")
	outFilename = filename[:FPos] + "_y28244lw.txt"
	OutFilePath = os.path.join(FolderOUT,outFilename)

	fout = open(OutFilePath,"w")
	fout.write(message)
	fout.close()



	


