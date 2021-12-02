import argparse

import os



parser = argparse.ArgumentParser()

parser.add_argument('input_file_path')

parser.add_argument('output_file_path')



config = parser.parse_args()





def deal(input_file, output_file):

    with open(input_file) as f:

        data = f.read().strip().split(':')

        a = data[0]

        if a == 'Morse Code':

            c = data[1].split(' ')

            text = morseCode(c)



        if a == 'Hex':

            c = data[1].split(' ')

            text = hexadecimal(c)



        if a == 'Caesar Cipher(+3)':

            c = data[1].split(' ')

            text = caesar3(c)



    with open(output_file, 'w+') as f:

        f.write(text)





def morseCode(ciphertext):

    morse = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..",



                   "e": ".", "f": "..-.", "g": "--.",



                   "h": "....", "i": "..", "j": ".---", "k": "-.-",



                   "l": ".-..", "m": "--", "n": "-.",



                   "o": "---", "p": ".--.", "q": "--.-",



                   "r": ".-.", "s": "...", "t": "-",



                   "u": "..-", "v": "...-", "w": ".--",



                   "x": "-..-", "y": "-.--", "z": "--..",

                   ' ': '/'}

    morse_decode = dict((value,key) for key,value in morse.items())

    text = ''

    for letter in ciphertext:

        if letter in morse_decode:

            text += morse_decode[letter]

        else:

            text += letter

    return text





def hexadecimal(ciphertext):

    text = ''

    for letter in ciphertext:

        text += chr(int(letter,16))

    return text





def caesar3(ciphertext):

    text = ''

    for letter in ciphertext:

        word = ''

        for w in letter:

            if w == "a":

                w = "{"

            if w == "b":

                w = "|"

            if w == "c":

                w = "}"

            word += chr(ord(w)-3)

        word += ' '

        text += word

    return text







files_name = os.listdir(config.input_file_path)

out_name = [f.split('.')[0]+'_k74082yd'+'.txt' for f in files_name]

for i,f in enumerate(files_name):

    deal(config.input_file_path + '/' + f, config.output_file_path + '/' + out_name[i])