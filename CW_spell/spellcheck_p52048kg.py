import sys
import os

punctuationList = ['.', '?', '!', ',', ':', ';', '‐', '‒', '(', ')', '[', ']', '{', '}', '\'', '"', '@', '#', '&', '%']
numberList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
upperCaseList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
formattingLine = "Formatting ###################"
spellcheckLine = "Spellchecking ###################"

englishFile = sys.argv[1]
inputFolder = sys.argv[2]
outputFolder = sys.argv[3]

engFile = open(englishFile, "rt")
engWords = engFile.readlines()
for i in range (len(engWords)):
    engWords[i] = engWords[i][:-1]

for filename in os.listdir(inputFolder):
    if filename.endswith(".txt"):
        if inputFolder.endswith("/"):
            inputFile = inputFolder+filename
        else:
            inputFile = inputFolder+"/"+filename

        outputFile = filename[:-4]+"_p52048kg"+".txt"
        if outputFolder.endswith("/"):
            outputPath = outputFolder+outputFile
        else:
            outputPath = outputFolder+"/"+outputFile

        file = open(str(inputFile), "rt")

        upperCaseCount = 0
        punctuationCount = 0
        numberCount = 0
        wordCount = 0
        correctWordCount = 0
        incorrectWordCount = 0

        data = file.read()
        data = data + " "
        word = ""

        for character in data:

            if (character == " ") and (word != ""):
                wordCount += 1
                if word in engWords:
                    correctWordCount += 1
                else:
                    incorrectWordCount += 1
                word = ""
            elif (character == " ") and (word == ""):
                pass
            elif character in punctuationList:
                punctuationCount += 1
            elif character in upperCaseList:
                upperCaseCount += 1
                word = word + character.lower()
            elif character in numberList:
                numberCount += 1
            elif character == "\n":
                pass
            else:
                word = word + character

        file.close()

        file = open(str(outputPath), "wt")

        spellCheckData = "p52048kg" + "\n" + formattingLine + "\n" + "Number of upper case words changed: "+ str(upperCaseCount) + "\n" + "Number of punctuations removed: " + str(punctuationCount) + "\n" + "Number of numbers removed: " + str(numberCount) + "\n" + spellcheckLine + "\n" + "Number of words: " + str(wordCount) + "\n" + "Number of correct words: " +  str(correctWordCount) + "\n" + "Number of incorrect words: " + str(incorrectWordCount)
        file.writelines(spellCheckData)
        file.close()

    else:
        pass

engFile.close()
