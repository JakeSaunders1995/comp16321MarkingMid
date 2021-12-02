def remove_type(text):
    i = 0
    for char in text:
        if char != ":":
            i += 1
        if char == ":":
            i += 1
            break
    text = text[i:]
    return(text)

def caesar_decrypt(text):
    decrypt = ""
    text_position = 0
    while text_position < len(text):
        text_char = text[text_position]
        if text_char == " ":
        	decrypt += " "
        else:
	        ascii_val = ord(text_char)
	        ascii_val -= 3
	        decrypt += chr(ascii_val)
        text_position += 1
    return(decrypt)

def hex_decrypt(text):
    decrypt = bytes.fromhex(text)
    decrypt = decrypt.decode("ascii")
    return(decrypt)

def morse_decrypt(text):
    morse_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', 'Error':	'........','&'	:'.-...',
					"'" 	:'.----.','@' :'.--.-.',')' :	'-.--.-',
					'(' :	'-.--.',':' :	'---...',',' :	'--..--',
					'=' :'-...-','!'  :	'-.-.--','.' :	'.-.-.-',
					'-'  :'-....-','+' :	'.-.-.','"' :	'.-..-.',
					'?'	:'..--..','/' :'-..-.', ';' : '-.-.-.'}

    text += ' '

    decipher = ''
    cipher = ''
    for letter in text:
        if letter == '/':
            decipher += ' '
            continue

        if (letter != ' '):
            i = 0
            cipher += letter
        else:
            i += 1
            if i == 2 :
                decipher += ''
            else:
                decipher += list(morse_dict.keys())[list(morse_dict.values()).index(citext)]
                cipher = ''
    return decipher

import sys
import os

in_dir = sys.argv[1]
out_dir = sys.argv[2]

files = os.listdir(in_dir)

for file in files:
    address = in_dir + "/" + file
    encrypted_file = open(address, "r")
    for text in encrypted_file:
    	text = text.rstrip()
    encrypted_file.close()

    if text[0] == "C":
    	text = remove_type(text)
    	text = caesar_decrypt(text)
    elif text[0] == "H":
    	text = remove_type(text)
    	text = hex_decrypt(text)
    elif text[0] == "M":
    	text = remove_type(text)
    	text = morse_decrypt(text)
    else:
    	text = "unable to decrypt"
    text = text.lower()

    name_len = len(file) - 4
    output_add = out_dir + "/" + file[:name_len] + "_g45512id.txt"
    decrypt_file = open(output_add, "w")
    decrypt_file.write(text)
    decrypt_file.close()