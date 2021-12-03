import os
import argparse
import os.path
from os import listdir
morseCodeDict = { '.-':'a', '-...':'b',
                    '-.-.':'c', '-..':'d', '.':'e',
                    '..-.':'f', '--.':'g', '....':'h',
                    '..':'i', '.---':'j', '-.-':'k',
                    '.-..':'l', '--':'m', '-.':'n',
                    '---':'o', '.--.':'p', '--.-':'q',
                    '.-.':'r', '...':'s', '-':'t',
                    '..-':'u', '...-':'v', '.--':'w',
                    '-..-':'x', '-.--':'y', '--..':'z', 
                    '/':' ', '.-.-.-':'.', '..--..':'?',
                    '-.-.--':'!','--..--':',','---...':':',
                    '-.-.-.':';','-....-':'-','-.--.-':'(',
                    '.----.':"'",'.-..-.':"''"}

parser = argparse.ArgumentParser()
parser.add_argument("input_folder_path", type = str)
parser.add_argument("output_folder_path", type = str)
args=parser.parse_args()
inputpath = args.input_folder_path
outputpath = args.output_folder_path

filenames = listdir(inputpath)
for k in range(len(filenames)):
    ciphertextfile = open(inputpath + filenames[k], "r")
    plaintextfile = open(outputpath + filenames[k], "w")

    plaintext = ""

    for ciphertext in ciphertextfile:
        if ciphertext[0] == "C":
            for i in range(len(ciphertext)):
                if ciphertext[i] == ":":
                    ciphertextPosition  = i + 1
            while (ciphertextPosition < len(ciphertext)):
                ciphertextChar = ciphertext[ciphertextPosition]
                if ciphertextChar == " ":
                    plaintext = plaintext + " "
                elif 32 < ord(ciphertextChar) < 48 or 57 < ord(ciphertextChar) < 65 or 90 < ord(ciphertextChar) < 97 or 122 < ord(ciphertextChar) < 127:
                    plaintext += ciphertextChar
                else:
                    if ciphertextChar == "a":
                        plaintext += "x"
                    elif ciphertextChar == "b":
                        plaintext += "y"
                    elif ciphertextChar == "c":
                        plaintext += "z"
                    else:
                        ASCIIValue = ord(ciphertextChar)
                        while ciphertextChar != chr(ASCIIValue):
                            ASCIIValue = ASCIIValue + 1
                        ASCIIValue = ASCIIValue - 3
                        plaintext = plaintext + chr(ASCIIValue)
                        print(plaintext)
                ciphertextPosition += + 1
        if ciphertext[0] == "H":
            for i in range(len(ciphertext)):
                if ciphertext[i] == ":":
                    ciphertextPosition  = i + 1
            while (ciphertextPosition < len(ciphertext)):
                ciphertextChar = ciphertext[ciphertextPosition] + ciphertext[ciphertextPosition + 1]
                hexValue = int("0x" + ciphertextChar, 16)
                plaintext = plaintext + chr(hexValue)
                ciphertextPosition += 3
        if ciphertext[0] == "M":
            ciphertext = ciphertext + " "
            for i in range(len(ciphertext)):
                if ciphertext[i] == ":":
                    ciphertextPosition = i + 1
            ciphertextChar = ""
            while ciphertextPosition < len(ciphertext):
                if ciphertext[ciphertextPosition] != " ":
                    ciphertextChar += ciphertext[ciphertextPosition]
                elif ciphertext[ciphertextPosition] == " ":
                    plaintext += morseCodeDict[ciphertextChar]
                    ciphertextChar = ""                
                ciphertextPosition += 1
    plaintextfile.write(str(plaintext))

plaintextfile.close()
for k in range(len(filenames)):
    oldname = filenames[k].strip("/").split(".")
    os.rename(outputpath + filenames[k], outputpath + oldname[0] + '_h85345ww.txt')

