import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument("pathIn")
parser.add_argument("pathOut")
inputPaths = parser.parse_args()
filelist = os.listdir(inputPaths.pathIn)

for x in range(len(filelist)):
	filename = os.path.join(inputPaths.pathIn, filelist[x])
	file = open(filename, "r")
	text = str(file.readline())
	text = text.split(":")
	plaintext = ""
	#print(ciphertext)
	if text[0] == "Hex":
		ciphertext = text[1].split()
		for i in range(len(ciphertext)):
			temp = ciphertext[i]
			temp = chr(int(temp, 16))
			plaintext += temp
	elif text[0] == "Morse Code":
		morse = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", 
		"f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..",
		"m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.",
		"s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-",
		"y":"-.--", "z":"--..", "1":".----", "2":"..---", "3":"...--",
		"4":"....-", "5":".....", "6":"-....", "7":"--...",
		"8":"---..", "9":"----.", "0":"-----", ".":".-.-.-", ",":"--..--", 
		"?":"..--..", "!":"-.-.--", ":":"---...", '"':".-..-.", 
		"'":".----.", "=":"-...-", "/":"-..-.", "(":"-.--.", ")":"-.--.-",
		"&":".-...", "+":".-.-.", "-":"-....-", "@":".--.-."}
		ciphertext = text[1].split("/")
		for i in range(len(ciphertext)):
			characters = ciphertext[i].split()
			for j in range(len(characters)):
				temp = characters[j]
				for k in range(len(morse)):
					if list(morse.values())[k] == temp:
						plaintext += list(morse.keys())[k]
			plaintext += " "
	else:
		ciphertext = text[1].split()
		for i in range(len(ciphertext)):
			word = ciphertext[i]
			for j in range(len(word)):
				temp = word[j]
				temp = ord(temp) - 3
				temp = chr(temp)
				plaintext += temp
			plaintext += " "
	file.close()
	outputFname = os.path.join(inputPaths.pathOut, filelist[x][0:-4]+"_r46739lt.txt")
	outputFile = open(outputFname,"w")
	outputFile.write(plaintext)
	outputFile.close()
