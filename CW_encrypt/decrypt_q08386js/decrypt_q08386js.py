import argparse
import re 
from os import X_OK, name
import os 
parser = argparse.ArgumentParser(description='Decryption')
parser.add_argument('ciphertxt', type=str, help='Cipher Input')
parser.add_argument('deciphertxt', type=str, help='Decipher Output')
args = parser.parse_args()

inputDirectory = args.ciphertxt
outputDirectory = args.deciphertxt

for i in os.listdir(inputDirectory):
    dirname = os.path.join(inputDirectory, i)
    directory = os.path.dirname(outputDirectory)
    file1 = open(dirname, "r")
    if outputDirectory[-1] != "/":
        nameout = outputDirectory + "/" + i.split(".txt")[0] + "_q08386js.txt"
    else:
        nameout = outputDirectory + i.split(".txt")[0] + "_q08386js.txt"
    if not os.path.exists(directory):
        os.makedirs(directory)
    stringinput = file1.readline()
     #alternatively use string.split
    splitstring = re.split(":", stringinput)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuations = [".", "?", "!", ",", ":", ";", "-", "_", "[]", "()", "{}", "..."]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    
    if splitstring[0][0] == "H":
        #For Hex
        hex = bytes.fromhex(splitstring[1])
        ans = hex.decode("ascii")
        lowans = ans.lower()

        file_write = open(nameout, "w")
        file_write.write(str(lowans))

        
    elif splitstring[0][0] == "M" or splitstring[0][0] == "m":
        #For Morse
        morseDictionary = { 
        'A':'.-', 'B':'-...',
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
        '?':'..--..', '/':'-..-.', '-':'-....-',
        '(':'-.--.', ')':'-.--.-', ' ': '/'
        }

        out = splitstring[1]
        decode =''
        code = ''
        out += " "
        for char in out:
            if (char != ' '):
                x = 0
                code += char
            else:
                x += 1
                if x == 2:
                    decode += ' '
                else:
                    decode += list(morseDictionary.keys())[list(morseDictionary.values()).index(code)]
                    code = ''

        filewrite = open(nameout, "w")
        filewrite.write(str(decode))

    elif splitstring[0][0] == "C" or splitstring[0][0] == "c":
        #For Caesar
        for x in range(len(splitstring[1])): 
        
            #lowercase
            if splitstring[1][x] in alphabet: 
                newpos = ((alphabet.find(splitstring[1][x])-3) % 26)
                char = alphabet[newpos]
                file_add = open(nameout, "a")
                file_add.write(str(char))
            
            elif splitstring[1][x] in punctuations and numbers:
                newpos = (alphabet.find(splitstring[1][x]))
                char = alphabet[newpos]
                file_add = open(nameout, "a")
                file_add.write(str(char))
            
            else: 
                char = splitstring[1][x]
                file_add = open(nameout, "a")
                file_add.write(str(char))