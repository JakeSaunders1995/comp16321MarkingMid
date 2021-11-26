import sys
import os

def decryptHex(text):
    hexstring = text[4:]
    hexstring.strip()
    bytes1 = bytes.fromhex(hexstring)
    bytes1 = bytes1.decode("ascii")
    bytes1 = bytes1.lower()
    return bytes1

def decryptMorse(text):
    morsestring = text[11:]
    morse_code1 = { 'a':'.-', 'b':'-...',
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
                    '(':'-.--.', ')':'-.--.-', '':''}
    morse_code= dict((v,k) for k,v in morse_code1.items())


    text = ""
    temptext = ""
    tempmorsechar = ""
    char = 0
    while char < len(morsestring)-2:
        if morsestring[char] == " " and morsestring[char+1] == "/" and morsestring[char+2] == " ":
            temptext += " "

            for morsechar in temptext:
                if morsechar != ' ':
                    tempmorsechar += morsechar
                else:
                    text += morse_code[tempmorsechar]
                    tempmorsechar = ""

            text += " "
            temptext = ""
            char += 2
        else:
            temptext += morsestring[char]
        char +=1

    temptext += morsestring[-2:] + " "

    for morsechar in temptext:
        if morsechar != ' ':
            tempmorsechar += morsechar
        else:
            text += morse_code[tempmorsechar]
            tempmorsechar = ""
    return text

def decryptCeasar(text):
    ceasarstring = text[18:]
    ceasarstring = ceasarstring[:-1]
    crypt = ""
    for letter in ceasarstring:
        if letter == " ":
            crypt += " "
        elif letter == "a":
            crypt += "x"
        elif letter == "b":
            crypt += "y"
        elif letter == "c":
            crypt += "z"
        else:
            crypt += chr(ord(letter)-3)
    crypt = crypt.lower()
    return crypt

output1 = []
listofFiles = os.listdir(sys.argv[1])
listofFiles.sort()
for files in listofFiles:
    with open(sys.argv[1]+"/"+files, 'r') as f:
        file = f.read()
        output = ""
        if file[0] == "H":
            output = decryptHex(file)
        elif file[0] == "C":
            output = decryptCeasar(file)
        else:
            output = decryptMorse(file)
        output1.append(output)

for i in range(0,len(output1)):
    listofFiles[i] = listofFiles[i][:-4]
    with open(sys.argv[2]+"/"+listofFiles[i]+"_c81776oa.txt", 'w') as f:
        string = output1[i]
        f.write(string)
