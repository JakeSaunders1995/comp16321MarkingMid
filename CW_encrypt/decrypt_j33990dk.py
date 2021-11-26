import re
import sys

def hex():
    global line
    global plaintext
    cipherText = line[4:]
    # print(cipherText)

    hex_string = bytes.fromhex(cipherText)
    plaintext = hex_string.decode("ascii")
    
    plaintext = plaintext.lower()
    # print(plaintext)

def caesar():
    global line
    global plaintext
    cipherText = line[18:]
    # print(cipherText)

    plaintext = ""

    for i in range(len(cipherText)):
        char = cipherText[i]
        if (char.isspace()):
            plaintext += " "
        else:
            plaintext += chr((ord(char) -3 -97) % 26 + 97)

    plaintext = plaintext.lower()
    # print(plaintext)

def morsecode():
    global line
    global plaintext
    cipherText = line[11:]
    # print(cipherText)

    dic = {'.-': 'A',
           '-...': 'B',
           '-.-.': 'C',
           '-..': 'D',
           '.': 'E',
           '..-.': 'F',
           '--.': 'G',
           '....': 'H',
           '..': 'I',
           '.---': 'J',
           '-.-': 'K',
           '.-..': 'L',
           '--': 'M',
           '-.': 'N',
           '---': 'O',
           '.--.': 'P',
           '--.-': 'Q',
           '.-.': 'R',
           '...': 'S',
           '-': 'T',
           '..-': 'U',
           '...-': 'V',
           '.--': 'W',
           '-..-': 'X',
           '-.--': 'Y',
           '--..': 'Z'}

    plaintext = ""

    for i in cipherText.split('/'):
        for j in i.split():
            plaintext += dic[j]
        plaintext += ' '

    plaintext = plaintext.lower()
    # print(plaintext)


# read file
file = open(sys.argv[1], "r")
line = file.readlines()
for line in line:
    # print(line)
    if line.lower().startswith("h"):
        hex()
    elif line.lower().startswith("c"):
        caesar()
    elif line.lower().startswith("m"):
        morsecode()

# create output file
newFile = open(sys.argv[2], "w")

newFile.write(plaintext)

newFile.close()

file.close()
