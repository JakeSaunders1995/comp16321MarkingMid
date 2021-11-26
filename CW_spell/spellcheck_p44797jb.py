import os
import sys

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
uppers = ['A', 'B', 'C', 'D', 'R', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
          'V', 'W', 'X', 'Y', 'Z']
punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

args = sys.argv
if len(args) != 4:
    print("error")
else:
    dictionaryfile = args[1]
    inputdirectorypath = args[2]
    outputdirectorypath = args[3]
    if not os.path.exists(outputdirectorypath):
        os.mkdir(outputdirectorypath)

    for filename in os.listdir(inputdirectorypath):
        inputfile = inputdirectorypath + "/" + filename

        punctuationscnt = 0
        numbercnt = 0
        uppercnt = 0

        file = open(inputfile, 'r')
        line = file.read()
        file.close()

        res = ""
        for char in line:
            if char in punctuation:
                punctuationscnt += 1
            elif char in numbers:
                numbercnt += 1
            elif char in uppers:
                uppercnt += 1
                res += char.lower()
            else:
                res += char

        words = []
        for item in res.split(" "):
            if item != "" and item != "\n":
                words.append(item)

        rightcnt = 0
        wrongcnt = 0

        file = open(dictionaryfile, 'r')
        englishwords = file.readlines()
        file.close()

        dictionary = []
        for item in englishwords:
            dictionary.append(item.strip())
        for word in words:
            if word in dictionary:
                rightcnt += 1
            else:
                wrongcnt += 1

        outputfile = outputdirectorypath + '/' + filename.split(".")[0] + "_p44797jb.txt"
        file = open(outputfile, "w")
        file.write("p44797jb\n")
        file.write("Formatting ###################\n")
        file.write("Number of upper case letters changed: " + str(uppercnt) + "\n")
        file.write("Number of punctuations removed: " + str(punctuationscnt) + "\n")
        file.write("Number of numbers removed: " + str(numbercnt) + "\n")
        file.write("Spellchecking ###################" + "\n")
        file.write("Number of words: " + str(len(words)) + "\n")
        file.write("Number of correct words: " + str(rightcnt) + "\n")
        file.write("Number of incorrect words: " + str(wrongcnt) + "\n")
        file.close()
