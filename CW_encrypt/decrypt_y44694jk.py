from argparse import ArgumentParser
import os

def determine_text():
    s = text.split(":")

    if s[0] == "Hex":
        return "Hex"

    elif "Caesar Cipher" in s[0]:
        a = s[0].split("(")[1]
        a = a[:2]
        return "Caesar Cipher", a

    elif s[0] == "Morse Code":
        return "Morse Code"

def decrypt_hex():
    a = ""
    word = text.split(":")[1].split(" ")
    for hex in word:
        byte_array = bytearray.fromhex(hex)
        a = a + byte_array.decode().lower()

    return a

def decrypt_Caesar(distance):
    a = ""
    if distance[0] == "+":
        alphabet = "zyxwvutsrqponmlkjihgfedcbazyx"
    elif distance[0] == "-":
        alphabet = "xyzabcdefghijklmnopqrstuvwxyz"
    distance = int(distance[1])
    word = text.split(":")[1].split(" ")

    for caesar in word:
        for char in caesar:
            a = a + alphabet[alphabet.index(char) + distance]
        a = a + " "

    return a

def decrypt_Morse():
    a = ""
    morse_code = { 'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----'}

    words = text.split(":")[1].split("/")
    for morse in words:
        word = morse.split(" ")
        for char in word:
            for key in morse_code:
                if morse_code[key] == char:
                    a = a + key
        a = a + " "
    return a

parser = ArgumentParser()
parser.add_argument('input_folder')
parser.add_argument('output_folder')
args = parser.parse_args()

dirname_i = args.input_folder
dirname_o = args.output_folder
for filename in os.listdir(args.input_folder):
   with open(os.path.join(dirname_i, filename)) as f:
       text = f.read()

       method = determine_text()

       ans = ""
       if method == "Hex":
           ans = decrypt_hex()
       elif "Caesar Cipher" in method:
           ans = decrypt_Caesar(method[1])
       elif method == "Morse Code":
           ans = decrypt_Morse()

       filename_o = filename.split(".")[0] + "_y44694jk.txt"
       with open(os.path.join(dirname_o, filename_o), 'w') as f_o:
           f_o.write(ans)
