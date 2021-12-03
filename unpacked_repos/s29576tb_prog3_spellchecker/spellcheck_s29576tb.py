
import sys
import re
import os

inputFile = sys.argv[2]
outputFile = sys.argv[3]

wordsList= []
# Open input file and read lines
for file in os.listdir(inputFile):
    with open(os.path.join(inputFile, file), 'r') as inp:
        line = inp.readlines()

    wordsList.append(line)

    wordsString = ''.join(str(i) for i in wordsList)[2:-2]


    # Remove all numbers and COUNT number of numbers removed
    numberList = '[0-9]'
    numbersRemoved = 0
    for numbers in wordsString:
        checkNumber = numbers[0]
        if bool(len(re.findall(numberList, checkNumber))) == True:
            numbersRemoved += 1

    wordsString = re.sub(numberList, '', wordsString)
    #print(wordsString)


    # Remove any punctuation and COUNT number of punctuation removed
    punctuationList = r'''[]–[—}()."?!:';,{-]'''
    ellipses = '...'
    punctuationRemoved = 0
    for punctuation in wordsString:
        if str(punctuation) in ('[', ']', '-', '–', '—', '{', '}', ';', ':', '""', "''", "?", "(", ")", ".", ",", "!"): 
            punctuationRemoved += 1
        else:
            pass

    if ellipses in wordsString:
        punctuationRemoved -= 2

    wordsString = re.sub(punctuationList, '', wordsString)


    # Transform upper case to lowercase and COUNT number of upper case words
    upperCaseWordsTransformed = 0
    for words in wordsString.split():
        for letter in words:
            if letter.isupper() == True:
                upperCaseWordsTransformed += 1

    wordsString = wordsString.lower()


    # Find number of words in file
    getRidOf = "\\n"
    wordsString = wordsString.replace(getRidOf, "")
    numberOfWords = 0
    for word in wordsString.split():
        numberOfWords += 1


    # Find number of CORRECT words in file
    numberOfCorrectWords = 0
    dictionary = open("EnglishWords.txt", "r")
    correctWords = ''
    englishWords = dictionary.read()
    for word in wordsString.split():
        if word in englishWords.split():
            numberOfCorrectWords += 1

    username = sys.argv[0][11:19]

    output1 = (username) + ("\nFormatting ###################") + ("\nNumber of upper case letters transformed: " + str(upperCaseWordsTransformed)) + ("\nNumber of punctuation's removed: " + str(punctuationRemoved)) + ("\nNumber of numbers removed: " + str(numbersRemoved)) + ("\nSpellchecking ###################") + ("\nNumber of words in file: " + str(numberOfWords)) + ("\nNumber of correct words in file: " + str(numberOfCorrectWords)) + ("\nNumber of incorrect words in file: " + str(numberOfWords - numberOfCorrectWords))

    # Output to txt file
    outputTxt = str(os.path.splitext(file)[0]) + "_s29576tb" + str(os.path.splitext(file)[1])
    fullOutputTxt = os.path.join("output_3/" + outputTxt)
    with open(fullOutputTxt, 'w') as out:
        for lines in output1:
            out.write(lines)

    wordsList= []