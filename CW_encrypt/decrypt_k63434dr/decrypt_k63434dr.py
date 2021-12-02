import argparse
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument("inputDirectory")
parser.add_argument("outputDirectory")
parsed_args = parser.parse_args(sys.argv[1:])

# Morse code dictionary taken from https://www.geeksforgeeks.org/morse-code-translator-python/
morseDict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
             'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
             'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
             'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
             '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
             '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}
# Convert dictionary to Morse:Letter(lowercase) to make the decryption algorithm below more readable
newDict = {k: v.lower() for v, k in morseDict.items()}


def decrypt(strInp):
    algorithm, ciphertext = strInp.split(':', 1)
    if algorithm == 'Hex':
        bytesObj = bytes.fromhex(ciphertext)
        decryptedStr = bytesObj.decode('ASCII').lower()
    elif algorithm == 'Caesar Cipher(+3)':
        # For each character, convert it to its unicode if the char is not a space, then take three from its value
        # and convert back into a character, once again only if the char is not a space
        decryptedStr = "".join(
            [chr(i - 3) if i != ' ' else i for i in list(map(lambda x: ord(x) if x != ' ' else x, ciphertext))])
    else:
        # Using list comprehension to first split ciphertext into words, seperated by /, then splitting the words
        # into characters, seperated by spaces. For each character replace it with it's corresponding value in the
        # morse dictionary
        decryptedStr = " ".join(["".join([newDict[char] for char in word.split()]) for word in ciphertext.split('/')])
    return decryptedStr


def getFiles(dirPath):
    return next(os.walk(dirPath))[2]


files = getFiles(parsed_args.inputDirectory)
for file in files:
    inp = open(f"{parsed_args.inputDirectory}\{file}", 'r')
    out = open(f"{parsed_args.outputDirectory}\{file.replace('.txt', '')}_k63434dr.txt", 'w+')
    solution = decrypt(inp.read())
    out.write(solution)
    out.close()
