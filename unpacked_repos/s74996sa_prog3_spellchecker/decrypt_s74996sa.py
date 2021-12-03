import sys
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))
parser.add_argument('outfile', type=argparse.FileType('w'))
agp = parser.parse_args()
list = []
numbers = ['1','2','3','4','5','6','7','8','9','0']

morse_code = { '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---' :'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '--..--': ',', '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')', '/': ' '
}



def cipher():
    plaintextPosition=0
    while (plaintextPosition < len(list[0])):
        decryption = ""
        if list[0][plaintextPosition] == ' ':
            decryption += ' '
        plaintextChar = list[0][plaintextPosition]
        ASCIIValue = ord(plaintextChar)
        ASCIIValue -=3
        decryption = decryption + chr(ASCIIValue)
        plaintextPosition +=1
        agp.outfile.write(decryption)

def hex():
    decryption = bytes.fromhex(list[0])
    decryption = decryption.decode('ascii')
    agp.outfile.write(decryption)

for line in agp.file:
    list.append(line)

if list[0][0] in numbers:
    hex()
elif list[0][0] == '.' or list[0][0] == '-':
    value = list[0]
    code = value.split()
    for element in range (0, len(code)):
        agp.outfile.write(morse_code.get(code[element]))
else:
    cipher()

