import os, glob, argparse
from pathlib import Path
morse_code = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ': '/', '!':'..--.', ':':'---...',
                    ';':'-.-.-.', '\'':'.----.', '\"':'.-..-.'}


parser = argparse.ArgumentParser()
parser.add_argument('folderin', help="input folderpath")
parser.add_argument('folderout', help="output folderpath")
args = parser.parse_args()
pathin = args.folderin
pathout = args.folderout
for filename in glob.glob(os.path.join(pathin, '*.txt')):
    with open(os.path.join(os.getcwd(), filename)) as f:
        namein = Path(filename).stem
        nameout = namein + "_j80841pg.txt"
        completeName = os.path.join(pathout, nameout)

        filein = open(filename)
        fileout = open(completeName, "w")
        text = filein.read()
        type = text.split(":")[0]
        text = text.split(":")[1]
        decrypted = ""
        type = type.lower()
        if type == "hex" or type == "hexadecimal":
            bytes_object = bytes.fromhex(text)
            ascii_string = bytes_object.decode("ASCII")
            decrypted = ascii_string.lower()
        elif type == "caesar cipher(+3)" or type == "caesar" or type == "caesar +3" or type == "caesar cipher":
            newtext = text.split()
            for i in newtext:
                ciphertext = i
                plaintext = ""
                ciphertextPosition = 0
                while (ciphertextPosition < len(ciphertext)):
                    ciphertextChar = ciphertext[ciphertextPosition]
                    ASCIIValue = ord(ciphertextChar)-3
                    plaintext = plaintext + chr(ASCIIValue)
                    ciphertextPosition += 1
                decrypted += plaintext.lower() + ' '
        elif type == "morse code" or type == "morse":
            newtext = text.split()
            for i in newtext:
                for j in morse_code:
                    if i == morse_code[j]:
                        decrypted += j
            decrypted = decrypted.lower()
        fileout.write(decrypted)
        filein.close()
        fileout.close()
