import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('inputPath', type=str)
parser.add_argument('outputPath', type=str)
args = parser.parse_args()

def morseCode(cipherText):
    cipherChars = cipherText.split()
    plainText = ""

    morse = {
        "/": " ",
        ".-": "a",
        "-...": "b",
        "-.-.": "c",
        "-..": "d",
        ".": "e",
        "..-.": "f",
        "--.": "g",
        "....": "h",
        "..": "i",
        ".---": "j",
        "-.-": "k",
        ".-..": "l",
        "--": "m",
        "-.": "n",
        "---": "o",
        ".--.": "p",
        "--.-": "q",
        ".-.": "r",
        "...": "s",
        "-": "t",
        "..-": "u",
        "...-": "v",
        ".--": "w",
        "-..-": "x",
        "-.--": "y",
        "--..": "z",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
        "-----": "0",
    }

    for char in cipherChars:
        plainText += morse.get(char)

    return plainText

def caesar(cipherText):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    shifted = "defghijklmnopqrstuvwxyzabc "

    plainText = ""

    for char in cipherText.lower():
        if char != "\n":
            i = shifted.index(char)
            plainText += alphabet[i]

    return plainText

def hex(cipherText):
    plainText = bytes.fromhex(cipherText)
    plainText = plainText.decode("ascii")
    return plainText.lower()

def decrypt(inputFilename):
    with open(args.inputPath + "/" + inputFilename) as file:
        text = file.read()

    colon = text.index(":")
    method = text[:colon]
    cipherText = text[colon+1:]

    if method == "Hex":
        output = hex(cipherText)
    elif method == "Caesar Cipher(+3)":
        output = caesar(cipherText)
    elif method == "Morse Code":
        output = morseCode(cipherText)

    outputFilename = inputFilename[0:-4] + "_w25478ia.txt"
    with open(args.outputPath + "/" + outputFilename, "w") as file:
        file.write(output)

dirs = os.listdir(args.inputPath)

for file in dirs:
    if file[-4:] == ".txt":
        decrypt(file)