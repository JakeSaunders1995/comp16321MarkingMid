import sys
import os
import re
OutputFolder = sys.argv[-1]
InputFolder = sys.argv[-2]
EngWordsfile = sys.argv[-3]

textFiles = os.listdir(InputFolder)

def removeAndCount(text):
    punctuation = ['.','?','!',',',':',';','-','–','(',')','{','}','[',']','\'','"']
    Numbers = 0 
    UpperCase = 0
    Symbols = 0 
    
    caps = re.findall('([A-Z])', text)
    UpperCase += len(caps)
    text = text.lower()
    
    nums = re.findall('([0-9])', text)
    Numbers += len(nums)
    text = re.sub('([0-9])','',text)
    
    ellipsis = re.findall(r'\.\.\.',text)
    Symbols += len(ellipsis)
    text = text.replace('...','')
    
    for each in text:
        if each in punctuation:
            Symbols += 1
            text = text.replace(each,'')
            
    return text, Numbers, UpperCase, Symbols    

def spellCheck(text,EngWordsfile):
    Words = 0
    correctWords = 0
    incorrectWords = 0
    
    f = open(EngWordsfile,'r') 
    EngWordsfile = f.read()
    f.close()
    wordList = text.split()
    for each in wordList:
        Words += 1
        inWords = re.search(rf"\b{re.escape(each)}\b", EngWordsfile)
        if not inWords == None:
            correctWords += 1
        else:
            incorrectWords += 1
    
    return Words, correctWords, incorrectWords
        
        
for each in textFiles:
    outFilePath = OutputFolder + '/' + each[0:-4] + '_h08963ob.txt'
    path = InputFolder + '/' + each
    inpf = open(path, "r")
    EnglishText = inpf.read()
    inpf.close()

    text, Numbers, UpperCase, Symbols = removeAndCount(EnglishText)
    Words, correctWords, incorrectWords = spellCheck(text,EngWordsfile)
    
    outFileFormat = (f"h089630b"
                    f"\nFormatting ###################"
                    f"\nNumber of upper case letters changed: {UpperCase}"
                    f"\nNumber of punctuations removed: {Symbols}"
                    f"\nNumber of numbers removed: {Numbers}"
                    f"\nSpellchecking ###################"
                    f"\nNumber of words: {Words}"
                    f"\nNumber of correct words: {correctWords}"
                    f"\nNumber of incorrect words: {incorrectWords}")
    
    outf = open(outFilePath, 'w+')
    outf.write(outFileFormat)
    outf.close()

    