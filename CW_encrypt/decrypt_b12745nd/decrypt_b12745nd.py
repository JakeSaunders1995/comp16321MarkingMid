import argparse
import os


def morse_decrypt(morse):
    final_string=""
    morse_code_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
                        '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', 
                        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                        '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2',
                        '...--': '3', '....-': '4', '.....': '5', '-....': '6',
                        '--...': '7', '---..': '8', '----.': '9', '-----': '0', 
                        '--..--': ', ', '.-.-.-': '.', '..--..': '?', 
                        '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')', '/': ' '}
    for i in morse.split():
        final_string+=morse_code_dict[i]
    return(final_string.lower())


def caesar_decrypt(caesar):
    caesar=caesar.lower()
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    finalstring = ''
    for i in caesar:
        if i not in alphabets:
            finalstring += i
        else:
            finalstring += alphabets[alphabets.find(i)-3]
    return (finalstring)


def hex_decrypt(hexa):
    finalstring = ''
    for i in hexa.split():
        finalstring+=chr(int(i,16))
    return finalstring.lower()



parser = argparse.ArgumentParser()
parser.add_argument('inputfile', type=str)
parser.add_argument('outputfile', type=str)
args = parser.parse_args()


input_folder = args.inputfile+'/'
output_folder = args.outputfile+'/'

for filename in os.listdir(input_folder):

    infile_address = input_folder+filename
    outfile_address = output_folder+filename[:-4]+'_b12745nd.txt'

    if '.txt' in filename:
        infile_handle = open(infile_address)
        outfile_handle = open(outfile_address, 'w')
        content=infile_handle.read().split(':')
        if content[0]in['Hex','hex']:
            decrypted_string=hex_decrypt(content[1])
        elif content[0] in ['Caesar Cipher(+3)', 'Caesar Cipher']:
            decrypted_string=caesar_decrypt(content[1])
        elif content[0] in ['Morse Code','morse code']:
            decrypted_string=morse_decrypt(content[1])
        outfile_handle.write(decrypted_string)
        
        
