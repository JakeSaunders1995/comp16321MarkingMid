import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('input', type=str)
parser.add_argument('output', type=str)
args = parser.parse_args()

morse_dictionary = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
'.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
'..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
'....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '--..--': ', ', '.-.-.-': '.', '..--..': '?',
'-.-.--': '!','---...':':','-.-.-.':';','-....-':'-', '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')', '/':' ',
'.----.':"'", '.-..-.':'"'}

# renames original .txt file to include _q26752aa
def get_name(file_name):
    for i in range(len(file_name)):
        if file_name[i] == '.':
            output_name = file_name[0:i]
            return output_name + '_q26752aa.txt'

# solves Caesar Cipher
def solveCaesar(message):
    plain_text = ""
    alphabet = ['X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C']

    for i in range(len(message)):
        if message[i].upper() in alphabet:
            for j in range(len(alphabet)):
                if message[i].upper() == alphabet[j]:
                    next_char = alphabet[j-3]
        else:
            next_char = message[i]
        plain_text += next_char
    return plain_text

# solves Hex
def solveHex(string):
    print(bytes.fromhex(string).decode('utf-8'))

# solves Morse Code
def solveMorse(message):
    plain_text = ''
    current_morse = ''
    i=0
    message += ' '
    while i < len(message):
        if message[i] == ' ':
            current_morse = message[0:i]
            plain_text += str(morse_dictionary.get(current_morse))
            message = message[i+1:len(message)]
            i=0

        i+=1
    return plain_text
#-----------------------------------------------#
os.chdir(args.input)
for file in os.listdir():
    if file.endswith(".txt"):
        decrypted_text = ''
        filepath = args.input + '/' + file
        f = open(filepath, "r")
        input = f.readline()
        f.close()
        for i in range(len(input)):
            if input[i]==":":
                encrypted_text = input[i+1:len(input)]
                break

        if input[0].lower()=="c":
            decrypted_text = solveCaesar(encrypted_text)
        elif input[0].lower()=="h":
            decrypted_text = bytes.fromhex(encrypted_text).decode('utf-8')
        elif input[0].lower()=="m":
            decrypted_text = solveMorse(encrypted_text)
            if decrypted_text[len(decrypted_text)-4:len(decrypted_text)] == "None":
                i=len(encrypted_text)-1
                while encrypted_text[i] != ' ':
                    i -= 1
                current = encrypted_text[i+1:len(encrypted_text)]
                current = current.strip()
                decrypted_text = decrypted_text[0:len(decrypted_text)-4]
                decrypted_text += str(morse_dictionary.get(current))

        filepath = args.output + '/' + get_name(file)

        w = open(filepath, "w")
        w.write(decrypted_text.lower())
        w.close()
