# --- Spellchecker ---
#takes input and output file as arguments
import argparse
import os
parser = argparse.ArgumentParser()
try:
    parser.add_argument('wordsFile', type=argparse.FileType('r'))
    parser.add_argument('inputFile')
    parser.add_argument('outputFile')
    args = parser.parse_args()
except:
    print("List arguments in the form: python3 rugby_m08320mm.py [words file path] [input file path] [output file path]")
    exit()

punctuationList = '".?!,:;-–(){}[]'+"'"
numbersList = "0123456789"
def processFile(text):
    #counting
    upperCaseWords = 0
    punctuation = 0
    numbers = 0
    correctWords = 0
    incorrectWords = 0
    contractions = 0

    #Get list of English words
    nextWord = ""
    englishWords = []
    for i in range(len(words)):
        if(words[i]=="\n"):
            englishWords.append(nextWord)
            nextWord=""
        else:
            nextWord+=words[i]
    englishWords.append(nextWord)

    #Get list of words in input file
    nextWord = ""
    fileWords = []
    for i in range(len(text)):
        if(text[i].isalpha()==False or text[i]==" " or text[i]=="\n"):
            for x in range(len(punctuationList)):
                if(punctuationList[x]==text[i]):
                    if(text[i]=="'"):
                        contractions+=1
                    if(text[i]=="."and text[i-1]=="." and text[i-2]=="."):
                        punctuation-=1
                    else:
                        punctuation+=1
            for x in range(len(numbersList)):
                if(numbersList[x]==text[i]):
                    numbers+=1

            if(nextWord!=""):
                if(nextWord.islower()==False):
                    upperCaseWords+=1
                fileWords.append(nextWord.lower())
                nextWord=""

        elif(text[i].isalpha()): #or text[i]=="#" or text[i]=="@"):
            nextWord+=text[i]
    if(nextWord!=""):
        fileWords.append(nextWord.lower())

    #Spellchecker
    for i in range(len(fileWords)):
        isWord = False
        for x in range(len(englishWords)):
            if(fileWords[i]==englishWords[x]):
                isWord = True
        if(isWord == False):
            incorrectWords+=1
    correctWords=len(fileWords)-incorrectWords

    output = "Formatting ###################\n"
    output +="Number of upper case words changed: "+str(upperCaseWords)+"\n"
    output +="Number of punctuations removed: "+str(punctuation)+"\n"
    output +="Number of numbers removed: "+str(numbers)+"\n"
    output +="Spellchecking ###################\n"
    output +="Number of words: "+str(len(fileWords)-contractions)+"\n"
    output +="Number of correct words: "+str(correctWords-contractions)+"\n"
    output +="Number of incorrect words: "+str(incorrectWords)
    return output

#gets info from english words file
with args.wordsFile as file:
    words = file.read()
    file.close()

#gets text from all files in folder
print(args.inputFile)
#iterates through file folder
for file in os.listdir(args.inputFile):
    #checks if text file
    if file.endswith(".txt"):
        print("\n"+file)
        #reads file
        currentPath = os.path.join(args.inputFile, file)
        f = open(currentPath, "r")
        new = f.read()
        f.close()
        #processes file
        result = processFile(new)
        print(result)
        #writes to new file
        newPath = os.path.join(args.outputFile, file[0:-4]+"_m08320mm.txt")
        f = open(newPath, "w")
        f.write("m08320mm\n"+result)
        f.close()
