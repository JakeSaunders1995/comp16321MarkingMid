#!/usr/bin/env python3

'''
COMP16321 Mid Term
Program 2 - Encryption
Felix Waller
'''

import os
import argparse

def getOutputFile(inputFileName, outputFolder): 
    return outputFolder + ("" if outputFolder[-1] == "/" else "/") + inputFileName[0 : inputFileName.find(".txt")] + "_g75462fw.txt"

def morseDecrypt(ciphertext):
    morse = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z", "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",
    ".-...":"&",".----.":"'",".--.-.":"@","-.--.-":")","-.--.":"(","---...":":","--..--":",","-...-":"=","-.-.--":"!",".-.-.-":".","-....-":"-","-..-":"×",".-.-.":"+",".-..-.":"\"","..--..":"?","-..-.":"/"
    }

    ciphertext = [x.split() for x in ciphertext.split("/")]
    plaintext = ""
    for word in ciphertext:
        for letter in word:
            plaintext = plaintext + morse[letter]
        plaintext = plaintext + " "
    return plaintext

def hexDecrypt(ciphertext):
    plaintext = ""
    for i in ciphertext.split():
        plaintext = plaintext + chr(int(i, 16))
    return plaintext.lower()

def caesarDecrypt(ciphertext):
    cipherlist = list(ciphertext.lower())
    for i in range(len(cipherlist)):
        if  cipherlist[i] >= 'a' and cipherlist[i] <= 'z':
            if cipherlist[i] <= 'c':
                cipherlist[i] = chr(ord(cipherlist[i]) + 23)
            else:
                cipherlist[i] = chr(ord(cipherlist[i]) - 3)
    return ''.join(cipherlist)

def decrypt(inputFilePath, inputFileName, outputFolder):
    with open(inputFilePath) as file:
        input = file.read().split(":")

    if input[0] == "Morse Code":
        plaintext = morseDecrypt(input[1])
    elif input[0] == "Caesar Cipher(+3)":
        plaintext = caesarDecrypt(input[1])
    else:
        plaintext = hexDecrypt(input[1])

    with open(getOutputFile(inputFileName, outputFolder), "w") as file:
        file.write(plaintext)

parser = argparse.ArgumentParser()
parser.add_argument("inputFolder")
parser.add_argument("outputFolder")
args = parser.parse_args()

for entry in os.scandir(args.inputFolder):
    if ".txt" in entry.name:
        decrypt(entry.path, entry.name, args.outputFolder)
