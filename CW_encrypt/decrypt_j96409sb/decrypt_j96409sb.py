import argparse
from os import listdir
from os.path import isfile, join

parser = argparse.ArgumentParser(description="Decrypt a message using the provided algorithm")
parser.add_argument("input", metavar="I", type=str,
                    help="Input file path", action="store")
parser.add_argument("output", metavar="O", type=str,
                    help="Output file path", action="store")


def read_file(file_path):
    '''Read the file given by the parser and return the text'''
    file = open(file_path, "r")
    file_text = file.read()
    file.close()
    return file_text

def write_file(file_path, filename, text):
    file = open(f"{file_path}/{filename}", "w")
    file.write(text)
    file.close()

def format_input(text):
    input_list = text.split(":")
    return input_list[0].lower(), input_list[1]
    
def hex_to_eng(ciphertext):
    plaintext = bytearray.fromhex(ciphertext).decode(encoding="Latin1")
    return plaintext

def bin_to_eng(ciphertext):
    ciphertext = ciphertext.replace(" ","")
    characters = [ciphertext[x:x+8] for x in range(0, len(ciphertext), 8)]
    plaintext = [chr(int(char,2)) for char in characters]
    return "".join(plaintext)

def morse_to_eng(ciphertext):
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
    plaintext = ""
    cipher_word_list = ciphertext.split("/")
    for morse_word in cipher_word_list:
        for morse_char in morse_word.split(" "):
            for key, value in MORSE_CODE_DICT.items():
                if value == morse_char:
                    plaintext += key
                    break
        plaintext += " "
    return plaintext[:-1]
    
def caesar_to_eng(ciphertext):
    ciphertext = ciphertext.lower()
    plaintext = ""
    for char in ciphertext:
        plaintext += shift_letter(char)
    return plaintext

def shift_letter(character):
    if not character.isalpha():
        return character
    elif ord(character) - 3 < 97:
        return chr(ord(character) - 23)
    else:
        return chr(ord(character) - 3)
    


def decrypt(algorithm, text):
    algorithm = algorithm.lower()
    if algorithm == 'hex':
        return hex_to_eng(text)
    elif algorithm == 'bin':
        return bin_to_eng(text)
    elif algorithm == 'morse code':
        return morse_to_eng(text)
    elif algorithm == 'caesar cipher(+3)':
        return caesar_to_eng(text)


if __name__ == '__main__':
    args = parser.parse_args()
    input_path = args.input
    output_path = args.output
    files = [file for file in listdir(input_path) if isfile(join(input_path, file))]
    filecount = 0
    for file in files:
        filecount += 1
        input_text = read_file(f"{input_path}/{file}")
        algo, ciphertext = format_input(input_text)
        plaintext = decrypt(algo, ciphertext)
        plaintext = plaintext.lower()
        output_file = write_file(output_path,f"test_file{filecount}_j96409sb.txt", plaintext)
