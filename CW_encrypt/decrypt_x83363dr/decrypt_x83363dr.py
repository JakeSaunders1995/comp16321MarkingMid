import argparse, re, os, pathlib

# Decrypt

parser = argparse.ArgumentParser(description="Need a input and output file")
parser.add_argument("inputFileDirectory", type=str)
parser.add_argument("outputFileDirectory", type=str)
args = parser.parse_args()

inputDirectory = args.inputFileDirectory
outputDirectory = args.outputFileDirectory


def findKindOfCipher(fileLineContent):
    if re.match(r"^Hex:", fileLineContent):
        return "Hex"
    elif re.match(r"^Caesar Cipher\(\+3\):", fileLineContent):
        return "Caesar Cipher (+3)"
    elif re.match(r"^Morse Code:", fileLineContent):
        return "Morse Code"


def decryptHex(fileLinesContent):
    newFileLineContents = []
    plainText = ""
    for line in fileLinesContent:
        hexValues = re.findall(r"[A-Za-z0-9]+", line)
        if hexValues != []:
            if hexValues[0] == "Hex":
                hexValues.pop(0)
        plainText = ""
        for item in hexValues:
            plainText += chr(int(item, 16))
        newFileLineContents.append(plainText.lower())
    finalFileContent = ""
    for item in newFileLineContents:
        finalFileContent += item + "\n"
    return finalFileContent


def decryptCaeserCipher(fileContent):
    cipherText = fileContent[18:]
    plainText = ""
    for character in cipherText:
        if (
            character != " "
            and character != "\n"
            and character != "&"
            and character != "C"
        ):
            plainText += chr((ord(character) - 3 - ord("a")) % 26 + ord("a"))
        else:
            if character == "&":
                plainText += "#"
            elif character == "C":
                plainText += "@"
            else:
                plainText += character
    return plainText.lower()


def decryptMorseCode(fileLinesContent):
    morseCodeDictionary = {
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
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
        "-----": "0",
        "--..--": ", ",
        ".-.-.-": ".",
        "..--..": "?",
        "-..-.": "/",
        "-....-": "-",
        "-.--.": "(",
        "-.--.-": ")",
        " ": "",
        "/": " ",
    }
    newFileLineContents = []
    for i in range(0, len(fileLinesContent)):
        cipherText = ""
        plainText = ""
        code = ""
        if i == 0:
            cipherText = fileLinesContent[i]
            cipherText = cipherText[11:]
        else:
            cipherText = fileLinesContent[i]
        for element in cipherText:
            if element != " " and element != "/":
                code += element
            elif element == " ":
                if code != "":
                    plainText += morseCodeDictionary[code]
                code = ""
            elif element == "/":
                plainText += " "
                code = ""
        if code != "":
            plainText += morseCodeDictionary[code]
        newFileLineContents.append(plainText.lower())
    finalFileContent = ""
    for item in newFileLineContents:
        finalFileContent += item + "\n"
    return finalFileContent


for file in os.listdir(inputDirectory):
    if file.endswith(".txt"):
        inputFilePath = inputDirectory + "/" + file
        outputFilePath = (
            outputDirectory + "/" + file.split(".")[0] + " _x83363dr" + ".txt"
        )
        fileContent = ""
        fileLinesContent = []
        plainText = ""
        with open(inputFilePath, "r") as f:
            fileContent = f.read()
        fileLinesContent = fileContent.split("\n")
        kindOfCipher = findKindOfCipher(fileContent)
        if kindOfCipher == "Hex":
            plainText = decryptHex(fileLinesContent)
        elif kindOfCipher == "Caesar Cipher (+3)":
            plainText = decryptCaeserCipher(fileContent)
        elif kindOfCipher == "Morse Code":
            plainText = decryptMorseCode(fileLinesContent)
        pathlib.Path(outputDirectory).mkdir(parents=True, exist_ok=True)
        outputFileContents = plainText
        with open(outputFilePath, "w") as f:
            f.write(outputFileContents)
