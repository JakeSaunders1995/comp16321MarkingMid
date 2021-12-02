import os
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input",type = str, help = "the file to input the text in")
parser.add_argument("output", type = str, help = "the file to output the text in")
args = parser.parse_args()

inputDir = args.input
outputDir = args.output

# input = ""
# output = ""

def hex(Finaloutputfile,inputfile):
    file = open(inputfile)
    for line in file:
        newLine = re.sub(r"\s+", "", line)
        start = newLine.index(":")
        newLine = newLine[start+1:]

    plainText = bytes.fromhex(newLine)
    plainText = plainText.decode("ascii")
    
    outputfile = open(Finaloutputfile,"w")
    outputfile.write(plainText.lower())
  
def morse(Finaloutputfile,inputfile):
    MorseDic = {        'A':'.-',    'B':'-...',
                        'C':'-.-.',  'D':'-..',   'E':'.',
                        'F':'..-.',  'G':'--.',   'H':'....',
                        'I':'..',    'J':'.---',  'K':'-.-',
                        'L':'.-..',  'M':'--',    'N':'-.',
                        'O':'---',   'P':'.--.',  'Q':'--.-',
                        'R':'.-.',   'S':'...',   'T':'-',
                        'U':'..-',   'V':'...-',  'W':'.--',
                        'X':'-..-',  'Y':'-.--',  'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ', ':'--..--', '.':'.-.-.-',
                        '?':'..--..',' ':'/', '-':'-....-',
                        '(':'-.--.', ')':'-.--.-',':':'---...',
                        '"':'.-..-.', ';':'-.-.-.','-':'-....-',
                        '!':'-.-.--'}

    morsecipher = ""
    file = open(inputfile)
    for line in file:
        start = line.index(":")
        line = line[start+1:]

    line = line.split(" ")
    keyList = list(MorseDic.keys())
    valList = list(MorseDic.values())

    for i in line:
        position = valList.index(i)
        morsecipher+= keyList[position]

    
    outputfile = open(Finaloutputfile,"w")
    outputfile.write(morsecipher.lower())

def caser(Finaloutputfile,inputfile):
    alpha = "abcdefghijklmnopqrstuvwxyz \n1234567890xyz"
    ciphertext = ''

    alphaposition = 0

    lineposition = 0
    file = open(inputfile)
    for line in file:
        start = line.index(":")
        line = line[start+1:]


    while len(ciphertext) < len(line):
        while alpha[alphaposition] != line[lineposition]:
            alphaposition += 1
        if alpha[alphaposition] == "\n":
            ciphertext+="\n"
            lineposition+=1
            alphaposition = 0
        elif alpha[alphaposition] == " ":
            ciphertext+=" "
            lineposition+=1
            alphaposition = 0
        elif alpha[alphaposition].isdigit():
            ciphertext += alpha[alphaposition]
            lineposition+=1
            alphaposition = 0
        else:
            ciphertext = ciphertext + alpha[int(alphaposition)-3]
            lineposition+=1
            alphaposition = 0
    
    outputfile = open(Finaloutputfile,"w")
    outputfile.write(ciphertext.lower())
   
for file in os.listdir(inputDir):
    inputfile = os.path.join(inputDir,file)
    name = file.split(".")[0]
    name = name + "_h48741ew.txt"
    outputdest = os.path.join(outputDir,name)
    openfile = open(inputfile)
    for line in openfile:
        if "Morse" in line:
            morse(outputdest,inputfile)
        elif "Hex" in line:
            hex(outputdest,inputfile)
        elif "Caesar" in line:
            caser(outputdest,inputfile)
        else:
            continue
