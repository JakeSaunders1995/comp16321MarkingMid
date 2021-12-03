import argparse, os, re

def HexDecrypt(cipher):
    plain = ""
    words = cipher.split()
    for w in words:
        plain += chr(int(w, 16))
    return plain

def CaesarDecrypt(cipher, k):
    plain = ""
    for ch in cipher:
        if ch == " ":
            plain += ch
        else:
            plain += chr(ord(ch) - k)
    return plain

def MorseDecrypt(cipher):
    MorseList = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
        "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
        "---": "O", ".--．": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",

        "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
        ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

        ".-.-.-": ".", "---...": ":", "--..--": ",", "-.-.-.": ";", "..--..": "?",
        "-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-",
        "..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")", "...-..-": "$",
        ".--.-.": "@", ".-.-.": "+",
    }

    plain = ""
    words = cipher.split()
    for w in words:
        if w == "/":
            plain += " "
        else:
            plain += MorseList.get(w).lower()
    return plain

parser = argparse.ArgumentParser()
parser.add_argument("inputFolder")
parser.add_argument("outputFolder")
args = parser.parse_args()

if not os.path.exists(args.inputFolder):
    print("Error! The input folder does not exist: ", args.inputFoler)
    exit(0)

if not os.path.exists(args.outputFolder):
    os.mkdir(args.outputFolder)
    print("Create new folder for output: ", args.outputFolder)

for fileName in os.listdir(args.inputFolder):
    filePath = os.path.join(args.inputFolder, fileName)
    if os.path.isdir(filePath):
        continue

    fin = open(filePath, "r")
    line = fin.readline()
    fin.close()


    line.strip()

    if line.startswith("Hex:"):
        cipherText = line[4:]
        plainText = HexDecrypt(cipherText)
    elif line.startswith("Caesar Cipher(+3):"):
        cipherText = line[18:]
        plainText = CaesarDecrypt(cipherText, 3)
    elif line.startswith("Morse Code:"):
        cipherText = line[11:]
        plainText = MorseDecrypt(cipherText)
    else:
        print("Error! Unknown encryption method in file: ", fileName)
        continue

    fname, ext = os.path.splitext(fileName)
    fname += "_g21434rb" + ext
    outputFilePath = os.path.join(args.outputFolder, fname)

    fout = open(outputFilePath, "w")
    fout.write(plainText)
    fout.close()
    print(plainText)


