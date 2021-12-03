import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("inPath", type=str)
parser.add_argument("outPath", type=str)
args = parser.parse_args()

morseDict = {
    '.-' : 'a',
    '-...' : 'b', 
    '-.-.' : 'c', 
    '-..' : 'd', 
    '.' : 'e', 
    '..-.' : 'f', 
    '--.' : 'g', 
    '....' : 'h', 
    '..' : 'i', 
    '.---' : 'j', 
    '-.-' : 'k', 
    '.-..' : 'l', 
    '--' : 'm', 
    '-.' : 'n', 
    '---' : 'o', 
    '.--.' : 'p', 
    '--.-' : 'q', 
    '.-.' : 'r', 
    '...' : 's', 
    '-' : 't', 
    '..-' : 'u', 
    '...-' : 'v', 
    '.--' : 'w', 
    '-..-' : 'x', 
    '-.--' : 'y', 
    '--..' : 'z', 
}

def hexDecrypt(text):
	characters = text.split()
	endWord = ""
	for i in characters:
		endWord += bytes.fromhex(i).decode("ASCII")
	endWord = endWord.lower()
	return endWord

def caesarDecrypt(text):
	words = text.split()
	endText = ""
	for i in words:
		newWord = ""
		for j in range(len(i)):
			letter = i[j]
			asciiNum = ord(letter)
			if(asciiNum < 100):
				asciiNum += 26
			newWord += chr(asciiNum-3)
		endText += (newWord + " ")
	endText = endText[:-1]
	return endText

def morseDecrypt(text):
	words = text.split("/")
	endText = ""
	for i in words:
		newWord = ""
		characters = i.split()
		for j in characters:
			newWord += morseDict[j]
		endText += (newWord + " ")
	endText = endText[:-1]
	return endText

#Main Function
def decrypt(inText):
	textSplit = inText.split(":")
	encodeType = textSplit[0]
	if(encodeType[0] == "H"):
		return hexDecrypt(textSplit[1])
	elif(encodeType[0] == "C"):
		return caesarDecrypt(textSplit[1])
	elif(encodeType[0] == "M"):
		return morseDecrypt(textSplit[1])

def main():
    files =	os.listdir(args.inPath)
    for i in files:
    	file1 = open(args.inPath + i, "r")
    	inText = file1.read()
    	file1.close()

    	outText = decrypt(inText)
    	fileName = i.split(".")[0] + "_z83313gg.txt"
    	file2 = open(args.outPath + fileName, "w")
    	file2.write(outText)
    	file2.close()

main()