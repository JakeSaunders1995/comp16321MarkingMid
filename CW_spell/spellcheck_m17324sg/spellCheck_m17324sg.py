import sys
import re
import filecmp

def spellCheck():
    with open(sys.argv[2], 'r') as f2:
        contents2 = f2.read()
        words = contents2.split()
        wordCount = len(words)
        upperText = re.findall(r'[A-Z]',contents2)
        upperCount = len(upperText)
        puncText = re.findall(r'[^\w\s]',contents2)
        puncCount = len(puncText)
        allNum = re.findall(r'[0-9]',contents2)
        numCount = len(allNum)
        line1 = "m17324sg"
        line2 = "Formatting ###################"
        line3 = "Number of upper case letters changed: " + str(upperCount)
        line4 = "Number of punctuations removed: " + str(puncCount) 
        line5 = "Number of numbers removed: " + str(numCount)
        line6 = "Spellchecking ###################"
        line7 = "Number of words: " + str(wordCount) 
        with open(sys.argv[1],'r') as f1: 
            countCorrect = 0
            countNcorrect = 0
            for word in words:
                for dictWord in f1:
                    if word == dictWord:
                        countCorrect = countCorrect + 1
                    else:
                        countNcorrect+=1
            line8 = "Number of correct words: " + str(countCorrect)
            line9 = "Number of incorrect words: " + str(countNcorrect)
            with open(sys.argv[3], 'w') as o:
                o.write(line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5 + "\n" + line6 + "\n" + line7 + "\n" + line8 + "\n" + line9)

spellCheck()


