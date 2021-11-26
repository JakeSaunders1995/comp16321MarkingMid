import sys
import os
import glob

pathEnglish = sys.argv[1]
pathIn = sys.argv[2]
pathOut = sys.argv[3]
dirIn = os.path.join(pathIn, '*.txt')
#dictionary/list start
punctuation = ['!', '&', '(', ')',
               '-', '[', '{', '}', ']', ':',
               ';', '\'', ',', '?', '/', '*',
               '`', '~', '$', '^', '+', '=',
               '<', '>', '\"', '.'
               ]
uppertolower = {'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e', 'F':'f',
               'G':'g', 'H':'h', 'I':'i', 'J':'j', 'K':'k', 'L':'l',
               'M':'m', 'N':'n', 'O':'o', 'P':'p', 'Q':'q', 'R':'r',
               'S':'s', 'T':'t', 'U':'u', 'V':'v', 'W':'w', 'X':'x',
               'Y':'y', 'Z':'z'
               }
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#dictionary/list end
for i in glob.glob(dirIn):
    fIn = open(os.path.join(os.getcwd(), i), 'r')
    filename = os.path.splitext(os.path.basename(i))[0]
    text = str(fIn.read())
    incompleteWords = text.split()
    noUpper = []
    noPunc = []
    noNum = []
    transformedUpper = 0
    removedPunc = 0
    removedNum = 0
    correctWords = 0

    #formatting start
    for word in incompleteWords:
        for letter in word:
            for uppercase in uppertolower:
                word = word.lower()
                if (letter == uppercase):
                    transformedUpper += 1
        noUpper.append(word)

    for word in noUpper:
        if ('...' in word):
            removedPunc += 1
            for letter in word:
                for punc in punctuation:
                    if (letter == punc and letter != '.'):
                        removedPunc += 1
            join1 = ''.join(a for a in word if a.isalnum())
            noPunc.append(join1)
            continue
        for letter in word:
            for punc in punctuation:
                if (letter == punc):
                    removedPunc += 1
        join1 = ''.join(a for a in word if a.isalnum())
        noPunc.append(join1)

    for word in noPunc:
        for letter in word:
            for num in numbers:
                if (letter == str(num)):
                    removedNum += 1
        join2 = ''.join(b for b in word if not b.isdigit())
        noNum.append(join2)
    noNum = list(filter(None, noNum))
    #formatting end

    NumOfWords = len(noNum)
    fEnglish = open(pathEnglish, 'r')
    EnglishWords = fEnglish.read().splitlines()
    for word in noNum:
        for enWord in EnglishWords:
            if (word == enWord):
                correctWords += 1
    incorrectWords = NumOfWords - correctWords

    if os.path.exists(pathOut):
        newFile = filename + '_r22997aa.txt'
        dirOut = os.path.join(pathOut, newFile)
        fOut = open(dirOut, 'a')
        print("r22997aa", file = fOut)
        print("Formatting ###################", file = fOut)
        print("Number of upper case letters changed:", transformedUpper, file = fOut)
        print("Number of punctuations removed:", removedPunc, file = fOut)
        print("Number of numbers removed:", removedNum, file = fOut)
        print("Spellchecking ###################", file = fOut)
        print("Number of words:", NumOfWords, file = fOut)
        print("Number of correct words:", correctWords, file = fOut)
        print("Number of incorrect words:", incorrectWords, file = fOut)
        fOut.close()
    else:
        os.makedirs(pathOut)
        newFile = filename + '_r22997aa.txt'
        dirOut = os.path.join(pathOut, newFile)
        fOut = open(dirOut, 'a')
        print("r22997aa", file = fOut)
        print("Formatting ###################", file = fOut)
        print("Number of upper case letters changed:", transformedUpper, file = fOut)
        print("Number of punctuations removed:", removedPunc, file = fOut)
        print("Number of numbers removed:", removedNum, file = fOut)
        print("Spellchecking ###################", file = fOut)
        print("Number of words:", NumOfWords, file = fOut)
        print("Number of correct words:", correctWords, file = fOut)
        print("Number of incorrect words:", incorrectWords, file = fOut)
        fOut.close()
