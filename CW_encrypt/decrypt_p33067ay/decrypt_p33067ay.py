import argparse
import re
import os

parser = argparse.ArgumentParser(description="Encryption to Strings")
parser.add_argument("encryptfile", type=str, help="Input for the encrypts")
parser.add_argument("stringfile", type=str, help="output for strings")
args = parser.parse_args()

encryptfile = args.encryptfile
stringfile = args.stringfile

morse_dictionary = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....',
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

for y in os.listdir(encryptfile):
    store_directory = os.path.join(encryptfile, y)
    file = open(store_directory, "r")

    if stringfile[-1] != "/":
        outputfile = stringfile + "/" + y.split(".txt")[0] + "_p33067ay"
        directory_create = os.path.dirname(outputfile)

    else:
        outputfile = stringfile + y.split(".txt")[0] + "_p33067ay"
        directory_create = os.path.dirname(outputfile)

    if not os.path.exists(stringfile):
        os.makedirs(stringfile)

    inputstring = file.readline()

    stringsplit = re.split(":", inputstring)

    if stringsplit[0] == "Hex":
        hex_bytes = bytes.fromhex(stringsplit[1])
        hex_ascii = hex_bytes.decode("ASCII")

        final = open(outputfile, "w")
        final.write(hex_ascii.lower())

    elif stringsplit[0] == "Caesar Cipher(+3)":
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for x in range(len(stringsplit[1])):
            if stringsplit[1][x] in alphabet:
                new_position = (alphabet.find(stringsplit[1][x]) - 3) % 26
                character = alphabet[new_position]
                add_file = open(outputfile, "a")
                add_file.write(str(character))


            else:
                add_file = open(outputfile, "a")
                add_file.write(" ")


    elif stringsplit[0] == "Morse Code":

        morse_split = stringsplit[1].split(" ")
        morse_len = len(morse_split)
        keys = list(morse_dictionary.keys())
        values = list(morse_dictionary.values())


        for x in range(morse_len):
                if morse_split[x] != "/":
                    morse_string = (keys[list(values).index(morse_split[x])])
                    final = open(outputfile, "a")
                    final.write(morse_string.lower())

                elif morse_split[x] == "/":
                    final = open(outputfile, "a")
                    final.write(" ")

                else:
                    continue
















































