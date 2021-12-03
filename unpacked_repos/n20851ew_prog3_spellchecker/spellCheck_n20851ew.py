import argparse
import sys
import os
import re
import string

parain = sys.argv[0]
filein = sys.argv[1]
fileout = sys.argv[2]

for filename in os.listdir(filein): 
    g = os.path.join(filein, filename)
    if os.path.isfile(g):
        filr = open(g, 'r')
        filen = os.path.basename(g)
        sfn = os.path.splitext(filen)[0]
        if  os.path.isdir(fileout):
            dname = os.path.join(fileout, sfn + "_n20851ew.txt")
            fn = open(dname, 'a')
            text = filr.read()
            fopen = open(parain, 'r')
            fread = fopen.read()
            fsep = fread.split()
            
            words = 0
            incorrectWords = 0
            correctWords = 0
            number = 0
            letterUpper = 0
            punctuation = 0
            
            english_Words = "EnglishWords.txt"
            with open(english_Words,'r') as file:
                for line in fsep:
                    words += len(line.split())
                for line in english_Words.lower():
                    if line in fsep:
                        correctWords += 1
                    else:
                        incorrectWords += 1






            for word in range(0, len(text)):
                if text[word].isnumeric():
                    number += 1
                if text[word] in ('!', '?', ',','.','...','@',':',';','#','-','(',')','[',']'):
                    punctuation += 1
                if text[word].isupper():
                    letterUpper += 1
                







            fn.write("n20851ew"),
            fn.write("\nFormatting ###################"),
            fn.write("\nNumber of upper case letters changed: " + str(letterUpper)),
            fn.write("\nNumber of punctuation removed: " + str(punctuation)),
            fn.write("\nNumber of numbers removed: " + str(number)),
            fn.write("\nSpellchecking ###################"),
            fn.write("\nNumber of words: " + str(words)),
            fn.write("\nNumber of correct words: " + str(correctWords)),
            fn.write("\nNumber of incorrect words: " + str(incorrectWords))


        else:
            os.mkdir(fileout)