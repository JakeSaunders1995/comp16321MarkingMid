import argparse
from pathlib import Path

#Set up and parse command line arguments
decryptParser = argparse.ArgumentParser('Input and output files.')
decryptParser.add_argument("inputFolderPath", type=Path)
decryptParser.add_argument("outputFolderPath", type=Path)
args = decryptParser.parse_args()

#Morse code dictionary
morseDict = {"/" : " ",
".-" : "a",
"-..." : "b",
"-.-." : "c",
"-.." : "d",
"." : "e",
"..-." : "f",
"--." : "g",
"...." : "h",
".." : "i",
".---" : "j",
".-." : "k",
".-.." : "l",
"--" : "m",
"-." : "n",
"---" : "o",
".--." : "p",
"--.-" : "q",
".-." : "r",
"..." : "s",
"-" : "t",
"..-" : "u",
"...-" : "v",
".--" : "w",
"-.--" : "y",
"--.." : "z",
".----" : "1",
"..---" : "2",
"...--" : "3",
"....-" : "4",
"....." : "5",
"-...." : "6",
"--..." : "7",
"---.." : "8",
"----." : "9",
"-----" : "0",
".-.-.-" : ".",
"--..--" : ",",
"..--.." : "?",
"-.-.-." : ";",
"---..." : ":",
"-....-" : "-",
"-..-." : "/",
".----." : "'",
".-..-." : "\"",
"-...-" : "=",
"...-..-" : "$",
".-..." : "&",
"..--.-" : "_",
".--.-." : "@",
"-.--.-" : ")",
"-.--." : "("}

#Iterate through files in input folder
for file in args.inputFolderPath.glob('*'):
    #Read input file
    try:
        with open(file, "r+") as inputFile:
            inputFileData = inputFile.read()
    except:
        print("Input file is not valid.")
        continue

    #Separate the cipher text from the name of the cipher used
    cipherText = inputFileData.split(":")[1]

    #Decryption
    plainText = ""
    if inputFileData.lower()[0] == "h":
        #Hex decrypter
        for character in cipherText.split(" "):
            plainText += chr(int(character, 16))
    elif inputFileData.lower()[0] == "c":
        #Caesar (+3) decrypter
        for i in range(0, len(cipherText)):
            if 91 > ord(cipherText[i]) > 64:
                plainText += chr((ord(cipherText[i]) - 68) % 26 + 65)
            elif 123 > ord(cipherText[i]) > 96:
                plainText += chr((ord(cipherText[i]) - 100) % 26 + 97)
            else:
                plainText += cipherText[i]
        pass
    elif inputFileData.lower()[0] == "m":
        #Morse decrypter
        for character in cipherText.split(" "):
            plainText += morseDict.get(character.replace("_", "-"), character)
    else:
        print("Unknown encryption type.")

    #Write the decrypted plain text
    try:
        args.outputFolderPath.mkdir(exist_ok=True)
        with open(args.outputFolderPath / str(file.stem + "_s13506jc.txt"), "w") as outputFile:
            outputFile.write(plainText.lower())
    except:
        print("Output folder path is not valid.")
        quit()
