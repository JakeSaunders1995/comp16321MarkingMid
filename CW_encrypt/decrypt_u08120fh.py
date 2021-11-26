import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('input_folder')
parser.add_argument('output_folder')
args = parser.parse_args()

input_directory = args.input_folder
output_directory = args.output_folder

for filename in sorted(os.listdir(input_directory)):

    output_file = filename.split(".")[0] + "_u08120fh.txt"

    with open(os.path.join(input_directory, filename), "r") as file:
        line = file.read()

    words = line.split(":")

    method = words[0]
    encrypted = words[1]

    def convert_hex(hexa):
        ascii_string = bytearray.fromhex(hexa).decode()
        return ascii_string.lower()

    def convert_morse(msg):
        morse_dict = {'A': '.-', 'B': '-...',
                      'C': '-.-.', 'D': '-..', 'E': '.',
                      'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-',
                      'L': '.-..', 'M': '--', 'N': '-.',
                      'O': '---', 'P': '.--.', 'Q': '--.-',
                      'R': '.-.', 'S': '...', 'T': '-',
                      'U': '..-', 'V': '...-', 'W': '.--',
                      'X': '-..-', 'Y': '-.--', 'Z': '--..',
                      '1': '.----', '2': '..---', '3': '...--',
                      '4': '....-', '5': '.....', '6': '-....',
                      '7': '--...', '8': '---..', '9': '----.',
                      '0': '-----', ', ': '--..--', '.': '.-.-.-',
                      '?': '..--..', '/': '-..-.', '-': '-....-',
                      '(': '-.--.', ')': '-.--.-', ' ': '/',
                      '&': '.-...', '@': '.--.-.', ':': '---...',
                      '=': '-...-', '!': '-.-.--', '+': '.-.-.',
                      '\"': '.-..-.', '\'': '.----.', ';': '-.-.-.',
                      '*': '-..-'}

        new_msg = msg.split()
        plaintext = []
        for i in range(0, len(new_msg)):
            if new_msg[i] in morse_dict.values():
                for key, value in morse_dict.items():
                    if value == new_msg[i]:
                        plaintext.append(key)

        plain_string = ""
        for i in plaintext:
            a = i.lower()
            plain_string += a

        return plain_string

    def convert_caesar(caesar):
        cipherText = caesar.split()
        plainText = ""
        alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"

        for text in cipherText:
            word = text.lower()
            cipherTextPosition = 0
            while cipherTextPosition < len(word):
                cipherTextChar = word[cipherTextPosition]
                alphabetPostion = 3

                while cipherTextChar != alphabet[alphabetPostion]:
                    alphabetPostion += 1

                alphabetPostion -= 3
                plainText += alphabet[alphabetPostion]
                cipherTextPosition += 1
            plainText += " "

        return plainText[0:len(plainText)-1]

    with open(os.path.join(output_directory, output_file), "w") as op:
        if "Hex" in method:
            msg = convert_hex(encrypted)
            op.write(msg)
        elif "Morse" in method:
            msg = convert_morse(encrypted)
            op.write(msg)
        elif "Caesar" in method:
            msg = convert_caesar(encrypted)
            op.write(msg)
