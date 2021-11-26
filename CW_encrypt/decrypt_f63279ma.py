import os, sys
import re

morseAlphabet = { # used to decrypt morse
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
        "-----":"0",
        ".----":"1",
        "..---":"2",
        "...--":"3",
        "....-":"4",
        ".....":"5",
        "-....":"6",
        "--...":"7",
        "---..":"8",
        "----.":"9",
        ".-...":"&",
        ".----.":"'",
        ".--.-.":"@",
        "-.--.-":")",
        "-.--.":"(",
        "---...":":",
        "--..--":",",
        "-...-":"=",
        "-.-.--":"!",
        ".-.-.-":".",
        "-....-":"-",
        ".-.-.":"+",
        ".-..-.":'"',
        "..--..":"?",
        "-..-.":"/",
        "/":" ",
    }

# decrypt message depending on type of encoding
def decrypt(stringData):
    encryptionMode, encryptedText = stringData.split(":")
    decryptedText = ""

    # using hex
    if re.search("hex", encryptionMode, re.IGNORECASE):

        characters = encryptedText.split()
        for c in characters:
            decryptedText += chr(int(c, 16)) # convert to integer then to character

    elif re.search("caesar", encryptionMode, re.IGNORECASE):
        ciphertextPosition = 0
        while ciphertextPosition < len(encryptedText): # go through each character 
            ciphertextChar = encryptedText[ciphertextPosition]
            ASCIIValue = ord(ciphertextChar)
            if ASCIIValue != 32:
                ASCIIValue -= 3             # take 3 away from ASCII value
            decryptedText += chr(ASCIIValue)
            ciphertextPosition += 1
    elif re.search("morse", encryptionMode, re.IGNORECASE):
        characters = encryptedText.split()
        for c in characters:
            decryptedText += morseAlphabet[c] # get value from dictionary 
    else:
        print("Error, no mode found!")

    decryptedText = decryptedText.lower() # only lower case required!
    return decryptedText



# save decrypted message in file
def saveMessage(inFile, decryptedText):
    # create output folder if it does not exist
    if not os.path.exists(sys.argv[2]):
        os.makedirs(sys.argv[2])

    outFile = inFile.replace(".txt", "_f63279ma.txt")

    resultFile = open(sys.argv[2] + "/" + outFile, "w")
    resultFile.write(decryptedText)
    resultFile.close()



# START
inputFiles = os.listdir(sys.argv[1])
for file in inputFiles:
    fileEncrypted = open(sys.argv[1] + "/" + file)
    stringData = fileEncrypted.read()

    decryptedText = decrypt(stringData)
    saveMessage(file, decryptedText)

    fileEncrypted.close()

