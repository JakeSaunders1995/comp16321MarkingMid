import os, sys
import string

# remove digits, punctuation, upper case and count
def formatText(inputText):
    formatString = ""
    upperCount, puncCount, numberCount = 0, 0, 0
    
    for c in inputText:
        if c.isdigit():
            numberCount += 1
        elif c in string.punctuation:
            puncCount += 1
        elif c.isupper():
            upperCount += 1
            formatString += c.lower()
        else:
            formatString += c
    
    return formatString, upperCount, puncCount, numberCount

# check spelling with english file and get count
def checkSpelling(text):
    englishWords = []
    spellingCount = 0

    with open(sys.argv[1], "r") as f:
        for line in f:
            englishWords.extend(line.split())
    
    words = text.split()

    for w in words:
        if w not in englishWords:
            spellingCount += 1
    

    return len(words), spellingCount


# save stats of this file
def saveStats(inFile, upperCount, puncCount,  numberCount, wordCount, spellingCount):
    # create output folder if it does not exist
    if not os.path.exists(sys.argv[3]):
        os.makedirs(sys.argv[3])

    outFile = inFile.replace(".txt", "_f63279ma.txt")

    resultFile = open(sys.argv[3] + "/" + outFile, "w")
    
    resultFile.write("f63279ma\nFormatting ###################\n")
    resultFile.write("Number of upper case words changed: {}\n".format(upperCount))
    resultFile.write("Number of punctuations removed: {}\n".format(puncCount))
    resultFile.write("Number of numbers removed: {}\n".format(numberCount))
    resultFile.write("Spellchecking ###################\n")

    correctWords = wordCount - spellingCount
    resultFile.write("Number of words: {}\n".format(wordCount))
    resultFile.write("Number of correct words: {}\n".format(correctWords))
    resultFile.write("Number of incorrect words: {}\n".format(spellingCount))
    
    resultFile.close()


# START
inputFiles = os.listdir(sys.argv[2])
for file in inputFiles:
    textFile = open(sys.argv[2] + "/" + file)
    inputText = textFile.read()

    formatString, upperCount, puncCount, numberCount = formatText(inputText)
    wordCount, spellingCount = checkSpelling(formatString)

    saveStats(file, upperCount, puncCount,  numberCount, wordCount, spellingCount)

    textFile.close()

