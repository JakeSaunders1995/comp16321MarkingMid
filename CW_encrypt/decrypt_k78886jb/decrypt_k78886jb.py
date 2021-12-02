import argparse
import os

inputs = argparse.ArgumentParser()
inputs.add_argument('input_path')
inputs.add_argument('output_path')

arguments = inputs.parse_args()

files = []
for file in os.listdir(arguments.input_path):
    files.append(os.path.join(arguments.input_path, file))

for input_file in files:

    f = open(input_file, 'r')
    text = f.read()
    f.close()

    i = -1
    while input_file[i] != '/':
        i -= 1
    filename = input_file[i:-4]

    i = 0
    while text[i] != ':':
        i += 1

    cipher = text[0:i]
    ciphertext = text[i+1:]
    plaintext = ''

    list = []
    temp = ''
    dec = 0

    if cipher == 'Hex':
        for i in range(0, len(ciphertext)):
            if ciphertext[i] != ' ':
                temp = temp + ciphertext[i]
            else:
                list.append(temp)
                temp = ''
        list.append(temp)

        for i in list:
            first_char = i[0]
            second_char = i[1]

            if first_char in '0123456789':
                dec = int(first_char)*16
            else:
                if first_char == 'a':
                    dec = 160
                elif first_char == 'b':
                    dec = 176
                elif first_char == 'c':
                    dec = 192
                elif first_char == 'd':
                    dec = 208
                elif first_char == 'e':
                    dec = 224
                else:
                    dec = 240

            if second_char in '0123456789':
                dec = dec + int(second_char)
            else:
                if second_char == 'a':
                    dec += 10
                elif second_char == 'b':
                    dec += 11
                elif second_char == 'c':
                    dec += 12
                elif second_char == 'd':
                    dec += 13
                elif second_char == 'e':
                    dec += 14
                else:
                    dec += 15

            plaintext = plaintext + chr(dec)
            dec = 0

    elif cipher == 'Caesar Cipher(+3)':
        for i in range(0, len(ciphertext)):
            if ciphertext[i] != ' ':
                plaintext = plaintext + chr(ord(ciphertext[i])-3)
            else:
                plaintext = plaintext + ' '
    else: #Morse code
        morse_code = {'.-': 'a',
                '-...': 'b',
                '-.-.': 'c',
                '-..': 'd',
                '.': 'e',
                '..-.': 'f',
                '--.': 'g',
                '....': 'h',
                '..': 'i',
                '.---': 'j',
                '-.-': 'k',
                '.-..': 'l',
                '--': 'm',
                '-.': 'n',
                '---': 'o',
                '.--.': 'p',
                '--.-': 'q',
                '.-.': 'r',
                '...': 's',
                '-': 't',
                '..-': 'u',
                '...-': 'v',
                '.--': 'w',
                '-..-': 'x',
                '-.--': 'y',
                '--..': 'z',
                '.----': '1',
                '..---': '2',
                '...--': '3',
                '....-': '4',
                '.....': '5',
                '-....': '6',
                '--...': '7',
                '---..': '8',
                '----.': '9',
                '-----': '0'}

        for i in range(0, len(ciphertext)):
            if ciphertext[i] != ' ':
                temp = temp + ciphertext[i]
            else:
                list.append(temp)
                temp = ''
        list.append(temp)

        for i in list:
            if i == '/':
                plaintext = plaintext + ' '
            else:
                plaintext += morse_code[i]

    output_file = arguments.output_path + '/' + filename + '_k78886jb.txt'
    plaintext = plaintext.lower()

    f = open(output_file, 'w')
    f.write(plaintext)
    f.close()
