import os
import argparse
import re

def readArg():
	#Read Argument from Terminal
	parse = argparse.ArgumentParser()
	parse.add_argument("FileInput", help="Text Input File Path")
	parse.add_argument("FileOutput", help="Text Output File Path")

	ArgReader = parse.parse_args()
	return ArgReader.FileInput, ArgReader.FileOutput

def readFile(path):
	previousPath = os.getcwd()
	os.chdir(path)
	files = os.listdir()
	FileNames = []
	pattern = re.compile(r"^.*.txt$")
	for x in files:
		#print(x)
		if (pattern.search(x)):
			FileNames.append(x)
	os.chdir(previousPath)
	return FileNames


#Read Argument from Terminal
FileInputLocation, FileOutputLocation = readArg()


#DetermineEncryption and starting point
def DetermineEncryption(line):
	EncryptionType = line[0: 3].upper()
	colonLocation = 0
	for a in range(0, len(line)):
		if (line[a: (a + 1)] == ":"):
			colonLocation = a
			break;
		

	return EncryptionType, colonLocation

def decryptCode(EncryptionType, colonLocation, line):
	colonLocation = colonLocation + 1
	max = len(line)
	hexWord = ""
	Text = ""
	if (EncryptionType == "HEX"):
		for x in range(colonLocation, max):
			if (line[x: x+1] == " "):
				if ((int(hexWord, 16) >64) and (int(hexWord, 16) < 91)):
					Text = Text + chr(int(hexWord, 16) + 32)
				else:
					Text = Text + chr(int(hexWord, 16))
				hexWord = ""
			elif(x == (max - 1)):
				hexWord = hexWord + line[x: x+1]
				#hexWord = "0x" + hexWord.upper()
				Text = Text + chr(int(hexWord, 16))
			else:
				hexWord = hexWord + line[x: x+1]
	elif(EncryptionType == "CAE"):
		alphabet = ["x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
		for x in range(colonLocation, max):
			character = False
			for y in range(3, len(alphabet)):
				if (alphabet[y] == line[x:x+1].lower()):
					Text = Text + alphabet[y - 3]
					character = True
			if (character == False):
				Text = Text + line[x : x + 1]
					
	elif(EncryptionType == "MOR"):
		morseAlphabet = {
			"/" : " ",
			".-" : "a",
			"-..." : "b",
			"-.-." : "c",
			"-.." : "d",
			"." : "e",
			"..-." : "f",
			"--." : "g",
			"...." : "h",
			".." : "i",
			".---" : "j",
			"-.-" : "k",
			".-.." : "l",
			"--" : "m",
			"-." : "n",
			"---" : "o",
			".--." : "p",
			"--.-" : "q",
			".-." : "r",
			"..." : "s",
			"-" : "t",
			"..-" : "u",
			"...-" : "v",
			".--" : "w",
			"-..-" : "x",
			"-.--" : "y",
			"--.." : "z",
			".----" : "1",
			"..---" : "2",
			"...--" : "3",
			"....-" : "4",
			"....." : "5",
			"-...." : "6",
			"--..." : "7",
			"---.." : "8",
			"----." : "9",
			"-----" : "0",
			".-.-.-" : ".",
			"--..--" : ",",
			"..--.." : "?",
			".----." : "'",
			"-..-." : "/",
			"---..." : ":",
			"-.-.-." : ";",
			".-.-." : "+",
			"-....-" : "-",
			"-...-" : "=",
			"-.-.--" : "!",
			"-.--." : "(",
			"-.--.-" : ")",
			".-..-." : '"'
		}
		morseWord = ""
		for x in range(colonLocation, max):
			if (line[x: x+1] == " "):
				Text = Text + morseAlphabet[str(morseWord)]
				morseWord = ""
			elif(x == (max - 1)):
				morseWord = morseWord + line[x: x+1]
				Text = Text + morseAlphabet[str(morseWord)]
			else:
				morseWord = morseWord + line[x: x+1]
	return(Text)


FileNames = readFile(FileInputLocation)

#Check to see if / is missing at the end of location
if (FileInputLocation[len(FileInputLocation)-1 : len(FileInputLocation)] != "/"):
		FileInputLocation = FileInputLocation + "/"
if (FileOutputLocation[len(FileOutputLocation)-1 : len(FileOutputLocation)] != "/"):
	FileOutputLocation = FileOutputLocation + "/"

for x in FileNames:
	print("Results from: " + x)

	#Open file at both Input and Output Location
	FileToRead = str(str(FileInputLocation) + x)
	FileInputReader = open(FileToRead, "r")
	FileInput = FileInputReader.readline()

	#Adding University Username to Output File
	FileWriteName = x [0: (int(len(x)) - 4)] + "_m19364tg.txt"
	FileToWrite = str(str(str(FileOutputLocation) + FileWriteName))
	FileOutputWriter = open(FileToWrite, "w")

	#Program Here
	EncryptionType, colonLocation = DetermineEncryption(FileInput)
	Text = decryptCode(EncryptionType, colonLocation, FileInput)

	#Write results to result folder and close files
	FileOutputWriter.write(Text)
	FileInputReader.close()
	FileOutputWriter.close()