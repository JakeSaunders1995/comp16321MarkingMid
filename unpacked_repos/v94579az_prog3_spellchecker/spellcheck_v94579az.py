import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument("dictionary")
parser.add_argument("input", help = "input folder")
parser.add_argument("output", help = "output folder")
args = parser.parse_args()
files = os.listdir(str(args.input))

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
punctuation = ['.', '?', '!', ',', ':', ';', '(', ')', '[', ']', '{', '}', "'", '"', '-', '―', '—', '–', '…']
def format(code):
    global numbersRemoved
    numbersRemoved = 0
    global punctuationRemoved
    punctuationRemoved = 0
    global upperChanged
    upperChanged = 0

    if '...' in code:
        punctuationRemoved += code.count('...')
        code = code.replace('...', '')
         
    global newtext
    newtext = ""
    for y in code:
        if y in numbers:
            numbersRemoved += 1
        elif y in punctuation:
            punctuationRemoved += 1
        elif (y.isupper() == True):
            upperChanged += 1
            newtext += y.lower()
        else:
            newtext += y




def spellchecker(code):
    code = code.split()
    global wordCount
    wordCount = len(code)
    global incorrect
    incorrect = 0
    with open(args.dictionary, 'r') as d:
        wordsFile = str(d.read())
        splitWordsFile = wordsFile.splitlines()
        for y in code:
            if y not in splitWordsFile:
                incorrect += 1

    global correctWords
    correctWords = (wordCount - incorrect)


def display():
    with open(outputPath, 'w') as o:
        o.write("v94579az \nFormatting ###################\nNumber of upper case letters changed: " + str(upperChanged) + "\nNumber of punctuations removed: " + str(punctuationRemoved) + "\nNumber of numbers removed: " + str(numbersRemoved) + "\nSpellchecking ###################\nNumber of words: " + str(wordCount) + "\nNumber of correct words: " + str(correctWords) + "\nNumber of incorrect words: " + str(incorrect))



for x in files:
    path = str(args.input + "/" + x)
    outputPath = str(args.output + "/" + x[:10] + "_v94579az" + x[10:])
    with open(path, 'r') as f:
        text = str(f.read())
        format(text)
        spellchecker(newtext)
        display()
