import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("in_path", type=str)
parser.add_argument("out_path", type=str)
args = parser.parse_args()
inPath = str(args.in_path).rstrip("/")
outPath = str(args.out_path).rstrip("/")

def decodeMorse(text):
    morse = {
            ".-": 'a', "-...": 'b', "-.-.": 'c', "-..": 'd',
            ".": 'e', "..-.": 'f', "--.": 'g', "....": 'h',
            "..": 'i', ".---": 'j', "-.-": 'k', ".-..": 'l',
            "--": 'm', "-.": 'n', "---": 'o', ".--.": 'p',
            "--.-": 'q', ".-.": 'r', "...": 's', "-": 't',
            "..-": 'u', "...-": 'v', ".--": 'w', "-..-": 'x',
            "-.--": 'y', "--..": 'z',
            "-----": '0', ".----": '1', "..---": '2', "...--": '3',
            "....-": '4', ".....": '5', "-....": '6', "--...": '7',
            "---..": '8', "----.": '9',
            "/": ' ',
            ".-.-.-": '.', "--..--": ',', "..--..": '?', ".----.": '\'', "-.-.--": '!', "-..-.": '/',
            "-.--.": '(', "-.--.-": ')', ".-...": '&', "---...": ':', "-.-.-.": ';', "-...-": '=',
            ".-.-.": '+', "-....-": '-', "..--.-": '_', ".-..-.": '"', "...-..-": '$', ".--.-.": '@',
        }
    
    decrypted = ""
    words = text.split(" ")
    for w in words:
        if (w not in morse):
            # This code does not exist in International Morse Code
            # Simply returning the original characters
            decrypted += w
        else:
            decrypted += morse[w]
    
    return decrypted


def decodeHex(text):
    decrypted = ""
    words = text.split(" ")
    for w in words:
        w = w.strip(" \n")
        if (w == ""): continue
        asc = int(w, 16)
        decrypted += chr(asc)

    return decrypted 


def decodeCaesar3(text):
    decrypted = ""
    for c in text:
        if (c >= 'a') and (c <= 'z'):
            if (ord(c) - 3 < 97):
                decrypted += chr(ord(c) + 23)
            else:
                decrypted += chr(ord(c) - 3)
        else:
            decrypted += c

    return decrypted 


# Main
for fileName in os.listdir(inPath):
    inFile = open(inPath + "/" + fileName, "r") 
    outFile = open(outPath + "/" + fileName[0:-4] + "_p72426yp.txt", "w")

    s = inFile.read().rstrip("\n")
    alg, cipher = s.split(":")
    alg, cipher = alg.lower(), cipher.lower()

    ans = ""

    if ("morse" in alg):
        ans = decodeMorse(cipher)
    elif ("hex" in alg):
        ans = decodeHex(cipher)
    else:
        ans = decodeCaesar3(cipher)

    outFile.write(str(ans).lower())

    inFile.close()
    outFile.close()

