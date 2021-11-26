import sys
import os 

directoryIn  = sys.argv[1]
directoryOut = sys.argv[2]

encryptionDict = {
    "M": "Morese Code has been used here.",
    "C": "Ceaser shift has been used here.",
    "H": "Hexadecimal has been used here.",
}

morseDict = {
    ".-": "a", 
    "-...": "b",
    "-.-.": "c", 
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "/": " ",
    ".-.-.-": ".",
    "--..--": ",",
    "---...": ":",
    "..--..": "?",
    ".----.": "'",
    "-....-": "-",
    "-..-.": "/",
    "-.--.-": ")",
    "-.--.": "(",
    ".-..-.": '"',
    "-.--.": "[",
    "-.--.-": "]",
    "---.": "!",
    "*----": "1",
    "**---": "2",
    "***--": "3",
    "****-": "4",
    "*****": "5",
    "-****": "6",
    "--***": "7",
    "---**": "8",
    "----*": "9",
    "-----": "0",
}

number = 1

for filename in os.listdir(directoryIn):
    f = os.path.join(directoryIn, filename)
    if os.path.isfile(f):
        file_in = open(f)
        data    = file_in.read()
        text    = data.split(":")

        if data[0] == "M":
            standardText = ""
            morseText    = text[1].split()
            standardWord = ""
            morseWordPosition = 0
            n = 0

            while morseWordPosition < len(morseText):
                morseWord = morseText[n]
                morsewordSel = morseText[morseWordPosition]
                standardWord = standardWord + morseDict[morsewordSel]
                morseWordPosition = morseWordPosition + 1
                n += 1
            standardText = standardText + standardWord
            standardText = standardText.lower()

            outFileName = filename[:-4] + "_p91607ma.txt"
            pathToFile = os.path.join(directoryOut, outFileName)
            outFile = open(pathToFile, "a")
            outFile.write(standardText)


        elif data[0] == "C":
            ciphertext = text[1].split()
            plaintext  = ""
            #print(ciphertext)
            i = 0
            for i in range(0, len(ciphertext)):
                plainWord = ""
                cipherWordPosition = 0
                cipherWord = ciphertext[i]
                while cipherWordPosition < len(cipherWord):
                    cipherWordChar      = cipherWord[cipherWordPosition]
                    ASCIIValue          = ord(cipherWordChar)
                    ASCIIValue          = ASCIIValue - 3
                    plainWord           = plainWord + chr(ASCIIValue) 
                    cipherWordPosition  = cipherWordPosition + 1
                plaintext = plaintext + plainWord + " "
                plaintext = plaintext.lower()

            outFileName = filename[:-4] + "_p91607ma.txt"
            pathToFile = os.path.join(directoryOut, outFileName)
            outFile = open(pathToFile, "a")
            outFile.write(plaintext)


        else:
            newText = ""
            hexCode = text[1].split()
            hexWordPosition = 0
            h = 0

            while hexWordPosition < len(hexCode):
                hexWord = hexCode[h]
                inter   = bytes.fromhex(hexWord)
                inter   = inter.decode("ascii")
                newText = newText + inter
                hexWordPosition = hexWordPosition + 1
                h += 1
                newText = newText.lower()

            outFileName = filename[:-4] + "_p91607ma.txt"
            pathToFile = os.path.join(directoryOut, outFileName)
            outFile = open(pathToFile, "a")
            outFile.write(newText)
        number += 1

