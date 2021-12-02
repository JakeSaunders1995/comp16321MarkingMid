import argparse
from argparse import ArgumentParser
import os

def checkSpelling(curWord):
    englishWords = open(args.engWords, "rt")
    finalWord=""
    for i, line in enumerate(englishWords):#for every line in englishWords
        checkFlag=True
        if(len(line)-1==len(curWord)):
            for j in range(len(curWord)):
                if(line[j]!=curWord[j]):#Check if it matches the current word passed in
                    checkFlag=False
        else:
            checkFlag=False
        if(checkFlag):
            finalWord=line
    if(finalWord!=""):#if it does return true
        return True
    else:
        return False

def validateFilePath(f):
    if not os.path.exists(f):
        raise argparse.ArgumentTypeError("The filepath {0} does not exist. Please enter a valid filepath".format(f))
    return f


#COMMAND LINE INPUT
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser()
parser.add_argument('engWords', type=str, help="English Words file path")
parser.add_argument('inpFold', type=str, help="Input file/test txt file path")
parser.add_argument('outFold', type=str, help="Output file/output txt path")
args = parser.parse_args()
validateFilePath(args.engWords)
validateFilePath(args.inpFold)
validateFilePath(args.outFold)
inpFile=""

for filename in os.listdir(args.inpFold):#Get the amount of files within the folder
    if filename.endswith(".txt"):#that are input files
        inpFile=(os.path.join(args.inpFold, filename))
        #print(filename)
        #print(inpFile)
        filename=filename[:-4]+"_r61875lj.txt"
        #print(filename)
        outFile=(os.path.join(args.outFold, filename))
        #INITIALIZATION
        file = open(inpFile, "rt")
        currentWord=""
        wordsList=[]
        correctWords=0
        incorrectWords=0
        upperCaseCharacters=0
        numberCharacters=0
        punctuationCharacters=0
        ellipsisCount=0
        
        #CHECK CHARACTER
        while True:
                char = file.read(1)#Read from file character by character
                #print(ord(char))
                if not char:#if we reach the end of the document, stop the loop
                    wordsList.append(currentWord.lower())#add the lowercase word to the list of words
                    #print(currentWord.lower())
                    currentWord=""
                    break

                #handling output stuff
                if(ord(char)>=65 and ord(char)<=90):#Check for uppercase chars
                    upperCaseCharacters+=1
                    #print("UPPER: "+char)
                elif (ord(char)>=48 and ord(char)<=57):#Check for number chars
                    numberCharacters+=1
                elif ((ord(char)>32 and ord(char)<65) or (ord(char)>90 and ord(char)<97) or (ord(char)>122 and ord(char)<127)):#Check for punctuation chars
                    if(ord(char)!=64 or ord(char)!=35):
                        punctuationCharacters+=1

                if(ord(char)==46):
                        ellipsisCount+=1
                        if ellipsisCount==3:
                            ellipsisCount=0
                            punctuationCharacters-=2
                else:
                    ellipsisCount=0
                    
                #words handling
                if(ord(char)==32 or (ord(char)>64 and ord(char)<91) or (ord(char)>96 and ord(char)<123)):#if the character is not punctuation or a number
                    if(ord(char)!=32):
                        currentWord+=char
                    elif(currentWord!=""):
                        wordsList.append(currentWord.lower())#add the lowercase word to the list of words
                        #print(currentWord.lower())
                        currentWord=""

##        #CHECK FOR UPPERCASE WORDS
##        for i in range(0,len(wordsList)):
##            upperCaseFlag=False
##            for j in range(0,len(wordsList[i])):
##                if(ord(wordsList[i][j])>=65 and ord(wordsList[i][j])<=90):#Check for uppercase chars
##                    upperCaseFlag=True
##            if upperCaseFlag:
##                upperCaseCharacters+=1
##            wordsList[i]=wordsList[i].lower()

        for i in range(0,len(wordsList)):#Now spell check every word in the list of words
            if(wordsList[i]==""):
                wordsList.remove("")
        
        #CHECK SPELLING
        for i in range(0,len(wordsList)):#Now spell check every word in the list of words
            if(checkSpelling(wordsList[i])):#if correct, increase correctWords
                correctWords+=1
            else:
                incorrectWords+=1

        #OUTPUT TO TEXT
        i = ["r61875lj", "\nFormatting ###################", "\nNumber of upper case letters changed: " + str(upperCaseCharacters),
             "\nNumber of punctuations removed: " + str(punctuationCharacters), "\nNumber of numbers removed: " + str(numberCharacters),
             "\nSpellchecking ###################", "\nNumber of words: " + str(len(wordsList)),
             "\nNumber of correct words: " + str(correctWords), "\nNumber of incorrect words: " + str(incorrectWords)]
        outputText = open(outFile, "w")
        outputText.writelines(i)
        outputText.close()
