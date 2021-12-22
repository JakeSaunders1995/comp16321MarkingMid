import re
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("cheese", type=str, nargs="+")
path = parser.parse_args()

scanned = os.scandir(path.cheese[0])
directories = []
for j in scanned:
    directories.append(j.path)
directories = sorted(directories)
fileNo = 1;
for i in directories:

    def check(listOfThings):
        Count =0;
        for i in range(len(text)):
            for j in range(len(listOfThings)):
                if (listOfThings[j] == text[i]):
                    Count+=1;
        return Count;
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    pattern = r'[0-9]'
    punctuation = "!\"$%&'()*+,-./:;<=>?[\]^_`{|}~"
    capitalCount = 0; punctuationCount = 0; wordCount = 0; correctCount = 0; wordFound = False; noPunctuation = ""

    w = open(i, "r")
    text = w.readline()
    numbersCount = check(numbers)
    punctuationCount = check(punctuation)
    text = re.sub(pattern, '', text)
    textList = text.lower()
    textList = textList.split()


    for i in range(len(textList)):
        textList[i] = re.sub(r'[^\w\s]', '', textList[i])


    #counts the capital letters
    for i in range(len(text)):
        if text[i].isupper():
            capitalCount+=1

    englishWords = open(r"/home/csimage/Desktop/midterm_files/EnglishWords.txt")
    englishArray = englishWords.readlines()
    for i in range(len(englishArray)):
        englishArray[i] = englishArray[i].strip("\n")

    for i in range(len(textList)):
        if textList[i] in englishArray:
            correctCount +=1

    incorrectCount = len(textList) - correctCount
    output = ("z34983bo \n Formatting ######## \n Number of upper case letters changed: " + str(capitalCount) + "\n Number of punctuations removed: " + str(punctuationCount) + "\n Number of numbers removed: " + str(punctuationCount) + "\n Spell Checking ######## \n Number of words: " + str(len(textList)) + "\n Number of correct words: " + str(correctCount) + "\n Number of incorrect words: " +  str(incorrectCount))
    file = open(path.cheese[1]+"/test_file" + str(fileNo) + "_z34983bo.txt", "w")
    fileNo+=1

    file.write(output)
    file.close()
