import argparse
import binascii
import os

def Decrypt(pathIn, pathOut, fileName):
    with open(pathIn, "r") as In:
        password = In.read()
        splitPassword = password.split(":", 1)
        print(splitPassword)
        passwordList = splitPassword[1].split(" ")

        if splitPassword[0] == "Hex":
            Result = ""
            Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            Lower = "abcdefghijklmnopqrstuvwxyz"
            for i in range(len(passwordList)):
                letter1 = str(binascii.a2b_hex(passwordList[i]))
                letter2 = letter1.replace("b", "")
                letter3 = letter2.replace("'", "")
                if letter3 in Upper:
                    position = Upper.find(letter3)
                    Result = Result + Lower[position]
                else:
                    Result = Result + letter3

        elif splitPassword[0] == "Caesar Cipher(+3)":
            Result = ""
            alphabet = "abcdefghijklmnopqrstuvwxyzabc"
            for i in range(len(passwordList)):
                position = 0
                while position < len(passwordList[i]):
                    temp = passwordList[i][position]
                    alphabetPosition = 0
                    while temp != alphabet[alphabetPosition]:
                        alphabetPosition += 1

                    alphabetPosition = alphabetPosition - 3
                    Result = Result + alphabet[alphabetPosition]
                    position += 1
                Result = Result + " "

        elif splitPassword[0] == "Morse Code":
            Result = ""
            MorseDict = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h',
                    '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p',
                    '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
                    '-.--': 'y', '--..': 'z', '/': ' ', '.-.-.-': '.', '---...': ':', '--..--': ',', '-.-.-.': ';', '..--..': '?',
                    '.----.': '\'', '-.-.--': '!', '-....-': '-', '.-..-.': '"', '-.--.': '(', '-.--.-': ')',
                    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
                    '--...': '7', '---..': '8', '----.': '9'}
            for i in range(len(passwordList)):
                Result = Result + MorseDict[passwordList[i]]

        In.close()
    fileOutput = open(pathOut + "/" + fileName + "_v54835xw" + ".txt", "w")
    fileOutput.write(Result)
    fileOutput.close()

def OpenFolder(pathIn, pathOut):
    path = os.path.abspath(pathIn)
    outputPathFolder = os.path.abspath(pathOut)
    fileList = os.listdir(path)
    for i in range(len(fileList)):
        Decrypt(path + "/" + fileList[i], outputPathFolder, fileList[i])

parser = argparse.ArgumentParser(description="Decrypt")
parser.add_argument("pathIn", type=str)
parser.add_argument("pathOut", type=str)
args = parser.parse_args()

OpenFolder(args.pathIn, args.pathOut)