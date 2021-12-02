from os import listdir
from os.path import isfile, join
import re

       
englishFile = sys.argv[1]

englishTxt = englishFile.split()


inputFolder = sys.argv[2]


testFiles = [f for f in listdir(inputFolder) if isfile(join(inputFolder, f))]

for file in testFiles:
       inputFile = open(f"{inputFolder}/{file}")
       txt = inputFile.readline()

correctWNum = 0
incorrectWcount = 0
numOfWords = 0

       
NumCounter = 0
PunCounter = 0
UpCaseCounter = 0

def formatTxt(text):
       global NumCounter,PunCounter, UpCaseCounter
       punctuations = '''!()-[]{};:, <>./?@#$%^&*_~'''

       for words in range(len(text)):
              isInt = True
              try:
                    int(text[words])
              except ValueError:
                    isInt = False
              if isInt:
                    text[words].replace(" ", " ")
                    NumCounter += 1
              elif text[words] in punctuations:
                    text[words].replace(" ", " ")
                    PunCounter += 1
              elif text[words].isupper() == True:
                    #text[words] = text[words].lower()
                    UpCaseCounter += 1
                    word = text[words]
                    word = word.lower()


def EngWords(text):
       global correctWNum, incorrectWcount,numOfWords
       for words in range(len(text)):
              numOfWords += 1
              spellWord = text[words]

              if spellWord in englishTxt :
                    correctWNum += 1
              else:
                    incorrectWcount += 1



for file in testFiles:
       ouputFolder = sys.argv[3]
       outputFile = open(f"{ouputFolder}/{file}_h15879ac.txt","w")
       
       formatTxt(txt)
       EngWords(englishTxt)



       text_list = ["h15879ac\n","Formatting ################### \n", "Number of upper case letters changed:" + str(UpCaseCounter) + "\n", "Number of punctuations removed:" + str(PunCounter) + "\n", "Number of numbers removed:" + str(NumCounter) + "\n" "Spellchecking ################### \n","Number of words:" + str(numOfWords) + "\n", "Number of correct words:" + str(correctWNum) + "\n", "Number of incorrect words:" + str(incorrectWcount) + "\n"]

       outputFile.writelines(text_list)

       inputFile.close()
       outputFile.close()
