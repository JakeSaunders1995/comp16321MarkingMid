import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()

def decrypt_Hex():
	# s = x[position + 1:len(x)].replace(" ", "")
	# bytes_object = bytes.fromhex(s)
	# original = bytes_object.decode("ASCII")
	s = x[position + 1:len(x)]
	original = ""
	upper_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	upper_to_lower = {
	'A':'a', 'B':'b', 'C':'c', 'D':'d' ,'E':'e', 'F':'f', 'G':'g', 'H':'h', 'I':'i', 'J':'j', 'K':'k', 'L':'l', 'M':'m', 'N':'n', 'O':'o', 'P':'p', 'Q':'q', 'R':'r', 'S':'s', 'T':'t', 'U':'u', 'V':'v', 'W':'w', 'X':'x', 'Y':'y', 'Z':'z'
	}
	for i in range(0, len(s), 3):
		Hex = s[i] + s[i + 1]
		Decimal = int(Hex, 16)
		if chr(Decimal) in upper_list:
			original += upper_to_lower[chr(Decimal)]
		else:
			original += chr(Decimal)
	return original

def decrypt_Caesar():
	s = x[position + 1:len(x)]
	original = ""
	alphabet = "xyzabcdefghijklmnopqrstuvwxyz"
	for i in range(len(s)):
		if s[i] == " " or s[i] == "\n":
			original += s[i]
		else:
			location = 3
			while s[i] != alphabet[location]:
				location += 1
			location = location - 3
			original += alphabet[location]
	return original

def decrypt_Morse():
	s = x[position + 1:len(x)] + " "
	# Add one space to the bottem to trigger 'if'
	original = ""
	morseDict = {
	'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-.':'f', 
	'--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k', '.-..':'l', 
	'--':'m', '-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r', 
	'...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x', 
	'-.--':'y', '--..':'z', '.----':'1', '..---':'2', '...--':'3', 
	'....-':'4', '.....':'5', '-....':'6', '--...':'7', '---..':'8', 
	'----.':'9', '-----':'0'
	}
	start = 0
	for i in range(len(s)):
		if s[i] == " " and s[i-1] != "/":
			original += morseDict[s[start:i]]
			start = i + 1
		elif s[i] == "/":
			original += " "
			start = i + 2
	return original

for file in os.listdir(args.input):
	readInput = open(os.path.join(args.input, file))
	x = readInput.read()
	position = 0
	while x[position] != ":":
		position += 1
	result = x[0:position]

	if result == "Hex":
		original = decrypt_Hex()
	elif result == "Caesar Cipher(+3)":
		original = decrypt_Caesar()	
	elif result == "Morse Code":
		original = decrypt_Morse()

	newFileName = str(file[0:len(file)-4]) + "_w21706bc.txt"
	writeOutput = open(os.path.join(args.output, newFileName), "w")
	writeOutput.write(original)