import os
import argparse
import string
parser = argparse.ArgumentParser()
parser.add_argument("echo_i")
parser.add_argument("echo_o")
args = parser.parse_args()

i_path = (args.echo_i)
o_path = (args.echo_o)

os.chdir(i_path)

alphabet = string.ascii_lowercase

global outText 

#Morse decryption                    
def mDecrypt(text):
    MORSE_CODE_DICT = { 'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ':'/'}
    text += ' '
    decipher = ''
    ciptext = ''
    for letter in text:
        if (letter != ' '):
            i = 0
            ciptext += letter
        else:
            i += 1
            if i == 2 :
                 decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(ciptext)]
                ciptext = ''
    return decipher

#Hexadecimal decryption
def hDecrypt(hexSubString):
    return chr(int(hexSubString, 16))

#Caesar +3
def cDecrypt(encrypted_message):
    key = +3
    
    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c
    return decrypted_message

#Txt file reader
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        cText = f.read()
        if cText.startswith("Morse Code:"):
            cText = cText.replace("Morse Code:", "")
            return decOutM(cText)
        elif cText.startswith("Hex:"):
            cText = cText.replace("Hex:", "")
            return decOutH(cText) 
        elif cText.startswith("Caesar Cipher(+3):"):
            cText = cText.replace("Caesar Cipher(+3):", "")
            return decOutC(cText)        

#Decription Function Caller
def decOutH(cText):
    outText = ""
    hexString = cText
    hexArray = hexString.split(" ")
    for letter in hexArray:
        outText += hDecrypt(letter)
    return(outText.lower())

def decOutC(cText):
    outText = cDecrypt(cText)
    return(outText)

def decOutM(cText):
    outText = mDecrypt(cText)
    return(outText)


#Output File Recorder
def outputFile(file_path, out_file): 
    os.chdir(o_path)
    with open(file_path, 'a') as k:
        k = open(file[:-4] + "_j90992mm.txt", "w")
        k.write(out_file)
        k.close
    os.chdir(i_path) 

#File Repeater
for file in os.listdir():
    file_path = f"{i_path}\{file}"
    outputFile(file_path, read_text_file(file_path))
