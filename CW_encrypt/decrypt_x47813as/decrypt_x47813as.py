import argparse, os


morse_alphabet = {
    '.-' : 'a',
    '-...' : 'b',
    '-.-.' : 'c',
    '-..' : 'd',
    '.' : 'e',
    '..-.' : 'f',
    '--.' : 'g',
    '....' : 'h',
    '..' : 'i',
    '.---' : 'j',
    '-.-' : 'k',
    '.-..' : 'l',
    '--' : 'm',
    '-.' : 'n',
    '---' : 'o',
    '.--.' : 'p',
    '--.-' : 'q',
    '.-.' : 'r',
    '...' : 's',
    '-' : 't',
    '..-' : 'u',
    '...-' : 'v',
    '.--' : 'w',
    '-..-' : 'x',
    '-.--' : 'y',
    '--..' : 'z',
    '/' : ' ',
    '.-.-.-' : '.',
    '..--..' : '?',
    '-.-.--' : '!',
    '--..--' : ',',
    '---...' : ':',
    '-.-.-.' : ';',
    '-....-' : '-',
    '-....-' : '—',
    '-.--.' : '(',
    '-.--.-' : ')',
}


def morse_decode(text):
    ciphertext = text[11:]
    morse_letter = ""
    plaintext = ""
    for x in range(len(ciphertext)):
        if ciphertext[x] != " ":
            morse_letter = morse_letter + ciphertext[x]
        else:
            plaintext = plaintext + morse_alphabet[morse_letter]
            morse_letter = ""
    if morse_letter != "":
        plaintext = plaintext + morse_alphabet[morse_letter]
    return plaintext


def caesar_decode(text):
    ciphertext = text[18:]
    plaintext = ""
    for x in range(len(ciphertext)):
        if ciphertext[x] == " ":
            plaintext = plaintext + " "
        else:
            ascii = ord(ciphertext[x])-3
            plaintext = plaintext + chr(ascii)
    return(plaintext)


def hexadecimal_decode(text):
    ciphertext = text[4:]
    hex_letter = ""
    plaintext = ""
    for x in range(len(ciphertext)):
        if ciphertext[x] != " ":
            hex_letter = hex_letter + (ciphertext[x]).upper()
        else:
            plaintext = plaintext + chr(int(hex_letter, 16))
            hex_letter = ""
    if hex_letter != "":
        plaintext = plaintext + chr(int(hex_letter, 16))
    return plaintext

parser = argparse.ArgumentParser()
parser.add_argument("input_directory")
parser.add_argument("output_directory")
args = parser.parse_args()
 # input_file_names = os.listdir(args.input_directory)
# input_files = [file for file in os.listdir(args.input_directory)]
input_files = os.listdir(args.input_directory)


for filename in input_files:
    input_file = open(os.path.join(args.input_directory, filename), "r")
    ciphertext = (input_file.readlines())[0]
    if ciphertext[0] == "m" or ciphertext[0] == "M":
        plaintext = morse_decode(ciphertext)
    elif ciphertext[0] == "c" or ciphertext[0] == "C":
        plaintext = caesar_decode(ciphertext)
    else:  # ciphertext[0] == "h" or ciphertext[0] == "H"
        plaintext = hexadecimal_decode(ciphertext)
    filename = filename[:-4] + "_x47813as.txt"
    output_file = open(os.path.join(args.output_directory, filename), "x")
    output_file.write(plaintext)
    output_file.close
    input_file.close
