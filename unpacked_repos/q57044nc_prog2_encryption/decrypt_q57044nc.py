import sys
import os

inputFolder = sys.argv[1]
outputFolder = sys.argv[2]

def trans(f):
    algAndText = f.read()
    justAlgAndText = algAndText.rstrip()
    algOrText = justAlgAndText.split(":", 1)
    decypheredText = []
    finalMessage = ""
    if algOrText[0] == "Morse Code":
        morseAlphabets = {'.-': 'a','-...': 'b','-.-.': 'c','-..': 'd','.': 'e','..-.': 'f','--.': 'g','....': 'h','..': 'i','.---': 'j','-.-': 'k','.-..': 'l','--': 'm','-.': 'n','---': 'o','.--.': 'p','--.-': 'q','.-.': 'r','...': 's','-': 't','..-': 'u','...-': 'v','.--': 'w','-..-': 'x','-.--': 'y','--..': 'z','-----': '0','.----': '1','..---': '2','...--': '3','....-': '4','.....': '5','-....': '6','--...': '7','---..': '8','----.': '9','/': ' '}
        mCode = algOrText[1]
        pureEncryptedText = mCode.split(" ")
        for y in range(0, len(pureEncryptedText)):
            if pureEncryptedText[y] in morseAlphabets.keys():
                decypheredText.append(morseAlphabets[pureEncryptedText[y]])
        finalMessage = ''.join(decypheredText)

    elif algOrText[0] == "Caesar Cipher(+3)":
        caesarCipher = algOrText[1]
        pureCaesarCipher = caesarCipher.split()
        caesarAlph = "xyzabcdefghijklmnopqrstuvwxyzabc"
        listReadableWords = []
        for word in pureCaesarCipher:
            readableWords = ""
            for plaintextPosition in range(0,len(word)):
                plaintextChar = word[plaintextPosition]
                alphabetPosition = 3
                while plaintextChar != caesarAlph[alphabetPosition]:
                    alphabetPosition += 1
                alphabetPosition -= 3
                readableWords += caesarAlph[alphabetPosition]
            listReadableWords.append(readableWords)
        plainText = ' '.join(listReadableWords)
        finalMessage = plainText

    elif algOrText[0] == "Hex":
        hexa = algOrText[1]
        pureHexa = hexa.split(" ")
        justNum = ''.join(pureHexa)
        declutterNum = bytearray.fromhex(justNum)
        finalMessage = declutterNum.decode()

    with open(outputFilePath, "w") as o:
        print(finalMessage, file = o)

for fileName in os.listdir(inputFolder):
    if fileName.endswith(".txt"):
        inputFilePath = os.path.join(inputFolder, fileName)
        outputFilePath = str(outputFolder) + "/" + str(fileName[:10]) + "_q57044nc" + str(fileName[10:])
        with open(inputFilePath, "r") as j:
            inputFileName = j
            trans(inputFileName)
