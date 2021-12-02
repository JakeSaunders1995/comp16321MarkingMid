import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('dictPath', type=str)
parser.add_argument('inputPath', type=str)
parser.add_argument('outputPath', type=str)
args = parser.parse_args()

# sets variables to the input and output path specified by the user
dictPath = args.dictPath 
inpPath = args.inputPath
outPath = args.outputPath


# sets variable dict to a list of all the words in the dictionary from file 
file = open(dictPath, 'r')
dict = file.read()
file.close()
dict = dict.split('\n')

punctuation = """!()-[]{};:'"\,<>./?@#$%^&*_~"""


# create output file from text 
def generate_file(inpText, outputFile):

    text = inpText.replace('\n', ' ')
    text = text.split(' ')

    upCase = 0
    punc = 0
    num = 0
    numWords = 0
    incWords = 0
    corWords = 0

    words = len(text)
    elipseCounter = 0

    for wordIndex in range(0, words):
        word = text[wordIndex]
        wordLen = len(word)
        newWord = word
       
        # loops through the letters in the words
        for letterIndex in range(0, wordLen):
            letter = word[letterIndex]
            # letter is uppercase
            if letter.isupper() == True:
                upCase += 1
                newWord = newWord.lower()
            if letter.isdigit() == True:
                num += 1
                newWord = newWord.replace(letter, "")
            if letter in punctuation:
                punc += 1
                newWord = newWord.replace(letter, "")
        if newWord != '':
            numWords += 1   
        # will recognise the word as incorect if it is not in the dictionary and is not an empty string
        if newWord not in dict and newWord != '':
            incWords += 1

        if '...' in word:
            elipseCounter += 1

    punc = punc - (elipseCounter * 2)
    corWords = numWords - incWords

    file = open(outputFile, 'a')
    file.write('e88144wm\n')
    file.write('Formatting ###################\n')
    file.write('Number of upper case letters changed: ' + str(upCase) + '\n')
    file.write('Number of punctuations removed: ' + str(punc) + '\n')
    file.write('Number of numbers removed: ' + str(num) + '\n')
    file.write('Spellchecking ###################\n')
    file.write('Number of words: ' + str(numWords) + '\n')
    file.write('Number of correct words: ' + str(corWords) + '\n')
    file.write('Number of incorrect words: ' + str(incWords) + '\n')
    file.close()


# looping through files
for name in os.listdir(inpPath):
    print(inpPath + '/' + name)
    file = open(inpPath + '/' + name, 'r')
    inpText = file.read()
    file.close()

    name = name[:-4] + "_e88144wm.txt"
    outputFile = outPath + '/' + name
    generate_file(inpText, outputFile)
