import argparse
import os

def hex_to_dec(text):
    digit2 = 0
    digit1 = 0
    if text[0] == "a":
        digit2 = 10
    elif text[0] == "b":
        digit2 = 11
    elif text[0] == "c":
        digit2 = 12
    elif text[0] == "d":
        digit2 = 13
    elif text[0] == "e":
        digit2 = 14
    elif text[0] == "f":
        digit2 = 15
    else:
        digit2 = int(text[0])

    if text[1] == "a":
        digit1 = 10
    elif text[1] == "b":
        digit1 = 11
    elif text[1] == "c":
        digit1 = 12
    elif text[1] == "d":
        digit1 = 13
    elif text[1] == "e":
        digit1 = 14
    elif text[1] == "f":
        digit1 = 15
    else:
        digit1 = int(text[1])

    dec_num = digit2 * 16 + digit1
    return dec_num
parser = argparse.ArgumentParser(description='input and output')
parser.add_argument('input', type=str, help='Input')
parser.add_argument('output', type=str, help='Output')
args = parser.parse_args()
path1 = args.input
path2 = args.output
fl =[i for i in os.listdir(path1)]
filelist1 = [path1 + i for i in os.listdir(path1)]
for files in filelist1:
    index = filelist1.index(files)
    file = open(files)
    read_char = file.read()
    file.close()


    code_type = read_char[0:3]
    code_type = code_type.lower()
    colon_index = read_char.find(":")+1
    message = ""

    if code_type == "hex":
        while True:
            if colon_index+2 < len(read_char):
                hex_num = read_char[colon_index:colon_index + 2]
            else:
                hex_num = read_char[colon_index:]
            hex_num = hex_to_dec(hex_num)
            message = message + chr(hex_num)
            if colon_index+3 >= len(read_char):
                break
            else:
                colon_index += 3

    elif code_type == "cae":
        while colon_index < len(read_char)-1:
            if read_char[colon_index] == " ":
                message = message + " "
                colon_index += 1

            plaintext = read_char.lower()
            alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
            plaintextChar = plaintext[colon_index]
            alphabetPosition = 3
            while plaintextChar != alphabet[alphabetPosition]:
                alphabetPosition += 1
            alphabetPosition -= 3
            message = message + alphabet[alphabetPosition]
            colon_index += 1


    else:
        code_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                     'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                     'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                     'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                     '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ':': '---...',
                     ',': '--..--', ';': '-.-.-.', '?': '..--..', '=': '-...-', "'": '.----.', '/': '-..-.', '!': '-.-.--',
                     '——': '-....-', '-': '..--.-', '"': '.-..-.', '(': '-.--.', ')': '-.--.-', ' ': '/'}

        read_char = read_char[colon_index:]
        read_list = read_char.split()
        for char in read_list:
            English_char = list(code_dict.keys())[list(code_dict.values()).index(char)]
            message = message + English_char


    message = message.lower()
    filename = fl[index]
    filename = filename[:-4]+"_k75018lg.txt"
    create = open(path2+filename,"w")
    create.write(message)
    create.close()

