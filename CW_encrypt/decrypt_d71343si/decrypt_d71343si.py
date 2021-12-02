import sys
import os
import string

morsecode_dictionary = { 'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ':'/'}
morsecode_dictionary_reverse = {value:key for key,value in morsecode_dictionary.items()}
alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"

input_name = sys.argv[1]
output_name = sys.argv[2]

for testfile in os.listdir(input_name):
    f = os.path.join(input_name, testfile)
    print("File:", testfile)
    input_file = open(f, 'r')
    text = input_file.read()
    print(text)
    ciphertext = []
    ciphercharacter = ""
    plaintext = ""
    count = len(text)
    for x in range(count):
        if text[x] == ":":
            ciphertext.append(text[x+1:])
    ciphertext.append(" ")
    # ciphertext = "".join(ciphertext)
    ciphertext_string = "".join(ciphertext)
    ciphertext_string = ciphertext_string.replace("\n","")
    # ciphertext_string = ciphertext[0]
    text_lower = text.lower()


    if text_lower[0] == "m":
        for character in ciphertext_string:
            if character != " ":
                y = 0
                ciphercharacter += character

            else:
                y += 1
                if y == 2:
                    plaintext = " "
                else:
                    plaintext += list(morsecode_dictionary.keys())[list(morsecode_dictionary.values()).index(ciphercharacter)]
                    ciphercharacter = ""
        plaintext = plaintext.lower()
        print(plaintext)

    if text_lower[0] == "c":
        for a in ciphertext_string:
            if a in alphabet:
                ciphertext_position = alphabet.find(a)
                plaintext_position = (ciphertext_position - 3) % 26
                plaintext_character = alphabet[plaintext_position]
                plaintext += plaintext_character
            else:
                plaintext += a
        plaintext = plaintext.lower()
        print(plaintext)

    if text_lower[0] == "h":
        plaintext = bytearray.fromhex(ciphertext_string).decode().lower()
        print(plaintext)


    output_file_name = testfile[:-4] + "_d71343si.txt"
    output_file_path = os.path.join(output_name, output_file_name)

    output_file = open(output_file_path, "w")
    output_file.write(plaintext)






   



