import argparse
import os
import re
code_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
                         'h': '....',
                         'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                         'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--',
                         'x': '-..-',
                         'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                         '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-',
                         ':': '---...',
                         ',': '--..--', ';': '-.-.-.', '?': '..--..', '=': '-...-', "'": '.----.', '/': '-..-.',
                         '!': '-.-.--',
                         }
parser = argparse.ArgumentParser()
parser.add_argument('input_folder')
parser.add_argument('output_folder')
args = parser.parse_args()

inputFolder = args.input_folder
outputFolder = args.output_folder
z = os.listdir(inputFolder)

for v in z:
    os.chdir(inputFolder)
    with open(v) as files:
        message = files.read()


        message_ = ""

        abc = message
        if message[0] == 'H':
            message1 = message.replace('Hex:', '').strip().split()
            for i in range(0, len(message1)):
                k = int(message1[i], 16)
                x = chr(k)
                message_ += x.lower()

        elif message[0]=='C':
            message = message.replace('Caesar Cipher(+3):', '')
            message = str.upper(message)

            for x in message:
                if (x == ' '):
                    message_= ' '
                elif (ord(x) - ord('A') - 3 < 0):
                    message_ = chr(ord(x) - 3 + 26).lower()

                else:
                    message_ = chr(ord(x) - 3).lower()


        elif abc[0]=='M':

            hex_string = message.replace('Morse Code:','')
            message = hex_string
            lis_0 = message.replace(' ', '/').strip('/').split('//')
            lis_1 = [lis_0[i].split('/') for i in range(len(lis_0))]
            code_dict = {v: k for k, v in code_dict.items()}
            for i in range(len(lis_1)):
                for j in range(len(lis_1[i])):
                    if lis_1[i][j] in code_dict:
                        lis_1[i][j] = code_dict[lis_1[i][j]]
                lis_1[i] = ''.join(lis_1[i])

            message_ = ' '.join(lis_1).capitalize().lower()


    os.chdir(outputFolder)
    l = os.listdir(outputFolder)
    filename = str(v)
    outputName = filename[:-4] + "f38903hq.txt"
    with open(outputName,'w') as K:
        K.write(message_)
