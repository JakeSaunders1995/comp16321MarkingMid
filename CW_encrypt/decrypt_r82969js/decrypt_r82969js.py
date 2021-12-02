import argparse
import os


def determineEncryption(cipher):
    encryption = cipher[0]
    if encryption == "H":
        return "hex"
    elif encryption == "C":
        return "caesar"
    elif encryption == "M":
        return "morse"


def trimCipher(cipher):
    cipher = cipher.split()
    if cipher[0] == "Caesar" or cipher[0] == "Morse":
        cipher.pop(0)
    tmpstring = cipher[0]
    result = ""
    for i in range(len(tmpstring)):
        eachChar = tmpstring[i]
        if eachChar == ":":
            for j in range(i + 1, len(tmpstring)):
                result += tmpstring[j]
            cipher[0] = result
            break
    return cipher


def decodeHex(cipher):
    final_out = ""
    for i in range(len(cipher) - 1):
        nxtword = cipher[i + 1]
        if nxtword == "/" and i != len(cipher) - 2:
            final_out += " "
        elif i == len(cipher) - 2:
            if cipher[i] == "/":
                finalword = bytes.fromhex(cipher[i + 1]).decode("ascii")
                final_out += " " + finalword
            else:
                eachword = bytes.fromhex(cipher[i]).decode("ascii")
                finalword = bytes.fromhex(cipher[i + 1]).decode("ascii")
                final_out = final_out + eachword + finalword
        else:
            eachword = bytes.fromhex(cipher[i]).decode("ascii")
            final_out += eachword
    return final_out


def decodeCaesar(cipher):
    final_out = ""
    for eachword in range(len(cipher)):
        for eachchar in cipher[eachword]:
            if 64 < ord(eachchar) - 3 <= 96:
                plainChar = chr(123 - (abs(ord(eachchar) - 3 - 97)))
            else:
                plainChar = chr(ord(eachchar) - 3)
            final_out += plainChar
        final_out += " "
    return final_out


def decodeMorse(cipher):
    morseDict = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        ",": "--..--",
        ".": ".-.-.-",
        "?": "..--..",
        "/": "-..-.",
        "-": "-....-",
        "(": "-.--.",
        ")": "-.--.-",
        "!": "-.-.--",
        "'": ".----.",
        "@": ".--.-.",
        "&": ".-...",
        ":": "---...",
        "=": "-...-",
        "%": "-..-.",
        "+": ".-.-.",
    }
    final_out = ""
    for i in range(len(cipher)):
        if cipher[i] == "/":
            final_out += " "
        else:
            for eachChar in morseDict:
                if morseDict[eachChar] == cipher[i]:
                    final_out += eachChar
                else:
                    continue
    return final_out


parser = argparse.ArgumentParser(description="decryptor")
parser.add_argument("input_folder_location", metavar="inp", type=str)
parser.add_argument("output_folder_location", metavar="outp", type=str)
args = parser.parse_args()
inputFolder = args.input_folder_location
outputFolder = args.output_folder_location

for eachFile in os.scandir(inputFolder):
    inFile = open(eachFile.path, "r")
    newstr = os.path.basename(eachFile.path)[:-4]
    outFile = open(outputFolder + "/" + newstr + "_r82969js.txt", "w")
    cipher = inFile.readline()
    encryptionType = determineEncryption(cipher)
    cipher = trimCipher(cipher)
    if encryptionType == "hex":
        plaintxt = decodeHex(cipher)
    elif encryptionType == "caesar":
        plaintxt = decodeCaesar(cipher)
    elif encryptionType == "morse":
        plaintxt = decodeMorse(cipher)
    outFile.write(plaintxt)
    inFile.close()
    outFile.close()
