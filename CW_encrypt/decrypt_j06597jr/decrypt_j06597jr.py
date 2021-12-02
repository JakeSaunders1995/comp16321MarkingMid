import re, os, argparse

def readfile(path):
	with open(path, "r", encoding="utf-8-sig") as f:
		cypher = f.read()
		cypher = cypher.strip()
		f.close()
	return cypher

def writefile(path):
	with open(path, "w", encoding="utf-8-sig") as f:
		result = f.write(decrypt)
		f.close()
	return result

parser = argparse.ArgumentParser(description="input and output files for encryption")
parser.add_argument("input", type=str, help="input file")
parser.add_argument("output", type=str, help="output file")
args = parser.parse_args()


inputFolder = args.input
outputFolder = args.output
inputFiles = os.listdir(inputFolder)
inputPath = os.listdir(inputFolder)
os.chdir(inputFolder)

for y in range(0,len(inputFiles)):
	inputFiles[y] = inputFiles[y][:-4]

alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
morseCode_Morse = ['.-', '-...','-.-.', '-..', '.','..-.', '--.', '....','..', '.---', '-.-','.-..', '--', '-.','---', '.--.', 
					'--.-','.-.', '...', '-','..-', '...-', '.--','-..-', '-.--', '--..','.----', '..---', '...--','....-', '.....', 
					'-....','--...', '---..', '----.','-----']
morseCode_Alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"

count = 0

for z in range(0,len(inputPath)):
	os.chdir(inputFolder)
	inputPath[z] = inputFolder+"/"+inputPath[z]
	cypher = readfile(inputPath[z])

	decrypt = ""

	algHex = re.search("Hex", cypher)
	if algHex:
		a = cypher.split(":", 2)
		b = str(a[1])
		b = b.split(" ")
		for x in b:
			asc = int(x, 16)
			decrypt += chr(asc)


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



	algMorse = re.search("Morse", cypher)
	if algMorse:
		a = cypher.split(":", 2)
		b = str(a[1])
		b = b.split(" ")
		for x in b:
			for i in range (0,36):
				if x == morseCode_Morse[i]:
					decrypt += morseCode_Alphabet[i]
			if x == "/":
				decrypt += " "

	os.chdir(outputFolder)
	outputPath = outputFolder +"/" + inputFiles[count]+"_j06597jr.txt"
	count += 1
	result = writefile(outputPath)