import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("inputFolder")
parser.add_argument("outputFolder")
parsedArgs = parser.parse_args()

files = os.listdir(parsedArgs.inputFolder)

for x in files:
    if "txt" not in x:
        files.remove(x)


for i in files:

    filepath = (str(parsedArgs.inputFolder) + "/" + i)
    file  = open(str(filepath))
    input = file.readline()

    algorithm = ""
    cipherText = ""
    found = False

    for x in range(0,len(input)):
        if input[x] == ":":
            found = True
        else:
            if(found == False):
                algorithm = algorithm + str(input[x])
            else:
                cipherText = cipherText + str(input[x])

    def ceaser(cipher):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        plainText = ""

        for x in range(0, len(cipher)):
            alphabetPosition = 3
            if cipher[x] not in alphabet:
                plainText += cipher[x]
            else:
                for y in range(0, len(alphabet)):
                    if cipher[x] == alphabet[y]:
                        plainText += alphabet[y-3]
        return plainText

    def hex(cipher):
        byte_array = bytearray.fromhex(cipher)
        return byte_array.decode()

    morseDictionary = { 'a':'.-', 'b':'-...',
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
                        '0':'-----'}

    def morse(cipher):

        characters = cipher.split(" ")
        plain = ""
        character = ""

        for char in characters:
            if char != "/":
                plain += list(morseDictionary.keys())[list(morseDictionary.values()).index(char)]
            else:
                plain += " "
        return plain

    result = ""

    if "m" in algorithm.lower():
        result = morse(cipherText)
    elif "x" in algorithm.lower():
        result = hex(cipherText)
    else:
        result = ceaser(cipherText)

    file.close()

    filename = i.split(".")

    outputFile = open((str(parsedArgs.outputFolder) + "/" + filename[0] + "_t09329lw.txt"), "x")
    outputFile.write(result.lower())

    outputFile.close()