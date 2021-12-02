import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input_path")
parser.add_argument("output_path")

p = parser.parse_args()



def convertFromMorseCode(morseCode):
	output = ""
	start = 0
	end = 0
	first_space = True
	for (index,char) in enumerate(morseCode):
		if char == " ": 
			if first_space == True:
				start = 0
				first_space = False
			else:
				start = end + 1
			end = index
			output += morseCodeTranslate[morseCode[start:end]]
		if index == len(morseCode) - 1:
			output += morseCodeTranslate[morseCode[end+1:len(morseCode)]]	
	
	output = output.lower()
	return output

morseCodeTranslate = {
	".-":"a",
	"-...":"b",
	"-.-.":"c",
	"-..":"d",
	".":"e",
	"..-.":"f",
	"--.":"g",
	"....":"h",
	"..":"i",
	".---":"j",
	"-.-":"k",
	".-..":"l",
	"--":"m",
	"-.":"n",
	"---":"o",
	".--.":"p",
	"--.-":"q",
	".-.":"r",
	"...":"s",
	"-":"t",
	"..-":"u",
	"...-":"v",
	".--":"w",
	"-..-":"x",
	"-.--":"y",
	"--..":"z",
	".-...":"&",
	".----.":"'",
	".--.-.":"@",
	"-.--.-":")",
	"-.--.":"(",
	"---...":":",
	"--..--":",",
	"-...-":"=",
	"-.-.--":"!",
	".-.-.-":".",
	"-....-":"-",
	".-.-.":"+",
	".-..-.":'"',
	"..--..":"?",
	"-..-.":"/",
	"/":" "
}

def splitHex(hex):
	newHex = ""
	for index,hexDigit in enumerate(hex):
		temp = int(hexDigit, 16)
		temp = bin(temp)
		temp = str(temp)[2:]
		missing_zeros = 4 - len(temp)
		temp = ("0"*missing_zeros) + temp
		newHex += temp
	newHex = "0b" + newHex
	newHex = int(newHex,2)
	newHex = chr(newHex)
	return(newHex)

def caesarCrack(word):
	plainText = ""
	for char in word:
		if ord(char) - 3 < 97:
			asciiValue = 122 - (97-(ord(char)-3)) + 1
			plainText += (chr(asciiValue))
			continue
		plainText += chr(ord(char) - 3)

	return plainText

	# return chr(int(str(bin(int(hex[0], 16))[2:] + str(bin(int(hex[1], 16)))),2))

def convertFromHex(hex):
	output = ""
	start = 0
	end = 0
	first_space = True
	for (index,char) in enumerate(hex):
		if char == " ": 
			if first_space == True:
				start = 0
				first_space = False
			else:
				start = end + 1
			end = index
			output += splitHex(hex[start:end])
		if index == len(hex) - 1:
			output += splitHex(hex[-2:])	
		
	return output

def decryptCaesar(cipherText):
	output = ""
	start = 0
	end = 0
	first_space = True
	for (index,char) in enumerate(cipherText):
		# print(char + "1")
		if char == " ": 
			if first_space == True:
				start = 0
				first_space = False
			else:
				start = end + 1
			end = index
			output = output +  caesarCrack(cipherText[start:end]) + " "
		if index == len(cipherText) - 1:
			output += caesarCrack(cipherText[end+1 : len(cipherText)])
			if "\n" in cipherText[end+1 : len(cipherText)]:
				output = output[:len(output)-1]
		
	return output




for index, filename in enumerate(os.listdir(p.input_path)):
	if filename.endswith(".txt"):
		input = open(os.path.join(p.input_path, filename), "r")
		firstLine = input.readline()
		if firstLine[0].lower() == "m":
			decryptedText = convertFromMorseCode(firstLine[11:])
		elif firstLine[0].lower() == "h":
			decryptedText = convertFromHex(firstLine[4:])
		elif firstLine[0].lower() == "c":
			decryptedText = decryptCaesar(firstLine[18:])
		output = open(os.path.join(p.output_path, "test_file{}_r89835eb.txt".format(os.path.join(p.input_path, filename)[-5])), "w")
		output.write(decryptedText.lower())
		input.close()
		output.close()
	else:
		pass

