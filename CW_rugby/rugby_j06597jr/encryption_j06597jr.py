import re
import argparse

def readfile(path):
	with open(path, "r", encoding="utf-8-sig") as f:
		cypher = f.read()
		cypher = cypher.strip()
		f.close()
	return cypher

parser = argparse.ArgumentParser(description="input and output files for encryption")
parser.add_argument("input", type=str, help="input file")
parser.add_argument("output", type=str, help="output file")
args = parser.parse_args()
cypher = readfile(args.input)

decrypt = ""
alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
morseCode_Morse = ['.-', '-...','-.-.', '-..', '.','..-.', '--.', '....','..', '.---', '-.-','.-..', '--', '-.','---', '.--.', 
					'--.-','.-.', '...', '-','..-', '...-', '.--','-..-', '-.--', '--..','.----', '..---', '...--','....-', '.....', 
					'-....','--...', '---..', '----.','-----', '--..--', '.-.-.-','..--..', '-..-.', '-....-','-.--.', '-.--.-']
morseCode_Alphabet = "abcdefghijklmnopqrstuvwxyz1234567890,.?/:()"

algHex = re.search(r"Hex", cypher)
if algHex:
	a = cypher.split(":", 2)
	b = str(a[1])
	b = b.split(" ")
	for x in b:
		asc = int(x, 16)
		decrypt += chr(asc)
	print(decrypt)


algCaesar = re.search("Caesar", cypher)
if algCaesar:
	a = cypher.split(":", 2)
	b = str(a[1])
	b = b.split(" ")
	for x in b:
		for i in x:
			n = 0
			cypherChar = i[n]
			alphabetPosition = 3
			while cypherChar != alphabet[alphabetPosition] :
				alphabetPosition += 1
			alphabetPosition -= 3
			decrypt += alphabet[alphabetPosition]
			n += 1
		decrypt += " "
	print(decrypt)



algMorse = re.search("Morse", cypher)
if algMorse:
	a = cypher.split(":", 2)
	b = str(a[1])
	b = b.split(" ")
	for x in b:
		for i in range (0,42):
			if x == morseCode_Morse[i]:
				decrypt += morseCode_Alphabet[i]
		if x == "/":
			decrypt += " "

def writefile(path):
	with open(path, "w", encoding="utf-8-sig") as f:
		result = f.write(decrypt)
		f.close()
	return result

result = writefile(args.output)



