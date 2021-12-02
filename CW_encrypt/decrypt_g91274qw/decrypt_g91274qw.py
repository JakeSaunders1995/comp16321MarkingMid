import argparse
import sys
import os

code_dict = {'.-...': '&', '--..--': ',', '....-': '4', '.....': '5',
             '-...': 'B', '-..-': 'X', '.-.': 'R',
             '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F',
             '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?',
             '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=',
             '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N',
             '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
             '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G',
             '--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':',
             '-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0',
             '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3'
             }

username = 'g91274qw'


def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    args = parser.parse_args()
    return args.input, args.output


def decode(input_file_path, output_file_path):
    try:
        with open(input_file_path) as f:
            line = f.readline().strip()
            algorithm = line.split(':')[0]
            ciphertext = line.split(':')[1]

    except Exception as e:
        print('Read file failed!')
        sys.exit(0)
    if algorithm == 'Hex':
        s = bytes.fromhex(ciphertext.replace(' ', '')).decode()
    elif algorithm == 'Morse Code':
        s = morse_decode(ciphertext).lower()
    else:
        s = caesar_decrypt(ciphertext, 3)
    try:
        with open(output_file_path, 'w') as f:
            f.write('{}'.format(s))
    except Exception as e:
        print("Write file failed!" + e)


def caesar_decrypt(ciphertext, shift):
    space = []

    ciphertext = ciphertext.split()

    sentence = []

    for word in ciphertext:
        cipher_ords = [ord(x) for x in word]
        plaintext_ords = [o - shift for o in cipher_ords]
        plaintext_chars = [chr(i) for i in plaintext_ords]
        plaintext = ''.join(plaintext_chars)
        sentence.append(plaintext)

    sentence = ' '.join(sentence)
    return sentence


def morse_decode(morseCode):
    information = ''
    consequence = []
    for stuff in morseCode.split(' '):
        consequence.append(code_dict.get(stuff))
    for g in consequence:
        if g:
            information += g
        else:
            information += ' '
    return information


if __name__ == '__main__':

    input, output = parse_args()
    file_list = os.listdir(input)
    for file in file_list:
        input_file = os.path.join(input, file)
        output_folder_path = os.path.abspath(output)
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)
        output_file = os.path.join(output_folder_path,
                                   os.path.splitext(file)[0] + '_' + username + '.txt')
        decode(input_file, output_file)
