import os
import sys
import argparse
from os import listdir
import os.path
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument("englishWords_file_path", type = str)
parser.add_argument("input_folder_path", type = str)
parser.add_argument("output_folder_path", type = str)
args=parser.parse_args()
englishWordsFile = args.englishWords_file_path
inputpath = args.input_folder_path
outputpath = args.output_folder_path

filenames = listdir(inputpath)
for k in range(len(filenames)):
    inputtext = open(inputpath + filenames[k], "r+")
    formatResult = open(outputpath + filenames[k], "w")
    englishWords = open(englishWordsFile, "r")
    
    englishWordsList = []
    for line in englishWords:
        line = line.rstrip()
        englishWordsList.append(line)

    text = inputtext.read()
    textCharList = []
    for l in range(len(text)):
        textCharList.append(text[l])
    
    uppercase = 0
    punctuation = 0
    number = 0
    for i in range(len(textCharList)):
        ASCIIValue = ord(textCharList[i])        
        if ASCIIValue == 35 or ASCIIValue == 64 or ASCIIValue == 38:
            break
        if 64 < ASCIIValue < 91:
            textCharList[i] = chr(ASCIIValue + 32)
            uppercase += 1
        elif 96 < ASCIIValue < 123 or ASCIIValue == 32:
            pass
        elif 47 < ASCIIValue < 58:
            textCharList[i] = ""
            number += 1
        else :
            textCharList[i] = ""
            punctuation += 1

    formattedText = "".join(textCharList)
    inputtext.seek(0)
    inputtext.truncate()
    inputtext.write(formattedText)


    textWordList = [str(w) for w in formattedText.split()]
    totalWord = len(textWordList)
    correctWord = 0
    for p in range(len(textWordList)):
        for q in range(len(englishWordsList)):
            if textWordList[p] == englishWordsList[q]:
                correctWord += 1
                break
    incorrectWord = totalWord - correctWord

    formatResult.write('h85345ww\nFormatting ###################\nNumber of upper case words transformed: ' + str(uppercase) \
    + '\nNumber of punctuations removed: ' + str(punctuation) \
    + '\nNumber of numbers removed: ' + str(number) \
    + '\nSpellchecking ###################\nNumber of words in file: ' + str(totalWord) \
    + '\nNumber of correct words in file: ' + str(correctWord) \
    + '\nNumber of incorrect words in file: ' + str(incorrectWord))

inputtext.close()
formatResult.close()
englishWords.close()

for k in range(len(filenames)):
    oldname = filenames[k].strip("/").split(".")
    os.rename(outputpath + filenames[k], outputpath + oldname[0] + '_h85345ww.txt')