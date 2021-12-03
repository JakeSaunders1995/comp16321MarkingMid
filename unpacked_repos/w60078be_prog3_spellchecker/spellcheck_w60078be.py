import argparse
import os


parser = argparse.ArgumentParser()      #argument setup
parser.add_argument("inputs")
parser.add_argument("outputs")
parser.add_argument("english")
args = parser.parse_args()



pathIn = args.inputs                #accepts argument 1 and argument 2 and assigns them as the path to folder
pathOut = args.outputs
wordsPath = args.english
fileNames = os.listdir(pathIn)

def ellipsis(punct):
    ellipsisPos = 0
    ellipsisNum = 0
    
    while ellipsisPos < len(punct): 
        stop = 0
        if punct[ellipsisPos] == ".":
            
            ellipsisPos +=1
            stop +=1
            ellipsis = True
            while ellipsis == True and ellipsisPos<len(punct)-1:
                ellipsisPos+=1
                
                if punct[ellipsisPos] == ".":
                    stop +=1
                    ellipsisPos +=1
                else:
                    ellipsis = False
                if stop == 2:
                    ellipsisNum +=1
                    break

            
        else:
            ellipsisPos +=1
    return ellipsisNum


def hyphen(punct):
    hyphenPos = 0
    hyphenNum = 0
    
    while hyphenPos < len(punct): 
        dash = 0
        if punct[hyphenPos] == "-":
            hyphenPos +=1
            dash +=1
            hyphen = True
            while hyphen == True and hyphenPos<len(punct)-1:
                #hyphenPos+=1
                if punct[hyphenPos] == "-":
                    dash +=1
                    hyphenPos +=1
                else:
                    hyphen = False
                if dash == 1:
                    hyphenNum +=1
                    break

            
        else:
            hyphenPos +=1
    return hyphenNum


def format_text(txtFile):
    
    txtFile = txtFile.lower()
    txtFile = txtFile.split()
    pos = 0
    removed = []
    while pos<len(txtFile):
        for i in txtFile[pos]:
            letter = ord(i)
            if letter >=96 and letter <= 122:
                continue
            else:
                removed.append(i)
                txtFile[pos] = txtFile[pos].replace(i,"")
        pos +=1
         
    return txtFile,removed



def comparison(word,spelling):
    incorrect = True
    if word in spelling:
        incorrect = False
    return incorrect

englishIn = wordsPath + "EnglishWords.txt"
file = open(englishIn)
spellings = file.read()
file.close()
spellings = spellings.split("\n")

for f in fileNames:

    textIn = pathIn + "/" + f
    file = open(textIn,"r")
    textFile = file.read()
    file.close()

    capitals = 0
    punctuation = 0 
    numbers = 0
    mistakes = 0
    correct = 0

    for j in textFile:
        
        letters = ord(j)
        
        if (letters >=33 and letters <=47) or (letters >=58 and letters <= 64) or (letters >=91 and letters <= 96) or letters>=123:
            punctuation +=1
        elif letters >=48 and letters <=57:
            numbers +=1
        elif letters >=65 and letters <=90:
            capitals +=1

    format_textOutput = format_text(textFile)
    formatText = format_textOutput[0]
    #print(formatText)
    ellipsisNo = ellipsis(textFile)
    hyphenNo = hyphen(textFile)

    pos = 0
    while pos<len(formatText):
        if formatText[pos] == "":
            
            formatText.remove(formatText[pos])
        pos+=1
    pos = 0
    
    while pos<len(formatText):
        if formatText[pos] == "":
            formatText.remove(formatText[pos])
        pos+=1
    
    #print(formatText)
    punctuation = punctuation - (ellipsisNo *3) + ellipsisNo
    punctuation = punctuation - (hyphenNo *2) + hyphenNo

    for i in formatText:
        
        spellCheck = comparison(i,spellings)
        if spellCheck == True:
            mistakes +=1
        else:
            correct +=1

    words = len(formatText)
    
    txtStripped = f.replace(".txt","")  #removes.txt from input file so username can be added
    textOut = pathOut +"/"+txtStripped+"_w60078be.txt"
    
    output = "w60078be\n" + "Formatting ###################\n" +"Number of upper case letters changed: "+ str(capitals) + "\n" +"Number of punctuations removed: "+ str(punctuation) + "\n" +"Number of numbers removed: "+ str(numbers)+"\n" + "Spellchecking ###################\n"+"Number of words: "+ str(words)+"\n"+ "Number of correct words: " +str(correct)+"\n"+"Number of incorrect words: " +str(mistakes)
    file = open(textOut,"w")               
    file.write(output)  
    file.close()
    
    
    
    
   












