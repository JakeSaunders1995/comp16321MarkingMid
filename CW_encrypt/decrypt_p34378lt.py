import sys
import os

inFolder = sys.argv[1]
outFolder = sys.argv[2]

for file in os.listdir(inFolder):
    if file.endswith('.txt'):

        cipher_file = open(inFolder + '/' + file, 'rt')
        cipher_text = (cipher_file.read()).strip()

        method = (cipher_text[0]).lower()

        reach_colon = False
        plain_text = ''
        if method == 'm':
            morse = {'.-': 'a', '-...': 'b', '-.-.': 'c',
                     '-..': 'd', '.': 'e', '..-.': 'f',
                     '--.': 'g', '....': 'h', '..': 'i',
                     '.---': 'j', '-.-': 'k', '.-..': 'l',
                     '--': 'm', '-.': 'n', '---': 'o',
                     '.--.': 'p', '--.-': 'q', '.-.': 'r',
                     '...': 's', '-': 't', '..-': 'u',
                     '...-': 'v', '.--': 'w', '-..-': 'x',
                     '-.--': 'y', '--..': 'z', '-----': '0',
                     '.----': '1', '..---': '2', '...--': '3',
                     '....-': '4', '.....': '5', '-....': '6',
                     '--...': '7', '---..': '8', '----.': '9',
                     '.-.-.-': '.', '--..--': ',', '..--..': '?', '-.-.--': '!', '---...': ':', '-.-.-.': ';',
                     '-....-': '-', '-.--.': '(', '-.--.-': ')', '.----.': "'", '.-..-.': '"'}
            morse_char = ''
            for char in cipher_text:
                if not reach_colon:
                    if char == ':':
                        reach_colon = True
                        continue
                    else:
                        continue
                if char == '/':
                    plain_text += ' '
                elif char == ' ' and morse_char != '':
                    plain_text += morse[morse_char]
                    morse_char = ''
                elif char != ' ':
                    morse_char += char
            plain_text += morse[morse_char]


        elif method == 'c':
            alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                        "t", "u",
                        "v", "w", "x", "y", "z"]
            caesar3_alph = ["d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                            "v", "w",
                            "x", "y", "z", "a", "b", "c"]
            for char in cipher_text:
                if not reach_colon:
                    if char == ':':
                        reach_colon = True
                        continue
                    else:
                        continue
                if char == ' ':
                    plain_text += ' '
                else:
                    plain_text += alphabet[caesar3_alph.index(char)]

        elif method == 'h':
            current_char = ''
            for char in cipher_text:
                if not reach_colon:
                    if char == ':':
                        reach_colon = True
                        continue
                    else:
                        continue
                if char != ' ':
                    current_char += char
                else:
                    byte_array = bytearray.fromhex(current_char)
                    plain_text += byte_array.decode()
                    current_char = ''
            byte_array = bytearray.fromhex(current_char)
            plain_text += byte_array.decode()
            current_char = ''

        plain_text = plain_text.lower()

        outputName = file[:-4] + "_p34378lt"
        try:
            new_file = open(outFolder + '/' + (outputName + '.txt'), 'x')
        except:
            new_file = open(outFolder + '/' + (outputName + '.txt'), 'w')

        new_file.write(plain_text)

        cipher_file.close()
        new_file.close()
