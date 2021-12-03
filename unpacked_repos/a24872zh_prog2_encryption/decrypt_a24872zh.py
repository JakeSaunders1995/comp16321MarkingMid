import argparse, os

def which_cipher(input_file):
	newfile = open(input_file, "r")
	line = newfile.readline()
	letter = line[0]
	split = line.split(":")
	cipher_text = split[1]
	newfile.close()
	if letter == "H":
		return solve_hex(cipher_text)
	elif letter == "C":
		return solve_caesar(cipher_text)
	elif letter == "M":
		return solve_morse(cipher_text)

def solve_hex(cipher_text):
	bytes_object = bytes.fromhex(cipher_text)
	ascii_string = bytes_object. decode("ASCII")
	return ascii_string.lower()

def solve_caesar(cipher_text):
	plain_text = ""
	alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
	plaintextPosition = 0
	while plaintextPosition < len(cipher_text):
		cyphertextChar = cipher_text[plaintextPosition]
		if cyphertextChar != " ":
			alphabetPosition = 3
			while cyphertextChar != alphabet[alphabetPosition]:
				alphabetPosition += 1
			alphabetPosition -= 3
			plain_text = plain_text + alphabet[alphabetPosition]
		else:
			plain_text = plain_text + " "
		plaintextPosition += 1
	return plain_text

def solve_morse(cipher_text):
	plain_text = ""
	list_of_words = cipher_text.split("/")
	for word in list_of_words:
		list_of_letters = word.split(" ")
		for letter in list_of_letters:
			plain_text += translateMorse(letter)
		plain_text += " "
	return plain_text

def translateMorse(letter):
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	morseAlphabet = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-.', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
	for i in range(len(morseAlphabet)):
		if letter == morseAlphabet[i]:
			return alphabet[i]
	return ""

def output_results(plain_text, output_path, input_name):
	nameOfOutput = input_name[:-4]
	nameOfOutput += "_a24872zh.txt"
	output_to = open(output_path + "/" + nameOfOutput, "w")
	output_to.write(plain_text)
	output_to.close()

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()

input_path = args.input_file
output_path = args.output_file
listOfTextFiles = os.listdir(input_path)
listToOutput = []

for item in listOfTextFiles:
	listToOutput.append(which_cipher(input_path + "/" + item))

for i in range(len(listToOutput)):
	output_results(listToOutput[i], output_path, listOfTextFiles[i])



