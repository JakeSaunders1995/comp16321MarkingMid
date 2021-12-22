import argparse, os, re

parser = argparse.ArgumentParser()
parser.add_argument("EnglishTextFile")
parser.add_argument("inputFolder")
parser.add_argument("outputFolder")
args = parser.parse_args()

if not os.path.isfile(args.EnglishTextFile):
    print("Error! The input EnglishWords file does not exist: ", args.EnglishTextFile)
    exit(0)

if not os.path.exists(args.inputFolder):
    print("Error! The input folder does not exist: ", args.inputFoler)
    exit(0)

if not os.path.exists(args.outputFolder):
    os.mkdir(args.outputFolder)
    print("Create new folder for output: ", args.outputFolder)

EnglishWords = []
file = open("EnglishWords.txt", "r")
for line in file.readlines():
    EnglishWords.append(line.strip())
file.close()

reg1 = r"[^ a-zA-Z0-9]"
reg2 = r"[^ a-zA-Z]"
reg3 = r"[A-Z]"

for fileName in os.listdir(args.inputFolder):
    filePath = os.path.join(args.inputFolder, fileName)
    if os.path.isdir(filePath):
        continue

    numberOfPunctuations = 0
    numberOfNumbers = 0
    numberOfUpcaseChanged = 0
    numberOfWords = 0
    numberOfCorrects = 0

    fin = open(filePath, "r")
    for line in fin.readlines():
        oriLen = len(line)

        line = re.sub(reg1, "", line)
        len1 = len(line)
        numberOfPunctuations += oriLen - len1

        line = re.sub(reg2, "", line)
        numberOfNumbers += len1 - len(line)

        words = line.split()
        numberOfWords += len(words)

        for word in words:
            if re.match(reg3, word):
                word = word.lower()
                numberOfUpcaseChanged += 1

            if word in EnglishWords:
                    numberOfCorrects += 1

    fin.close()

    print("g21434rb")
    print("Formatting ###################")
    print("Number of upper case words changed: ", numberOfUpcaseChanged)
    print("Number of punctuations removed: ", numberOfPunctuations)
    print("Number of numbers removed: ", numberOfNumbers)
    print("Spellchecking ###################")
    print("Number of words: ", numberOfWords)
    print("Number of correct words: ", numberOfCorrects)
    print("Number of incorrect words: ", numberOfWords - numberOfCorrects)

    fname, ext = os.path.splitext(fileName)
    fname += "_g21434rb" + ext
    outputFilePath = os.path.join(args.outputFolder, fname)

    fout = open(outputFilePath, "w")
    fout.writelines("g21434rb\n")
    fout.write("Formatting ###################\n")
    fout.write("Number of upper case words changed: %d\n" % numberOfUpcaseChanged)
    fout.write("Number of punctuations removed: %d\n" % numberOfPunctuations)
    fout.write("Number of numbers removed: %d\n" % numberOfNumbers)
    fout.write("Spellchecking ###################\n")
    fout.write("Number of words: %d\n" % numberOfWords)
    fout.write("Number of correct words: %d\n" % numberOfCorrects)
    fout.write("Number of incorrect words: %d\n" %(numberOfWords - numberOfCorrects))
    fout.close()
