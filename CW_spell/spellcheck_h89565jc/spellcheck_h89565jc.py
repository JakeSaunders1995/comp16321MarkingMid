import argparse
import os

# Sort out parsing from command line and get the necessary file paths
parser = argparse.ArgumentParser(description='Spell Check Text')
parser.add_argument('englishFile', type=str, help='File path to English.txt')
parser.add_argument('inFolder', type=str, help='Path of folder containing text files')
parser.add_argument('outFolder', type=str, help='Path of folder to store calculated spell check data')
args = parser.parse_args()

englishFilePath = args.englishFile
inFolderpath = args.inFolder
outFolderpath = args.outFolder

if (inFolderpath[0:-1] != "/"):
        inFolderpath += "/"

if (outFolderpath[0:-1] != "/"):
        outFolderpath += "/"

for filename in os.listdir(inFolderpath):

    # Open file for reading
    inputFileHandle = open(inFolderpath + filename, 'r')

    originalString = ''

    # Ewwww I hate python
    while (True):
        newline = inputFileHandle.readline()
        if (newline):
            newline = newline.replace('\n', ' ')
            originalString += newline
        else:
            break

    inputFileHandle.close()

    updatedString = ''
    numbersRemoved = 0
    punctuationRemoved = 0
    upperCaseTransformed = 0
    consecutiveFullStop = 0

    for char in originalString:
        # Skip processing on spaces (just there to make life easier in a minute)
        if (char == ' '):
            updatedString += ' '
        # Remove numbers and increment counter
        elif (char.isdigit()):
            numbersRemoved += 1
            consecutiveFullStop = 0
        # Check for alphaberical character
        elif (char.isalpha()):
            consecutiveFullStop = 0
            # Transform to lower case if necessary
            if(char != char.lower()):
                upperCaseTransformed += 1
                updatedString += char.lower()
            else:
                updatedString += char
        # Everything else treated as "punctuation" (removed newlines earlier so shouldn't get erroneous count hopefully)
        else:
            if (char == "."):
                consecutiveFullStop += 1
            
            if (consecutiveFullStop == 3):
                consecutiveFullStop = 0
                punctuationRemoved -= 2
            
            punctuationRemoved += 1

    # Split remaining string into words
    wordList = updatedString.split(' ')

    # Clean up the list so any empty elements are removed (symptom of the way the updated list is produced)
    while wordList.__contains__(''):
        wordList.remove('')

    # Get total number of words in file
    totalWords = len(wordList)

    # Get words to spell check against
    correctWordsFileHandle = open('EnglishWords.txt', 'r')
    correctWordList = []

    for word in correctWordsFileHandle:
        correctWordList.append(word.strip('\n'))

    correctWordsFileHandle.close()

    # Spell check words
    incorrectWords = 0
    isWordCorrect = False

    for word in wordList:
        isWordCorrect =  False
        for correctWord in correctWordList:
            if (word == correctWord):
                isWordCorrect = True
                break
        if (isWordCorrect == False):
            incorrectWords += 1


    outputFileName = filename[0:len(filename) - 4] + "_h89565jc.txt"

    # Write output to file
    outFileHandle = open(outFolderpath + outputFileName, 'w')
    outFileHandle.write('h89565jc\n')
    outFileHandle.write('Formatting ###################\n')
    outFileHandle.write('Number of upper case letters changed: %i\n' % upperCaseTransformed)
    outFileHandle.write('Number of punctuations removed: %i\n' % punctuationRemoved)
    outFileHandle.write('Number of numbers removed: %i\n' % numbersRemoved)
    outFileHandle.write('Spellchecking ###################\n')
    outFileHandle.write('Number of words: %i\n' % totalWords)
    outFileHandle.write('Number of correct words: %i\n' % (totalWords - incorrectWords))
    outFileHandle.write('Number of incorrect words: %i\n' % incorrectWords)
    outFileHandle.close()