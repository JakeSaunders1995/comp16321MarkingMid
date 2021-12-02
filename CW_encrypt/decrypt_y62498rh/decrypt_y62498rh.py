import argparse
import os
import re

#Arguments
parser = argparse.ArgumentParser(description = "Input and Output to folders specified")
parser.add_argument("input", type = str, help = "Input folder path")
parser.add_argument("output", type = str, help = "Output folder path")
args = parser.parse_args()

#Initial
morseCodeDict = {".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j", "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o", ".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y", "--..":"z", ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9", "-----":"0", "/":" "}
	#Morse code for some punctuation below, not needed for final program.
	#, ".-.-.-":".", "..--..":"?", "-.-.--":"!", "--..--":",", "---...":":", "-.-.-.":";", "-....-":"—", "-....-":"-", "-.--.":"(", "-.--.-":")", "U-.--.":"[", "U-.--.-":"]", "U-.--.":"{", "U-.--.-":"}"
alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"

#Functions
def CheckInput():
	exists = os.path.isdir(args.input)
	if exists == False:
		print("The specified input folder does not exist")
		exit()
	else:
		return

def CheckOutput():
	exists = os.path.isdir(args.output)
	if exists == False:
		os.mkdir(args.output)
	else:
		return

def GetCypher():
	opendir = str(args.input) + "/" + str(inputlist[file])
	f = open(opendir)
	cypher = f.read()
	return cypher

def StripNewLines():
	morsecypher = ""
	morsecypher = cypher.strip()
	return morsecypher

def DecryptMorse():
	decryption = ""
	plaintext = ""
	morseletter = ""
	for x in range(11, len(cypher)):
		if cypher[x] != " ":
			morseletter += cypher[x]	
		elif cypher[x] == " " and morseletter != "":
			plaintext += morseCodeDict[morseletter]
			morseletter = ""
	return plaintext

# def DecryptCaesar():
# 	decryption = ""
# 	plaintext = ""
# 	cypherposition = 18
# 	while (cypherposition < len(cypher)):
# 		cyphertextchar = cypher[cypherposition]
# 		ASCIIValue = ord(cyphertextchar)
# 		if ASCIIValue == 32:
# 			plaintext += chr(ASCIIValue)
# 		elif ASCIIValue != 32:
# 			ASCIIValue -= 3
# 			plaintext += chr(ASCIIValue)
# 		cypherposition += 1
# 		pass
# 	return plaintext

def DecryptCaesar():
	cypherPosition = 17
	plaintext = ""
	while cypherPosition < (len(cypher) - 1):
		cypherPosition += 1
		Position = 0
		if cypher[cypherPosition].isalpha():
			while cypher[cypherPosition] != alphabet[Position]:
				Position += 1
				pass
			Position -= 3
			plaintext += alphabet[Position]
			Position = 0
			pass
		elif cypher[cypherPosition].isnumeric():
			while cypher[cypherPosition] != numbers[Position]:
				Position += 1
				pass
			Position -= 3
			plaintext += numbers[Position]
			Position = 0
			pass
		else:
			plaintext += " "
	return plaintext

def StripHex():
	hexcypher = ""
	for x in range(4, len(cypher)):
		hexcypher += cypher[x]
	pattern = re.compile(r"\s+")
	hexcypher = re.sub(pattern, "", hexcypher)
	return hexcypher

def DecrpytHexadecimal():
	plaintext = bytes.fromhex(cypher)
	plaintext = plaintext.decode("ascii")
	return plaintext.lower()

def Output():
	opendir = str(args.output) + "/" + str(inputlist[file].rstrip(".txt") + "_y62498rh.txt")
	g = open(opendir, "w")
	g.write(decryption)

#Main
CheckInput()
CheckOutput()
inputlist = os.listdir(args.input)
for file in range (0, len(inputlist)):
	cypher = GetCypher()
	cypher = StripNewLines()
	if cypher[0] == "M":
		cypher += " "
		decryption = DecryptMorse()
	elif cypher[0] == "C":
		decryption = DecryptCaesar()
	elif cypher[0] == "H":
		cypher = StripHex()
		decryption = DecrpytHexadecimal()
	Output()