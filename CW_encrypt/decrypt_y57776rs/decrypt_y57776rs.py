import sys
import os
import string
argumentlist = sys.argv
inputfolder = str(argumentlist[1])
outputfolder = str(argumentlist[2])
file_name = "_y57776rs.txt"

def decrypter(type, words):
	if type == "Morse Code":
		MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-', '!':'-.-.--', ':':'---...', ';':'-.-.-.', '"':'.-..-.'}
		words += ' '
		newwords = words.replace('/', '')
		decipher = ''
		citext = ''
		for letter in newwords:
			if (letter != ('' or ' ')):
				i = 0
				citext += letter
			else:
				i += 1
				if i == 2 :
					decipher += ' '
				else:
					decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
					citext = ''
		return(decipher.lower())
	elif type == "Hex":
		bytes_object = bytes.fromhex(words)
		ascii_string = bytes_object.decode("ASCII")
		return(ascii_string)
	elif type == "Caesar Cipher(+3)":
		alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"
		decrypted_message = ""
		for c in words:
			if c in alphabet:
				position = alphabet.find(c)
				new_position = (position - 3) % 26
				new_character = alphabet[new_position]
				decrypted_message += new_character
			else:
				decrypted_message += c
		return(decrypted_message)

basepath = inputfolder + "/"
with os.scandir(basepath) as entries:
        for entry in entries:
                if entry.is_file():
                        filename = entry.path
                        name = os.path.basename(filename).split('.')[0]
                        newname = name + file_name
                        completeName = os.path.join(outputfolder, newname)
                        f = open(str(filename), "r")
                        file = str(f.read())
                        encryptiontype = file.rpartition(':')[0]
                        encryptedwords = file.rpartition(':')[2]
                        output = decrypter(encryptiontype, encryptedwords)
                        x = open(completeName, "a")
                        x.write(output)
                        x.close()
                        f.close()
