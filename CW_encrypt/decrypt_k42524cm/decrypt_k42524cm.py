import os, re, argparse

from pathlib import Path
DIR = Path(__file__).parent.absolute()
os.chdir(DIR)

parser = argparse.ArgumentParser()
parser.add_argument("input_folder", help="The folder that contains the input files for the program")
parser.add_argument("output_folder", help="The folder that will contain the output files for the program")
args = parser.parse_args()
# python3 decrypt_k42524cm.py ../Example_inputs/Example_inputs_program2 ../Example_outputs/Example_outputs_program2

hexample = 'Hex:53 6f 6c 76 69 6e 67 20 68 65 78 20 69 73 20 76 65 72 79 20 65 61 73 79 20 69 6e 20 70 79 74 68 6f 6e'
# solving hex is very easy in python
caesarChan = 'Caesar Cipher(+3):exw fdhvdu lv d olwwoh pruh gliilfxow defghijklmnopqrstuvwxyzabc'
# but caesar is a little more difficult
morseExample = 'Morse Code:.... --- .-- . ...- . .-. / ... --- .-.. ...- .. -. --. / -- --- .-. ... . / -.-. --- -.. . / -- .- -.-- / -... . / - .... . / -- --- ... - / -.. .. ..-. ..-. .. -.-. ..- .-.. -'
# however solving morse code may be the most difficult

mcVals = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    ".-.-.-": ".",
    "--..--": ",",
    "..--..": "?",
    ".----.": "'",
    "-.-.--": "!",
    "-.--.": "(",
    "-.--.-": ")",
    "---...": ":",
    "-.-.-.": ";",
    "-....-": "-",
    ".-..-.": '"',
    "/": " ",
}

def Hex(message):
    message = message.replace(' ','')
    message = bytearray.fromhex(message).decode().lower()
    return message

def Caesar(message):
    message = message.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    mess = ''
    for letter in message:
        if letter in alpha:
            mess += alpha[alpha.index(letter)-3]
        else:
            mess += letter
    return mess

def Morse(message):
    message = message.split(' ')
    output = ''
    for char in message:
        output += mcVals[char]
    return output

def Decipher(message):
    message = message.split(':', 1)
    ciphers = {
        'Hex': Hex,
        'Caesar Cipher(+3)': Caesar,
        'Morse Code': Morse
    }
    return ciphers[message[0]](message[1])

def write(input_file, output_file):
    f = open(input_file, 'r')
    message = f.read()
    f.close()

    message = Decipher(message)

    f = open(output_file, 'w')
    f.write(message)
    f.close()

for file in os.listdir(args.input_folder):
    output_file = re.sub('\.txt$', '', file)
    file = f'{args.input_folder}/{file}'
    output_file = f'{args.output_folder}/{output_file}_k42524cm.txt'
    write(file, output_file)


# .?!,:;–-(){}[]'"…

'''
1. Be able to run using command line arguments in the form of:
• python3 decrypt [username].py [input file path] [output file path]
• where [username] is your university 8 digit identifier that normally consists of an alpha
character, followed by five digits and ends with two alpha characters.
2. Read in a .txt file containing a single cipher-text (the encrypted string) in the form of:
• binary:01010101
• (algorithm):(ciphertext)
3. Determine which encryption method is used to encrypt the string (the cipher-text):
• morseCode
• caesar +3
• hexadecimal
4. Decrypt the cipher-text to produce the original decrypted plaintext (a sentence written in English):
• Including spaces, symbols and numbers
• With no upper case letters
5. Output to a .txt file to the [output file path] containing only the decrypted sentence:
• “encryption is fun!”
'''
