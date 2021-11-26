import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input", help="Input file path")
parser.add_argument("output", help="Output file path")
args = parser.parse_args()
files = []
for file in os.listdir(args.input):
    if file.endswith(".txt"):
        files.append(file)
for x in files:
    with open(os.path.join(args.input, x)) as file1:
        text = file1.readline().split(":")
    result = ""
    if text[0] == "Hex":
        cypher = text[1].split(" ")
        for i in cypher:
            result += chr(int(i, 16))
    elif text[0] == "Caesar Cipher(+3)":
        for i in text[1]:
            if i.isupper():
                result += chr((ord(i) - 68) % 26 + 97)
            elif i.islower():
                result += chr((ord(i) - 100) % 26 + 97)
            else:
                result += i
    elif text[0] == "Morse Code":
        cypher = text[1].split(" ")
        morse = {"/": " ", ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z", "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9", ".-...": "&", ".----.": '"', ".--.-.": "@", "-.--.-": ")", "-.--.": "(", "---...": ":", "--..--": ",", "-...-": "=", "-.-.--": "!", ".-.-.-": ".", "-....-": "-", ".-.-.": "+", ".-..-.": '"', "..--..": "?", "-..-.": "/"}
        for i in cypher:
            result += morse[i]
    with open(os.path.join(args.output, f"{x[:-4]}_w27888ms.txt"), "w") as file2:
        file2.write(result)
