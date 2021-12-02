import argparse
import os

#Entire bulk of code here to decrypt. Made it into the function since it needed to get called multiple times due to the file path input ambiguity.
def Decrypt(code):
	#Opens the file to work with the string inside and sets up some variables for the decrypted text and to make the while loop possible.
	encrypted = open(code, "r").read()
	output = ''
	i = 0

	#Assuming the string starts with the same words the input test files started with, this will work. If not then it's on the course not me.
	if encrypted.startswith('M') or encrypted.startswith('m'):
		#Gets rid of the encryption classification. Will only work if it's done similar to the test input files.
		encryptedmorse = encrypted[11:]
		#Sets up the list of words. I could have used .split(), but I prefered this way because I understand what I've done here.
		morseList = ['']
		morseListIndex = 0
		#Checks every character, adding a code character to the correct element in the list of morse words, using spaces to define new elements aka new letters.
		while i < len(encryptedmorse):
			if encryptedmorse[i] == '.' or encryptedmorse[i] == '-' or encryptedmorse[i] == '/':
				morseList[morseListIndex] += encryptedmorse[i]
				i += 1
				continue
			elif encryptedmorse[i] == ' ':
				morseList.append('')
				morseListIndex += 1
				i += 1
				continue
			#This is for the very real possibility that the tests given won't be the same as promised, and hence will throw a error message and just end the decryption more or less.
			else: print('Morse code is not valid'); break

		#This converts each element in the list to a letter or space, using a dictionary I made by hand below in the code. Letters and numbers should all work.
		for letter in morseList: output += morseCodeDic[letter]

	elif encrypted.startswith('C') or encrypted.startswith('c'):
		#Same as previous.
		encryptedcaesar = encrypted[18:]
		#Loops through every character, checks for spaces to skip and then checks for a,b, and c so that the shift goes back to x,y and z. Other than that, just a simple ASCII shift of 3. They're all put into lowercase as well.
		while i < len(encryptedcaesar):
			if encryptedcaesar[i] == ' ':
				output += ' '
				i += 1
				continue
			elif encryptedcaesar[i] == '\n':
				output += '\n'
				i += 1
				continue
			elif encryptedcaesar[i] == 'a' or encryptedcaesar[i] == 'b' or encryptedcaesar[i] == 'c':
				output += chr(ord(encryptedcaesar[i])+23).lower()
				i += 1
				continue
			output += chr(ord(encryptedcaesar[i])-3).lower()
			i += 1

	elif encrypted.startswith('H') or encrypted.startswith('h'):
		#Same as previous.
		encryptedhex = encrypted[4:]
		#Loops through the string 3 characters at a time, taking the first two and turning them to a byte array using built in functions, and then decoding them and setting them all to lowercase.
		while i < len(encrypted):
			output += bytearray.fromhex(encryptedhex[i:i+2]).decode().lower()
			i += 3

	else:
		#For if the file is not set up correctly. Fairly difficult to achieve.
		print('Invalid text in the file')

	#Opens an output file in the given file path and names it accordingly, followed by writing the output into the file.
	open(args.Output_Path + '\\' + os.path.splitext(os.path.basename(code))[0] + "_e55646sa.txt", 'w').write(output)

#A morse code dictionary I made
morseCodeDic = {
	'.-': 'a',
	'-...': 'b',
	'-.-.': 'c',
	'-..': 'd',
	'.': 'e',
	'..-.': 'f',
	'--.': 'g',
	'....': 'h',
	'..': 'i',
	'.---': 'j',
	'-.-': 'k',
	'.-..': 'l',
	'--': 'm',
	'-.': 'n',
	'---': 'o',
	'.--.': 'p',
	'--.-': 'q',
	'.-.': 'r',
	'...': 's',
	'-': 't',
	'..-': 'u',
	'...-': 'v',
	'.--': 'w',
	'-..-': 'x',
	'-.--': 'y',
	'--..': 'z',
	'.----': '1',
	'..---': '2',
	'...--': '3',
	'....-': '4',
	'.....': '5',
	'-....': '6',
	'--...': '7',
	'---..': '8',
	'----.': '9',
	'-----': '0'
	'/': ' '
}

my_parser = argparse.ArgumentParser(description='Spell Checker')

my_parser.add_argument(
	'Input_Path',
    metavar='path',
    type=str,
    help='the path to the input file')

my_parser.add_argument(
	'Output_Path',
    metavar='path',
    type=str,
    help='the path to output directory')

args = my_parser.parse_args()

inputFolder = args.Input_Path

#Checks whether the input file path is a folder, then it would iterate through that folder and calculate for all text files in the folder.
if os.path.isdir(inputFolder):
	for file in os.scandir(inputFolder):
	    if file.path.endswith(".txt") and file.is_file():
	        Decrypt(file.path)
else: print("Please input a text file or an existing folder/directory")