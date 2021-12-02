import argparse
import os
import sys

#command-line argument parser
argp = argparse.ArgumentParser(description='Input a file to spell check')
argp.add_argument('Dictionary', metavar='dictionary_path', type=str,
                    help='dictionary file (.txt)')
argp.add_argument('Input', metavar='input_path', type=str,
                    help='input folder')
argp.add_argument('Output', metavar='output_path', type=str,
                    help='output folder')

args = argp.parse_args()
dictionaryPath = args.Dictionary
inputPath = args.Input
outputPath = args.Output

#check if file exists
if not os.path.isdir(inputPath):
    print("Input directory does not exist...")
    sys.exit()
elif not os.path.isdir(outputPath):
    print("Creating output directory")
    os.makedirs(outputPath)
elif not os.path.isfile(dictionaryPath):
    print("Dictionary file does not exist")
    sys.exit()

#check for anything (Caps, Punct, Num) and formats before spell check
def xCheck(text, xList):
    xCount = 0
    letterCount = 0
    for x in text:
        if x in xList:
            xCount += 1
            if x.isupper():
                text = text[:letterCount] + x.lower() + text[letterCount+1:]
            else:
                text = text[:letterCount] + text[letterCount+1:]
                letterCount -= 1
        letterCount += 1
    return text, xCount

#checks spelling, recounts via console, formats output
def spellCheck(text):
    with open(dictionaryPath, 'r') as d:
        dictionary = d.read().split()
    words = text.split()
    incorrectCount = 0
    correctCount = 0
    wordCount = 0
    for word in words:
        if word not in dictionary:
            words[wordCount] = word.upper()
            incorrectCount += 1
        else:
            correctCount += 1
        wordCount += 1
    print(' '.join(words))
    print("{} Incorrect Word(s) {:>10} Correct Word(s) {:>13} Word(s) Total".format(incorrectCount, correctCount,wordCount))
    print("{} Number(s) Removed {:>10} Capital(s) Removed {:>10} Punctuation Removed \n\n".format(numCount, capsCount, punctCount))
    out = """g21898tg
Formatting {0}
Number of uppercase word(s) transformed: {1}
Number of punctuation removed: {2}
Number of number(s) removed: {3}
Spellchecking {0}
Number of words in file: {4}
Number of correct words in file: {5}
Number of incorrect words in file: {6}
    """.format('#'*10, capsCount, punctCount, numCount, wordCount, correctCount, incorrectCount)
    return out

#outputs to a file
def outputFormat(outputText, filePath):
    with open(filePath, 'w') as f:
        f.write(outputText)
    print("Output File Created at: {} \n".format(filePath))

#the starting procedure
files = os.listdir(inputPath)
for x in files:
    print(" File: {} ".format(x).center(50, '#'))
    with open("{}/{}".format(inputPath, x), 'r') as f:
        docText = f.read()
    docText, numCount = xCheck(docText, ["0","1","2","3","4","5","6","7","8","9",'0'])
    docText, punctCount = xCheck(docText, [".",";",":","!","?",",","[","]","-","'",'"',")","(", "@"])
    docText, capsCount = xCheck(docText, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    output = spellCheck(docText)
    outputFormat(output, "{}/{}".format(outputPath, x))


