import argparse
import glob
import sys
import os

def MorseDictator(x):
    if x == ".-":
        return "a"
    elif x == "-...":
         return "b"
    elif x == "-.-.":
         return "c"
    elif x == "-..":
        return "d"
    elif x == ".":
        return "e"
    elif x == "..-.":
        return "f"
    elif x == "--.":
        return "g"
    elif x == "....":
        return "h"
    elif x == "..":
        return "i"
    elif x == ".---":
        return "j"
    elif x == "-.-":
        return "k"
    elif x == ".-..":
        return "l"
    elif x == "--":
        return "m"
    elif x == "-.":
        return "n"
    elif x == "---":
        return "o"
    elif x == ".--.":
        return "p"
    elif x == "--.-":
        return "q"
    elif x == ".-.":
        return "r"
    elif x == "...":
        return "s"
    elif x == "-":
        return "t"
    elif x == "..-":
        return "u"
    elif x == "...-":
        return "v"
    elif x == ".--":
        return "w"
    elif x == "-..-":
        return "x"
    elif x == "-.--":
        return "y"
    elif x == "--..":
        return "z"
    elif x == "-----":
        return "0"
    elif x == ".----":
        return "1"
    elif x == "..---":
        return "2"
    elif x == "...--":
        return "3"
    elif x == "....-":
        return "4"
    elif x == ".....":
        return "5"
    elif x == "-....":
        return "6"
    elif x == "--...":
        return "7"
    elif x == "---..":
        return "8"
    elif x == "----.":
        return "9"
    elif x == ".-.-.-":
        return "."
    elif x == "--..--":
        return ","
    elif x == "..--..":
        return "?"
    elif x == ".----.":
        return "'"
    elif x == "-.-.--":
        return "!"
    elif x == "-..-.":
        return "/"
    elif x == "-.--.":
        return "("
    elif x == "-.--.-":
        return ")"
    elif x == ".-...":
        return "&"
    elif x == "---...":
        return ":"
    elif x == "-.-.-.":
        return ";"
    elif x == "-...-":
        return "="
    elif x == ".-.-.":
        return "+"
    elif x == "-....-":
        return "-"
    elif x == "..--.-":
        return "_"
    elif x == ".-..-.":
        return '"'
    elif x == "...-..-":
        return "$"
    elif x == ".--.-.":
        return "@"
    elif x == ".-.-.-.-.-.-.-.-.-":
        return "..."
parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()

file = os.path.join(args.input, "*")
filenames = glob.glob(file)

for f in filenames:
    msg = open(f, "r")
    msg = msg.read()

    hexCase = msg.split(" ")

    i = 0
    count = 0
    pos = 0
    hResult = ""
    cResult = ""
    mResult = ""
    result = ""
    alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
    msg = msg.replace("\n","")

    if msg.startswith("H"):
        while i < len(hexCase):
            if i == 0:
                    letter = chr(int(hexCase[0][4:], 16))
                    hResult += letter
            else:
                    letter = chr(int(hexCase[i][0:], 16))
                    hResult += letter
            i += 1

        result = hResult.lower()

    elif msg.startswith("C"):
        msg = msg.lower()
        msg = msg.replace("\n","")
        while pos < len(msg):
            if pos == 0:
                currentChar = msg[18]
                alphPos = 3
                if currentChar == " ":
                    pos = 19
                    cResult += " "
                    continue

                while currentChar != alphabet[alphPos]:
                    alphPos +=1
                else:
                    alphPos -= 3
                    cResult += alphabet[alphPos]
                    pos = 19

            else:
                currentChar = msg[pos]
                alphPos = 3
                if currentChar == " ":
                    pos += 1
                    cResult += " "
                    continue
                while currentChar != alphabet[alphPos]:
                    alphPos +=1
                else:
                    alphPos -= 3
                    cResult += alphabet[alphPos]
                    pos += 1

        result = cResult.lower()

    elif msg.startswith("M"):
        while count < len(hexCase):
            if count == 0:
                count += 1
                continue
            elif count == 1:
                if hexCase[count] == "/":
                    mResult += " "
                    count += 1
                    continue
                currentChar = MorseDictator(hexCase[count][5:])
                mResult += currentChar
            else:
                if hexCase[count] == "/":
                    mResult += " "
                    count += 1
                    continue
                currentChar = MorseDictator(hexCase[count])
                mResult += currentChar
            count +=1

        result = mResult.lower()

    filename = os.path.basename(f)
    filename = filename.split(".")
    newname = filename[0] + "_b69141na.txt"

    outputfolder = os.path.join(args.output, "")
    newpath = os.path.join(outputfolder, newname)

    filename = open(newpath, "a")

    filename.write(result)
