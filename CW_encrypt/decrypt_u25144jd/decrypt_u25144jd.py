import sys
import os

# Function that decrypts Hex encryption
def hexDecrypt(encryptedString):
    newEncryptedString = encryptedString[4:]
    encryptedList = newEncryptedString.split(" ")
    decryptedString = ""
    for hexValue in encryptedList:
        decryptedString = decryptedString + chr(int(hexValue, 16))
    return decryptedString.lower()

# Function that decrypts Caesar Cipher (+3) encryption without punctuation
def caesarCipherDecrypt(encryptedString):
    newEncryptedString = encryptedString[18:]
    alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
    decryptedString = ""
    for char in newEncryptedString:
        alphabetPosition = 3
        if char in alphabet:
            while char != alphabet[alphabetPosition]:
                alphabetPosition = alphabetPosition + 1
            alphabetPosition = alphabetPosition - 3
            decryptedString = decryptedString + alphabet[alphabetPosition]
        else:
            decryptedString = decryptedString + char
    return decryptedString

# Function that decrypts Morse Code encryption
def morseCodeDecrypt(encryptedString):
    newEncryptedString = encryptedString[11:]
    encryptedList = newEncryptedString.split(" / ")
    morseCodeDict = {".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e",
                     "..-.":"f", "--.":"g", "....":"h", "..":"i", ".----":"j",
                     "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o",
                     ".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t",
                     "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y",
                     "--..":"z", ".----":"1", "..---":"2", "...--":"3", "....-":"4",
                     ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9",
                     "-----":"0", ".-.-.-":".", "--..--":",", "..--..":"?",
                     "-.-.--":"!", ".----.":"'", ".-..-":"\"", "-.--.":"(",
                     "-.--.-":")", ".-...":"&", "---...":":", "-.-.-.":";",
                     "-..-.":"/", "..--.-":"_", "-...-":"=", ".-.-.":"+",
                     "-....-":"-", "...-..-":"$", ".--.-.":"@"}
    decryptedString = ""
    for word in encryptedList:
        encryptedCharList = word.split(" ")
        for char in encryptedCharList:
            decryptedString = decryptedString + morseCodeDict[char]
        decryptedString = decryptedString + " "
    return decryptedString

# Checks to see which encryption is being used and then calls appropriate fucntion
def decryption(encryptedString):
    if encryptedString.lower()[0:3] == "hex":
        return hexDecrypt(encryptedString)

    elif encryptedString.lower()[0:17] == "caesar cipher(+3)":
        return caesarCipherDecrypt(encryptedString)

    elif encryptedString.lower()[0:10] == "morse code":
        return morseCodeDecrypt(encryptedString)

    else:
        return "This form of encryption is not supported."

inputFiles = os.listdir(sys.argv[1])
for inputFile in inputFiles:
    output = decryption(open(sys.argv[1] + inputFile, "r").read())
    outputFile = open(sys.argv[2] + inputFile[:-4] + "_u25144jd.txt", "x")
    outputFile.write(output)
