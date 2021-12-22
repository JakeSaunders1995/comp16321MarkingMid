import os
import argparse
from pathlib import Path
import re

morse_language = {
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.","g": "--.","h": "....","i": "..","j": ".---","k": "-.-","l":
        ".-..","m": "--","n": "-.","o": "---","p": ".--.","q": "--.-","r": ".-.","s": "...","t": "-","u": "..-","v": "...-","w": ".--","x": "-..-",
        "y": "-.--","z": "--..",
        "0": "-----","1": ".----","2": "..---","3": "...--","4": "....-","5": ".....","6": "-....","7": "--...","8": "---..","9": "----.",
        "&": ".-...","'": ".----.","@": ".--.-.",")": "-.--.-","(": "-.--.",":": "---...",",": "--..--","=": "-...-","!": "-.-.--",".": ".-.-.-",
        "-": "-....-","+": ".-.-.",'"': ".-..-.","?": "..--..","/": "-..-.",
    }

def convert_morseCode(text):
    morse_to_decode = re.split('[/]',text)

    plain_text = ""
    # Loop through each word
    for word in morse_to_decode:
        # Loop through each letter
        morse_letter = re.split('[ ]',word)
        for l in morse_letter:

            for plain_letter in morse_language:
                if morse_language[plain_letter] == l:
                    plain_text += plain_letter

        plain_text += " "

    return plain_text
def convert_caeser(cipherText):
    cipherTextPos = 0
    plainText = ""
    while cipherTextPos < len(cipherText):
        cipherTextChar = cipherText[cipherTextPos]

        if ord(cipherTextChar) == 32:
            plainText += " "
        else:
            charValue = ""
            if (re.search('[a-z]', cipherTextChar)) :
                charValue = chr((ord(cipherTextChar) - 100)%26 + 97)
            else:
                ASCIIvalue = ord(cipherTextChar) - 3
                charValue = chr(ASCIIvalue)
            plainText += charValue
        cipherTextPos += 1

    return plainText.lower()

def convert_hex(text):
    #Split the hex by the spaces between bytes
    hextodecode = re.split('[ ]',text)
    plain_text = ""
    for x in hextodecode:
        decimal = int(x,16)
        plain_text += str(chr(decimal))
    return plain_text.lower()

# Get input for the testfiles
parser = argparse.ArgumentParser(description = "Decrypt a cipher with a given algorithm")

parser.add_argument('input_folder', help="The input folder")
parser.add_argument('output_folder', help="The output folder")
files = parser.parse_args()

input_exists, output_exists = os.path.exists(files.input_folder), os.path.exists(files.output_folder)

if len(os.listdir(files.input_folder)) == 0:
    print('No files in input folder')
    os._exit(1)

if input_exists and output_exists:
    pass
else:
    print("Incorrect file paths were entered")
    os._exit(1)

# Loop through files in the input folder
for filename in os.listdir(files.input_folder):
    if filename.endswith('.txt'):

        # Open the current txt file
        input_filepath = os.path.join(files.input_folder, filename)
        input_file = open(str(input_filepath), "r")

        output_filename = str(Path(filename).stem + "_k77872uk.txt")

        # Make the output file
        output_filepath = os.path.join(files.output_folder, output_filename)
        output_file = open(str(output_filepath), "w")

        output_text = ""

        # Check what kind of algorithm the current file needs
        text = re.split('[:]',input_file.readline().rstrip())
        #print(text[0])
        if text[0] == "Hex":
            hex_output = convert_hex(text[1])
            #print(hex_output)
            output_text = hex_output

        elif text[0] == "Caesar Cipher(+3)":
            caesar_output = convert_caeser(text[1])
            output_text = caesar_output

        elif text[0] == "Morse Code":
            output_text =convert_morseCode(text[1])
        else:
            print('Input text in incorrect format')

        # Write to the output file, then close the files
        output_file.write(output_text)
        input_file.close()
        output_file.close()
