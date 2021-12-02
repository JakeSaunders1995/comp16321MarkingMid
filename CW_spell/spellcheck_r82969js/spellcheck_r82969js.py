import argparse, re, os


def formatting(string):
    initialString = len(string)
    string = "".join([i for i in string if not i.isdigit()])
    numRemoved = initialString - len(string)
    initialString = len(string)
    string = re.sub(r"[^\w\s]", "", string)
    puncRemoved = initialString - len(string)
    upperTransformed = 0
    for eachChar in string:
        if eachChar.isupper():
            upperTransformed += 1
    string = string.lower()
    return string, upperTransformed, puncRemoved, numRemoved


def spellCheck(string, correctList):
    checkList = string.split()
    numOfWords = len(checkList)
    wrongNum = 0
    correctNum = 0
    for eachWord in range(numOfWords):
        curWord = checkList[eachWord]
        correctSpelling = False
        while not correctSpelling:
            for i in range(len(correctList)):
                if curWord == correctList[i]:
                    correctNum += 1
                    correctSpelling = True
                    break
            if correctSpelling == False:
                wrongNum += 1
                break
    return numOfWords, correctNum, wrongNum


parser = argparse.ArgumentParser(description="spell check")
parser.add_argument("english_words_file", metavar="engFile", type=str)
parser.add_argument("input_folder_location", metavar="inp", type=str)
parser.add_argument("output_folder_location", metavar="outp", type=str)
args = parser.parse_args()
dictionaryLocation = args.english_words_file
dictionary = open(dictionaryLocation, "r")
correctList = dictionary.readlines()
for i in range(len(correctList)):
    correctList[i] = correctList[i].strip()
inputFolder = args.input_folder_location
outputFolder = args.output_folder_location

for eachFile in os.scandir(inputFolder):
    inFile = open(eachFile.path, "r")
    newstr = os.path.basename(eachFile.path)[:-4]
    outFile = open(outputFolder + "/" + newstr + "_r82969js.txt", "w")
    original = inFile.readline()
    formatted, upperTrans, punRe, numRe = formatting(original)
    altered = False
    wordTotal, correctTotal, incorrectTotal = spellCheck(formatted, correctList)

    outFile.write("r82969js\n")
    outFile.write(f"Formatting {20*'#'}\n")
    outFile.write(f"Number of upper case words transformed: {upperTrans}\n")
    outFile.write(f"Number of punctuation's removed: {punRe}\n")
    outFile.write(f"Number of numbers removed: {numRe}\n")
    outFile.write(f"SpellChecking {20*'#'}\n")
    outFile.write(f"Number of words in file: {wordTotal}\n")
    outFile.write(f"Number of correct words in file: {correctTotal}\n")
    outFile.write(f"Number of incorrect words in file: {incorrectTotal}\n")

    inFile.close()
    outFile.close()
