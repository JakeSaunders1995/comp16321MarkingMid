## Spellcheck program

## Past tests are green light, will test again for final
import sys, os

def writeDataToFile(filename, data):
    for i in range(len(filename)):
        if filename[i] == '.':
            fileExtention = filename[i:]
            filename = filename[:i] ## remove the file extention (most likely .txt)
            break
    else:
        fileExtention = ''
    
    fileWrite = open((folderWritePath+'/'+filename+'_'+username+fileExtention), "wt")
    fileWrite.write(data)
    fileWrite.close()

## returns true if it can find the word in the dictionary list else return false
def checkWord(word, dictWords):
    for i in dictWords:
        if word == i.strip('\n'):
            return True
    return False

## return true (if ellipsis) flase if not
def isEllipsis(index, string):
    ## first dot ahs been confirmed so lets see if there is 2 and 3
    try:
        if (string[index+1] == '.' and string[index+2] == '.'):
            return True
        return False ## if not true
    except: ## if index error thrown (out of range)
        return False

fileWordsPath = (sys.argv)[1]
folderReadPath = (sys.argv)[2] 
folderWritePath = (sys.argv)[3]

username = "j16919mb"

fileWords = open(fileWordsPath, "rt")
dictWords = fileWords.readlines()

for filename in os.listdir(folderReadPath):
    
    finalString = ""
    upperCases = 0
    punctuation = 0
    numbers = 0
    spellingError = 0
    totalWords = 0
    
    fileR = open(folderReadPath+'/'+filename, "rt")
    ## # and @ are not punctuation
    ## ... is considered as 1 

    ## formatting
    ## go through and turn all uppercase to lowercase characters
    data = fileR.read()

    ## artificial for i  in range

    i = 0 ## initalize
    while (i < len(data)):
        ## if a letter then turn to lowercase
        if ord(data[i]) > 64 and ord(data[i]) < 91: ## A to Z (capitals) 
            finalString += data[i].lower()
            upperCases += 1
        elif ord(data[i]) > 96 and ord(data[i]) < 123: ## a to z (lowercase)
            finalString += data[i]
        elif data[i] == '\n' or data[i] == ' ' or data[i] == '#' or data[i] == '@': ## space and newline char and # and @
            finalString += data[i]
        elif ord(data[i]) > 47 and ord(data[i]) < 58: ## 0-9 numbers
            numbers += 1
        ## check if its an elipsies 
        ## will only get called is the current char is a fullstop
        elif data[i] == '.' and isEllipsis(i, data): ## this function will look ahead to see if its an ellipsis
            punctuation += 1
            i += 2 ## skip over the next 2 full stops
        else:
            punctuation += 1
        i += 1 ## increment

    ## spelling
    word = ""
    for i in range(len(finalString)):
        if finalString[i] == ' ' or finalString[i] == '\n':
            if not word == '':
                totalWords += 1
                if not (checkWord(word, dictWords)): ## check if the word is spelt correctly
                    spellingError += 1
            word = ""
        else:
            word += finalString[i] ## append character onto the word
    if not word == "":
        totalWords += 1

        if not checkWord(word, dictWords):
            spellingError += 1

    ## if not a letter then get rid of it except for spaces and newline chars
    fileR.close()

    dataToWrite = ("""{0}
Formatting ###################
Number of upper case words transformed: {1}
Number of punctuation's removed: {2}
Number of numbers removed: {3}
Spellchecking ###################
Number of words in file: {4}
Number of correct words in file: {5}
Number of incorrect words in file: {6}
""".format(username, upperCases, punctuation, numbers, totalWords, (totalWords-spellingError), spellingError))

    writeDataToFile(filename, dataToWrite)

fileWords.close()
