import sys
import os

files = os.listdir(sys.argv[2])

for filename in files:
    file = open(sys.argv[2] + "/" + filename, "r")
    words = ""
    wordlist = []
    correctWordCount = 0
    removedNumbers = 0
    removedPunctuation = 0
    caseChanged = 0

    for line in file:
        newline = ""
        for character in line:
            if character.isalpha() or character == " ":
                if character != character.lower():
                    caseChanged += 1
                newline += character.lower()
            elif character.isnumeric():
                removedNumbers += 1
            else:
                removedPunctuation += 1
            
        lineArray = newline.split()
        for words in lineArray:
            wordlist.append(words)

    file.close()
    file = open(sys.argv[1], "r")

    englishwords = []
    for words in file:
        englishwords.append(words.rstrip())

    for words in wordlist:
        if words in englishwords: correctWordCount += 1

    file.close()
    newFile = sys.argv[3] + "/" + filename[:len(filename)-4] + "_e78508hb.txt"
    
    file = open(newFile, "w")
    file.write("e78508hb\n")
    file.write("Formatting ###################\n")
    file.write("Number of upper case words changed: " + str(caseChanged))
    file.write("\nNumber of punctuations removed: " + str(removedPunctuation))
    file.write("\nNumber of numbers removed: " + str(removedNumbers))
    file.write("\nSpellchecking ###################")
    file.write("\nNumber of words: " + str(len(wordlist)))
    file.write("\nNumber of correct words: " + str(correctWordCount))
    file.write("\nNumber of incorrect words: " + str(len(wordlist) - correctWordCount))
    file.close()
