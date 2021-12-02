import sys
import os

file_paths = sys.argv

input_path = file_paths[1]
output_path = file_paths[2]

os.chdir(input_path)
files_in_directory = os.listdir()

MORSE_CODE_ALPHABET = {
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


def decryption(input_file_string):

    os.chdir(input_path)

    def morse_code(input_string):
        output_string = ""
        string_to_parse = input_string.split(" ")
        for code_part in string_to_parse:
            add_space = False
            if "/" in code_part:
                code_part = code_part.replace("/", "")
                add_space = True
            try:
                output_string += MORSE_CODE_ALPHABET[code_part]
            except KeyError:
                pass
            if add_space:
                output_string += " "
    
        return output_string.lower()
    
    
    def caesar_cipher(input_string):
        output_string = ""
        for character in input_string:
            if character == "a":
                output_string += "x"
            elif character == "b":
                output_string += "y"
            elif character == "c":
                output_string += "z"
            elif character == " ":
                output_string += " "
            else:
                hexadecimal_value = ord(character)
                hexadecimal_value -= 3
                output_string += chr(hexadecimal_value)
    
        return output_string.lower()
    
    
    def hexadecimal(input_string):
        output_string = bytearray.fromhex(input_string).decode()
        return output_string.lower()

    encryption_methods = {
        "Morse Code": morse_code,
        "Caesar Cipher(+3)": caesar_cipher,
        "Hex": hexadecimal
    }

    input_file = open(input_file_string, "r")
    file_contents = input_file.read()
    values_to_parse = file_contents.split(":")
    input_method = values_to_parse[0]
    input_string = values_to_parse[1]
    
    output_string = encryption_methods[input_method](input_string)

    os.chdir(output_path)
    output_file_name = input_file_string.replace(".txt", "") + "_m59511md.txt"
    output_file = open(output_file_name, "w")
    output_file.write(output_string)


for file in files_in_directory:
    decryption(file)


