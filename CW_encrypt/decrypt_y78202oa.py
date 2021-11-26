import argparse
import os

#Command Line Arguments
parser = argparse.ArgumentParser()
parser.add_argument('inputFolder',type=str)
parser.add_argument('outputFolder', type=str)
args = parser.parse_args()



def Hex(cipherText):
    cipherText = cipherText.replace(" ","")
    
    plainText = bytes.fromhex(cipherText).decode("ASCII")
    
    return plainText

def Ceasar(shift ,cipherText):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newAlphabet = GetNewAlphabet(shift)

    plainText = ""
    for i in range(len(cipherText)):
        if cipherText[i] != ' ':
            plainText = plainText + newAlphabet[ alphabet.index(cipherText[i]) ]
        else:
            plainText = plainText + " "
    
    return plainText
        
def GetNewAlphabet(shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newAlphabet = ""

    currentChar = ''
    if shift[0] == "+":
        shift = int(shift.replace("+",""))
        newAlphabet = alphabet[26 - shift:]
        for i in range(26 - shift):        
            newAlphabet = newAlphabet + alphabet[i]
        return newAlphabet
    elif shift[0] == "-":
        print("Read Comment")
        #do the same thing but other way

def Morse(cipherText):
    morseDict = {
        ".-":"a",
        "-...":"b",
        "-.-.":"c",
        "-..":"d",
        ".":"e",
        "..-.":"f",
        "--.":"g",
        "....":"h",
        "..":"i",
        ".---":"j",
        "-.-":"k",
        ".-..":"l",
        "--":"m",
        "-.":"n",
        "---":"o",
        ".--.":"p",
        "--.-":"q",
        ".-.":"r",
        "...":"s",
        "-":"t",
        "..-":"u",
        "...-":"v",
        ".--":"w",
        "-..-":"x",
        "-.--":"y",
        "--..":"z",
        ".----":"1",
        "..---":"2",
        "...--":"3",
        "....-":"4",
        ".....":"5",
        "-....":"6",
        "--...":"7",
        "---..":"8",
        "----.":"9",
        "-----":"0"
    }

    characters = cipherText.split(" ")
    plainText = ""
    for i in range(len(characters)):
        if characters[i] != "/":
            plainText = plainText + str(morseDict.get(characters[i]))
        else:
            plainText = plainText + " "

    return plainText

for j in range (len(os.listdir(args.inputFolder))):

    if (os.listdir(args.inputFolder)[j].__contains__(".txt")):
        string = os.path.join(args.inputFolder, os.listdir(args.inputFolder)[j])
        iFile = open(string, "r")
        line = iFile.read() 

        plainText = ""
        parts = line.split(":")
        if parts[0] == "Hex":
            plainText = Hex(parts[1])
        elif parts[0][0:13] == "Caesar Cipher":
            plainText = Ceasar(parts[0][14:-1],parts[1])
        elif parts[0] == "Morse Code":
            plainText = Morse(parts[1])

        outputFileName = os.listdir(args.inputFolder)[j].replace(".txt","") + "_y78202oa.txt"
        pathToSave = os.path.join(args.outputFolder, outputFileName)
        oFile = open(pathToSave, "w+")
        oFile.write(plainText)
        oFile.close()
        