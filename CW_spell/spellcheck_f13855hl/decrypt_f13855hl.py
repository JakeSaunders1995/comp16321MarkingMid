import os
import argparse

# Hex Cipher
def hexmain(hex):
    decrypted_string = ''.join(chr(int(i, 16)) for i in hex.split())

    temp = filename.split(".")
    output_file_name = temp[0] + "_" + "f13855hl" + "." + temp[1]
    outputFile = open(outputfolderpath + "/" + output_file_name, "w")
    outputFile.write(decrypted_string)
    outputFile.close()
# hexmain()

# Caesar Cipher +3
def caesarcipher(letter):
    caesardecryted = ord(letter) - 3
    return chr(caesardecryted)

def caesarmain(caesar):    
    decrypted_string = ""

    for letter in caesar:
        if letter == " ":
            decrypted_string = decrypted_string + " "
        else:
            decrypted_string = decrypted_string + caesarcipher(letter)

    temp = filename.split(".")
    output_file_name = temp[0] + "_" + "f13855hl" + "." + temp[1]
    outputFile = open(outputfolderpath + "/" + output_file_name, "w")
    outputFile.write(decrypted_string)
    outputFile.close()
# caesarmain()

# Morse Code
morsecodeDict = { '.-':'A', '-...':'B',
                    '-.-.':'C', '-..':'D', '.':'E',
                    '..-.':'F', '--.':'G', '....':'H',
                    '..':'I', '.---':'J', '-.-':'K',
                    '.-..':'L', '--':'M', '-.':'N',
                    '---':'O', '.--.':'P', '--.-':'Q',
                    '.-.':'R', '...':'S', '-':'T',
                    '..-':'U', '...-':'V', '.--':'W',
                    '-..-':'X', '-.--':'Y', '--..':'Z',
                    '.----':'1', '..---':'2', '...--':'3',
                    '....-':'4', '.....':'5', '-....':'6',
                    '--...':'7', '---..':'8', '----.':'9',
                    '-----':'0', '--..--':',', '.-.-.-':'.',
                    '..--..':'?', '-..-.':'/', '-....-':'-',
                    '-.--.':'(', '-.--.-':')', '/':' '}

def morse(morse):
    decrypted_string = ''.join(morsecodeDict.get(i) for i in morse.split())
    decrypted_string = decrypted_string.lower()
    
    temp = filename.split(".")
    output_file_name = temp[0] + "_" + "f13855hl" + "." + temp[1]
    outputFile = open(outputfolderpath + "/" + output_file_name, "w")
    outputFile.write(decrypted_string)
    outputFile.close()
    
# morse()

parser = argparse.ArgumentParser()

parser.add_argument("input_folder_path")
parser.add_argument("output_folder_path")

args = parser.parse_args()

inputfolderpath = (args.input_folder_path)
outputfolderpath = (args.output_folder_path)

for filename in os.listdir(inputfolderpath):
    if filename.endswith(".txt"):
        inputfile = open(inputfolderpath + "/" + filename)

        file = inputfile.readline()
        file = file.split(":", 1)

        if file[0] in ("Hex"):
            hexmain(file[1])
        elif file[0] in ("Caesar Cipher(+3)"):
            caesarmain(file[1])
        elif file[0] in ("Morse Code"):
            morse(file[1])
