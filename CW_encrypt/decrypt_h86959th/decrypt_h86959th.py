# python3 decrypt_h86959th.py /home/csimage/16321_python_coursework_h86959th/midterm_files/Example_inputs/Example_inputs_program2 /home/csimage/16321_python_coursework_h86959th/midterm_files/Example_outputs/Example_outputs_program2
# python3 decrypt_h86959th.py ./Example_inputs/Example_inputs_program2 ./Example_outputs/Example_outputs_program2

import argparse
from argparse import ArgumentParser
import os


parser = argparse.ArgumentParser() # argument setup
parser.add_argument('inputFolder', type=str, help="Input folder")
parser.add_argument('outputFolder', type=str, help="Output folder")
args = parser.parse_args()
inFile = ""


for filename in os.listdir(args.inputFolder): # goes thru all files in input folder
    if filename.endswith(".txt"): # goes thru all txt files

        inFile = (os.path.join(args.inputFolder, filename))
        filename = filename[:-4] + "_h86959th.txt" # removes txt and replace w ur username
        outFile = (os.path.join(args.outputFolder, filename))

        inputFile = open(inFile, "rt")
        encrypt = inputFile.read()

        if encrypt[0].lower() == "m":

            morseCode = { # add numbers, remove punctuation except for /: " "
            ".-": "a", "-...": "b", 
            "-.-.": "c", "-..": "d", 
            ".": "e", "..-.": "f", 
            "--.": "g", "....": "h", 
            "..": "i", ".---": "j", 
            "-.-": "k", ".-..": "l", 
            "--": "m", "-.": "n", 
            "---": "o", ".--.": "p", 
            "--.-": "q", ".-.": "r", 
            "...": "s", "-": "t", 
            "..-": "u", "...-": "v", 
            ".--": "w", "-..-": "x", 
            "-.--": "y", "--..": "z",
            "/": " "
            }
            
            encrypt = encrypt.split(":")
            encrypt1 = encrypt[1]
            encrypt2 = encrypt1.split(" ")
            converted = ""

            for word in range(0, len(encrypt2)):
                if encrypt2[word] in morseCode:
                    converted = converted + morseCode[encrypt2[word]]

            outputText = open(outFile, "wt")
            outputText.write(converted)
            outputText.close()
            

        # if encrypt[0].lower() == "c": # caeser doesn't work, might have to create a dictionary
        #     # need to count \n as a word i think
        #     encrypt = encrypt.replace('Caesar Cipher(+3):', '')
        #     encryptPos = 0
        #     decrypt = ""

        #     while encryptPos < len(encrypt):
        #         encryptChar = encrypt[encryptPos]

        #         if encryptChar == " ":
        #             decrypt = decrypt + " "
        #             encryptPos += 1
        #         else:
        #             ascVal = ord(encryptChar)
        #             ascVal = ascVal - 3
        #             decrypt = decrypt + chr(ascVal)
        #             encryptPos = encryptPos + 1
        #             # this would be where i use the dictionary
        #             # might have to create a numbers and letters dictionary to seperate between them
        #             # need to include \n 
        #     else:
        #         decrypt1 = decrypt.lower()

        #     outputText = open(outFile, "wt")
        #     outputText.write(decrypt1)
        #     outputText.close()

        if encrypt[0].lower() == "c":
            encrypt = encrypt.replace('Caesar Cipher(+3):', '')
            encryptPos = 0
            decrypt = ""
            encrypt = encrypt.lower()

            numbers = {
            "0": "7", "1": "8",
            "2": "9", "3": "0",
            "4": "1", "5": "2",
            "6": "3", "7": "4",
            "8": "5", "9": "6"
            }

            letters = {
            "a": "x", "b": "y",
            "c": "z", "d": "a",
            "e": "b", "f": "c",
            "g": "d", "h": "e",
            "i": "f", "j": "g",
            "k": "h", "l": "i",
            "m": "j", "n": "k",
            "o": "l", "p": "m",
            "q": "n", "r": "o",
            "s": "p", "t": "q",
            "u": "r", "v": "s",
            "w": "t", "x": "u",
            "y": "v", "z": "w"
            }

            for char in encrypt:
                if char == " ":
                    decrypt = decrypt + " "
                    encryptPos += 1
                elif char in numbers:
                    decrypt = decrypt + numbers[encrypt[encryptPos]]
                    encryptPos += 1
                elif char in letters:
                    decrypt = decrypt + letters[encrypt[encryptPos]]
                    encryptPos += 1

            outputText = open(outFile, "wt")
            outputText.write(decrypt)
            outputText.close()

        if encrypt[0].lower() == "h":
            encrypt = encrypt.replace('Hex:', '')
            encryptAscii = bytearray.fromhex(encrypt).decode()
            encryptAscii = encryptAscii.lower()

            outputText = open(outFile, "wt")
            outputText.write(encryptAscii)
            outputText.close()