import sys
import os

inputFile = sys.argv[2]
outFile = sys.argv[3]
textFile = sys.argv[1]

files = os.listdir(inputFile)

englishWords = []
file = open(textFile,"r")
for line in file:
    line = line.rstrip()
    englishWords += [line]
file.close()

loweralphabet = "abcdefghijklmnopqrstuvwxyz"
upperalphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"

for fileName in files:
    file = open(inputFile+"/"+fileName,"r")
    text = file.readline()
    for line in file:
        text = text + line.rstrip()
    file.close()
    caseChange = 0
    for char in text:
        if char in upperalphabet:
            text = text.replace(char,loweralphabet[upperalphabet.index(char)],1)
            caseChange += 1
    numChanged = 0
    pos = 0
    while pos < len(text):
        if text[pos] in numbers:
            numChanged += 1
            while text[pos] in numbers:
                text = text.replace(text[pos],"",1)
                if pos == len(text):
                    break
        pos += 1
    punkChanged = 0
    pos = 0
    while pos < len(text):
        if text[pos] not in numbers and text[pos] not in loweralphabet and text[pos] != " " and text[pos] != "\n":
            punkChanged += 1
            text = text.replace(text[pos],"",1)
        else:
            pos += 1
    wordStarted = False
    wordsInText = []
    word = ""
    for char in text:
        if char in loweralphabet:
            wordStarted = True
            word += char
        elif wordStarted and char not in loweralphabet:
            wordStarted = False
            wordsInText += [word]
            word = ""
    if wordStarted:
        wordsInText += [word]
    correctWords = 0
    for word in wordsInText:
        if word in englishWords:
            correctWords += 1
    words = len(wordsInText)
    incorrectWords = str(words - correctWords)
    words = str(words)
    correctWords = str(correctWords)
    caseChange = str(caseChange)
    punkChanged = str(punkChanged)
    numChanged = str(numChanged)
    file = open(outFile+"/"+fileName[:-4]+"_h10505jd.txt","w")
    file.write("h10505jd\n")
    file.write("Formatting  ###################\n")
    file.write("Number of upper case words transformed: " + caseChange + "\n")
    file.write("Number of punctuations removed: " + punkChanged + "\n")
    file.write("Number of numbers removed: " + numChanged + "\n")
    file.write("Spellchecking ###################\n")
    file.write("Number of words in file: " + words + "\n")
    file.write("Number of correct words in file: " + correctWords + "\n")
    file.write("Number of incorrect words in file: " + incorrectWords)
    file.close()
