import argparse
import re
import os

parser = argparse.ArgumentParser()

parser.add_argument("input_folder")
parser.add_argument("output_folder")

args = parser.parse_args()

inputfolderpath = (args.input_folder)
outputfolderpath = (args.output_folder)

for files in os.listdir(inputfolderpath):
    inputfiles = open(inputfolderpath + "/" + files, "r")
    words = inputfiles.readline()
    textfiles = files.split(".")

    reader = words
    caesar = "[a-zA-z\\s]+$"
    hexa = "[\\da-fA-F\\s]+$"
    Morse = "[\\W]+$"

    #For Caesar Cipher
    alphlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for i in range(len(reader)):
        if reader[i] == ":":
            text = reader[i+1:len(reader)]

    if re.match(caesar,text):#Caesar
        a = text
        result = ""
        for i in range(len(a)):
            if a[i] == " ":
                result += " "
                continue
            else:
                for x in range(len(alphlist)):
                    if a[i] == alphlist[x]:
                        result += alphlist[x-3]


    elif re.match(hexa,text):#Hexadecimal
        bytes_array = bytes.fromhex(str(text))
        ascii_str = bytes_array.decode()
        result = ascii_str
        result = result.lower()


    elif re.match(Morse,text):#Morse Code
        morse = { 'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-',
                  'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
                  'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..', '1':'.----', '2':'..---', '3':'...--',
                  '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ',':'--..--', '.':'.-.-.-',
                  '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-', ' ': '/'}

        message = str(text)
        def decrypt(message):
            message += ' '
            decipher = ''
            citext = ''
            for letter in message:
                if (letter != ' '):
                    i = 0
                    citext += letter
                else:
                    i += 1

                    if i == 2 :
                        decipher += ' '
                    else:
                        decipher += list(morse.keys())[list(morse.values()).index(citext)]
                        citext = ''
            return decipher
        result = decrypt(message)


    outputfilename = textfiles[0] + "_[n95301jf].txt"
    outputfiles = open(outputfolderpath + "/" + outputfilename, "w")
    outputfiles.write(str(result))
    outputfiles.close()
