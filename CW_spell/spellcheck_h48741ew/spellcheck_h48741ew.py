import argparse
import os
import re

parser = argparse.ArgumentParser()
parser.add_argument("file",type = str, help = "the file to input the text in")
parser.add_argument("input",type = str, help = "the folder path to input the file in")
parser.add_argument("output", type = str, help = "the folder path to output the file in")

args = parser.parse_args()

EnglishText = args.file
input = args.input
output = args.output
punctuation = [
    '.','?','!',',',':',';','-','——','[',']','{','}','(',')','\'','…','"'
]
for file in os.listdir(input):
    Uppercase = 0
    punctuationNum = 0
    numbers = 0
    wordNum = 0
    corWordNum = 0
    incorWordNum = 0
    digits = 0
    filename = file.split(".")[0]
    outputname = filename + "_h48741ew.txt"
    eng = open(EnglishText)
    engline = eng.read().split("\n")

    inputfile = open(os.path.join(input,file),encoding='utf-8').read()

    number = re.findall('[0-9]+',inputfile)

    for i in number:
        digit = len(i)
        digits = digits + digit
    numbers = digits

    inputfile = inputfile.split()

    for i in inputfile:
        ellipses = re.search(r'(\w+)\.{3,}', i)
        if ellipses:
            punctuationNum+=1
        for b in i:
            if b in punctuation:
                punctuationNum+=1
                
    filestr = " ".join(inputfile)


    filestr = re.sub("\d+", "", filestr) # remove the numbers.

    filestr = re.sub(r'[^\w\s]','', filestr)  #haven't change to lower case yet.
    purewords = filestr.strip().split()

    for words in purewords:
        if words[0].isupper():
            Uppercase+=1
            purewords[purewords.index(words)] = words.lower() #Change upper case to lower case


    for words in purewords:
        if words in engline:
            corWordNum+=1
        else:
            incorWordNum+=1
    
    outputfile = open(os.path.join(output,outputname), "w")
    # outputfile.write("hello")
    outputfile.write("username: h48741ew"+"\nFormatting ###################"+"\nNumber of upper case letters changed: "
    + str(Uppercase)+
    "\nNumber of punctuations removed: "+str(punctuationNum)+"\nNumber of numbers removed: "+str(numbers)+"\nSpellchecking ###################"+"\nNumber of words: "+str(len(purewords))+"\nNumber of correct words: "+str(corWordNum)+"\nNumber of incorrect words: "+str(incorWordNum))