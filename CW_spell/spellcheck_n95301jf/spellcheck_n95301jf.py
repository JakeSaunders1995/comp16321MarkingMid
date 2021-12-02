import re
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("english_folder")
parser.add_argument("input_folder")
parser.add_argument("output_folder")

args = parser.parse_args()

englishfolderpath = (args.english_folder)
inputfolderpath = (args.input_folder)
outputfolderpath = (args.output_folder)

for files in os.listdir(englishfolderpath):
    inputfiles1 = open(englishfolderpath + "/" + files, "r")
    read1 = inputfiles1.read()
    inputfiles1.close()

for files in os.listdir(inputfolderpath):
    inputfiles2 = open(inputfolderpath + "/" + files, "r")
    words = inputfiles2.readline()
    textfiles = files.split(".")


    dictionry = read1.split()
    qtyupper = 0
    qtypunc = 0
    qtynum = 0
    correct = 0
    incorrect = 0

    reader = words
    newtext = ""
    
    punc = ["!", "(", ")", "_", "-", "[", "]", "'", '"', ",", ".", "*", "..."]
    for i in range(len(reader)):

        if reader[i].isalpha():
            if reader[i].isupper():
                newtext += reader[i].lower()
                qtyupper += 1
            else:
                newtext += reader[i]

        elif reader[i] == " ":
            newtext += " "

        elif reader[i].isnumeric():
            qtynum += 1

        else:
            for x in range(len(punc)):
                if reader[i] == punc[x]:
                    qtypunc += 1



    clearedtext = newtext.split()
    textlength = len(clearedtext)



    for i in range(len(clearedtext)):
        for x in range(len(dictionry)):
            if clearedtext[i] == dictionry[x]:
                correct += 1

    incorrect = textlength-correct




    outputfilename = textfiles[0] + "_[n95301jf].txt"
    outputfiles = open(outputfolderpath + "/" + outputfilename, "w")
    outputfiles.write("[n95301jf]" + "\n"
    + "Formatting ################### " + "\n"
    + "Number of upper case letters changed: " + str(qtyupper) + "\n"
    + "Number of punctuations removed: " + str(qtypunc) + "\n"
    + "Number of numbers removed: " + str(qtynum) + "\n"
    + "Spellchecking ################### " + "\n"
    + "Number of words: " + str(textlength) + "\n"
    + "Number of correct words: " + str(correct) + "\n"
    + "Number of incorrect words: " + str(incorrect))
    outputfiles.close()

        