import argparse
import re
import os
docParse = argparse.ArgumentParser(description="InputFile")
docParse.add_argument('EnglishWords', metavar='englishwordpath', type=str, help='filepath to englishwords.txt')
docParse.add_argument('Path', metavar='input path', type=str, help='filepath to input')
docParse.add_argument('Path2', metavar='output path', type=str, help='filepath to output')
args = docParse.parse_args()
englishWords = open(args.EnglishWords)
englishCheck = englishWords.read()

for file in os.listdir(args.Path):
    inputfile = open(args.Path +"/"+ file)

    input = inputfile.read()

    WordsRemoved = 0
    PunctuationRemoved = 0
    NumbersRemoved = 0
    punctuation = ['.','?','!',',',';',':','—','-','[',']','{','}','(',')','\'','"','...','…']
    for character in input:
        if character.isdigit():
            NumbersRemoved += 1
    input = re.sub('[0-9]','',input)

    for character in input:
        if character in punctuation:
            PunctuationRemoved += 1
    input = re.sub('[^\w\s]','',input)

    capsWords = re.findall('[A-Z]',input)
    CapsRemoved = len(capsWords)

    wordsLowered = len(capsWords)
    input = input.lower()
    eng = englishCheck.split('\n')
    inputWords = input.split()
    correctWords = []
    incorrectWords = []
    for word in inputWords:
        if word not in eng:
            WordsRemoved += 1
            incorrectWords.append(word)
        else:
            correctWords.append(word)
    inputWords = ' '.join(inputWords)
    NumberofWords = len(correctWords) + len(incorrectWords)

    if not os.path.exists(args.Path2):
        outputDir = os.mkdir(args.Path2)
    filename = file[:-4]
    outputfile = open(args.Path2 +"/"+filename+ "_f57695ks.txt", "w")
    outputfile.write("f57695ks\n")
    outputfile.write("Formatting ###################\n")
    outputfile.write("Number of upper case letters changed: " + str(wordsLowered) +"\n")
    outputfile.write("Number of punctuations removed: " + str(PunctuationRemoved) + "\n")
    outputfile.write("Number of numbers removed: " +str(NumbersRemoved) +'\n')
    outputfile.write("Spellchecking ###################\n")
    outputfile.write("Number of words: " + str(NumberofWords) +'\n')
    outputfile.write("Number of correct words: " + str(len(correctWords)) + "\n")
    outputfile.write("Number of incorrect words: " + str(len(incorrectWords)))
    outputfile.close()