import os
import sys
f = open(sys.argv[1], "rt")
edict = f.read().split()
def getFiles():
    basepath = sys.argv[2]
    files = []
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            files.append(entry)
    return files

def outputFiles(output, filename):
    filename = filename[:len(filename)-4]
    f=open(sys.argv[3]+"\\"+filename+"_x33731ed.txt", "w+")
    for i in output:
        f.write(i+"\n")
    f.close

def spellcheck(inp, edict):
    out = []
    length = len(inp)
    numcount = 0
    capitalCount = 0
    punctuationCount = 0
    convertedText = ""
    correctWords = 0
    incorrectWords = 0
    for i in range(0, length):
        char = ord(inp[i])
        if(inp[i].isnumeric()):
            numcount+=1
        elif(inp[i].isalpha()):
            if(char<95):
                char += 32
                capitalCount += 1
            char = chr(char)
            convertedText += char
        elif(inp[i]==" "):
            convertedText += inp[i]
        else:
            punctuationCount += 1
    wordList = convertedText.split()
    for i in range(len(wordList)):
        if(wordList[i] in edict):
            correctWords += 1
        else:
            incorrectWords += 1
    out = ["x33731ed","Formatting ###################","Number of upper case words changed: "+str(capitalCount),"Number of punctuations removed: "+str(punctuationCount),"Number of numbers removed: "+str(numcount),"Spellchecking ###################","Number of words: "+str(len(wordList)),"Number of correct words: "+str(correctWords),"Number of incorrect words: "+str(incorrectWords)]
    return out

files = getFiles()
for i in files:
    f = open(sys.argv[2]+"\\"+i,"r")
    inp = f.read()
    outputFiles(spellcheck(inp, edict), i)
    f.close()
print("done :)")
