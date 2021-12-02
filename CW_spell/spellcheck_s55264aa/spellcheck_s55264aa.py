import re, os, sys

for file in (os.listdir(sys.argv[2])):
    f = open(os.path.join(sys.argv[2],file),"r")
    unchangedText = f.read()
    f.close()

    textWithoutNumbers = re.sub(r'[0-9]',' ',unchangedText)
    textWithoutPuncutation = re.sub(r'[^\w\s]',' ',unchangedText)
    textWithoutUpperCase = unchangedText.lower()

    def seperateWords(text):
        return(text.split())

    def compareAlterations(original, new):
        changes = 0
        for i in range(len(original)):
            if original[i] != new[i]:
                changes += 1
        return changes

    ListUnchangedText = seperateWords(unchangedText)
    ListTextWithoutNumbers = seperateWords(textWithoutNumbers)
    ListTextWithoutPuncutation = seperateWords(textWithoutPuncutation)
    ListTextWithoutUpperCase = seperateWords(textWithoutUpperCase)

    numberOfChangesNumber = compareAlterations(unchangedText, textWithoutNumbers)
    numberOfChangesPunctution = compareAlterations(unchangedText, textWithoutPuncutation)
    elipsis = unchangedText.count("...")
    numberOfChangesPunctution = numberOfChangesPunctution - (elipsis * 2)
    numberOfChangesUpperCase = compareAlterations(unchangedText, textWithoutUpperCase)


    textWithoutNumbers = re.sub(r'[0-9]',' ',unchangedText)
    textWithoutPuncutation = re.sub(r'[^\w\s]',' ',textWithoutNumbers)
    textWithoutUpperCase = textWithoutPuncutation.lower()
    newText = textWithoutUpperCase
    ListNewText = seperateWords(newText)

    Englishfile = open(sys.argv[1],"r")
    EnglishWords = Englishfile.read()
    Englishfile.close()
    EnglishWords = seperateWords(EnglishWords)

    correctWords = 0
    incorrectWords = 0
    wordFound = False
    for checkingWords in ListNewText:
        for i in range(len(EnglishWords)):
            if checkingWords == EnglishWords[i]:
                correctWords += 1
                wordFound = True   
        if wordFound == False:
            incorrectWords += 1
        wordFound = False


    newFile = open(os.path.join(sys.argv[3],file[0:len(file) - 4] + "_s55264aa.txt"),"w")
    newFile.write("s55264aa \n")
    newFile.write("Formatting ################### \n")
    newFile.write(f"Number of upper case words changed: {numberOfChangesUpperCase} \n")
    newFile.write(f"Number of punctuations removed: {numberOfChangesPunctution} \n")
    newFile.write(f"Number of numbers removed: {numberOfChangesNumber} \n")
    newFile.write("Spellchecking ################### \n")
    newFile.write(f"Number of words: {len(ListNewText)} \n")
    newFile.write(f"Number of correct words: {correctWords} \n")
    newFile.write(f"Number of incorrect words: {incorrectWords}")
    newFile.close()
