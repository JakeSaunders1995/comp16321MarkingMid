import argparse
import glob
import string
import sys
import os

def isNumber(x):
    for i in x:
        if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
            return i
    return ""

def isUpper(x):
    for i in x:
        if not i.islower():
            return i
    return ""

def isPunct(x):
    for i in x:
        if ((i in string.punctuation or i in also) and not i in pls):
            return i
    return ""

also = "..."
pls = "@#"

parser = argparse.ArgumentParser()
parser.add_argument("allWords", type = argparse.FileType("r"))
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()

file = os.path.join(args.input, "*")
filenames = glob.glob(file)

englishWords = args.allWords.read()
englishWords = englishWords.rsplit()

for f in filenames:
    tester = open(f, "r")
    tester = tester.read()
    # for line in tester:
    #     line = line.rstrip()
    # print (tester)
    # print (tester)
    tester = tester.split(" ")
    # print(tester)

    # for thing in tester:
    #     thing = thing.replace("\n", "")
    # print (tester)
    totalWords = 0
    totalCorrect = 0
    totalWrong = 0
    totalChanged = 0
    totalPunc = 0
    totalNum = 0

    for word in tester:
        if isPunct(word) != "":
            while isPunct(word) != "":
                # print(word + " is wrong")
                totalPunc += 1
                pos = word.find(isPunct(word))
                word = word[:pos] + word[pos+1:]
                # print("I changed it to " + word)

        if isNumber(word) != "":
            while isNumber(word) != "":
                # print(word + " is wrong")
                totalNum += 1
                pos = word.find(isNumber(word))
                word = word[:pos] + word[pos+1:]
                # print("I changed it to " + word)

        if isUpper(word) != "":
            while isUpper(word) != "" and not word.islower():
                totalChanged += 1
                pos = word.find(isUpper(word))
                word = word[:pos] + word[pos:pos+1].lower() + word[pos+1:]

        if word in englishWords and word != "":
            # print(word + " is correct :)")
            totalCorrect += 1
            totalWords += 1
        elif not word in englishWords and word != "":
            # print(word + " is wrong IDIOT")
            totalWrong += 1
            totalWords += 1
        else:
            continue



        # print ("????" + word)

    filename = os.path.basename(f)
    filename = filename.split(".")
    newname = filename[0] + "_b69141na.txt"

    outputfolder = os.path.join(args.output, "")
    newpath = os.path.join(outputfolder, newname)

    filename = open(newpath, "a")

    filename.write("b69141na\n")
    filename.write("Formatting ###################")
    filename.write("\n")
    filename.write("Number of upper case letters changed: " + str(totalChanged))
    filename.write("\n")
    filename.write("Number of punctuations removed: " + str(totalPunc))
    filename.write("\n")
    filename.write("Number of numbers removed: " + str(totalNum))
    filename.write("\n")
    filename.write("Spellchecking ###################")
    filename.write("\n")
    filename.write("Number of words: " + str(totalWords))
    filename.write("\n")
    filename.write("Number of correct words: " + str(totalCorrect))
    filename.write("\n")
    filename.write("Number of incorrect words: " + str(totalWrong))
