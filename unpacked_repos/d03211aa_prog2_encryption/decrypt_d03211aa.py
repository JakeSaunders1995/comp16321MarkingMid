import os
import argparse
import sys
import re

username = "_d03211aa"

parser = argparse.ArgumentParser()

parser.add_argument('inputs')

parser.add_argument('outputs')

args = parser.parse_args()


files = sorted(os.listdir(args.inputs))


for filename in files:
    file = open(args.inputs.strip("./") + '/' + filename)

    text = ""
    for line in file:
        text += line

    file.close()

    text = text.split(':')

    if filename[-4:] == ".txt": 
        edited_filename = filename[:len(filename) - 4] + username + ".txt"
    else:
        edited_filename = filename + username

    if text[0] == "Morse Code":

        morse_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
                      '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                      '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                      '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                      '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                      '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                      '-.--': 'Y', '--..': 'Z', '/': ' '}

        encrypted = text[1]
        encrypted = encrypted.split()
        for index in range(len(encrypted)):
            letter = encrypted[index]
            encrypted[index] = morse_dict[letter]

        encrypted = "".join(encrypted)
        encrypted = encrypted.lower()
        text = encrypted

    elif text[0] == "Caesar Cipher(+3)":
        # Initialize variables
        cipher_text = text[1]
        plain_text = ""
        cipher_text_position = 0

        # Outer while loop will go through plain_text
        while cipher_text_position < len(cipher_text):
            cipher_text_char = cipher_text[cipher_text_position]

            if cipher_text_char == ' ':
                plain_text = plain_text + ' '
            else:
                ASCIIValue = int(ord(cipher_text_char)) - 3

                plain_text = plain_text + chr(ASCIIValue)

            cipher_text_position = cipher_text_position + 1

        text = plain_text

    elif text[0] == "Hex":
        hex_string = "53 6f 6c 76 69 6e 67 20 68 65 78 20 69 73 20 76 65 72 79 20 65 61 73 79 20 69 6e 20 70 79 74 68 6f 6e"
        byte_array = bytearray.fromhex(hex_string)
        hex_string = byte_array.decode().lower()
        text = hex_string

    file = open(args.outputs.strip("./") + '/' + edited_filename, "w")

    file.write(text)

    file.close()