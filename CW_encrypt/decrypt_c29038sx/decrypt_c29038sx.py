import argparse
import os

parser = argparse.ArgumentParser(description = "decryption")
parser.add_argument("input", type = str, help = "give me the source path")
parser.add_argument("output", type = str, help = "give me the targat path")
args = parser.parse_args()

morse_eng_dict = {".-":"A", "-...":"B", "-.-.":"C", "-..":"D", ".":"E", "..-.":"F", "--.":"G", 
                  "....":"H", "..":"I", ".---":"J", "-.-":"K", ".-..":"L", "--":"M", "-.":"N", 
                  "---":"O", ".--.":"P", "--.-":"Q", ".-.":"R", "...":"S", "-":"T", "..-":"U", 
                  "...-":"V", ".--":"W", "-..-":"X", "-.--":"Y", "--..":"Z", "/":" "}

def typeIdentifier(inputFile):
    f = open(inputFile)
    text = f.read()
    f.close()
    if text[0] == "H":
        return 1
    elif text[0] == "C":
        return 2
    elif text[0] == "M":
        return 3
    else:
        return 4
    
def fileExc(inputFile):
    f = open(inputFile)
    text = f.read()
    f.close()
    text = text[text.index(":") + 1:]
    return text
    
def hex(inputFile):
    text = fileExc(inputFile).split()
    result = ""
    for i in text:
        result += chr(int(i, 16))
    return result.lower()

def caesar(inputFile):
    text = fileExc(inputFile)
    text = text.lower()
    text2 = ""
    for i in text:
        if i != " " and i != "a" and i != "b" and i != "c":
            text2 += chr(ord(i) - 3)
        elif i == "a":
            text2 += "x"
        elif i == "b":
            text2 += "y"
        elif i == "c":
            text2 += "z"
        else:
            text2 += " "
    return text2
    
def morse(inputFile):
    text = fileExc(inputFile).split()
    result = ""
    for i in text:
        for j in morse_eng_dict.keys():
            if i == j:
                result += morse_eng_dict[j]
    return result.lower()
     
def decrypt(inputFile):
    if typeIdentifier(inputFile) == 4:
        print("Invalida type")
        return
    if typeIdentifier(inputFile) == 1:
        return hex(inputFile)
    if typeIdentifier(inputFile) == 2:
        return caesar(inputFile)
    if typeIdentifier(inputFile) == 3:
        return morse(inputFile)
    
def fileWriter(inputPath, outputPath):
    text = decrypt(inputPath)
    f = open(outputPath, "w")
    f.write(text)
    f.close()
    return

def checkdir(path):
    if os.path.isdir(path):
        return
    else:
        os.mkdir(path)
    return

def nameGenerater(path):
    return os.path.splitext(os.path.basename(path))[0] + "_c29038sx.txt"

def fileFilter(fileList):
    for inx, val in enumerate(fileList):
        if os.path.splitext(val)[1] != ".txt":
            del fileList[inx]

#chceking if the output directory exist, if not creat it
checkdir(args.output)

#get file list in the input folder and only take .txt file
fileList = os.listdir(args.input)
fileFilter(fileList)

for i in fileList:
    inputPath = os.path.join(args.input, i)
    outputPath = os.path.join(args.output, nameGenerater(inputPath))
    fileWriter(inputPath, outputPath)