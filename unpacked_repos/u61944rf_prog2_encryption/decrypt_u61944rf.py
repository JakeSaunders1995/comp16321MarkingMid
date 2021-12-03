import os
import argparse
import re

INPUT_PATH = "midterm_files/Example_inputs/Example_inputs_program2"
OUTPUT_PATH = "midterm_files/Example_outputs/Example_outputs_program2"
USER_NAME = 'u61944rf'



MORSE_CODE_DICT = { 'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ':'/'}


def mose_dec(message, *args):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2 :
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
    return decipher

def hex_dec(message, *args):
    return "".join([chr(i) for i in [int(b, 16) for b in message.split(' ')]])


def cipher_dec(message, number=3):
    str_list = []
    for a in message:
        if a != ' ':
            str_list.append(chr(ord(a)-number))
        else:
            str_list.append(' ')
    return "".join(str_list)
    

class Decrypt():
    def __init__(self) -> None:
        self.alg_set = {'Hex':hex_dec, 'Caesar Cipher':cipher_dec, 'Morse Code':mose_dec}
    
    def __call__(self, input_f, output_f): #read str
        with open(input_f) as f:
            all_str = f.read()

        algorithm = ''
        for idx, letter in enumerate(all_str):
            if letter == ':':
                start_idx = idx+1
                secret_num = None
                break
            elif letter == '(':
                start_idx = idx+5
                secret_num = int(all_str[idx+2])
                break
            algorithm += letter
        message = all_str[start_idx:]
        decode = self.alg_set[algorithm](message, secret_num)
        decode = decode.lower()
        
        with open(output_f, 'w') as f:
            f.write(decode)

                                 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', default=INPUT_PATH)
    parser.add_argument('output', default=OUTPUT_PATH)

    opt = parser.parse_args()

    #run calculate
    algo = Decrypt()
    for file_name in os.listdir(opt.input):
        input_file = opt.input + '/' + file_name
        output_file = opt.output + '/' + file_name[:-4]+'_'+USER_NAME+'.txt'
        algo(input_file, output_file)
    

