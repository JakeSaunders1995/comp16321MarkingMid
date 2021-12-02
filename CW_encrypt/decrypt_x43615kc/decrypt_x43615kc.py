import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("input_path")
parser.add_argument("output_path")
args = parser.parse_args()

def caesar_three(ciphertext: str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plaintext = ""
    for c in ciphertext.lower():
        if c.isalpha():
            shifted = alphabet[(alphabet.index(c) - 3) % len(alphabet)]
            plaintext += shifted
        else:
            plaintext += c
    return plaintext    

def hex_thing(ciphertext):
    return ''.join([chr(int(x, 16)) for x in ciphertext.split(" ")]).lower()


morse_conversions = {
    "/": " ", # spaces
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
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9"
}
def morse(ciphertext):
    phrases = ciphertext.split(' ')
    plaintext = ""
    for p in phrases:
        plaintext += morse_conversions[p]
    return plaintext

def convert_file(path):
    with open(path, "r") as file:
        file_text = file.read()
        algorithm, ciphertext = file_text.split(":", maxsplit=1)
        plaintext = ""
        if algorithm == "Hex":
            plaintext = hex_thing(ciphertext)
        elif algorithm == "Caesar Cipher(+3)":
            plaintext = caesar_three(ciphertext)
        elif algorithm == "Morse Code":
            plaintext = morse(ciphertext)
        else: #shouldnt happen
            plaintext = "algorithm not known!"
        return plaintext
        
def main():
    for dir, subdirs, files in os.walk(args.input_path):
        for file in files:
            result = convert_file(os.path.join(dir,file))
            output_path = os.path.join(args.output_path, os.path.splitext(file)[0] + "_x43615kc.txt")
            if not os.path.exists(args.output_path):
                os.makedirs(args.output_path)
            with open(output_path, "w") as file:
                file.write(result)



if __name__ == '__main__':
    main()