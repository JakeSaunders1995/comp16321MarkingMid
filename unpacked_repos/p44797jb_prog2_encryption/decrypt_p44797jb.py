import os
import sys

morsechardict = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h',
                  '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p',
                  '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
                  '-.--': 'y', '--..': 'z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
                  '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'}



args = sys.argv
if len(args) != 3:
    print("error")
else:
    inputdirectorypath = args[1]
    outputdirectorypath = args[2]
    if not os.path.exists(outputdirectorypath):
        os.mkdir(outputdirectorypath)
    for filename in os.listdir(inputdirectorypath):
        inputfilepath = inputdirectorypath + "/" + filename

        file = open(inputfilepath, 'r')
        line = file.read()
        file.close()

        linesplit = line.split(":")
        algo = linesplit[0]
        cipher = linesplit[1].strip()

        cipherlist = cipher.split(' ')
        result = ""
        if algo == "Hex":
            for item in cipherlist:
                result += chr(int(item, 16))
        elif algo == "Caesar Cipher(+3)":
            for char in cipher:
                if char == " ":
                    result += char
                elif ord(char) - 3 < 97:
                    result += chr(ord(char) - 3 + 26)
                else:
                    result += chr(ord(char) - 3)
        elif algo == "Morse Code":
            for item in cipherlist:
                if item == "/":
                    result += " "
                else:
                    result += morsechardict[item]

        outputfilename = outputdirectorypath + "/" + filename.split(".")[0] + "_p44797jb.txt"
        file = open(outputfilename, "w")
        file.write(result.lower())
        file.close()
