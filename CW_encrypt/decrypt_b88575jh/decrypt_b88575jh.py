import argparse
import os

def getContents(path):
    f = open(path, "r")
    contents = (f.read()).split(":")
    f.close()
    return contents

def caeserDecrypt(cipherText):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plain = ""

    for char in cipherText:
        if char != ' ':
            alphaIndex = alphabet.index(char) - 3
            plain += alphabet[alphaIndex]
        else:
            plain += " "

    return plain

def morseDecrypt(cipherText):
    alphabet = {
        ".-" : "A",
        "-..." : "B",
        "-.-." : "C",
        "-.." : "D",
        "." : "E",
        "..-." : "F",
        "--." : "G",
        "...." : "H",
        ".." : "I",
        ".---" : "J",
        "-.-" : "K",
        ".-.." : "L",
        "--" : "M",
        "-." : "N",
        "---" : "O",
        ".--." : "P",
        "--.-" : "Q",
        ".-." : "R",
        "..." : "S",
        "-" : "T",
        "..-" : "U",
        "...-" : "V",
        ".--" : "W",
        "-..-" : "X",
        "-.--" : "Y",
        "--.." : "Z"
    }

    words = cipherText.split(" / ")
    plainText = ""

    for word in words:
        letters = word.split(" ")
        plainWord = ""
        for letter in letters:
            plainWord += alphabet[letter]
        plainText += (plainWord + " ")

    return plainText

def hexDecrypt(cipherText):
    hexNumbers = cipherText.split(" ")
    plainText = ""
    for hex in hexNumbers:
        plainText += chr(int(hex,16))

    return plainText

def save(path, text):
    f = open(path, "w")
    f.write(text)
    f.close()

encryptions = {
    'Caesar Cipher(+3)' : caeserDecrypt,
    'Morse Code' : morseDecrypt,
    'Hex' : hexDecrypt
}

parser = argparse.ArgumentParser(description='Decrypts Morse, +3 shift Caeser and Hexadecimal')
parser.add_argument('source', type=str,help='Source folder path')
parser.add_argument('dest', type=str, help='Destination folder file')
args = parser.parse_args()

if not args.source.endswith("/"):
    args.source += "/"
if not args.dest.endswith("/"):
    args.dest += "/"

os.makedirs(args.dest, exist_ok=True)

for filename in os.listdir(args.source):
    input = getContents(args.source + filename)
    output = encryptions[input[0]](input[1])
    save(args.dest+filename[:-4]+"_b88575jh.txt", output)
