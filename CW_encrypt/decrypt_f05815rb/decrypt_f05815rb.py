import argparse
import glob

def decryptMorse(cipher_text):
    morseDict = {'.-': 'a', '-...': 'b', '-.-.': 'c',
    '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h',
    '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm',
    '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
    '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w',
    '-..-': 'x', '-.--': 'y', '--..': 'z'}
    
    decoded = ''

    for sequence in cipher_text.split('/'):
        for symbols in sequence.split(' '):
            if len(symbols) > 0:
                decoded += morseDict[symbols]
        decoded += ' '
    
    return decoded

my_parser = argparse.ArgumentParser()

my_parser.add_argument('input', type = str)
my_parser.add_argument('output', type = str)

args = my_parser.parse_args()

cipherText = ''

for input_file_path in glob.glob(args.input + '/*.txt'):
    with open(input_file_path, "r") as f:
        cipherText = f.readline()

    cipher, cipherText = cipherText.split(':')

    plainText = ''

    if cipher == 'Hex':
        plainText = bytes.fromhex(cipherText).decode().lower()
    elif cipher == 'Caesar Cipher(+3)':
        for symbol in cipherText.lower():
            if (symbol.isalpha()):
                if symbol in 'abc':
                    plainText += 'xyz'[ord(symbol) - 97]
                else:
                    plainText += chr(ord(symbol) - 3)
            else:
                plainText += symbol
    elif cipher == 'Morse Code':
        plainText = decryptMorse(cipherText)

    input_file = input_file_path.split('/')[-1]

    with open(f'{args.output}/{input_file[0:-4]}_f05815rb.txt', "w") as g:
        g.write(f'{plainText}')
