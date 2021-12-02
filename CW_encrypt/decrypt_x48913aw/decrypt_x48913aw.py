import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("inputPath")
parser.add_argument("outputPath")
args = parser.parse_args()

inputFolder = str(args.inputPath)
listFiles = os.listdir(inputFolder)

for x in listFiles:
    if ".txt" not in x:
        listFiles.remove(x)

noOfFiles = len(listFiles)

for y in range(noOfFiles):
    inputFile = open(inputFolder+"/"+listFiles[y])
    txt = inputFile.read()

    plainText = ""
    splitText = txt.split(":")
    typeOfEncryption = (str(splitText[0])).lower()
    cipherText = (str(splitText[1]))

    morseCodeDictionary = { 'a':'.-', 'b':'-...','c':'-.-.',
                            'd':'-..', 'e':'.','f':'..-.',
                            'g':'--.', 'h':'....','i':'..',
                            'j':'.---', 'k':'-.-','l':'.-..',
                            'm':'--', 'n':'-.','o':'---',
                            'p':'.--.', 'q':'--.-','r':'.-.',
                            's':'...', 't':'-','u':'..-',
                            'v':'...-', 'w':'.--','x':'-..-',
                            'y':'-.--', 'z':'--..','1':'.----',
                            '2':'..---', '3':'...--','4':'....-',
                            '5':'.....', '6':'-....','7':'--...',
                            '8':'---..', '9':'----.','0':'-----',
                            ', ':'--..--', '.':'.-.-.-','?':'..--..',
                            '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-',
                            '!':'-.-.--', ':':'---...', ';':'-.-.-.',
                            '"':'.-..-.'}

    def ceaserShift(cipherText):
        plainText = ""
        cipherText = cipherText.lower()
        alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
        ciphertextPosition = 0

        while (ciphertextPosition < len(cipherText)):
            ciphertextChar = cipherText[ciphertextPosition]
            if(ciphertextChar not in alphabet):
                plainText = plainText + ciphertextChar
                ciphertextPosition = ciphertextPosition + 1
            else:
                alphabetPosition = 3
                if (ciphertextChar == " "):
                    ciphertextPosition = ciphertextPosition + 1
                    plainText = plainText + " "
                else:
                    while ciphertextChar != alphabet[alphabetPosition]:
                        alphabetPosition = alphabetPosition + 1
                    alphabetPosition = alphabetPosition - 3
                    plainText = plainText + alphabet[alphabetPosition]
                    ciphertextPosition = ciphertextPosition + 1

        return plainText

    def hexadecimal(cipherText):
        plainText = bytes.fromhex(cipherText).decode('utf-8')
        plainText = plainText.lower()
        return(plainText)

    def morseCode(cipherText):
        plainText = ""
        words = cipherText.split("/")
        sentanceLength = len(words)
        for x in range(sentanceLength):
            letter = words[x].split(" ")
            wordLength = len(letter)
            for i in range(wordLength):
                if (letter[i] == ''):
                    continue
                else:
                    plainText = plainText + (
                    list(morseCodeDictionary.keys())[list(morseCodeDictionary.values()).index(letter[i])])
            plainText = plainText + " "
        return(plainText)

    if("m" in typeOfEncryption):
        plainText = morseCode(cipherText)
    elif("x" in typeOfEncryption):
        plainText = hexadecimal(cipherText)
    else:
        plainText = ceaserShift(cipherText)

    fileName = ""
    name = str(listFiles[y])

    for i in name:
        if i == ".":
            break
        else:
            fileName = fileName + i

    outputfile = open((str(args.outputPath)+"/"+fileName+"_x48913aw.txt"), "x")
    outputfile.write(plainText)
