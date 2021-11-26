import sys
from os import listdir
from os.path import isfile, join
input_folder = sys.argv[1]
 
files = [file for file in listdir(input_folder) if isfile(join(input_folder, file)) and file[0] != '.']
 
 
 
 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
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
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', ' ':'/', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'} 
 
def get_message(text):
    for i in range(len(text)):
        if text[i] == ':':
            return text[i+1:]
 
 
 
def decrypt(message):
    message += ' '
 
    decipher = ''
    citext = ''
    for letter in message:
 
        if (letter != ' '):
            i = 0
            citext += letter 
 
        else:
            i += 1
            if i == 2 :
 
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
 
    return decipher 
 
 
def cipherd(string, shift):
 
  cipher = ''
  for char in string:
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
 
  return cipher
 
 
def answer(text):
    if text[0] == "H":
    	return bytes.fromhex(get_message(text)).decode('utf-8').lower()
    if text[0] == "M":
    	return decrypt(get_message(text)).lower()
    if text[0] == "C":
    	return cipherd(get_message(text[:-1]), -3).lower()
 
 
 
 
for file in files:
    input_file = open(f"{input_folder}/{file}")
    text = input_file.readline()
 
    output_folder = sys.argv[2]
    output_file = open(f"{output_folder}/{file[:-4]}_p99614sy.txt", "w")
    output_file.write(str(answer(text)))
 
    input_file.close()

        output_file.close()


