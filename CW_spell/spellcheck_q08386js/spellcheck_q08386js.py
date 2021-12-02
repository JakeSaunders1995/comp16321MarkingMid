import argparse
import re 
from os import X_OK, name
import os 
parser = argparse.ArgumentParser(description='Decryption')
parser.add_argument('readWord', type=str, help='OpenDictionary')
parser.add_argument('inputcheck', type=str, help='Input Check')
parser.add_argument('outputcheck', type=str, help='Output Checked')
args = parser.parse_args()

inputDirectory = args.inputcheck
outputDirectory = args.outputcheck
Dictionary = args.readWord


for i in os.listdir(inputDirectory):
    dirname = os.path.join(inputDirectory, i)
    directory = os.path.dirname(outputDirectory)
    fileOpen = open(dirname, "r")
    wordOpen = open(Dictionary, "r")
    if outputDirectory[-1] != "/":
        nameout = outputDirectory + "/" + i.split(".txt")[0] + "_q08386js.txt"
    else:
        nameout = outputDirectory + i.split(".txt")[0] + "_q08386js.txt"
    if not os.path.exists(directory):
        os.makedirs(directory)
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    punctuations = [".","?","!",",",":",";","-","—","[","]","{","}","(",")","'","\"","…"]

    wordInput = wordOpen.read()
    stringInput = fileOpen.read()

    #counter
    upper = 0
    num = 0
    punc = 0
    for i in stringInput:    
        if i.isupper():
            upper += 1
        if i in punctuations: 
            punc += 1

    removedNumUpper = ""
    for x in stringInput.lower(): 
        if x in numbers:
            num += 1
        else:
            removedNumUpper += x

    removedNumPunc = re.sub("[^\w\s]","",removedNumUpper)

    splitRemoved = removedNumPunc.split()
    splitWords = wordInput.split()

    numberofWords = len(splitRemoved)

    correctWords = 0
    incorrectWords = 0
    for i in range(len(splitRemoved)):
        if splitRemoved[i] in splitWords:
            correctWords += 1
        else:
            incorrectWords += 1

    outputSignal = "q08386js \n" + "Formatting ################### \n" + "Number of upper case letters changed: " + str(upper) + "\n" + "Number of punctuations removed: " + str(punc) + "\n" + "Number of numbers removed: " + str(num) + "\n" + "Spellchecking ################### \n" + "Number of words: " + str(numberofWords) + "\n" + "Number of correct words: " + str(correctWords) + "\n" + "Number of incorrect words: " + str(incorrectWords) 

    writeTo = open(nameout, "w")
    writeTo.write(outputSignal)