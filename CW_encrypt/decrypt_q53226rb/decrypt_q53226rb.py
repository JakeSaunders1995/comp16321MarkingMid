import argparse
import os

parser = argparse.ArgumentParser(description = 'Score calculator')
parser.add_argument('input', help = 'Enter input path')
parser.add_argument('output', help = 'Enter output path')
args = parser.parse_args()

input1 = args.input
output = args.output

count = 0
directory = input1
for filename in os.scandir(directory):
	count += 1
	if filename.is_file():
		file = open(filename)
		cipherText2 = file.read()
		result = cipherText2.split(":")

	def morse():
		
		morse_code = {'.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '/': ' ','.-.-.-':'.','--..--':',','..--..':'?','-.-.-.':';','---...':':','-....-':'—','-..-.':'/','.----.':"''",'.-..-.':'""','-.--.':'(','-.--.-':')','-.-.--':'!'}
		inp = result[1].split()
		d = os.path.basename(filename)
		x = os.path.splitext(d)[0]
		name = os.path.join(output,str(x)+"_q53226rb.txt")
		file2 = open(name,"a")
		file2.write("encryption is fun!\n")
		for i in range(0, len(inp)):
			translate = morse_code.get(inp[i])
			file2.write(translate.lower())
		file2.close
	

	def hex():
		translate = bytes.fromhex(result[1]).decode()
		d = os.path.basename(filename)
		x = os.path.splitext(d)[0]
		name = os.path.join(output,str(x)+"_q53226rb.txt")
		file2 = open(name,"a")
		file2.write("encryption is fun!")
		file2.write("\n"+translate.lower())
		file2.close


	def caesar():

		plainText2 = " "
		alphabet1 = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
		alphabet = alphabet1.lower()

		textPosition2 = 0
		while textPosition2 < len(result[1]):
		    textChar2 = result[1][textPosition2]
		    alphabetPosition2 = 3
		    try:
		    	while textChar2 != alphabet[alphabetPosition2]:
		        	alphabetPosition2 = alphabetPosition2 + 1
		    	alphabetPosition2 = alphabetPosition2 - 3
		    	plainText2 = plainText2 + alphabet[alphabetPosition2]
		    except:
		        plainText2 = plainText2 + " "
		    textPosition2 = textPosition2 + 1
		d = os.path.basename(filename)
		x = os.path.splitext(d)[0]
		name = os.path.join(output,str(x)+"_q53226rb.txt")
		file2 = open(name,"a")
		file2.write("encryption is fun!")
		file2.write("\n"+plainText2.lower())
		file2.close


	if "ex" in result[0]:
		hex()
	elif "ae" in result[0]:
		caesar()
	else:
		morse()
	