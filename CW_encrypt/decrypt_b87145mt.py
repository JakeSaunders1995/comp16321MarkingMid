import os
import argparse

#file = "Morse Code:.... --- .-- . ...- . .-. / ... --- .-.. ...- .. -. --. / -- --- .-. ... . / -.-. --- -.. . / -- .- -.-- / -... . / - .... . / -- --- ... - / -.. .. ..-. ..-. .. -.-. ..- .-.. -"

#parser is created to take arguments from command line
parser = argparse.ArgumentParser()
parser.add_argument("InputDir", help="Input file path", type=str)
parser.add_argument("OutputDir", help="Output file path", type=str)
args = parser.parse_args()


code = ""
decryptedCode = ""
encryptionMode = ""

#The code below creates a list of files from the input directory
fileList = os.listdir(args.InputDir)
#The code below puts the output directory name in a variable
outputDirectory = args.OutputDir

#Looks through the file for the first colon and returns the characters before it
def DetectDecryption(codeFile):
    length = len(codeFile)
    codeType = ""
    charCounter = 0

    while charCounter < length and codeFile[charCounter] != ":":
        codeType = codeType + codeFile[charCounter]
        charCounter += 1

    return codeType



def GetCode(codeFile,mode):
    encrypted = ""
    for i in range((len(mode) + 1), len(codeFile)):
        encrypted = encrypted + codeFile[i]
    return encrypted



def CaesarDecrypt(code):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decryptedText = ""
    currentChar = ""

    for chara in range(len(code)):
        currentChar = code[chara]

        letter = 0
        found = False
        while letter < len(alphabet) and not found:
            decryptedLetter = ""
            if currentChar == alphabet[letter]:
                decryptedText = decryptedText + alphabet[(letter-3)]
                found = True

            if letter == (len(alphabet) - 1):
                decryptedText = decryptedText + currentChar

            letter += 1

    return decryptedText



def HexDecrypt(code):
    count = 1
    hexCode = ""
    decryptedText = ""

    for i in range(len(code) + 1):
        if (count % 3) == 0:
            asciiCode = int(hexCode, 16)
            decryptedText = decryptedText + chr(asciiCode)
            hexCode = ""
        elif (count % 3) != 0 and i < len(code):
            hexCode = hexCode + code[i]
        count += 1

    return decryptedText



def MorseDecrypt(code):
    key = {".-": "a","-...": "b","-.-.": "c","-..": "d",".": "e","..-.": "f","--.": "g","....": "h","..": "i",".---": "j","-.-": "k",".-..": "l","--": "m","-.": "n","---": "o",".--.": "p","--.-": "q",".-.": "r","...": "s","-": "t","..-": "u","...-": "v",".--": "w","-..-": "x","-.--": "y","--..": "z",".----": "1","..---": "2","...--": "3","....-": "4",".....": "5","-....": "6","--...": "7","---..": "8","----.": "9","-----": "0","..--..": "?","-.-.--": "!",".-.-.-": ".","--..--": ",","-.-.-.": ";","---...": ":",".-.-.": "+","-....-": "-","-..-.": "/","-...-": "="}

    decryptedText = ""
    morseChar = ""


    #Go through each character in the code
    for i in range(len(code)):
        #This if statement signifies when the end of each character in morse is done
        if (code[i] == " " and len(morseChar) >= 1) or (i == (len(code) - 1)):
            #the last morsechar is not added because there is no space after it. This code fixes it
            if i == len(code) - 1:
                morseChar = morseChar + code[i]
            #go search for the current current morse code charcter in the "key" dictionary
            currentChar = key[morseChar]
            decryptedText = decryptedText + currentChar
            morseChar = ""
        elif code[i] == "/":
            decryptedText = decryptedText + " "
        elif code[i] != " ":
            morseChar = morseChar + code[i]

    return decryptedText



def GetFileName(inputFile):
    count = 0
    name = ""
    while count < len(inputFile) and inputFile[count] != ".":
        name = name + inputFile[count]
        count += 1
    return name



for fileNumber in range(len(fileList)):
    #Goes through each file in the list of files, puts current file in a variable called "file"
    fileName = fileList[fileNumber]
    location = args.InputDir + "/" + fileName
    f = open(location, "r")
    file = f.read()
    f.close()

    encryptionMode = DetectDecryption(file)
    code = GetCode(file,encryptionMode).upper()


    if encryptionMode == "Caesar Cipher(+3)":
        decryptedCode = CaesarDecrypt(code.lower())
    elif encryptionMode == "Hex":
        decryptedCode = HexDecrypt(code)
    elif encryptionMode == "Morse Code":
        decryptedCode = MorseDecrypt(code)



    fileTitle = GetFileName(fileName)

    outputPath = outputDirectory + "/" + fileTitle + "_b87145mt.txt"
    out = open(outputPath, "w")
    out.write(decryptedCode)
    out.close()
