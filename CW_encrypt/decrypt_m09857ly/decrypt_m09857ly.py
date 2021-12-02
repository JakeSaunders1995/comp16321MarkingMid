from argparse import ArgumentParser
import os

parser = ArgumentParser(description="Take in files")
parser.add_argument("input", help="Take in input folder.")
parser.add_argument("output", help="Take in output folder.")
args = parser.parse_args()
folders = args

def decrypt(filename):
    f = open(f'{folders.input}/{filename}', "r")
    line = f.read().split(':', 1)
    text = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    if line[0] == "Hex":
        text = bytes.fromhex(line[1]).decode('utf-8').lower()
    elif line[0] == "Caesar Cipher(+3)":
        shift = 3
        line[1] = line[1].lower()
        for char in line[1]:
            if char not in alphabet:
                if char in numbers or char == " ":
                    text += char
            else:
                text += alphabet[alphabet.find(char) - shift]
    elif line[0] == "Morse Code":
        symbols_dict = { '.-':'a', '-...':'b',
                        '-.-.':'c', '-..':'d', '.':'e',
                        '..-.':'f', '--.':'g', '....':'h',
                        '..':'i', '.---':'j', '-.-':'k',
                        '.-..':'l', '--':'m', '-.':'n',
                        '---':'o', '.--.':'p', '--.-':'q',
                        '.-.':'r', '...':'s', '-':'t',
                        '..-':'u', '...-':'v', '.--':'w',
                        '-..-':'x', '-.--':'y', '--..':'z',
                        '-----':'0', '.----':'1', '..---':'2', 
                        '...--':'3', '....-':'4', '.....':'5', 
                        '-....':'6', '--...':'7', '---..':'8', 
                        '----.':'9'}
        codes = line[1].split()
        for code in codes:
            if code == '/':
                text += ' '
            elif code in symbols_dict:
                text += symbols_dict[code]
        
    with open(f'{folders.output}/{filename[:-4]}_m09857ly.txt', "w") as output:
        output.write(text)
        output.close()

try:
    os.mkdir(folders.output)
except:
    pass

for file in os.listdir(folders.input):
    decrypt(file)