import sys
import os

files = os.listdir(sys.argv[1])

for filename in files:
    
    file = open(sys.argv[1] + "/" + filename, "r")

    plaintext = ""

    line = file.readline()
    lineList = line.split(":")

    cipherText = lineList[1]

    for line in file:
        cipherText += line

    if lineList[0]  == "Morse Code":
        morseCodeAlphabet = [".-", "-...",
    "-.-.", "-..", ".",
    "..-.", "--.", "....",
    "..", ".---", "-.-",
    ".-..", "--", "-.",
    "---", ".--.", "--.-",
    ".-.", "...", "-",
    "..-", "...-", ".--",
    "-..-", "-.--", "--.."]
        morseCodeSymbols = [".----.", "-.--.", "-.--.-", 
    "", "", "--..--",
    "-....-", ".-.-.-", "-..-.",
    "-----", ".----", "..---", "...--",
    "....-", ".....", "-....",
    "--...", "---..", "----.", "---...", "-.-.-."] # "'" to ";"

        encryptedList = cipherText.split()

        for morseCode in encryptedList:
            if morseCode == "/":
                plaintext += " "
            elif morseCode in morseCodeAlphabet:
                plaintext += chr(morseCodeAlphabet.index(morseCode) + 97)
            elif morseCode in morseCodeSymbols:
                plaintext += chr(morseCodeSymbols.index(morseCode) + 39)
            elif morseCode == "..--..": plaintext += "?"
            elif morseCode == "-.-.--": plaintext += "!"
            elif morseCode == ".-..-.": plaintext += '"'

    elif lineList[0]  == "Caesar Cipher(+3)":
        for characters in cipherText.lower():

            if ord(characters) >= 100 and ord(characters) <= 122:
                plaintext += chr(ord(characters)-3)
            elif ord(characters) >= 97 and ord(characters) < 100:
                plaintext += chr(ord(characters)+23)
            else:
                plaintext += characters
                
    elif lineList[0]  == "Hex":
        encryptedList = cipherText.split(" ")
        for hexNum in encryptedList:
            plaintext += chr(int(hexNum, 16)).lower()
            
    file.close()
    newFile = sys.argv[2] + "/" + filename[:len(filename)-4] + "_e78508hb.txt"
    file = open(newFile, "w")
    file.write(plaintext)
    file.close()
