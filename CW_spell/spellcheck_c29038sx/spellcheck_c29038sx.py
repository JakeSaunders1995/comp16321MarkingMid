import argparse
import os

parser = argparse.ArgumentParser(description = "Generating the spelling check report")
parser.add_argument("check", type = str, help = "Path of EnglishWords file")
parser.add_argument("input", type = str, help = "Path of input folder")
parser.add_argument("output", type = str, help = "Path of output folder")
args = parser.parse_args()

punctuations = ['!', '"', "'", '(', ')', ',', '-', '.', ':', ';', '?', '[', ']', '^', '_', '`', '{', '}', '…', '“', '”', '‘', '’', '——', '—']

#the path of english checking file
checkingPath = args.check

#function blocks
def wordTransformer(wordFile):
    f = open(wordFile)
    text = f.read()
    wordsLs = text.split()
    f.close()
    return wordsLs

def formater(wordFile):
    f = open(wordFile)
    text = f.read()
    lowText = text.lower()
    for i in punctuations:
        lowText = lowText.replace(i, '')
    for i in range(10):
        lowText = lowText.replace(str(i), '')
    f.close()
    return lowText

def pCounter(wordFile):
    f = open(wordFile)
    text = f.read()
    pNum = 0
    for i in text:
        for j in punctuations:
            if i == j:
                pNum += 1    
    f.close()       
    return pNum

def wordsCounter(text):
    text = text.split()
    num = len(text)
    return num

def capCounter(wordFile):
    capNum = 0
    f = open(wordFile)
    text = f.read()
    f.close()
    for i in text:
        for j in range(65, 91):
            if ord(i) == j:
                capNum += 1
    return capNum

def numCounter(wordFile):
    nNum = 0
    f = open(wordFile)
    text = f.read()
    for i in text:
        for j in range(10):
            if i == str(j):
                nNum += 1
    f.close()
    return nNum
    
def wordChecker(text, checkLst):
    wNum = 0
    wordsLs = text.split()
    for i in wordsLs:
        for j in wordTransformer(checkLst):
            if i == j:
                wNum += 1
    return wNum

def report(checkLst, wordFile, outputPath):
    f = open(outputPath, 'w')
    f.write("c29038sx\n")
    f.write("Formatting ###################\n") 
    f.write("Number of upper case letters changed: ")
    f.write(str(capCounter(wordFile)))
    f.write("\n")
    f.write("Number of punctuations removed: ")
    f.write(str(pCounter(wordFile)))
    f.write("\n") 
    f.write("Number of numbers removed: ")
    f.write(str(numCounter(wordFile)))
    f.write("\n")
    f.write("Spellchecking ###################\n")
    f.write("Number of words: ")
    f.write(str(wordsCounter(formater(wordFile))))
    f.write("\n")
    f.write("Number of correct words: ")
    f.write(str(wordChecker(formater(wordFile), checkLst)))
    f.write("\n") 
    f.write("Number of incorrect words: ")
    f.write(str(wordsCounter(formater(wordFile)) - wordChecker(formater(wordFile), checkLst)))
    
def checkdir(path):
    if os.path.isdir(path):
        return
    else:
        os.mkdir(path)
    return

def nameGenerater(path):
    return os.path.splitext(os.path.basename(path))[0] + "_c29038sx.txt"

def fileFilter(fileList):
    for inx, val in enumerate(fileList):
        if os.path.splitext(val)[1] != ".txt":
            del fileList[inx]

#chceking if the output directory exist, if not creat it
checkdir(args.output)

#get file list in the input folder and only take .txt file
fileList = os.listdir(args.input)
fileFilter(fileList)

#report generation
for i in fileList:
    inputPath = os.path.join(args.input, i)
    outputPath = os.path.join(args.output, nameGenerater(inputPath))
    report(checkingPath, inputPath, outputPath)
    
