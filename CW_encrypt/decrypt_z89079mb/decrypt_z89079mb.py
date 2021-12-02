import sys
import os
def morse_decryption():
    global output
    for encrypted_letter in encrypted_word:
        for key, value in morse_dictionary.items():
            if value == encrypted_letter:
                try:
                    output += key.lower()
                except:
                    output += key 
    output += ' '

directory = sys.argv[1]
all_files = []
for filename in os.listdir(directory):
    input_file = os.path.join(directory, filename)
    if os.path.isfile(input_file):
        all_files.append(input_file)

morse_dictionary = {    
          "!": "-.-.--",      "\"": ".-..-.",     "$": "...-..-",    "'": ".----.",  
          "(": "-.--.",      ")": "-.--.-",     "+": ".-.-.",      ",": "--..--", 
          "-": "-....-",     ".": ".-.-.-",     "/": "-..-.", 
          "0": "-----",      "1": ".----",      "2": "..---",      "3": "...--", 
          "4": "....-",      "5": ".....",      "6": "-....",      "7": "--...", 
          "8": "---..",      "9": "----.", 
          ":": "---...",     ";": "-.-.-",     "=": "-...-",      "?": "..--.", 
          "@": ".--.-.", 
          "A": ".-",         "B": "-...",       "C": "-.-.",       "D": "-..", 
          "E": ".",          "F": "..-.",       "G": "--.",        "H": "....", 
          "I": "..",         "J": ".---",       "K": "-.-",        "L": ".-..", 
          "M": "--",         "N": "-.",         "O": "---",        "P": ".--.", 
          "Q": "--.-",       "R": ".-.",        "S": "...",        "T": "-", 
          "U": "..-",        "V": "...-",       "W": ".--",        "X": "-..-", 
          "Y": "-.--",       "Z": "--..", 
          "[": "-.--.",      "]": "-.--.-",     "_": "..--.-",}


for a in all_files:
    with open(a) as file:
        file = file.read()
        file = file.split(':')
    output = str()
    if file[0] == 'Hex':
        output = bytearray.fromhex(file[1]).decode()
        output = output.lower()
    elif file[0] == 'Caesar Cipher(+3)':
        alphabet = 'xyzabcdefghijklmnopqrstuvwxyz'
        for i in file[1]:
            for index in range(3,len(alphabet)):
                if alphabet[index] == i:
                    output += alphabet[index-3]
                elif i == " ":
                    output += i
                    break
    elif file[0] == 'Morse Code':
        input = file[1].split('/')
        for i in input:
            i = i.strip(" ")
            encrypted_word = i.split(" ")
            morse_decryption()

    filename = a[:-4]+'_z89079mb.txt'
    filename = filename.replace(sys.argv[1],sys.argv[2])
    with open(filename,'w') as fi:
        fi.write(output)
