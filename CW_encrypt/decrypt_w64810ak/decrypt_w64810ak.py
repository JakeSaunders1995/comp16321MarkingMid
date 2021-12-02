import sys
import re
import os
import argparse

parser = argparse.ArgumentParser(description='Add the file path')
parser.add_argument('input', type=str, help="file path")
parser.add_argument('output', type=str, help='filepath')
args = parser.parse_args()


def decrypt_text(textdata):

    split_string = re.findall('...', textdata)


    #print(split_string[1])


def hex(string):
    hex_string = (string[4:])
    nospace_string = hex_string.replace(" ", "")
    print(nospace_string)
    bytes_object = bytes.fromhex(nospace_string)
    #
    decode_string = bytes_object.decode("utf-8")
    print(decode_string)
    f = open("/home/csimage/Desktop/16321_python_coursework_w64810ak/midterm/midterm_files/output_folder/output_program2/test_file1.txt", "a")
    f.write(decode_string)
    f.close()
    file_change = (os.path.splitext(args.output+filename)[0])
    old_file = os.path.join(args.output, filename)
    new_file = os.path.join(args.output, file_change+'_w64810ak.txt')
    os.rename(old_file, new_file)



alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesar_cipher(string):
    caesar_string = (string[18:])
    encrypted_message = caesar_string.strip()
    print()
    key = int(3)

    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)

            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c
    lower = (decrypted_message.lower())
    f = open(args.output+filename, 'a')
    f.write(lower)
    f.close()
    file_change = (os.path.splitext(args.output+filename)[0])
    old_file = os.path.join(args.output, filename)
    new_file = os.path.join(args.output, file_change+'_w64810ak.txt')
    os.rename(old_file, new_file)


for filename in os.listdir(args.input):
    f = open(args.input+filename)
    string = f.read()
    if string[0] == 'H':
        hex(string)
    if string[0] == 'C':
        caesar_cipher(string)
