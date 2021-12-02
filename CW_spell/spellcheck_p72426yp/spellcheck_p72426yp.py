import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("word_file", type=str)
parser.add_argument("in_path", type=str)
parser.add_argument("out_path", type=str)
args = parser.parse_args()
wordList = open(args.word_file, "r").readlines()
inPath = str(args.in_path).rstrip("/")
outPath = str(args.out_path).rstrip("/")

# Main
wordList = [word.rstrip("\n") for word in wordList]

for fileName in os.listdir(inPath):
    inFile = open(inPath + "/" + fileName, "r") 
    outFile = open(outPath + "/" + fileName[0:-4] + "_p72426yp.txt", "w") 

    numup = 0; numpunc = 0;   numrm = 0;
    numwd = 0;  numcor = 0;

    s = inFile.read()

    s2 = ""
    i = 0
    while i < len(s):
        if (s[i:i+5] == ". . ."):
            numpunc += 1
            #s2 += ' '
            i += 5
        else:
            s2 += s[i]
            i += 1

    s = s2

    symbols = ".?!,:;-–—{}[]()\'’\"“”" 
    
    ss = ""
    for c in s:
        if (c in symbols):
            numpunc += 1
            #ss += ' '
        elif ((c >= '0') and (c <= '9')):
            numrm += 1
            #ss += ' '
        elif ((c >= 'A') and (c <= 'Z')):
            numup += 1
            ss += c.lower()
        else:
            ss += c

    ss = ss.replace("\n", " ")
    #print(ss.split(" "))

    for w in ss.split(" "):
        curWord = w.replace(" ", "")
        if (curWord == ""): continue
        numwd += 1
        if (curWord in wordList):
            numcor += 1

    outFile.write("p72426yp\n")
    outFile.write("Formatting ###################\n")
    outFile.write("Number of upper case letters changed: "+str(numup)+"\n")
    outFile.write("Number of punctuations removed: "+str(numpunc)+"\n")
    outFile.write("Number of numbers removed: "+str(numrm)+"\n")
    outFile.write("Spellchecking ###################\n")
    outFile.write("Number of words: "+str(numwd)+"\n")
    outFile.write("Number of correct words: "+str(numcor)+"\n")
    outFile.write("Number of incorrect words: "+str(numwd - numcor))
    outFile.write("\n")

    inFile.close()
    outFile.close()

