import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("inputfolder")
parser.add_argument("outputfolder")
args = parser.parse_args()

def AccessFolder(inputFolder, outputFolder):

    for file in sorted(os.listdir(inputFolder)):
        encryptionTechnique, cypherText = GetEncryptionTypeAndCypherText(os.path.join(inputFolder, file))
        print(encryptionTechnique)
        if encryptionTechnique == "Hex":
            plaintext = DecryptHex(cypherText)
            print(plaintext)
        elif encryptionTechnique == "Caesar":
            plaintext = DecryptCaesar(cypherText)
            print(plaintext)
        elif encryptionTechnique == "MorseCode":
            plaintext = DecryptMorse(cypherText)
            print(plaintext)

        filename = os.path.basename(os.path.join(inputFolder, file))
        prefix = filename.split(".txt")
        outputFileName = prefix[0] + "_r94627as.txt"
        WriteFile(outputFolder, outputFileName, plaintext)

def GetEncryptionTypeAndCypherText(file):
    with open(file, "r") as encryptedFile:
        content = encryptedFile.readlines()
        encryptedFile.close()
        content = content[0].split(":")
        if content[0] == "Hex":
            return "Hex", content[1]
        elif content[0] == "Caesar Cipher(+3)":
            return "Caesar", content[1]
        else:
            return "MorseCode", content[1]

def DecryptHex(cypherText):
    plaintext = ""
    cypherText = cypherText.split(" ")
    for n in cypherText:

        plaintext = plaintext + bytes.fromhex(n).decode('utf-8')

    return plaintext

def DecryptCaesar(cypherText):
    plaintext = ""
    for char in cypherText:
        if char == " ":
            plaintext = plaintext + " "
            continue
        #convert to binary
        char = ord(char)
        #-3
        char = char - 3
        #convert back
        char = chr(char)
        plaintext = plaintext + char
    return plaintext

def DecryptMorse(cypherText):
    morseCodeKey = {
    '.-':'a',
    '-...':'b',
    '-.-.':'c',
    '-..':'d',
    '.':'e',
    '..-.':'f',
    '--.':'g',
    '....':'h',
    '..':'i',
    '.---':'j',
    '-.-':'k',
    '.-..':'l',
    '--':'m',
    '-.':'n',
    '---':'o',
    '.--.':'p',
    '--.-':'q',
    '.-.':'r',
    '...':'s',
    '-':'t',
    '..-':'u',
    '...-':'v',
    '.--':'w',
    '-..-':'x',
    '-.--':'y',
    '--..':'z'}
    cypherText = cypherText.split(" ")
    plaintext = ""
    for char in cypherText:
        if char == "/":
            plaintext = plaintext + " "
            continue
        char = morseCodeKey[char]
        plaintext = plaintext + char
    return plaintext

def WriteFile(outputFolder, filename, plaintext):
    with open(os.path.join(outputFolder, filename), "w") as plaintextFile:
        plaintextFile.write(plaintext.lower())
        plaintextFile.close()

#REMEMBER TO MAKE LOWER CASE
AccessFolder(args.inputfolder, args.outputfolder)
