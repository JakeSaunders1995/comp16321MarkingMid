import sys
import os 

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
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
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
MORSE_CODE_DECRYPT_DICT = dict([(v, k) for k, v in MORSE_CODE_DICT.items()])

inputFilePath = sys.argv[1]
outputFilePath = sys.argv[2]

inputFiles = []
for file in os.listdir(inputFilePath):
    if file.endswith(".txt"):
        inputFiles.append(file.split(".")[0])

def decrypt(fileName):
    global bytes
    inputFile = open(os.path.join(inputFilePath, fileName + ".txt"))
    encryptedFile = inputFile.read()
    inputFile.close()

    encryptedFileArr = encryptedFile.split(":")
    decryptedStr = ""

    if encryptedFileArr[0] == "Hex":
        hexArr = encryptedFileArr[1].rstrip().split(" ")
        for i in hexArr:
            bytes = bytes.fromhex(i)
            decryptedStr += bytes.decode("ASCII")

    elif encryptedFileArr[0] == "Caesar Cipher(+3)":
        cipherText = encryptedFileArr[1].rstrip()
        cipherText = str.upper(cipherText)
        alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
        cipherTextPosition = 0
        while (cipherTextPosition < len(cipherText)):
            cipherTextChar = cipherText[cipherTextPosition]
            if cipherTextChar != " ":
                alphabetPosition = 3
                while (cipherTextChar != alphabet[alphabetPosition]):
                    alphabetPosition += 1
                alphabetPosition -= 3
                decryptedStr = decryptedStr + alphabet[alphabetPosition]
            else: 
                decryptedStr += " "
            cipherTextPosition += 1

    elif encryptedFileArr[0] == "Morse Code":
        morseCodeWordArr = hexArr = encryptedFileArr[1].rstrip().split("/")
        for i in range(len(morseCodeWordArr)):
            morseCodeLettersArr = morseCodeWordArr[i].split(" ")
            for j in range(len(morseCodeLettersArr)):
                if morseCodeLettersArr[j] != " " and morseCodeLettersArr[j] != "":
                    decryptedStr += MORSE_CODE_DECRYPT_DICT.get(morseCodeLettersArr[j])
            decryptedStr += " "

    decryptedStr = decryptedStr.lower()

    outputFile = open(os.path.join(outputFilePath, str(str(fileName) + "_v78643ld.txt")), "w")
    outputFile.write(decryptedStr)
    outputFile.close()


for i in inputFiles:
    decrypt(i)
