import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()
inputFile = args.input
outputFile = args.output
file = open(inputFile, "r")
for line in file:
    cipher = line
for x in range(len(cipher)):
	if cipher[x] == ":":
		mode = cipher[0:x]
		break
code = cipher[len(mode)+1:]
message = ""
if mode == "Hex":
	code = code.replace(" ", "")
	for x in range(0,len(code),8):
		temp = bytes.fromhex(code[x:x+8])
		message += temp.decode("ASCII")
elif mode == "Caesar Cipher(+3)":
	for x in range(len(code)):
		if code[x] == " ":
			message += " "
			continue
		tempNum = ord(code[x])
		if tempNum - 3 < 0:
			tempNum += 26
		tempStr = chr(tempNum - 3)
		message += tempStr
	
elif mode == "Morse Code":
	morseCode = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....','i':'..', 'j':'.---', 'k':'-.-','l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}
	temp = ""
	for x in range(len(code)):
		if code[x] == "/":
			message += " "
			continue
		if code[x] == " ":
			if temp == "":
				continue
			message += list(morseCode.keys())[list(morseCode.values()).index(temp)]
			temp = ""
		else:
			temp += code[x]
	message += list(morseCode.keys())[list(morseCode.values()).index(temp)]
file = open(outputFile, "w")
file.write(message)