import os
import argparse
import re

parser = argparse.ArgumentParser(description="Decrypt")
parser.add_argument("IN_FOLDER")
parser.add_argument("OUT_FOLDER")

args = parser.parse_args()

MORSE_CODE = {
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
    "/": " "
}

ALPHAS = "abcdefghijklmnopqrstuvwxyz"

for input_filename in os.scandir(args.IN_FOLDER):
    with open(input_filename, "r") as input_file:
        input_str = input_file.read()

    encryption_method, ciphertext = input_str.split(":", 1)

    output_str = ""
    if encryption_method == "Hex":
        output_str = bytes.fromhex("".join(ciphertext.split())).decode("ascii").lower()
    elif encryption_method == "Caesar Cipher(+3)":
        output_str = ""
        for char in ciphertext:
            if char in ALPHAS:
                character_num = ord(char) - ord("a")
                new_character_num = (character_num + 23) % 26
                new_char = chr(new_character_num + ord("a"))
                output_str += chr(new_character_num + ord("a"))
            else:
                output_str += char
    elif encryption_method == "Morse Code":
        for letter in ciphertext.split():
            if letter not in MORSE_CODE:
                raise Exception("Invalid morse code letter")
            else:
                output_str += MORSE_CODE[letter]
    else:
        raise Exception("Invalid encryption method!")

    output_filename = os.path.join(
        args.OUT_FOLDER,
        os.path.splitext(
            os.path.basename(input_filename))[0] +
        "_c60952ti" +
        os.path.splitext(input_filename)[1])

    with open(output_filename, "w") as output_file:
        output_file.write(output_str)
