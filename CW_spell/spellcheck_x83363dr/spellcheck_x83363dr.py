import argparse, re, os, pathlib

# Spellchecker

parser = argparse.ArgumentParser(description="Need a input and output file")
parser.add_argument("englishWordsFile", type=str)
parser.add_argument("inputFileDirectory", type=str)
parser.add_argument("outputFileDirectory", type=str)
args = parser.parse_args()

englishWordsFilePath = args.englishWordsFile
inputDirectory = args.inputFileDirectory
outputDirectory = args.outputFileDirectory


def Main():
    for file in os.listdir(inputDirectory):
        if file.endswith(".txt"):
            inputFilePath = inputDirectory + "/" + file
            outputFilePath = (
                outputDirectory + "/" + file.split(".")[0] + " _x83363dr" + ".txt"
            )
            fileLineContent = ""
            englishWords = ""
            with open(inputFilePath, "r") as f:
                fileLineContent = f.read()
            with open(englishWordsFilePath, "r") as f:
                englishWords = f.read().split()
            numberOfNumbersRemoved = numberOfNumbersToRemove(fileLineContent)
            fileLineContent = removeNumbers(fileLineContent)
            numberOfPunctuationRemoved = numberOfPunctuationToRemove(fileLineContent)
            fileLineContent = removePunctuation(fileLineContent)
            numberOfUpperCaseTransformed = numberOfUpperCaseToBeTransformed(
                fileLineContent
            )
            fileLineContent = toLowerCase(fileLineContent)
            words = splitString(fileLineContent)
            obj = checkWordsInList2(words, englishWords)
            wordsInEnglishWords = obj["numberOfWordsInList2"]
            wordsNotInEnglishWords = obj["numberOfWordsNotInList2"]
            linesOfOutputFile = [
                "x83363dr\n",
                "Formatting ###################\n",
                (
                    "Number of upper case letters changed: "
                    + str(numberOfUpperCaseTransformed)
                    + "\n"
                ),
                (
                    "Number of punctuations removed: "
                    + str(numberOfPunctuationRemoved)
                    + "\n"
                ),
                ("Number of numbers removed: " + str(numberOfNumbersRemoved) + "\n"),
                "Spellchecking ###################\n",
                ("Number of words: " + str(len(words)) + "\n"),
                ("Number of correct words: " + str(wordsInEnglishWords) + "\n"),
                ("Number of incorrect words: " + str(wordsNotInEnglishWords)),
            ]
            pathlib.Path(outputDirectory).mkdir(parents=True, exist_ok=True)
            writeContent = ""
            for element in linesOfOutputFile:
                writeContent += element
            with open(outputFilePath, "w") as f:
                f.write(writeContent)


def numberOfNumbersToRemove(string):
    return len(re.findall(r"\d", string))


def removeNumbers(string):
    return re.sub(r"\d+", "", string)


def numberOfPunctuationToRemove(string):
    numberOfEllipses = len(re.findall(r"\.\.\.", string))
    string = re.sub(r"\.\.\.", "", string)
    numberOfFullStops = len(re.findall(r"\.", string))
    string = re.sub(r"\.", "", string)
    numberOfOtherPunctuation = len(re.findall(r"[^\w\s@#]", string))
    return numberOfEllipses + numberOfFullStops + numberOfOtherPunctuation


def removePunctuation(string):
    return re.sub(r"[^\w\s@#]", "", string)


def numberOfUpperCaseToBeTransformed(string):
    return len(re.findall(r"[A-Z]", string))


def toLowerCase(string):
    return string.lower()


def splitString(string):
    return string.split()


def checkWordsInList2(list, list2):
    numberOfWordsInList2 = 0
    numberOfWordsNotInList = 0
    for word in list:
        if word in list2:
            numberOfWordsInList2 += 1
        else:
            numberOfWordsNotInList += 1
    return {
        "numberOfWordsInList2": numberOfWordsInList2,
        "numberOfWordsNotInList2": numberOfWordsNotInList,
    }


Main()
