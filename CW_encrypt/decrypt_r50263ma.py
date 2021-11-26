import argparse
import os

parser = argparse.ArgumentParser(description="Calculating the rugby scores")
parser.add_argument("inputFolder")
parser.add_argument("outputFolder")
args = parser.parse_args()


files = os.listdir(args.inputFolder)
for f in files:
    if f != ".DS_Store":
        inputFile = open(args.inputFolder + "/" + f, 'r')
        outputFileName = f[:-4] + "_r50263ma" + ".txt"
        outputFile = open(args.outputFolder + "/" + outputFileName, "w")
        file = inputFile.read()
        index = file.index(":")
        message = file[index+1:]
        decryptedMessage = ''
        if file[:index] == "Hex":
            splitChars = message.split(" ")
            for char in splitChars:
                decryptedMessage += chr(int(char, 16))
        elif file[:index] == "Morse Code":
            splitChars = message.split(" ")
            morseDictionary = { ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z"}
            for char in splitChars:
                if char == "/":
                    decryptedMessage += " "
                else:
                    charachter = morseDictionary.get(char)
                    decryptedMessage += charachter
        elif file[:index] == "Caesar Cipher(+3)":
            for char in message:
                if char == " ":
                    decryptedMessage += " "
                else:
                    valueAscii = ord(char)
                    originalChar = chr(valueAscii - 3)
                    decryptedMessage += originalChar
        outputFile.write(decryptedMessage)
        inputFile.close()
        outputFile.close()
