# python3 spellcheck_h86959th.py EnglishWords.txt /home/csimage/16321_python_coursework_h86959th/midterm_files/Example_inputs/Example_inputs_program3 /home/csimage/16321_python_coursework_h86959th/midterm_files/Example_outputs/Example_outputs_program3
# python3 spellcheck_h86959th.py EnglishWords.txt ./Example_inputs/Example_inputs_program3 ./Example_outputs/Example_outputs_program3

import argparse
from argparse import ArgumentParser
import os

parser = argparse.ArgumentParser() # argument setup
parser.add_argument('englishWords', type=str, help="EnglishWords.txt")
parser.add_argument('inputFolder', type=str, help="Input folder")
parser.add_argument('outputFolder', type=str, help="Output folder")
args = parser.parse_args()
inFile = ""


for filename in os.listdir(args.inputFolder): # goes thru all files in input folder
    if filename.endswith(".txt"): # goes thru all txt files

        inFile = (os.path.join(args.inputFolder, filename))
        filename = filename[:-4] + "_h86959th.txt" # removes txt and replace w ur username
        outFile = (os.path.join(args.outputFolder, filename))

        inputFile = open(inFile, "rt")
        file = inputFile.read()

        num = 0
        punc = 0
        # capital = 0
        lett = 0

        # lowercase file
        isLower = file
        isLower = isLower.islower()

        # check for ellipses using .count()
        ellipsis1 = file.count(". . .")
        file = file.replace(". . .", '')

        ellipsis2 = file.count("...")
        file = file.replace("...", '')

        punc = punc + ellipsis1 + ellipsis2

        file = file.replace("-", '')
        file = file.replace("–", '')
        file = file.replace("—", '')

        # remove numbers, punctuation, count capitals
        for word in file:
            ascVal = ord(word) # convert to ascii

            if ((ascVal >= 48) and (ascVal <= 57)): # numbers
                file = file.replace(word, '')
                num += 1
            # elif (((ascVal >= 33) and (ascVal <= 47)) or ((ascVal >= 58) and (ascVal <= 64)) or ((ascVal >= 91) and (ascVal <= 96)) or ((ascVal >= 123) and (ascVal <= 126))): # punctuation
            elif (() or ((ascVal >= 33) and (ascVal <= 34)) or ((ascVal >= 36) and (ascVal <= 47)) or ((ascVal >= 58) and (ascVal <= 63)) or  ((ascVal >= 91) and (ascVal <= 96)) or ((ascVal >= 123) and (ascVal <= 126))): # punctuation
                file = file.replace(word, '')  
                punc += 1 
            elif ((ascVal >= 65) and (ascVal <= 90)): # letters
                # if isLower == False:
                #     capital += 1 # need to change this to count ALL capital letters
                file = file.replace(word, '')
                lett += 1

        # if this doesn't work, create 3 different dictionaries and run through them then replace and increment

        compare = []
        fileLen = len(file)

        ourWords = file.lower()
        ourWords = ourWords.split(' ')

        # remove spaces 
        for element in ourWords:
            if (element != "" and element != "\n"):
                compare.append(element)

        engWords = open(args.englishWords, "rt")
        engWords = engWords.read().split('\n')

        correct = []
        incorrect = []

        count = 0

        # comparing to englishwords.txt, adding to correct or incorrect list
        for word in compare:
            checkFlag = False
            count += 1

            for entry in engWords:
                if word == entry:
                    checkFlag = True
            
            if checkFlag:
                correct.append(word)
            else:
                incorrect.append(word)

        outputText = open(outFile, "w")
        outputText.write("h86959th \nFormatting ################### \nNumber of upper case letters changed: " + str(lett) + "\nNumber of punctuations removed: " + str(punc) + "\nNumber of numbers removed: " + str(num) + "\nSpellchecking ################### \nNumber of words: " + str(count) + "\nNumber of correct words: " + str(len(correct)) + "\nNumber of incorrect words: " + str(len(incorrect)))
        outputText.close() 
