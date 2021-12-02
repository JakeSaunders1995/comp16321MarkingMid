import os
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('input_path')
parser.add_argument('output_path')
args = parser.parse_args()
a = os.listdir(args.input_path)
b = sorted(a)
for i in range(len(os.listdir(args.input_path))):
    with open(args.input_path + "/" + b[i], "r") as f:
        file = f.read()

    algorithm, cipherText = file.split(":")


    def morse_code(code: str) -> str:
        morse_map = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                     '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                     '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                     '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
                     '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '/': ' '}
        words = []
        for w in code.split(" "):
            words.append(morse_map[w])
        return "".join(words).lower()


    def caesar(code: str) -> str:
        l = []
        for c in code:
            if c.isalpha():
               
                num = ord(c)-3
                if num < 97:
                    num += 26
                    l.append(chr(num))
                else:
                    l.append(chr(num))
            else:
                l.append(c)
        return "".join(l).lower()


    def hexadecimal(code: str) -> str:
        return "".join([chr(int(c, 16)) for c in code.split(" ")]).lower()


    decrypted = ""
    if algorithm == "Morse Code":
        decrypted = morse_code(cipherText)
    elif algorithm == "Caesar Cipher(+3)":
        decrypted = caesar(cipherText)
    elif algorithm == "Hex":
        decrypted = hexadecimal(cipherText)

    with open(args.output_path+"/test_file"+str(int(i)+1)+"_m60493kw.txt", "w") as f:
        f.write(decrypted)
