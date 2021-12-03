import argparse, re, os

def defArguments():
	global args
	ap = argparse.ArgumentParser()
	ap.add_argument("inputFolder", help="input folder")
	ap.add_argument("outputFolder", help="out folder")
	args = ap.parse_args()
def GenerateFileList():
	fileList=[]
	for file in os.listdir(args.inputFolder):
	    if file.endswith(".txt"): 
	         fileList.append(os.path.join(args.inputFolder, file))
	return fileList
def accessFile(f):
	inFile  = open(f)
	txt = inFile.read().strip()
	inFile.close()
	return txt
def generateOutput(f):
	f = accessFile(f).lower()
	if re.search("hex", f):
		decryption = decryptHex(f)
	elif re.search("caesar", f):
		decryption = decryptCaesar(f)
	elif re.search("morse", f):
		decryption = decryptMorse(f)
	return decryption.lower()
def decryptHex(cipher):
	cipher = re.sub("^.*[:,=]", "", cipher)
	charList= re.split("\s", cipher)
	for i in range(len(charList)):
		hexi= int(charList[i], base=16)		#coverts from hex string to dec int
		charList[i] = chr(hexi)
	solution = ""
	for c in charList:
		solution += c
	return solution
def decryptCaesar(cipher):
	cipher = re.sub("^.*[:,=]", "", cipher)
	solution=""
	for char in cipher:
		ASCIIValue = ord(char)
		if ASCIIValue !=32:     #space
			ASCIIValue -= 3
		solution += chr(ASCIIValue)
	return solution
def decryptMorse(cipher):
	cipher = re.sub("^.*[:,=]", "", cipher)
	charList = cipher.split()
	solution=""
	for char in charList:
		solution += convertMorseChar(char)
	return solution
def convertMorseChar(seq):
    morseDict = {'.-' : 'a',
    '-...' : 'b',
    '-.-.' : 'c',
    '-..': 'd',
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
    '-----':'0',
    '.----':'1',
    '..---':'2',
    '...--':'3',
    '....-':'4',
    '.....':'5',
    '-....':'6',
    '--...':'7',
    '---..':'8',
    '----.':'9',
    '.-.-.-' : '.',
    '--..--' : ',',
    '-.-.--':'!',
    '..--..' : '?',
    "---...":":",
    "-.-.-":';',
    "-....-":"-",
    "-.--.":"(",
    "-.--.-":")",
    ".----.":"'",
    '.-..-.':'"',
    '/' : ' ',
    ".......": " "
    }
    return morseDict[seq]
def writeOutput():
	if not os.path.exists(args.outputFolder):
		os.makedirs(args.outputFolder)
	for f in GenerateFileList():
		filename=re.sub((".+/"), "", f)
		filename=re.sub((".txt"), "_j14088na.txt", filename)
		outFile = open(os.path.join(args.outputFolder, filename), "w")
		outFile.write(generateOutput(f))
		outFile.close()


defArguments()
writeOutput()