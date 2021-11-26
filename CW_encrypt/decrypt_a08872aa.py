import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input_folder")
parser.add_argument("output_folder")
args = parser.parse_args()
input_folder_name = args.input_folder
output_folder_name = args.output_folder

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
MORSE_DICT = {
    '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '....' : 'h', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' '
}

files_to_loop = os.listdir(input_folder_name)

for file in files_to_loop:
    input_file_name = file
    output_file_name = "{}_a08872aa.txt".format(input_file_name.replace(".txt",""))
    if "/" in input_folder_name:
        input_file = open("{}/{}".format(input_folder_name, input_file_name), "r")
    else:
        input_file = open("{}\{}".format(input_folder_name, input_file_name), "r")

    plaintext = ""
    ciphertext = input_file.read()

    if ciphertext[0:3] == "Hex":
        ciphertext = ciphertext[4:]
        plaintext = bytearray.fromhex(ciphertext).decode() 
    elif ciphertext[0] == "C":
        ciphertext = ciphertext[18:]
        for letter in ciphertext:
            if letter != " " and letter != "":
                try:
                    index = ALPHABET.index(letter)
                    new_letter = ALPHABET[index-3]
                    plaintext = plaintext + new_letter
                except:
                    pass
            else:
                plaintext = plaintext + " "
    else:
        ciphertext = ciphertext[11:]
        split_ciphertext = ciphertext.split(" ")
        for char in split_ciphertext:
            plaintext = plaintext + MORSE_DICT[char]
    
    if "/" in input_folder_name:
        output_file = open("{}/{}".format(output_folder_name, output_file_name), "w")
    else:
        output_file = open("{}\{}".format(output_folder_name, output_file_name), "w")
    output_file.write(plaintext.lower())
    output_file.close()

