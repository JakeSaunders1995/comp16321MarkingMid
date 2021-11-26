import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input", help="Input directory. Directory is scanned for valid input files.")
parser.add_argument("output", help="Output directory. Output files are written to directory. Will overwrite file if it already exists.")
args = parser.parse_args()

def MorseDecode(ciphertext: str):
    encoding = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9", "-----": "0", ".-.-.-": ".", "--..--": ",", "..--..": "?", ".----.": "'", "-.-.--": "!", "-..-.": "/", "-.--.": "(", "-.--.-": ")", ".-...": "&", "---...": ":", "-.-.-.": ";", "-...-": "=", ".-.-.": "+", "-....-": "-", "..--.-": "_", ".-..-.": "\"", "...-..-": "$", ".--.-.": "@"}
    plaintext = ""
    words = ciphertext.split(" / ")
    for word in words:
        characters = word.split(" ")
        for character in characters:
            plaintext += encoding[character]
        plaintext += " "
    return plaintext.strip() #Otherwise there will be a trailing space character

def CaesarDecode(ciphertext: str, shift: int):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    plaintext = ""
    for character in ciphertext:
        if character in alphabet:
            index = alphabet.index(character)
            index -= shift
            if index < 0:
                index = len(alphabet) + index
            elif index >= len(alphabet):
                index = index - len(alphabet)
            plaintext += alphabet[index]
        else:
            plaintext += character
    return plaintext

def HexDecode(ciphertext: str):
    plaintext = ""
    characters = ciphertext.split(" ")
    for character in characters:
        charVal = int(character, base=16)
        plaintext += chr(charVal)
    return plaintext

files = os.scandir(args.input)
for file in files:
    if not file.is_file() or file.name[-4:] != ".txt":
        continue
    text = ""
    with open(file) as f:
        text = f.read()
    splitText = text.split(":")
    if len(splitText) != 2:
        continue
    algorithm = splitText[0]
    ciphertext = splitText[1]
    plaintext = ""
    if algorithm == "Morse Code":
        plaintext = MorseDecode(ciphertext)
    elif algorithm == "Caesar Cipher(+3)":
        plaintext = CaesarDecode(ciphertext, 3)
    elif algorithm == "Hex":
        plaintext = HexDecode(ciphertext)
    else:
        continue
    fileName = os.path.join(args.output, file.name[:-4] + "_v31903mb.txt")
    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    with open(fileName, "w") as f:
        f.write(plaintext.lower())
