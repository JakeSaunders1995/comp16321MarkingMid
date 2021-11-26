import sys
import os
import string
numbers= ["0","1","2","3","4","5","6","7","8","9"]
file = open(sys.argv[1])
wordlist = file.readlines()
wordlist = [line.rstrip() for line in wordlist]
file.close()
path = sys.argv[2]
filelist=[]
files=os.listdir(path)
for f in files:
        filelist.append(f)
for x in filelist:
    file = open(str(path)+x, "r")
    text = file.read()
    file.close()
    currentPosition=0
    noOfNum=0
    noOfUps=0
    noOfPunc=0
    noOfWords=0
    noOfCorrect=0
    noOfIncorrect=0
    word=""
    while currentPosition < len(text):
        currentChar= text[currentPosition]
        if currentChar == " ":
            noOfWords+=1
            if word in wordlist:
                noOfCorrect+=1
                word=""
            else:
                noOfIncorrect+=1
                word=""
            currentPosition+=1
        elif currentChar != " ":
            if currentChar in string.punctuation:
                noOfPunc += 1
                text=text.replace(currentChar, "", 1)
            elif currentChar in numbers:
                noOfNum += 1
                text=text.replace(currentChar, "", 1)
            elif currentChar.isupper() == True:
                noOfUps += 1
                text=text.replace(currentChar, currentChar.lower(), 1)
            else:
                word=word+currentChar
                currentPosition+=1


        temp=text.split()
        text=" ".join(temp)
    if word !="":
        noOfWords+=1
        if word in wordlist:
            noOfCorrect+=1
            word=""
        else:
            noOfIncorrect+=1
            word=""
    currentPosition=0






    #noOfWords
    #noOfUps
    #noOfNum
    #noOfPunc
    #noOfCorrect
    #noOfIncorrect
    out= str(x)
    index = out.find('.txt')
    outfile = out[:index]+"_f49277np.txt"
    outpath = str(sys.argv[3])+outfile
    file = open(outpath, "x")
    file.write("f49277np\n"+"Formatting ###################\n"+"Number of upper case letters changed: "+str(noOfUps)+"\n"+"Number of punctuations removed: "+str(noOfPunc)+"\n"+"Number of numbers removed: "+str(noOfNum)+"\n"+"Spellchecking ###################\n" + "Number of words: " + str(noOfWords)+"\n" + "Number of correct words: " + str(noOfCorrect) + "\n" +"Number of incorrect words: "+str(noOfIncorrect))
    file.close()
