import sys
import os

if (len(sys.argv) != 3):
	print("check the number of arguments\nprogram will exit")
	sys.exit(0)
# morse code dictionary
morseCode = {
	'.-' : 'a',
	'-...' : 'b',
	'-.-.' : 'c',
	'-..' : 'd',
	'.' : 'e',
	'..-.' : 'f',
	'--.' : 'g',
	'....' : 'h',
	'..' : 'i',
	'.---' : 'j',
	'-.-' : 'k',
	'.-..' : 'l',
	'--' : 'm',
	'-.' : 'n',
	'---' : 'o',
	'.--.' : 'p',
	'--.-' : 'q',
	'.-.' : 'r',
	'...' : 's',
	'-' : 't',
	'..-' : 'u',
	'...-' : 'v',
	'.--' : 'w',
	'-..-' : 'x',
	'-.--' : 'y',
	'--..' : 'z',
	
	'.----' : '1',
	'..---' : '2',
	'...--' : '3',
	'....-' : '4',
	'.....' : '5',
	'-....' : '6',
	'--...' : '7',
	'---..' : '8',
	'----.' : '9',
	'-----' : '0',

	'.-.-.-' : '.',
	'..--..' : '?',
	'-.-.--' : '!',
	'--..--' : ',',
	'---...' : ':',
#	'' : '—' #dash
	'-....-' : '‐', #hyphen
#	'' : '['
#	'' : ']'
#	'' : '{'
#	'' : '}'
	'-.--.' : '(',
	'-.--.-' : ')',
	'.----.' : '’',
#	'' : '\''
	'.-..-.' : '\"',
#	'' : '…'
	' ': '',
	'/': ' ',
	'' : ''
}




for file in os.listdir(sys.argv[1]):
	file = sys.argv[1] +"/"+ file
#	print(file)
	counter = file[-5]
	fileIn = open(file)
	line = fileIn.read()

	translated = ""
	if(line[0] == 'M' or line[0] == 'm'):
		line = line[11:]
		char = ""
		for i in line:
			if (i == " "):	# translating a full charachter			
				translated += morseCode[char]
				char = ""
			elif (i == "/"):
				translated += " "
				char = ""
			else:
				char += i
		translated += morseCode[char]
	elif (line[0] == 'c' or line[0] == 'C'):
		line = line[18:]
		for char in line:
			if(char == " "):
				translated += " "
			else:
				asc = ord(char) - 3
				
				if(asc <= 96 and asc >= 94):
					asc += 26
				if(asc == 7): continue
				translated += chr(asc)
			print(translated)
	else:
		line = line[4:]
		translated = bytes.fromhex(line).decode()

	# save output
	fileOutPath = sys.argv[2] + "/test_file" + str(counter) + "_p93899aa.txt"
	# print(fileOutPath)
	fileOut = open(fileOutPath,'w')
	fileOut.write(translated)