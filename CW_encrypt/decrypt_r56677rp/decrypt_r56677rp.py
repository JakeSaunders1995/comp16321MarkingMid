import argparse
import os
import re

# MORSECODE TRANSLATION
morseCode = { 'a':'.-', 'b':'-...',
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
              '0':'-----',
              ', ':'--..--', '.':'.-.-.-', '?':'..--..',
              '/':'-..-.', '-':'-....-', '(':'-.--.',
              ')':'-.--.-', '!':'-.-.-', ':':'---...',
              ';':'-.-.-.', '"':'.-..-.', "'":'.----.',
              ' ':'/'}

punctuationString = '''!()-[]{;}:'"\,<>./?@#$%^&*_~'''

parser = argparse.ArgumentParser()
parser.add_argument("inputFolder")
parser.add_argument("outputFolder")
args = parser.parse_args()

for files in os.walk(args.inputFolder):
    index = 0
    while index < len(files[2]):
        if ".txt" in files[2][index]:
            with open(args.inputFolder + "/" + files[2][index], "r") as currentFile:
                for line in currentFile:

                    # EXTRACT THE ALGO AND ENCRYPTED MSG
                    algorithm = line.split(":")[0]
                    encryptedCode = line.split(":")[1]
                    encryptedCodeWords  = encryptedCode.split(" ")

                    decryptedCode = ""

                    # HEX DECRYPTION
                    if algorithm == "Hex":
                        for hexCode in range(0, len(encryptedCodeWords)):
                            byteObj = bytes.fromhex(encryptedCodeWords[hexCode])
                            decryptedCode += byteObj.decode("ASCII")

                    # CAESAR DECRYPTIO
                    if algorithm == "Caesar Cipher(+3)":
                        # CHECK FOR PUNCTUATION AND DIGITS and remove
                        encryptedCodeWords = [word for word in encryptedCodeWords if not re.search(r'\d', word)]
                        encryptedCode = ' '.join(encryptedCodeWords)
                        for char in encryptedCode:
                            if char in punctuationString:
                                encryptedCode.strip(char)

                        plaintextPosition = 0
                        while (plaintextPosition < len(encryptedCode)):
                            plaintextChar = encryptedCode[plaintextPosition]
                            
                            if plaintextChar == " ":
                                decryptedCode = decryptedCode + " "

                            ASCIIValue = ord(plaintextChar)
                            ASCIIValue = ASCIIValue - 3
                            decryptedCode += chr(ASCIIValue)
                            plaintextPosition = plaintextPosition + 1

                    # MORSECODE DECRYPTION
                    if algorithm == "Morse Code":
                        for currentChar in encryptedCodeWords:
                            for asciiChar, char in morseCode.items():
                                if currentChar == char:
                                    decryptedCode += asciiChar

                    #TRANSFORM TO LOWER
                    decryptedCode = decryptedCode.lower()

                    #WRITE TO FILES IN FOLDER
                    with open(args.outputFolder + "/" + files[2][index][:-4] + "_r56677rp.txt", "w") as writeFile:
                        writeFile.write(decryptedCode)
                    writeFile.close()
            currentFile.close()
        index += 1