import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument("input", help = "input folder")
parser.add_argument("output", help = "output folder")
args = parser.parse_args()
files = os.listdir(str(args.input))

myDictionary = {'a':'.-', 'b':'-...','c':'-.-.', 'd':'-..', 'e':'.','f':'..-.', 'g':'--.', 'h':'....','i':'..', 'j':'.---', 'k':'-.-','l':'.-..', 'm':'--', 'n':'-.','o':'---', 'p':'.--.', 'q':'--.-','r':'.-.', 's':'...', 't':'-','u':'..-', 'v':'...-', 'w':'.--','x':'-..-', 'y':'-.--', 'z':'--..', '!': '-.-.--', ':': '---...', ';' : '-.-.-.',"'" : '.----.', '"' : '.-..-.','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.','0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-' }
myDictionary = {v: k for k, v in myDictionary.items()}
caesarDictionary = {'a':'x', 'b':'y','c':'z', 'd':'a', 'e':'b','f':'c', 'g':'d', 'h':'e','i':'f', 'j':'g', 'k':'h','l':'i', 'm':'j', 'n':'k','o':'l', 'p':'m', 'q':'n','r':'o', 's':'p', 't':'q','u':'r', 'v':'s', 'w':'t','x':'u', 'y':'v', 'z':'w'}
def Morse(code):
	code = code[11:]
	code = code.split(" ")
	plaintext = ""  
	for y in code:
		if y in myDictionary:
			plaintext += myDictionary[y]
		elif y == "/":
			plaintext += " "



	with open(outputPath, 'w') as o:
		o.write(str(plaintext))

def Hex(code):
	code = code[4:]
	code = code.split(" ")
	plaintext = ""
	for y in code:
		plaintext += bytearray.fromhex(y).decode()
		
	plaintext = plaintext.lower()
	with open(outputPath, 'w') as o:
		o.write(str(plaintext))	


def Caesar(code):
	code = code[18:]
	code = code.lower()
	plaintext = ""
	for y in code:
		if y in caesarDictionary:
			plaintext += caesarDictionary[y]
		elif y == " ":
			plaintext += " "
		else:
			plaintext += y

	with open(outputPath, 'w') as o:
		o.write(str(plaintext))








for x in files:
	path = str(args.input + "/" + x)
	outputPath = str(args.output + "/" + x[:10] + "_v94579az" + x[10:])
	with open(path, 'r') as f:
		encryptedCode = str(f.readline())
		if "Morse" in encryptedCode:
			Morse(encryptedCode)
		elif "Hex" in encryptedCode:
			Hex(encryptedCode)
		elif "Caesar" in encryptedCode:
			Caesar(encryptedCode)

			

		

		

