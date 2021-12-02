import os
import re
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument('output')
args = parser.parse_args()
input_folder = args.input
output_folder = args.output
directory = input_folder
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        f = open(f, 'r')
        encryption = f.read()
        f.close()
        hexa = re.search("Hex:", encryption)
        caesar = re.search('Caesar Cipher\\(\\+3\\):', encryption)
        morse = re.search('Morse Code:', encryption)
        morse_code = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '.---': 'j', '-.-': 'k', '.-..': 'l',
                      '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '/': ' ', '.---': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '----': '0', '.-.-.-': '.', '--..--': ',', '---...': ':', '..--..': '?', '.----.': '\'', '-....-': '-', '-..-.': '/', '-.--.-': ')', '.-..-.': '"', '-.--.': '('}
        caesar_code = {'a': 'x', 'b': 'y', 'c': 'z', 'd': 'a', 'e': 'b', 'f': 'c', 'g': 'd', 'h': 'e', 'i': 'f','j': 'g', 'k': 'h', 'l': 'i',
                      'm': 'j', 'n': 'k', 'o': 'l', 'p': 'm', 'q': 'n', 'r': 'o', 's': 'p', 't': 'q', 'u': 'r', 'v': 's', 'w': 't', 'x': 'u', 'y': 'v', 'z': 'w'}
        decryption = ''
        decrypted_words = []
        if(hexa):
            encryption = re.split("Hex:", encryption)
            word_list = encryption[1]
            decry = bytearray.fromhex(word_list).decode()
            decryption = decry.lower()
        elif(caesar):
            encryption = re.split("Caesar Cipher\\(\\+3\\):", encryption)
            word_list = encryption[1].split()
            for word in word_list:
                for i in word.lower():
                    if i in caesar_code:
                        decryption += caesar_code[i].lower()
                decryption += " "
        elif(morse):

            encryption = re.split("Morse Code:", encryption)
            word_list = encryption[1].split()
            for word in word_list:
            
                if word in morse_code:
                    decryption += morse_code[word]

        else:
            print("Could not identify encryption type.")

       
        filename1 = filename[0:(len(filename)-4)]
        output_path = f'{output_folder}/{filename1}_y42270sg.txt'
        g = open(output_path, 'w')
        g.write(decryption)
        g.close()
