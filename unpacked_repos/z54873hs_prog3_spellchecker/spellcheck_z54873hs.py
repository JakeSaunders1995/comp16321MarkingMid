username = "_z54873hs.txt"
number = "1234567890"
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetU= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = ",.?!,:;—-()}{[]'"+""
elipsescounter = 0
IncorrectWords = 0
Cwc = 0
text=""
username = "_z54873hs.txt"
import sys
import os
Englsihword = sys.argv[1]
LoadFile = sys.argv[2]
OutputFile = sys.argv[3]

for path , dir ,file in os.walk(LoadFile):
    Files = (file)


Eword = open(rf"{Englsihword}", "r")
Eword = Eword.read()
Eword = Eword.split()
for j in Files:
    IncorrectWords=0
    file = open(rf"{LoadFile}/{j}","r")
    file=file.read()

    text=file


    correcttext=""
    numbercounter = 0
    punctuationcounter = 0
    uppercase = 0
    for i in text:

        if i in number :
            numbercounter+=1
        if i in punctuation:
            punctuationcounter +=1

        if i in alphabetU:
            uppercase += 1
        #if i == ".":
            #if i+1 == ".":
                #if i+2==".":
                    #print("dsdsds")
    wctext= text.split()
    for i in wctext:
        if i == "...":
            punctuationcounter-=2
            elipsescounter +=1
    #print(wctext)
    wc= len(wctext)
    correctwords = 0

    text=text.lower()
    for h in text:
        if h in alphabet:
            correcttext += h
        if h ==" ":
            correcttext += " "
    correcttext = correcttext.split()
    for p in correcttext:
        if p not in Eword:
            IncorrectWords +=1

    wordcount = len(correcttext)

    FinalWordCount = wordcount - IncorrectWords
    g = j.split(".")
    OutFile=open(f"{OutputFile}/{g[0]}{username}","w")
    OutFile.write(username+"\n")
    OutFile.write("Formatting ###################"+"\n")
    OutFile.write("Number of upper case letters changed: "+str(uppercase)+"\n")
    OutFile.write("Number of punctuations removed: "+str(punctuationcounter)+"\n")
    OutFile.write("Number of numbers removed: "+str(numbercounter)+"\n")
    OutFile.write("Spellchecking ###################"+"\n")
    OutFile.write("Number of words: "+str(wordcount)+"\n")
    OutFile.write("Number of correct words: "+str(FinalWordCount)+"\n")
    OutFile.write("Number of incorrect words: "+str(IncorrectWords)+"\n")
    OutFile.close()
