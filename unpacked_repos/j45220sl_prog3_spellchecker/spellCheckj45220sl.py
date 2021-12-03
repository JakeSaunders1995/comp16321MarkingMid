import argparse
# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('wordfile', action='store', type=str)
parser.add_argument('inputfile', action='store', type=str)
parser.add_argument('outputfile', action='store', type=str)
args = parser.parse_args()
wordfile = args.wordfile
inputfile = args.inputfile
outputfile = args.outputfile

# read input
with open(wordfile, 'r') as FILE:
    words_right = [word.strip() for word in FILE.readlines()]


with open(inputfile, 'r') as FILE:
    lines = FILE.readlines()


# words = ''.join([c.lower() for c in string if c.isalpha()])
Nnumber = 0
Npunc = 0
Nupper = 0
newLines = []
for line in lines:
    newLine = []
    for rawWord in line.split():
        if rawWord.isalpha():
            for char in rawWord:
                if char.isupper():
                    Nupper += 1
        else:
            for char in rawWord:
                if char.isnumeric():
                    Nnumber += 1
                if not (char.isnumeric() or char.isalpha()):
                    Npunc += 1
        newWord = ''.join([char for char in rawWord if char.isalpha()])
        newLine.append(newWord)
    newLines.append(newLine)
Nword = len([word for line in newLines for word in line])
Ncorrect = 0
Nwrong = 0
for line in newLines:
    for word in line:
        if word in words_right:
            Ncorrect += 1
        else:
            Nwrong += 1

# output
outputstring = """j45220sl
Formatting ###################
Number of upper case words transformed: %d
Number of punctuation's removed: %d
Number of numbers removed: %d
Spellchecking ###################
Number of words in file: %d
Number of correct words in file: %d
Number of incorrect words in file: %d
""" % (Nupper, Npunc, Nnumber, Nword, Ncorrect, Nwrong)
with open(outputfile, "w") as file:
    file.write(outputstring)
