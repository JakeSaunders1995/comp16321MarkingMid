import os
import re
import argparse
import sys
import glob

from os import waitpid
parser = argparse.ArgumentParser()
parser.add_argument("dictionaryFile")
parser.add_argument("inputfile")
parser.add_argument("outputfile")

args = parser.parse_args()
inputPath = args.inputfile
outputPath = args.outputfile
dictionary = args.dictionaryFile




#letterfilePosition = 0
#while (letterfilePosition < len(letterfile)):
 #   letter = letterfile[letterfilePosition]




dictionary = open(dictionary, "r")
words = dictionary.read()
kamus = re.split("\n", words)

def spelling(fpath):
    username = "b89545ss"
    format ="\nFormatting ###################"

    hurufbesar = re.findall("[A-Z]", txt)
    capital ="\nNumber of upper case words changed: " + str(len(hurufbesar))

    punctuation = re.findall("[^A-Za-z0-9\s]", txt)
    wacana = "\nNumber of punctuations removed: " + str(len(punctuation))

    nombor = re.findall("[0-9]", txt)
    number = "\nNumber of numbers removed: " + str(len(nombor))

    spellcheck = "\nSpellchecking ###################"

    hurufkecik = txt.lower()

    y = re.sub("[^a-z\s]", "", hurufkecik)


    huruf = re.split("\s", y)
    perkataan = "\nNumber of words: " + str(len(huruf))

    huruf_betul = 0
    huruf_salah = 0

    for x in huruf:
        if x in kamus:
            huruf_betul = huruf_betul + 1

        else:
            huruf_salah = huruf_salah + 1

    betul = "\nNumber of correct words: " + str(huruf_betul)
    salah = "\nNumber of incorrect words: " + str(huruf_salah)
    print()

    os.chdir(outputPath)
    results = open(f[:-4] + "_b89545ss.txt", "w")
    results.write(username)
    results.write(format)
    results.write(capital)
    results.write(wacana)
    results.write(number)
    results.write(spellcheck)
    results.write(perkataan)
    results.write(betul)
    results.write(salah)
    results.close()




for f in os.listdir(inputPath):
    if f.endswith(".txt") and f !="EnglishWords.txt":
        fpath = f"{inputPath}/{f}"
        print(fpath)
        file = open(fpath, "r")
        txt = file.read()
        file.close
        run = spelling(fpath)
