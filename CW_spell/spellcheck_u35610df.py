import os
import sys

englishFilePath = sys.argv[1]
inputFolder = sys.argv[2]
outputFolder = sys.argv[3]
inputFiles = os.listdir(inputFolder)
englishWords = open(englishFilePath, 'r')

import datetime
beginTime = datetime.datetime.now()


def binarySearch(list = [], word = '', index = 0):
    low = 0
    high = len(list)

    for i in range(0, 16):
        mid = low + (high - low) // 2

        if ord(list[mid][0]) > ord(word[0]):
            high = mid - 1
        elif ord(list[mid][0]) < ord(word[0]):
            low = mid + 1
        elif ord(list[mid][0]) == ord(word[0]):
            return list[low:high+1]


def spellCheck(string, fileName):
    global outputFolder
    # split all the words by their spaces
    splitString = string.split(' ')

    # set up variables 
    upCase = 0
    upCaseFlag = False
    punc = 0
    puncFlag = False
    numbers = 0
    numbersFlag = False
    numberWords = 0
    numberCorrect = 0

    # print(f'{splitString = }')
    for index, each in enumerate(splitString):
        if '\n' in each:
            # print(f'We know that a newline is in {each = } and {index = } so {splitString[index] = }')
            each = each.split('\n')
            # print(f'{each = }')
            splitString[index:index + 1] = each
            # print(f'{splitString = }')


    for index, each in enumerate(splitString):
        for i in range(0, len(each)):
            # check if uppercase
            if ord(each[i]) > 64 and ord(each[i]) < 91:
                tmpList = list(splitString[index])
                tmpList[i] = each[i].lower()
                splitString[index] = "".join(tmpList)
                upCaseFlag = True

            # check if number
            if ord(each[i]) >  47 and ord(each[i]) < 58:
                tmpList = list(splitString[index])
                tmpList.remove(each[i])
                splitString[index] = "".join(tmpList)
                numbersFlag = True
            
            # check if punctuation
            if (ord(each[i]) == 8230): # elipsis
                tmpList = list(splitString[index])
                tmpList.remove(each[i])
                splitString[index] = "".join(tmpList)
                puncFlag = True
            elif ord(each[i]) == 46:
            # ord(each[i+1]) == 46 and ord(each[i+2]) == 46):
                try:
                    if ord(each[i + 1]) == 46 and ord(each[i + 2]) == 46:
                        tmpList = list(splitString[index])
                        tmpList.remove(each[i] + each[i + 1] + each[i + 2])
                        splitString[index] = "".join(tmpList)
                        puncFlag = True

                except:
                    tmpList = list(splitString[index])
                    tmpList.remove(each[i])
                    splitString[index] = "".join(tmpList)
                    puncFlag = True
            elif (ord(each[i]) > 20 and ord(each[i]) < 48) or (ord(each[i]) > 90 and ord(each[i]) < 97) or (ord(each[i]) > 122 and ord(each[i]) < 127) or (ord(each[i]) > 57 and ord(each[i]) < 65):
                # print(f'Punctuation: {each[i] = }')
                tmpList = list(splitString[index])
                tmpList.remove(each[i])
                splitString[index] = "".join(tmpList)
                puncFlag = True

            # check for hyphen
            if ord(each[i]) == 8211:
                tmpList = list(splitString[index])
                tmpList.remove(each[i])
                splitString[index] = "".join(tmpList)
                puncFlag = True


            if numbersFlag:
                numbers += 1
                numbersFlag = False

            if puncFlag:
                punc += 1
                puncFlag = False
             # if any flags were set, update the variables accordingly
            if upCaseFlag:
                upCase += 1 
                upCaseFlag = False



        




    for each in splitString:
        # remove any values with no leters (empty)
        try:
            splitString.remove('')
        except:
            pass



    numberWords = len(splitString)

    for each in splitString:
        # using a binary search to narrow down if the word is in the file
        potWords = []
        potWords = binarySearch(wordList, each, index = 0)

        try:
            
            potWords.index(each)
            numberCorrect += 1
        except:
            print(f'{each = } is incorrect')
            print(f'{each in englishWords = }')
            pass

    # print(f'{splitString = }')
    # print(f'{upCase = } and {numbers = } and {punc = }')
    # print(f'{numberWords = } and {numberCorrect = } and {numberWords - numberCorrect = }')
    # print(f'time to complete: {datetime.datetime.now() - beginTime}')


    outputFileName = os.path.join(outputFolder, fileName.rstrip('.txt') + '_u35610df.txt')
    outputFile = open(outputFileName, 'w')
    content = ["u35610df\n", 'Formatting ###################\n', f'Number of upper case letters changed: {upCase}\n', f'Number of punctuations removed: {punc}\n'
        f'Number of numbers removed: {numbers}\n', 'Spellchecking ###################\n', f'Number of words: {numberWords}\n', f'Number of correct words: {numberCorrect}\n', 
        f'Number of incorrect words: {numberWords - numberCorrect}'
    ]
    outputFile.writelines(content)
    outputFile.close()

wordList = []
for line in englishWords:
    # read in all the words from the file, and strip out the '\n'
    wordList.append(line.rstrip('\n'))

for each in inputFiles:
    filename = each 
    # filepath = inputFolder + "/" + filename
    filepath = os.path.join(inputFolder, filename)
    tmpFile = open(filepath, 'r')
    string = "".join(tmpFile.readlines())
    # print(string)
    print(f'{filename = }\n\n')
    spellCheck(string, filename)
    tmpFile.close()



# TestString = "It was going to rain. The weather forecast didn't say that, but the steel plate in his hip did. He had learned over the years to trust his hip over the weatherman. It was going to rain, so he better get outside and prepare."


print('end')