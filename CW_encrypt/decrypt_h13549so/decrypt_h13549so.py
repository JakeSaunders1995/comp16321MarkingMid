import sys
import os

# iterates over input directory and stores an array of the files 
files = os.listdir(sys.argv[1])
for i in range(len(files)-1):
    if files[i] == ".DS_Store":
        files.remove(".DS_Store")
    else:
        continue

# decrypt hex
def decryptHex(hex):
    cleaned = hex.replace(" ", "")
    words = bytearray.fromhex(cleaned).decode()
    return words.lower()

# decrypt caesar
def decryptCaesar(caesar):
    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    alphabet = alphabet.replace(" ","" )
    for i in range(len(caesar)):
        if caesar[i] == " ":
            caesar = caesar
        else:
            if caesar[i] not in alphabet:
                caesar = caesar 
            else:
                plusThreeIndex = alphabet.find(caesar[i])
                decryptedChar = alphabet[plusThreeIndex - 3]
                caesar = caesar[:i] + decryptedChar + caesar[i+1:]
    return caesar.lower()

# decrypt morse
def decryptMorse(morse):
    # Dictionary representing the morse code chart
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
                    '(':'-.--.', ')':'-.--.-', ' ': '/'}
    splitmorse = morse.split()
    new = ""
    for i in range (len(splitmorse)):
        alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        alphabet = alphabet.replace(" ","" )
        alphabet = alphabet + ' '
        for j in alphabet:
            if splitmorse[i] == MORSE_CODE_DICT[j]:
                new += j
    return new.lower()
    
# output to relevant txt files
for file in files:
    readFrom = open(sys.argv[1]+"/"+file, "r")
    cipher = readFrom.read()
    if cipher[0] == 'h' or 'H' and cipher[0] != 'C' and cipher[0]!= 'M':
        hex = cipher[4:]
        readFrom.close()
        writeTo = open(sys.argv[2]+"/"+file.removesuffix(".txt")+"_h13549so.txt", "w")
        writeTo.write(decryptHex(hex))
    elif cipher[0] == 'c' or 'C' and cipher[0]!= 'M':
        caesar = cipher[18:]
        readFrom.close()
        writeTo = open(sys.argv[2]+"/"+file.removesuffix(".txt")+"_h13549so.txt", "w")
        writeTo.write(decryptCaesar(caesar))
    else:
        morse = cipher[11:]
        readFrom.close()
        writeTo = open(sys.argv[2]+"/"+file.removesuffix(".txt")+"_h13549so.txt", "w")
        writeTo.write(decryptMorse(morse))
        writeTo.close()
        





      
