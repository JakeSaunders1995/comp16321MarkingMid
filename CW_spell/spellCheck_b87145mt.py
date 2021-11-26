import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("EnglishWordstxt", help="File path for the english words text file", type=str)
parser.add_argument("InputDir", help="Input file path", type=str)
parser.add_argument("OutputDir", help="Output file path", type=str)
args = parser.parse_args()

dictionaryDirectory = args.EnglishWordstxt + "/EnglishWords.txt"
fileList = os.listdir(args.InputDir)
outputDirectory = args.OutputDir


dictionaryList = []
punctuation = ".?!,:;-[]{}()'\"@#~<>|\\`¬£$%^&*/"
numbers = "1234567890"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


#Fills the wordsList with the each line in the EnglishWords.txt file
w = open(dictionaryDirectory, "r")
for line in w:
    line = line.rstrip()
    dictionaryList.append(line)
w.close()

#input = "The alarm went off and Jake rose awake. Rising early had become a daily ritual, one that he could not fully explain. From the outside, it was a wonder that he was able to get up so early each morning for someone who had absolutely no plans to be productive during the entire day."




#Gets the name of each individual file in the input directory
def GetFileName(inputFile):
    count = 0
    name = ""
    while count < len(inputFile) and inputFile[count] != ".":
        name = name + inputFile[count]
        count += 1
    return name



#Will be used for detecting if a string is either punctuation or a number
def DetectInSet(chara,set):
    detected = False
    if chara in set:
        detected = True
    return detected



def CheckWordCorrect(word, dictionary):
    count = 0
    found = False
    while (count < len(dictionary)) and (not found):
        if word == dictionary[count]:
            found = True
        count += 1
    return found



def ListInputWords(inputString):
    wordList = []
    currentWord = ""
    for i in range(len(inputString)):
        if (inputString[i] == " ") and (len(currentWord) > 0) or (i == len(inputString) - 1):
            if i == (len(inputString) -1):
                currentWord = currentWord + inputString[i]
            if currentWord.strip() != "":
                wordList.append(currentWord.strip())
            currentWord = ""
        elif inputString != " ":
            currentWord = currentWord + inputString[i]
    return wordList




def GiveOutput(caps,puncts,nums,tot,cor,incor,outPath,inputName):
    outputName = outPath + "/" + inputName + "_b87145mt.txt"
    out = open(outputName, "w")
    out.write("b87145mt\n")
    out.write("Formatting ###################\n")
    out.write("Number of upper case letters changed: " + str(caps) + "\n")
    out.write("Number of punctuations removed: " + str(puncts) + "\n")
    out.write("Number of numbers removed: " + str(nums) + "\n")
    out.write("Spellchecking ###################\n")
    out.write("Number of words: " + str(tot) + "\n")
    out.write("Number of correct words: " + str(cor) + "\n")
    out.write("Number of incorrect words: " + str(incor) + "\n")
    out.close()








for fileNumber in range(len(fileList)):
    fileName = fileList[fileNumber]
    location = args.InputDir + "/" + fileName
    f = open(location, "r")
    input = f.read()
    f.close()




    capsTransformed = 0
    punctsRemoved = 0
    numsRemoved = 0
    newString = ""

    correctWords = 0
    incorrectWords = 0
    wordCount = 0


    for i in range(len(input)):
        isCap = DetectInSet(input[i],capital)
        isNum = DetectInSet(input[i],numbers )
        isPunct = DetectInSet(input[i],punctuation)
        if (not isCap) and (not isNum) and (not isPunct):
            newString = newString + input[i]
        elif isCap:
            capsTransformed += 1
            newString = newString + input[i].lower()
        elif isNum:
            numsRemoved += 1
        elif isPunct:
            punctsRemoved += 1

    inputWords = ListInputWords(newString)

    for i in range(len(inputWords)):
        realWord = CheckWordCorrect(inputWords[i], dictionaryList)
        if realWord:
            correctWords += 1
        else:
            incorrectWords +=1
        wordCount += 1

    fileTitle = GetFileName(fileName)

    GiveOutput(capsTransformed,punctsRemoved,numsRemoved,wordCount,correctWords,incorrectWords,outputDirectory,fileTitle)
