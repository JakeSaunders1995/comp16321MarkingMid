import argparse
import os
import re

parser = argparse.ArgumentParser(
        description="Decryption program"
    )
parser.add_argument(
        "inp_folder"
    )
parser.add_argument(
        "out_folder"
    )
args = parser.parse_args()

morse_translation = {
    '/': ' ',
    '.-': 'a',
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
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9'
}

alphabet = "abcdefghijklmnopqrstuvwxyz"

if not os.path.isdir(args.out_folder):
    os.mkdir(args.out_folder)

username = "v35417sp"
for input in sorted(os.listdir(args.inp_folder)):
    name = re.match("(.*)\.txt", input).groups()[0]
    name += f"_{username}.txt"

    with open(args.inp_folder + "/" + input, 'r') as f:
        alg, ct = f.read().split(":")
        alg = alg.lower()

    pt = ''
    if alg == 'hex':
        pt = ct.replace(" ", "")
        pt = bytearray.fromhex(pt).decode('utf-8')
    elif "morse code" in alg:
        ct = ct.split(' ') 
        pt = ''.join([morse_translation[c] for c in ct]) 
    elif "caesar" in alg:
        shift = re.match("caesar cipher\((.*)\)", alg).groups()[0]
        shift = int(shift)

        for c in ct:
            if c == ' ':
                pt += ' '
            else:
                pt += alphabet[ (alphabet.index(c) - shift) % len(alphabet) ]

    with open(args.out_folder + '/' + name, 'w') as f:
        f.write(pt.lower())
