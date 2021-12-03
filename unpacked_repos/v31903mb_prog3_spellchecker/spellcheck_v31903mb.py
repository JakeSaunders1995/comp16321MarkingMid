import argparse
import re
import os

parser = argparse.ArgumentParser()
parser.add_argument("wordlist", help="Wordlist file path.")
parser.add_argument("input", help="Input directory. Directory is scanned for valid input files.")
parser.add_argument("output", help="Output directory. Output files are written to directory. Will overwrite file if it already exists.")
args = parser.parse_args()
wordlist = []
punctuationPattern = "[!-\/:-@\[-`\{-~]{1}" #Regex pattern to match any ASCII punctuation character

with open(args.wordlist) as f:
    wordlist = f.read().split("\n")
files = os.scandir(args.input)
for file in files:
    if not file.is_file() or file.name[-4:] != ".txt":
        continue
    text = ""
    with open(file) as f:
        text = f.read()
    upperCaseCount = len(re.findall("[A-Z]{1}", text)) #Counts number of upper case characters
    text = text.lower() #Converts upper case characters to lower case
    punctuationCount = len(re.findall(punctuationPattern, text)) #Counts number of punctuation characters
    text = re.sub(punctuationPattern, "", text) #Removes punctuation characters
    numberCount = len(re.findall("[0-9]{1}", text)) #Counts number of numbers
    text = re.sub("[0-9]{1}", "", text) #Removes numbers
    words = text.split()
    totalWordCount = len(words)
    correctWordCount = 0
    for word in words:
        if word in wordlist:
            correctWordCount += 1
    output = f"""v31903mb
Formatting ###################
Number of upper case letters changed: {upperCaseCount}
Number of punctuations removed: {punctuationCount}
Number of numbers removed: {numberCount}
Spellchecking ###################
Number of words: {totalWordCount}
Number of correct words: {correctWordCount}
Number of incorrect words: {totalWordCount - correctWordCount}"""
    fileName = os.path.join(args.output, file.name[:-4] + "_v31903mb.txt")
    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    with open(fileName, "w") as f:
        f.write(output)