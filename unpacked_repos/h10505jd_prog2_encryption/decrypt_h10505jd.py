import sys
import os

inputFile = sys.argv[1]
outFile = sys.argv[2]

files = os.listdir(inputFile)

morseDic = {".-":"a",
            "-...":"b",
            "-.-.":"c",
            "-..":"d",
            ".":"e",
            "..-.":"f",
            "--.":"g",
            "....":"h",
            "..":"i",
            ".---":"j",
            "-.-":"k",
            ".-..":"l",
            "--":"m",
            "-.":"n",
            "---":"o",
            ".--.":"p",
            "--.-":"q",
            ".-.":"r",
            "...":"s",
            "-":"t",
            "..-":"u",
            "...-":"v",
            ".--":"w",
            "-..-":"x",
            "-.--":"y",
            "--..":"z",
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
            ".-.-.-":".",
            "--..--":",",
            "..--..":"?",
            ".----.":"\'",
            "-.-.--":"!",
            "-..-.":"/",
            "-.--.":"(",
            "-.--.-":")",
            ".-...":"&",
            "---...":":",
            "-.-.-.":";",
            "-...-":"=",
            ".-.-.":"+",
            "-....-":"-",
            "..--.-":"_",
            ".-..-.":"\"",
            "...-..-":"$",
            ".--.-.":"@"}

alphabet = "abcdefghijklmnopqrstuvwxyz"

for fileName in files:
    file = open(inputFile+"/"+fileName,"r")
    line = file.readline()
    file.close()
    algorithm = line[:line.index(":")]
    line = line[line.index(":")+1:]
    plaintext = ""
    if algorithm == "Hex":
        while " " in line:
            hex = line[:line.index(" ")]
            line = line[line.index(" ")+1:]
            char = int(hex,16)
            char = chr(char)
            plaintext += char
        char = int(line,16)
        char = chr(char)
        plaintext += char
    elif algorithm == "Morse Code":
        while " " in line:
            char = line[:line.index(" ")]
            line = line[line.index(" ")+1:]
            char = morseDic[char]
            plaintext += char
            if line[0] == "/":
                plaintext += " "
                line = line[2:]
        char = morseDic[line]
        plaintext += char
    else:
        for char in line:
            if char == " ":
                plaintext += char
            else:
                plaintext += alphabet[alphabet.index(char)-3]
    file = open(outFile+"/"+fileName[:-4]+"_h10505jd.txt","w")
    file.write(plaintext)
    file.close()
