import argparse
import re
import os
parser = argparse.ArgumentParser()
parser.add_argument("input_filepath", help="input file path")
parser.add_argument("output_filepath", help="output file path")
args = parser.parse_args()

args.input_filepath = os.path.abspath(args.input_filepath)
args.output_filepath = os.path.abspath(args.output_filepath)

for file_name in os.listdir(args.input_filepath):
    os.chdir(args.input_filepath)
    with open(os.path.join(os.getcwd(), file_name), 'r') as f:
        ciphertext = ""
        ciphertext1 = open((os.path.join(os.getcwd(), file_name)), "r")
        for line in ciphertext1:
            line = line.rstrip()
            ciphertext += line
        temp = ""
        for i in ciphertext:
            temp += i
        if temp[0] == "H" or temp[0] == "h":
            step = 2
            sentence = ''
            a = [temp[i:i+step] for i in range(4, len(temp), 3)]
            for i in range(0, len(a)):
                ad = int(a[i], 16)
                sentence += chr(ad)
                sentence = sentence.lower()

        elif temp[0] == "C" or temp[0] == "c":
            
            sentence = ''
            punc = '''!()-[]{};:'",<>./?_'''
            for i in range(18, len(temp)):
                if temp[i] == " ":
                    sentence += " "
                elif temp[i] in punc:
                    sentence += temp[i]
                else:
                    asciiofword = ord(temp[i])
                    if asciiofword < 100:
                        asciiofword = asciiofword + 26 - 3
                        sentence += chr(asciiofword)
                    else:
                        sentence += chr(asciiofword-3)
                   

        elif temp[0] == "M" or temp[0] == "m":
            binary = ''
            binary_in_array = []
            for i in range(11, len(temp)):
                if temp[i] == ".":
                    binary += "0"
                elif temp[i] == "-":
                    binary += "1"
                elif temp[i] == "/":
                    binary += "/"
                else:
                    binary += " "

            binary = re.split(r'( )', binary)
            code = {'01': 'A', '1000': 'B', '1010': 'C', '100': 'D', '0': 'E', '0010': 'F', '110': 'G', '0000': 'H',
                    '00': 'I', '0111': 'J',
                    '101': 'K', '0100': 'L', '11': 'M', '10': 'N', '111': 'O',
                    '0110': 'P', '1101': 'Q', '010': 'R', '000': 'S', '1': 'T', '001': 'U', '0001': 'V', '011': 'W',
                    '1001': 'X', '1011': 'Y', '1100': 'Z', '11111': '0', '01111': '1',
                    '00111': '2', '00011': '3', '00001': '4', '00000': '5', '10000': '6', '11000': '7',
                    '11100': '8', '11110': '9', '011111': ".", "101111": "?", "010000": "!", "100000": ",",
                    "011110": ":", "100001": ";", "01110": "-", "011000": "[", "100111": "]", "00110": "{",
                    "11001": "}", "111000": "(", "000111": ")", "001000": "'", "000110": '"', "0011": " "
                    }
            sentence = ''
            for element in binary:
                if element in code.keys():
                    sentence += code[element].lower()
                elif element == "/":
                    sentence += " "

    os.chdir(args.output_filepath)
    file_name = file_name[:-4] + "_t17981qx.txt"
    with open(file_name, 'w') as d:
        d.write(str(sentence))

