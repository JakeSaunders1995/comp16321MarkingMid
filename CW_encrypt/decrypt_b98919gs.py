import argparse
import os

# file_input = "T1tT2pT2pT1cT1d"
# file_input = "T1tT2tT2tT2pT2c"
# file_input = "T1cT1pT2tT2tT1t"
# file_output = ""

# Parse command line input
parser = argparse.ArgumentParser()
parser.add_argument('input_path', metavar='path', type=str)
parser.add_argument('output_path', metavar='path', type=str)
arguments = parser.parse_args()
input_path = arguments.input_path
output_path = arguments.output_path

# file_input = "Hex:53 6f 6c 76 69 6e 67 20 68 65 78 20 69 73 20 76 65 72 79 20 65 61 73 79 20 69 6e 20 70 79 74 68 6f 6e"
# file_input = "Morse Code:.... --- .-- . ...- . .-. / ... --- .-.. ...- .. -. --. / -- --- .-. ... . / -.-. --- -.. . / -- .- -.-- / -... . / - .... . / -- --- ... - / -.. .. ..-. ..-. .. -.-. ..- .-.. -"
# file_input = "Caesar Cipher(+3):exw fdhvdu lv d olwwoh pruh gliilfxow"

MORSE_CODE_SYMBOLS = {
    '.-': 'a', '-...': 'b', '-.-.': 'c',
    '-..': 'd', '.': 'e', '..-.': 'f',
    '--.': 'g', '....': 'h', '..': 'i',
    '.---': 'j', '-.-': 'k', '.-..': 'l',
    '--': 'm', '-.': 'n', '---': 'o',
    '.--.': 'p', '--.-': 'q', '.-.': 'r',
    '...': 's', '-': 't', '..-': 'u',
    '...-': 'v', '.--': 'w', '-..-': 'x',
    '-.--': 'y', '--..': 'z', '.----': '1',
    '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9', '-----': '0',
    '--..--': ', ', '.-.-.-': '.', '..--..': '?',
    '-..-.': '/', '-....-': '-', '-.--.': '(',
    '-.--.-': ')', '.-...': '&', '.----.': '\'',
    '.--.-.': '@', '---...': ':', '-...-': '=',
    '-.-.--': '!', '.-.-.': '+', '.-..-.': '"',
    '..--..': '?'. '-..-.': '/'
}

CAESAR_ALPHABET = "xyzabcdefghijklmnopqrstuvwxyzabc"

def morse_code(cipher_text):
    words = cipher_text.split('/')
    result = ""
    for word in words:
        chars = word.split()
        for char in chars:
            result += MORSE_CODE_SYMBOLS[char]
        result += " "
    return result

def caesar(cipher_text):
    result = ""
    cipher_text = cipher_text.lower()
    cipher_key = 3

    for char in cipher_text:
        if char == " ":
            result += char
            continue

        alphabet_position = cipher_key

        while char != CAESAR_ALPHABET[alphabet_position]:
            alphabet_position += 1

        alphabet_position -= cipher_key
        result += CAESAR_ALPHABET[alphabet_position]

    return result

def hexadecimal(cipher_text):
    hexs = cipher_text.split()
    result = ""
    for hex in hexs:
        decimal = int(hex, 16)
        result += chr(decimal)
    return result.lower()

ENCRYPTION_METHODS = {
    "morse": morse_code,
    "caesar": caesar,
    "hex": hexadecimal
}

def write_to_file(file_input, file_name):
    input_args = file_input.split(":")
    encryption_type = input_args[0].lower()

    for key, func in ENCRYPTION_METHODS.items():
        if key in encryption_type:
            result = func(input_args[1])
            break

    file_name = file_name.replace(".txt", "")

    # Write to output file
    with open(os.path.join(output_path, f"{file_name}_b98919gs.txt"), 'w') as f:
        f.write(result)

# Command line files, input and output folder
try:
    os.mkdir(output_path)
except OSError as e:
    print(e)

for file in os.listdir(input_path):
    with open(os.path.join(input_path, file), 'r') as f:
        inp = f.read().rstrip()
        write_to_file(inp, file)

# print(result)
# print(ENCRYPTION_METHODS[input_args[0]](input_args[1]))
