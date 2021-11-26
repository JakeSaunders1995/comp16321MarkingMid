import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('englishwords')
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()

wordfile = open(args.englishwords)
templist = []
wordlist = []

for line in wordfile:
    templist.append(line)
wordfile.close()

for item in templist:
    wordlist.append(item.strip())


inputfolder = args.input
outputfolder = args.output
inputfiles = os.listdir(inputfolder)


for i in inputfiles:
    filepath = os.path.join(inputfolder, i)
    currentfile = open(filepath)
    inputtext = currentfile.read()
    currentfile.close()

    inputtext.replace('"', ',')

    uppercount = 0
    punctuationcount = 0
    numbercount = 0
    newtext = ""

    for char in inputtext:
        if char.isupper():
            uppercount += 1
            newtext += char.lower()
        elif char.isdigit():
            numbercount += 1
        elif char == " ":
            newtext += " "
        elif not char.isalpha():
            punctuationcount += 1
        else:
            newtext += char

    textwordlist = newtext.split()
    wordcount = len(textwordlist)
    correctcount = 0
    incorrectcount = 0
    wordcorrect = False
    for word in textwordlist:
        for wordcheck in wordlist:
            if word == wordcheck:
                wordcorrect = True
                break

        if wordcorrect:
            correctcount += 1
            wordcorrect = False
        else:
            incorrectcount += 1

    finalmessage = "w73862jb\nFormatting ###################\nNumber of upper case words changed: " + str(uppercount) + "\nNumber of punctuations removed: " + str(punctuationcount) + "\nNumber of numbers removed: " + str(numbercount) + "\nSpellchecking ###################\nNumber of words: " + str(wordcount) + "\nNumber of correct words: " + str(correctcount) + "\nNumber of incorrect words: " + str(incorrectcount)

    outputname = i[:-4] + "_w73862jb.txt"
    outputpath = os.path.join(outputfolder, outputname)

    outputfile = open(outputpath, "w")
    outputfile.write(finalmessage)
    outputfile.close()
