import argparse
import os
import string

#Command Line Arguments
parser = argparse.ArgumentParser()
parser.add_argument('dictionary' , type=str)
parser.add_argument('inputFolder',type=str)
parser.add_argument('outputFolder', type=str)
args = parser.parse_args()

words = []
with open(args.dictionary, "r") as dictFile:
    for line in dictFile:
        words.append(line.replace("\n",""))

for j in range (len(os.listdir(args.inputFolder))):
    if (os.listdir(args.inputFolder)[j].__contains__(".txt")):
        iFile = open(os.path.join(args.inputFolder, os.listdir(args.inputFolder)[j]), "r")
        inputStr = iFile.read()
        
        #Formatting part
        #Number of UpperCase characters and Punctuation
        upperCaseCount = 0
        punctuationCount = 0
        numberCount = 0
        for i in range(len(inputStr)):
            if (inputStr[i].isupper()):
                upperCaseCount = upperCaseCount + 1
            if (string.punctuation.__contains__(inputStr[i])):
                punctuationCount = punctuationCount + 1
            if (inputStr[i].isdigit()):
                numberCount = numberCount + 1

        #Remove all upper case characters
        inputStr = inputStr.lower()
        #Remove all punctuations
        for i in range(len(string.punctuation)):
            inputStr = inputStr.replace(string.punctuation[i],"")  
        #Remove all numbers
        emptyStr = ""
        inputStr = emptyStr.join(a for a in inputStr if not a.isdigit())

        #Spellchecking part
        arrayOfWords = inputStr.split(" ")
        correctWordCount = 0
        incorrectWordCount = 0 
        for word in arrayOfWords:
            if (word != ""):
                if (words.__contains__(word)):
                    correctWordCount = correctWordCount + 1
                else:
                    incorrectWordCount = incorrectWordCount + 1

        outputFileName = os.listdir(args.inputFolder)[j].replace(".txt","") + "_y78202oa.txt"
        pathToSave = os.path.join(args.outputFolder, outputFileName)
        oFile = open(pathToSave, "w+")
        oFile.write("y78202oa\n")
        oFile.write("Formatting ###################\n")
        oFile.write("Number of upper case words changed: " + str(upperCaseCount) + "\n")
        oFile.write("Number of punctuations removed: " + str(punctuationCount)+ "\n")
        oFile.write("Number of numbers removed: " + str(numberCount)+ "\n")
        oFile.write("Spellchecking ###################\n")
        oFile.write("Number of words: " + str(correctWordCount + incorrectWordCount)+ "\n")
        oFile.write("Number of correct words: " + str(correctWordCount)+ "\n")
        oFile.write("Number of incorrect words: " + str(incorrectWordCount)+ "\n")
        oFile.close()
        

        





                 