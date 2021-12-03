import argparse
import re
import os

mappings = {".-": "a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j", "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o", ".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y", "--..":"z", ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9", "-----":"0"}
# , ".-.-.-":".", "--..--":",", "..--..":"?", "---...":":", "-..-.":"/", "-....-":"-", "-...-":"=", ".----.":"'", "-.--.-":")", "-.--.":"(", "..--.-":"_", "-.-.--":"!", ".-...":"&", ".-..-.":"\"", "-.-.-.":";", "...-..-":"$"}

def decrypt(filepath):
	global mappings
	global outputFilePath

	inputFile = open(filepath)
	contents = inputFile.readline()

	encTypeSearch = re.search(r'(.+):(.*)', contents)
	encType = encTypeSearch.group(1)
	encryptedMessage = encTypeSearch.group(2)
	# print(encType)

	decryptedText = ""
	# print(encryptedMessage)

	if "Hex" in encType or "hex" in encType:
		hexElements = encryptedMessage.split()
		for hexNum in hexElements:
			decryptedText += (bytearray.fromhex(hexNum).decode()).lower()

	elif "morse" in encType or "Morse" in encType:
		morseArr = encryptedMessage.split()
		for code in morseArr:
			if code == "/":
				decryptedText += " "
			else:
				decryptedText += mappings[code]

	elif "caesar" in encType or "Caesar" in encType:
		for char in encryptedMessage:
			if char == " ":
				decryptedText += " "
			else:
				if ord(char) in [65, 66, 67, 97, 98, 99]:
					decryptedText += chr(ord(char) + 23).lower()
				else:
					decryptedText += chr(ord(char) - 3).lower()

	inputFile.close()


	outputFile = open(os.path.join(outputFilePath, os.path.basename(filepath[0:-4] + "_x62967rr.txt")), "w")
	outputFile.write(decryptedText)
	outputFile.close()


parser = argparse.ArgumentParser()
parser.add_argument("inputFilePath")
parser.add_argument("outputFilePath")
args = vars(parser.parse_args())

outputFilePath = args["outputFilePath"]

for parent, dirnames, filenames in os.walk(args["inputFilePath"]):
    for fn in filenames:
        filepath = os.path.join(parent, fn)
        # print(filepath)
        if (os.path.join(args["inputFilePath"], os.path.basename(filepath)) == filepath) and os.path.basename(filepath)[-4:] == ".txt":
        	decrypt(filepath)

