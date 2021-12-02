import sys
import os


def output_caesar(full_sentance_caesar, path):
	ouput_directory = sys.argv[2]
	if ".txt" in path:
		output_path = path.replace(".txt", "_w13634ps.txt")
	else:
		output_path = path + "_w13634ps.txt"
	full_output_path = os.path.join(ouput_directory, output_path)
	create_file = open(full_output_path, "w")
	create_file.write(full_sentance_caesar)

def output_hex(full_sentance_hex, path):
	ouput_directory = sys.argv[2]
	if ".txt" in path:
		output_path = path.replace(".txt", "_w13634ps.txt")
	else:
		output_path = path + "_w13634ps.txt"
	full_output_path = os.path.join(ouput_directory, output_path)
	create_file = open(full_output_path, "w")
	create_file.write(full_sentance_hex)

def output_morse(full_sentance_morse, path):
	ouput_directory = sys.argv[2]
	if ".txt" in path:
		output_path = path.replace(".txt", "_w13634ps.txt")
	else:
		output_path = path + "_w13634ps.txt"
	full_output_path = os.path.join(ouput_directory, output_path)
	create_file = open(full_output_path, "w")
	create_file.write(full_sentance_morse)





file = sys.argv[1]
#turning the file path into string for join
filelist = str(file)
#for each file in that directory 
for path in sorted(os.listdir(file)):
	##This is basically getting the directory you given and turned to string and adding the directory of the file
	full_path = os.path.join(filelist, path)
	f = open(full_path, "r")
	for file in f:
		for letter in file:
			if letter == ":":
				split = file.split(letter)
				typecipher = str(split[0])
				codecipher = str(split[1])
				print("This cipher is " + typecipher)
				typecipher = typecipher.lower()
				

				if "caesar" in typecipher:
					full_sentance_caesar = ""
					numbers = "0123456789"
					for letter in codecipher:
						if letter in numbers:
							full_sentance_caesar = full_sentance_caesar + str(letter)
						else:
							ASCIIValue = ord(letter)
							for i in range(0,3):
								if ASCIIValue >= 65 and ASCIIValue <= 90:
									ASCIIValue = ASCIIValue - 1
								if ASCIIValue >= 97 and ASCIIValue <= 122:
									ASCIIValue = ASCIIValue - 1
								if ASCIIValue == 64 or ASCIIValue == 96:
									ASCIIValue = ASCIIValue + 26			 
							ASCIILetter = chr(ASCIIValue)
							full_sentance_caesar = full_sentance_caesar + ASCIILetter
						full_sentance_caesar = full_sentance_caesar.lower()
						output_caesar(full_sentance_caesar, path)	

							
						
				if "hex" in typecipher:
					words = codecipher.split(" ")
					full_sentance_hex = ""
					for word in words:
						hex_byte = bytes.fromhex(word)
						word = hex_byte.decode("ASCII")
						full_sentance_hex = full_sentance_hex + word
					full_sentance_hex = full_sentance_hex.lower()
					output_hex(full_sentance_hex, path)

				if "morse" in typecipher:
					words = codecipher.split("/")
					morse = [
					".-",	"-...",	"-.-.",	"-..",	".",	"..-.",
					"--.",	"....",	"..",	".---",	"-.-",	".-..",
					"--",	"-.",	"---",	".--.",	"--.-",	".-.",
					"...",	"-",	"..-",	"...-",	".--",	"-..-",
					"-.--",	"--..",

					"-----",	".----",	"..---",	"...--",	"....-",	".....",
					"-....",	"--...",	"---..",	"----.",

					".-.-.-",	"--..--",	"..--..",	".----.",	"-.-.--",	"-..-.",
					"-.--.",	"-.--.-",	".-...",	"---...",	"-.-.-.",	"-...-",
					".-.-.",	"-....-",	"..--.-",	".-..-.",	"...-..-",	".--.-.",
					"..-.-",	"--...-",]

					character = [
					"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "Z",
					"0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
					".", ",", "?", "'", "!", "/", "(", ")", "&", ":", ";", "=", "+", "-", "_", '"', "$", "@", "¿", "¡"]  

					full_sentance_morse = ""
					for word in words:
						letters = word.split(" ")
						full_word_morse = ""
						for letter in letters:
							index = 0
							for i in morse:
								if i == letter:
									letter = character[index]
									full_word_morse = full_word_morse + letter
								index = index + 1	
						full_sentance_morse = full_sentance_morse + full_word_morse	+ " "
					full_sentance_morse = full_sentance_morse.lower()
					output_morse(full_sentance_morse, path)

