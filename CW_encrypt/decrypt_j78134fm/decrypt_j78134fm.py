import os
import argparse
import re

def slash_n_scrub(string):
    string = string.replace("\n", "")

def encryption_method(cipher):
    lst = cipher.split(":")

    algorithm = lst[0]

    if algorithm == "Caesar Cipher(+3)":
        return "caesar"
    elif algorithm == "Hex":
        return "hexadecimal"
    elif algorithm == "Morse Code":
        return "morse"

def cipher_func(cipher):
    lst = cipher.split(":")
    cipher_text = lst[1]

    return cipher_text

def morse(cipher):
    lst = cipher.split(" ")
    morse_alphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", ".-.-.-", "--..--", "..--..", ".----.", "-.-.--", "-..-.", "-.--.", "-.--.-", ".-...", "---...", "-.-.-.", "-...-", ".-.-.", "-....-", "..--.-", ".-..-.", "...-..-", ".--.-." ]
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    alphabet = list(alphabet)
    decrypted_cipher = ""

    for morse in lst:
        morse = re.sub("\n", "", morse)
        morse = morse.lower()
        if morse != "/":
            morse_index = morse_alphabet.index(morse)
            char = alphabet[morse_index]
            decrypted_cipher += char
        elif morse == "/":
            decrypted_cipher += " "

    decrypted_cipher_joined = "".join(decrypted_cipher)

    return decrypted_cipher_joined

def caesar(cipher):
    cipher = cipher.lower()
    cipher = re.sub("\n", "", cipher)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = list(alphabet)
    decrypted_cipher = []
    shift = 3

    for character in cipher:
        if character != " ":
            character_index = alphabet.index(character)
            character_index -= shift
            if character_index < 0:
                character_index += 26
            elif character_index > 25:
                character_index -= 26
            decrypted_character = alphabet[character_index]
            decrypted_cipher += decrypted_character
        else:
            decrypted_cipher += character

    decrypted_cipher_joined = "".join(decrypted_cipher)

    return decrypted_cipher_joined

def hexadecimal(cipher):
    lst = cipher.split(" ")
    decrypted_cipher = []
    for hex in lst:
        ascii_integer = int(hex, base=16)
        char = chr(ascii_integer)
        decrypted_cipher += char

    decrypted_cipher_joined = "".join(decrypted_cipher)
    return decrypted_cipher_joined


parser = argparse.ArgumentParser()
parser.add_argument("inputfilepath", help="The input file path")
parser.add_argument("outputfilepath", help="The output file path")
args = parser.parse_args()

inputdirectory = args.inputfilepath
outputdirectory = args.outputfilepath

for filename in os.listdir(inputdirectory):
        with open(os.path.join(inputdirectory, filename)) as inputfile:
            cipherandalgorithm = inputfile.read()

        cipher = cipher_func(cipherandalgorithm)
        algorithm = encryption_method(cipherandalgorithm)

        if encryption_method(cipherandalgorithm) == "caesar":
            decrypted_cipher = caesar(cipher)
            decrypted_cipher_lower = decrypted_cipher.lower()
        elif encryption_method(cipherandalgorithm) == "morse":
            decrypted_cipher = morse(cipher)
            decrypted_cipher_lower = decrypted_cipher.lower()
        elif encryption_method(cipherandalgorithm) == "hexadecimal":
            decrypted_cipher = hexadecimal(cipher)
            decrypted_cipher_lower = decrypted_cipher.lower()

        filename_split = filename.split(".")
        filename_split.insert(1, "_j78134fm.")
        filename_otpt = "".join(filename_split)
        filename_output = os.path.join(outputdirectory, filename_otpt)

        with open(filename_output, "w") as outputfile:
            outputfile.write(decrypted_cipher_lower)
