import sys
import os

def createTextFile():
    line = everyFile
    index = line.find(".txt")
    createTextFile.output_file = line[:index] + "_h52171rh" + ".txt"
    pass

def outputFileToFolder():
        completeName = os.path.join(outputPath, createTextFile.output_file)
        #create ouput file
        file1 = open(completeName, "w")
        file1.write("h52171rh")
        file1.write("\nFormatting ###################")
        file1.write("\nNumber of upper case words changed: " + str(transformCaptoLow.capitalisations))
        file1.write("\nNumber of punctuations removed: "+ str(remove.removedPunct))
        file1.write("\nNumber of numbers removed: "  + str(remove.removedNumber))
        file1.write("\nSpellchecking ###################")
        file1.write("\nNumber of words: " + str(splitToListandSearch.correctWord + splitToListandSearch.incorrectWord))
        file1.write("\nNumber of correct words: " + str(splitToListandSearch.correctWord))
        file1.write("\nNumber of incorrect words: " + str(splitToListandSearch.incorrectWord))
        file1.close()

def remove(outputText):
    remove.removedPunct = 0
    remove.removedNumber = 0
    newText = ""
    for character in outputText:
        if  character.isalpha() == False and character != " ":
            if character.isdigit():
                remove.removedNumber += 1
                newchar = ""
            else:    
                #find any ellipses
                #remove the ellipses and count as one punt
                if character != '\\':
                    remove.removedPunct += 1
                newchar = ""
        else:
            newchar = character
        newText += newchar
    return newText

def transformCaptoLow(outputText):
    transformCaptoLow.capitalisations = 0
    newText = ""
    for character in outputText:
        if character.isupper() == True:
            transformCaptoLow.capitalisations += 1
            newchar = character.lower()
        else: 
            newchar = character
        newText += newchar
    return newText

def readDict(dictionaryPath):
    readDict.dictionary = {}
    os.chdir(os.path.dirname(os.getcwd()))
    englishWords = open(dictionaryPath)
    for line in englishWords:
        line = line.rstrip()
        readDict.dictionary[line] = ""

def splitToListandSearch(outputText):
    splitToListandSearch.correctWord = 0
    splitToListandSearch.incorrectWord = 0
    
    words = outputText.split(" ")
    
    for word in words:
        if word == "":
            words.remove("")

    for word in words: 
        if word in readDict.dictionary.keys():
            splitToListandSearch.correctWord+=1 
        else:
            splitToListandSearch.incorrectWord+=1
        pass

#reads from the command line
dictionaryPath = sys.argv[1]
inFolder = sys.argv[2]
inFolderPath = os.path.abspath(inFolder)
outFolder = sys.argv[3]

#if outFolder already exists, quit program
if os.path.exists(outFolder) == False:
    os.mkdir(outFolder)     
    outputPath = os.path.abspath(outFolder)
else:
    outputPath = os.path.abspath(outFolder)

arr = os.listdir(inFolder)

for everyFile in arr:
    if os.getcwd() != inFolderPath:
        os.chdir(inFolderPath)
    with open(everyFile,'r') as i:
        textFile = (i.readlines())
        
        newTextFile = ""
        for line in textFile:
            newline = line.rstrip()
            newTextFile += newline 
        textFile = str(newTextFile)
        textFile = textFile.replace("...", ".")
        textFile = textFile.replace("\xe2\x80\xa6", ".")    
        textFile2 = remove(textFile)
        textFile3 = transformCaptoLow(textFile2)
        readDict(dictionaryPath)
        splitToListandSearch(textFile3)
        createTextFile()
        outputFileToFolder()
    pass