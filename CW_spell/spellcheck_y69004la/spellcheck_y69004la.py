import os
import sys
import re

num = ["0","1","2","3","4","5","6","7","8","9"]
pun = ['.','?','!',':',';',',','-','_','[','{',']','}','(',')','⋯','"',"'"]
wordlist = []
c = 0
ic = 0
n =0
p=0
u=0
z=0

directory = sys.argv[1]
outputdirectory = sys.argv[2]
for filename in os.listdir(directory):
    filepath = directory + "/" + filename
    textfile = open(filepath, "r")
    text = textfile.read()

    z=text.count("...")
    
    for i in text:
        if i in pun:
            i = ""
            p+=1
        if i in num:
            i = ""
            n +=1
        if(i.isupper()):
            u+=1
    p = p - (z*3-z)
    upper = "Number of upper case letters changed: "+ str(u)
    punct ="Number of punctuations removed: "+ str(p)
    number = "Number of numbers removed: "+ str(n)
    
    p=0
    u=0
    n=0

    for words in pun:
        if words in text:
            text=text.replace(words,"")
    for word in num:
        if word in text:
            text=text.replace(word,"")

    
    
    
    text2 = text.lower()
    wordlist = text2.split()

    file = open("EnglishWords.txt", "r")
    file2 = file.read()
    file3 = file2.split()
    w = len(wordlist)
    wordsnum = "number of word: " + str(w)

    
    for i in wordlist:
        if i in file3:
            c +=1
        else:
            ic+=1
    correct = "number of correct word: "+ str(c)
    incorrect = "number of incorrect word: " + str(ic)
    c=0
    ic=0

    path = outputdirectory

    if not os.path.exists(path):
        os.makedirs(path)


    outputfile = outputdirectory + "/" + filename[0:-4] + "_" + "y69004la" + ".txt"
    s = open(outputfile, "w")
    s.write("y69004la" + "\n" + "Formatting ###################" + "\n" + upper + "\n" + punct + "\n" + number + "\n" +"Spellchecking ###################""\n" + wordsnum + "\n"+ correct+ "\n"+ incorrect)
    s.close() 



	
