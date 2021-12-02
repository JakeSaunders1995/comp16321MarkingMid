import argparse
import os 

def MorseCode(text):
	morse_dict = { 'A':'.-', 'B':'-...',
                   'C':'-.-.', 'D':'-..', 'E':'.',
                   'F':'..-.', 'G':'--.', 'H':'....',
                   'I':'..', 'J':'.---', 'K':'-.-',
                   'L':'.-..', 'M':'--', 'N':'-.',
                   'O':'---', 'P':'.--.', 'Q':'--.-',
                   'R':'.-.', 'S':'...', 'T':'-',
                   'U':'..-', 'V':'...-', 'W':'.--',
                   'X':'-..-', 'Y':'-.--', 'Z':'--..',
                   '1':'.----', '2':'..---', '3':'...--',
                   '4':'....-', '5':'.....', '6':'-....',
                   '7':'--...', '8':'---..', '9':'----.',
                   '0':'-----', ', ':'--..--', '.':'.-.-.-',
                   '?':'..--..', '!':'-.-.--', ':':'---...', 
                   ';':'-.-.-.','/':'-..-.', '-':'-....-',
                   '-':'-....-','—':'','{':'','}':'',
                   '[':'-.--.',']':'-.--.-',"'":'.----.',
                   '"':'.-..-.','...':'.-.-.-.-.-.-.-.-.-',
      			   '(':'-.--.', ')':'-.--.-', ' ':'/'}
# dash, curly brackets and ellipsis not done

	text += " "
	plaintext = ""
	ciphertext = ""
	for char in text:
		if char == "\n":
			char = ""
		if char != " ":
			i = 0
			ciphertext += char
		else:
			i += 1
			if i == 2:
				plaintext += " "
			else:
				plaintext += list(morse_dict.keys())[list(morse_dict.values()).index(ciphertext)]
				ciphertext = ""
		


	decipher = plaintext.lower()
	return(plaintext.lower())


def CaesarCode(text):
	ciphertextpos = 0
	plaintext = ""

	while (ciphertextpos < len(text)):
		ciphertextchar = text[ciphertextpos]
		if ciphertextchar == " ":
			plaintext = plaintext + " "
		else:
			charascii = ord(ciphertextchar)
			if (charascii >= ord("d")) and (charascii <= ord("z")):
				charascii -= 3
				plaintext += chr(charascii)
			elif charascii == ord("a"):
				plaintext += "x"
			elif charascii == ord("b"):
				plaintext += "y"
			elif charascii == ord("c"):
				plaintext += "z"

		ciphertextpos += 1

	decipher = plaintext.lower()
	return(plaintext.lower())



def HexCode(text):
	plaintext = bytes.fromhex(text).decode('utf-8')
	decipher = plaintext.lower()
	return(plaintext.lower())
	
#main program starts here

parser = argparse.ArgumentParser()

parser.add_argument("inputfolderpath")
parser.add_argument("outputfolderpath")

args = parser.parse_args()

#creating list to store input file paths
inputfilelist = []
for filename in os.scandir(args.inputfolderpath):
	if filename.path.endswith(".txt") and filename.is_file():
		inputfilelist.append(filename.path)

for files in inputfilelist:
	inputfile = open(files)

	line = inputfile.read()

	for char in line:
		if char == ":":
			algo = line[0:line.find(":")]
			cipher = line[line.find(":")+1:]

	if algo == "Morse Code":
		decipher = MorseCode(cipher)

	if algo == "Caesar Cipher(+3)":
		decipher = CaesarCode(cipher)

	if algo == "Hex":
		decipher = HexCode(cipher)

	#creating complete output file path 
	inputfilename = os.path.basename(files)
	outputfilename = inputfilename[0:(len(inputfilename)-4)] + '_u24264cw'
	completefilepath = os.path.join(args.outputfolderpath, outputfilename + ".txt")

	outputfile = open(completefilepath,'w')

	outputfile.write(decipher)

	outputfile.close()
inputfile.close()