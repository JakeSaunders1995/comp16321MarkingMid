import argparse
import os
import re

parser = argparse.ArgumentParser()
parser.add_argument("engWordsFile")
parser.add_argument("inputFolder")
parser.add_argument("outputFolder")
args = parser.parse_args()


# CREATE AND FORMAT THE WORD LIST
engWordsList = []
with open(args.engWordsFile, "r") as wordsFile:
    lines = wordsFile.readlines()
    for line in lines:
        engWordsList.append(line.strip())

punctuationString = '''!()-[]{;}:'"\,<>./?@#$%^&*_~'''

for files in os.walk(args.inputFolder):
    index = 0
    while index < len(files[2]):
        if ".txt" in files[2][index]:
            with open(args.inputFolder + "/" + files[2][index], "r") as currentFile:
                lines = currentFile.readlines()

                numbersFound = 0
                punctuationFound = 0
                upperFound = 0
                wordsList = []
                correctWordsFound = 0

                for line in lines:
                    # FORMATING CHECKING
                    for char in line:
                        if char.isdigit():              # IS NUMBER
                            numbersFound += 1
                        if char in punctuationString:        # IS PUNCTUATION
                            punctuationFound += 1;
                        if char.isupper():              # IS UPPER CHAR
                            upperFound += 1;
                    
                    # SPELL CHECKING
                    wordsList = re.findall(r"[\w']+", line)     # SPLIT THE STRINGS INTO WORDS
                    for word in wordsList:
                        if word.isdigit():                      # REMOVE DIGITS FROM LIST
                            wordsList.remove(word)
                    
                    for x in range(len(wordsList)):             # TRANSFORM TO LOWERCASE
                        wordsList[x] = wordsList[x].lower()

                    for word in wordsList:
                        for correctWord in engWordsList:
                            if word == correctWord:
                                correctWordsFound += 1          # CORRECT WORDS FOUND

                    outputInfo = ["r56677rp\n",
                                "Formatting ###################\n",
                                "Number of upper case words changed: " + str(upperFound) + "\n",
                                "Number of punctuations removed: " + str(punctuationFound) + "\n",
                                "Number of numbers removed: " + str(numbersFound) + "\n",
                                "Spellchecking ###################\n",
                                "Number of words: " + str(len(wordsList)) + "\n",
                                "Number of correct words: " + str(correctWordsFound) + "\n",
                                "Number of incorrect words: " + str(len(wordsList) - correctWordsFound) + "\n"]

                with open(args.outputFolder + "/" + files[2][index][:-4] + "_r56677rp.txt", "w") as writeFile:
                    writeFile.writelines(outputInfo)
                writeFile.close()

            currentFile.close()
        index += 1