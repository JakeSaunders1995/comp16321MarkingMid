import sys, os

dictPath = sys.argv[1]
inPath = sys.argv[2]
outPath = sys.argv[3]

inFiles = os.listdir(inPath)
inFiles.sort()

punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~+='''
numbers = "1234567890"
upperChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars = "abcdefghijklmnopqrstuvwxyz "



count = 0

for file in inFiles:

    count += 1
    fIn = open(inPath + "/" + file, "r")
    fOut = open(outPath + "/test_file"+str(count)+"_j08328hd.txt", "w")
    dictFile = open(dictPath, "r")
    data = fIn.read()
    dictionary = dictFile.read()
    dictionary = dictionary.split('\n')

    uppers = 0
    punc = 0
    numbs = 0
    words = 0
    correct = 0
    incorrect = 0

    charCount = 0

    for i in data:
        if i == '.':
            if charCount + 2 <= len(data):
                if data[charCount +1] == '.' and data[charCount + 2] == '.':
                    punc += 1
                    continue
        if i in punctuation:
            punc +=1
        elif i in numbers:
            numbs +=1
        elif i in upperChars:
            uppers +=1
        charCount +=1

    lowerData = data.lower()
    for i in lowerData:
        if i not in chars:
            lowerData = lowerData.replace(i, '')
    
    words = lowerData.split(" ")
    if '' in words:
        words.remove('')

    for word in words:
        if word in dictionary:
            correct += 1
        elif word == '':
            continue
        else:
            incorrect +=1
    total = correct + incorrect

    fOut.write('j08328hd')
    fOut.write('\nFormatting ###################')
    fOut.write('\nNumber of upper case letters changed: ' + str(uppers))
    fOut.write('\nNumber of punctuations removed: '+ str(punc))
    fOut.write('\nNumber of numbers removed: '+ str(numbs))
    fOut.write('\nSpellchecking ###################')
    fOut.write('\nNumber of words: ' + str(total))
    fOut.write('\nNumber of correct words: '+ str(correct))
    fOut.write('\nNumber of incorrect words: ' + str(incorrect))

