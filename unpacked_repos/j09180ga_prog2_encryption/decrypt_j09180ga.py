import os
import sys
decryption = ""
alphabet = list('abcdefghijklmnopqrstuvwxyz')
#https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1677-1-200910-I!!PDF-E.pdf
morsecode = {'.-': 'a', '-...': 'b', '-.-.': 'c',
             '-..': 'd', '.': 'e', '..-.': 'f',
             '--.': 'g', '....': 'h', '..': 'i',
             '.---': 'j', '-.-': 'k', '.-..': 'l',
             '--': 'm', '-.': 'n', '---': 'o',
             '.--.': 'p', '--.-': 'q', '.-.': 'r',
             '...': 's', '-': 't', '..-': 'u',
             '...-': 'v', '.--': 'w', '-..-': 'x',
             '-.--': 'y', '--..': 'z', '.----': '1',
             '..---': '2', '...--': '3', '....-': '4',
             '.....': '5', '-....': '6', '--...': '7',
             '---..': '8', '----.': '9', '-----': '0',
             "..--..": "?", "-.-.--": "!", ".-.-.-": ".", "--..--": ",",
             "-.-.-.": ";", "---...": ":", ".-.-.": "+",
             "-....-": "-", "-..-.": "/", "-...-": "=",
             ".----.": "'", "-.--.": "(", "-.--.-": ")",
             ".-...": "&", ".-..-.": "\"", "": ""}


def hex_key(ciphertext):
    plaintext = ''
    for cipherchr in ciphertext.split(":")[1].split():
        plaintext += chr((int(cipherchr, 16))).lower()
    output_file(plaintext)

def morse_key(ciphertext):
    plaintext = ''
    for cipherword in ciphertext.split(":")[1].split(' / '):
        for cipherchr in cipherword.split():
            plaintext += morsecode.get(cipherchr)
        plaintext += " "
    output_file(plaintext.rstrip())

def caesar_key(ciphertext):
    plaintext = ''
    for cipherword in ciphertext.split(":")[1].rstrip():
        for cipherchr in cipherword:
            if cipherchr == " ":
                plaintext += " "
                continue
            position = alphabet.index(cipherchr.lower())
            plaintext += alphabet[position - 3]
    plaintext += ' '
    output_file(plaintext.rstrip())

def output_file(plaintext):
    with open(outputfolder + file[0:-4] + "_j09180ga.txt", 'w') as f:
        f.write(plaintext)

inputfolder = sys.argv[1] + '/'
outputfolder = sys.argv[2] + '/'


files = os.listdir(inputfolder)
for file in files:
    myfile = inputfolder + file
    with open(myfile) as f:
        mydata = f.read()
        if (mydata.startswith("h") or mydata.startswith("H")):
            hex_key(mydata)
        elif (mydata.startswith("m") or mydata.startswith("M")):
            morse_key(mydata)
        elif (mydata.startswith("c") or mydata.startswith("C")):
            caesar_key(mydata)
