import argparse as pa
import os
import re

parser = pa.ArgumentParser()
parser.add_argument("englishwords", type=str)
parser.add_argument("inputpath", type=str)
parser.add_argument("outputpath", type=str)
args = parser.parse_args()
EnglishWords = args.englishwords
InputPath = args.inputpath
OutputPath = args.outputpath


wordFile = open(EnglishWords, 'r')
wordList = []
temp = 's'
while temp != '':
    temp = wordFile.readline()
    wordList.append(temp[0:len(temp)-1])
wordFile.close()

dirs = os.listdir(InputPath)
for file in dirs:
    fileLocation = InputPath + '/' + file
    readfile = open(fileLocation, 'r')
    content = readfile.read()
    readfile.close()
    numOfUpperCase = 0
    numOfPun = 0
    numOfNum = 0
    clearText = ''
    punctuation = "!,.—:;-_…[](){}“”?'"
    for i in range(len(content)):
        if content[i].isdigit():
            numOfNum += 1
        elif content[i].isalpha():
            if content[i].isupper():
                numOfUpperCase += 1
                clearText += content[i].lower()
            else:
                clearText += content[i]
        elif content[i] == ' ':
            clearText += ' '
        else:
            for x in range(len(punctuation)):
                if content[i] == punctuation[x]:
                    numOfPun +=1
    clearText = re.sub(r"\s+", " ", clearText)
    clearText = clearText.rstrip()
    words = []
    words = clearText.split(' ')

    numOfWords = len(words)
    numOfCorrectWord = 0
    numOfIncorrect = 0
    for word in words:
        if word in wordList:
            numOfCorrectWord += 1
        else:
            numOfIncorrect += 1


    fileWithoutTxt = file[0:len(file)-4]
    fileLocation = OutputPath + '/'+ fileWithoutTxt + '_j24834et.txt'
    writefile = open(fileLocation, 'w')
    writefile.write('j24834et')
    writefile.write('\r\n')
    writefile.write('Formatting ###################')
    writefile.write('\r\n')
    writefile.write('Number of upper case letters changed: '+str(numOfUpperCase))
    writefile.write('\r\n')
    writefile.write('Number of punctuations removed: '+str(numOfPun))
    writefile.write('\r\n')
    writefile.write('Number of numbers removed: '+str(numOfNum))
    writefile.write('\r\n')
    writefile.write('Spellchecking ###################')
    writefile.write('\r\n')
    writefile.write('Number of words: '+str(numOfWords))
    writefile.write('\r\n')
    writefile.write('Number of correct words:'+str(numOfCorrectWord))
    writefile.write('\r\n')
    writefile.write('Number of incorrect words:'+str(numOfIncorrect))
    writefile.close()