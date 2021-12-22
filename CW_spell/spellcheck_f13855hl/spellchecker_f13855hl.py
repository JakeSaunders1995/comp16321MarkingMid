import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("Path_of_English_Words")
parser.add_argument("input_folder_path")
parser.add_argument("output_folder_path")


args = parser.parse_args()

englishwordspath = (args.Path_of_English_Words)
inputfolderpath = (args.input_folder_path)
outputfolderpath = (args.output_folder_path)

for filename in os.listdir(inputfolderpath):
    if filename.endswith(".txt"):
        inputfile = open(inputfolderpath + "/" + filename)

        testFile = inputfile.read()

        numbers = "1234567890"
        punctuation = '''.?!,:;/-()[]{}'"…'''
        noNumbers = ""
        noPunc = ""
        lowercharBefore = 0
        lowercharAfter = 0
        numWords = 0
        numCorrect = 0
        numWrong = 0
        i = 0

        # Remove stuff
        for char in testFile:
            if char not in numbers:
                noNumbers = noNumbers + char
        numRemoved = len(testFile) - len(noNumbers)

        for char in noNumbers:
            if char not in punctuation:
                noPunc = noPunc + char
                
        puncRemoved = len(noNumbers) - len(noPunc)

        for char in noPunc:
            if(char.islower()):
                lowercharBefore = lowercharBefore + 1

        lowercasefile = noPunc.lower()

        for char in lowercasefile:
            if(char.islower()):
                lowercharAfter = lowercharAfter + 1

        numlower = lowercharAfter - lowercharBefore
        cleantextfile = lowercasefile.replace("  "," ")

        file2 = open(englishwordspath)
        englishWords = file2.read()

        wordList = cleantextfile.split(" ")
        wordList2 = [string for string in wordList if string != ""]
        wordList3 = [string for string in wordList2 if string != "\n"]
        englishwordsList =englishWords.split("\n")

        for element in wordList3:
            if element in englishwordsList:
                numCorrect = numCorrect + 1
            else:
                numWrong = numWrong + 1

        sentence1 = "f13855hl"
        sentence2 = "\nFormatting ###################"
        sentence3 = "\nNumber of upper case letters changed: " + str(numlower)
        sentence4 = "\nNumber of punctuations removed: " + str(puncRemoved)
        sentence5 = "\nNumber of numbers removed: " + str(numRemoved)
        sentence6 = "\nSpellchecking ###################"
        sentence7 = "\nNumber of words: " + str(len(wordList3))
        sentence8 = "\nNumber of correct words: " + str(numCorrect)
        sentence9 = "\nNumber of incorrect words: " + str(numWrong)

        final = sentence1 + sentence2 + sentence3 + sentence4 + sentence5 + sentence6 + sentence7 + sentence8 + sentence9

        temp = filename.split(".")
        output_file_name = temp[0] + "_" + "f13855hl" + "." + temp[1]
        outputFile = open(outputfolderpath + "/" + output_file_name, "w")
        outputFile.write(final)
        outputFile.close()