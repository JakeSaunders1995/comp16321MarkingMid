import sys
import os

morseCodeDictionary = { '':'', 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '–':'-....-',
                    '(':'-.--.', ')':'-.--.-', ';':'-.-.-.',
                    ':':'---...', '!':'-.-.--', '\'':'.----.',
                    '"':'.-..-.'  }

punctuationList = ['.', '?', '!', ',', ':', ';', '‐', '‒', '(', ')', '[', ']', '{', '}', '\'', '"', '@', '#']

inputFolder = sys.argv[1]
outputFolder = sys.argv[2]

for filename in os.listdir(inputFolder):
    if filename.endswith(".txt"):
        if inputFolder.endswith("/"):
            inputFile = inputFolder+filename
        else:
            inputFile = inputFolder+"/"+filename

        outputFile = filename[:-4]+"_p52048kg"+".txt"
        if outputFolder.endswith("/"):
            outputPath = outputFolder+outputFile
        else:
            outputPath = outputFolder+"/"+outputFile

        file = open(str(inputFile), "rt")
        data = file.readline()
        parts = data.split(":")
        encryption = parts[0]
        ciphertext = parts[1]
        decryptedData = str("")

        if encryption == "Hex":
            hexArray = bytearray.fromhex(ciphertext)
            decryptedData = str(hexArray.decode()).lower()
            
        elif encryption == "Caesar Cipher(+3)":
            ciphertextPosition = 0
            while ciphertextPosition < len(ciphertext):
                ciphertextChar = ciphertext[ciphertextPosition]
                ASCIIValue = ord(ciphertextChar)
                if ciphertextChar not in punctuationList:
                    ASCIIValue -= 3
                else:
                    pass
                if ciphertextChar == " ":
                    decryptedData = decryptedData + str(" ")
                else:
                    decryptedData = decryptedData + chr(ASCIIValue).lower()
                ciphertextPosition += 1
            
        elif encryption == "Morse Code":
            ciphertext = ciphertext + " "
            item = ""
            for character in ciphertext:
                if character == "/":
                    decryptedData = decryptedData + str(" ")
                    item = ""
                    pass
                elif character == " ":
                    decryptedData = decryptedData + str(list(morseCodeDictionary.keys())[list(morseCodeDictionary.values()).index(item)]).lower()
                    item = ""
                    pass
                elif character != " ":
                    item = item + character
                    
        file.close()

        file = open(str(outputPath), "wt")
        file.write(decryptedData)
        file.close()
    
    else:
        pass



