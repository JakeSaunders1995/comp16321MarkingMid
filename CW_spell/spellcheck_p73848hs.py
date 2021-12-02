import string
import os
import sys
username = "p73848hs"

def SpellCheck():
    for y in CorrectWords:
        if x.split()==y.split():
            return True
    return False

def UpperCheck():
    for y in x:
        if y.isupper():
            return True
    return False

def isstring(testing,against):
    for y in against:
        if x == y:
            return True
    return False



files=(os.listdir(sys.argv[2].strip("./")))
for filename in files:
    file = open(sys.argv[2].strip("./") + "/" + filename)
    filecontent=""
    for line in file:
        filecontent= filecontent + line
    file.close()

    NumOfUpperCase = 0
    NumOfPunc = 0
    NumOfNum = 0
    NumOfWords = 0
    NumOfCorrect = 0
    NumOfIncorrect = 0


    for x in filecontent:
        if isstring(x, string.digits):
            NumOfNum += 1
        if isstring(x, string.punctuation):
            NumOfPunc += 1
            
    nonum = filecontent.translate(str.maketrans('','',string.digits))
    nopunc=nonum.translate(str.maketrans('','',string.punctuation))




        
    for x in nopunc:
        if UpperCheck():
            NumOfUpperCase += 1


    words=(nopunc.lower()).split()
    NumOfWords = len(words)


    file=open(sys.argv[1].strip("./"))
    CorrectWords=[]
    for line in file:
        CorrectWords.append(line)
    file.close()
    for x in words:
        Check=SpellCheck()
        if Check ==False:
            NumOfIncorrect += 1
    NumOfCorrect = NumOfWords - NumOfIncorrect

    file=open(sys.argv[3].strip("./") +"/" + filename + username, "w")
    file.write("Formatting ###################\n")
    file.write("Number of upper case words transfored: " + str(NumOfUpperCase) + "\n")
    file.write("Number of punctuation's removed: " + str(NumOfPunc) + "\n")
    file.write("Number of numbers removed: " + str(NumOfNum) + "\n")
    file.write("SpellChecking ###################\n")
    file.write("Number words in file: " + str(NumOfWords) + "\n")
    file.write("Number of correct words in file: " + str(NumOfCorrect) + "\n")
    file.write("Number of incorrect words in file: " + str(NumOfIncorrect) + "\n")
    file.close()
               
               

    
