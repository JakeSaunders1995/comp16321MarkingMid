import argparse
from os import listdir
from os.path import isfile, join
def terminal_file():
    enterer = argparse.ArgumentParser(description="decrypting program")
    enterer.add_argument("input", metavar="In", type=str, help="enter input file path", action="store")
    enterer.add_argument("output", metavar="Out", type=str, help="enter output file path", action="store")
    global args
    args = enterer.parse_args()

    return args.input, args.output

terminal_file()

newfilelist = []
unordredfile = []
for fichier in listdir(args.input):
    output = ""
    if isfile(join(args.input, fichier)):
        if fichier[-4:] == ".txt" and fichier[:3] != '.DS':
            if fichier[-5] not in "0123456789":
                unordredfile.append(fichier)
            else:
                for i in range(10):
                    if fichier[-5] == f"{i}":
                        newfilelist.insert(i-1,fichier)
unordredfile.reverse()

final_list = newfilelist + unordredfile

for f in final_list:
    output = ""
    file = open(f"{args.input}/{f}", "r")
    line = file.readlines()


    def Encryption_Reader(index, fileparttoread):
        for character in fileparttoread[index]:
            if character == ":":
                global position
                position = fileparttoread[index].index(character)
                encryption_method = fileparttoread[index][:position]
                encryption_method = encryption_method.lower()
                return encryption_method


    def Hexadecimal_decryption(place, fin, line_element):
        decryption_text = ""
        list_alphabet = ["a", "b", "c", "d", "e", "f"]
        letters_converter = {
            "a": 10,
            "b": 11,
            "c": 12,
            "d": 13,
            "e": 14,
            "f": 15,
        }
        for f in range(place + 1, fin - 1, 3):
            if line_element[f] in list_alphabet:
                hexcharacter1 = letters_converter[line_element[f]]
            elif line_element[f] not in list_alphabet:
                hexcharacter1 = int(line_element[f])
            if line_element[f + 1] in list_alphabet:
                hexcharacter2 = letters_converter[line_element[f + 1]]
            elif line_element[f + 1] not in list_alphabet:
                hexcharacter2 = int(line_element[f + 1])
            ACSIIValue = hexcharacter1 * 16 + hexcharacter2
            textchar = chr(ACSIIValue)
            decryption_text += textchar.lower()
        global output
        output = decryption_text.lower()


    def Caesar_cipher(plaintext2):
        plaintext = plaintext2.lower()
        ciphertext2 = ""
        alphabet = "xyzabcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        plaintextPosition = 0
        alphabetPosition = 0
        plaintextchar = ""
        while plaintextPosition < len(plaintext):
            if plaintext[plaintextPosition] == " " or plaintext[plaintextPosition] in numbers:
                ciphertext2 += plaintext[plaintextPosition]
                plaintextPosition += 1
            elif plaintext[plaintextPosition] in alphabet:
                plaintextchar = plaintext[plaintextPosition]
                alphabetPosition = 3
                while plaintextchar != alphabet[alphabetPosition]:
                    alphabetPosition += 1
                alphabetPosition -= 3
                ciphertext2 += alphabet[alphabetPosition]
                plaintextPosition += 1
        global output
        output = ciphertext2

    def Morse_Code(text):
        Morse_equivilants = {'.-': 'a', '-...': 'b',
                             '-.-.': 'c', '-..': 'd', '.': 'e',
                             '..-.': 'f', '--.': 'g', '....': 'h',
                             '..': 'i', '.---': 'j', '-.-': 'k',
                             '.-..': 'l', '--': 'm', '-.': 'n',
                             '---': 'o', '.--.': 'p', '--.-': 'q',
                             '.-.': 'r', '...': 's', '-': 't',
                             '..-': 'u', '...-': 'v', '.--': 'w',
                             '-..-': 'x', '-.--': 'y', '--..': 'z',
                             '.----': '1', '..---': '2', '...--': '3',
                             '....-': '4', '.....': '5', '-....': '6',
                             '--...': '7', '---..': '8', '----.': '9',
                             '-----': '0', '/': ' '}
        starting_point = 0
        decrypted_text = ""
        for i in range(1, len(text)):
            if text[i] == " ":
                encrypted_char = text[starting_point:i]
                starting_point = i + 1
                decrypted_char = Morse_equivilants[encrypted_char]
                decrypted_text += decrypted_char.lower()
            elif i == (len(text) - 1):
                encrypted_char = text[starting_point:i + 1]
                starting_point = i + 1
                decrypted_char = Morse_equivilants[encrypted_char]
                decrypted_text += decrypted_char.lower()
        global output
        output = decrypted_text.lower()


    def Encryption_technique(encryptionmethod, blassa):
        if encryptionmethod == 'hex':
            Hexadecimal_decryption(position, len(line[blassa]), line[blassa])
        elif encryptionmethod == 'caesar cipher(+3)':
            Caesar_cipher(line[blassa][position + 1:len(line[blassa])])
        elif encryptionmethod == 'morse code':
            Morse_Code(line[blassa][position + 1:len(line[blassa])])
        else:
            print("I don't know this encrypting method.")


    for i in range(len(line)):
        Encryption_Reader(i, line)
        Encryption_technique(Encryption_Reader(i, line), i)

    file.close()

    f2 = f[:-4]
    with open(f"{args.output}/{f2}_p40515mt.txt", 'w') as output_file:
        output_file.write(output)
        output_file.close()















