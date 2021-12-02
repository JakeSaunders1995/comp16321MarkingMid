import os, argparse
from typing import List, Tuple

NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
PUNCTUATION = [".","?","!",",",":",";","-","(",")","[","]","{","}","'",'"', "…"] # nb ellipses are threefold occurences of .
USER_NAME = "j90095jb"

def ReadFileWithJoin(path):
    file = open(path)
    data = "\r\n".join(file.readlines())
    file.close()
    return data

def ReadFileWithoutJoin(path):
    return [x.strip() for x in open(path).readlines() ] # mmm file handling one liners. it's all gced anyway lol

def WriteToFile(path, data):
    file = open(path, "w")
    file.write(data)
    file.close()
    
def GetAllFilesAtPath(dir) -> "list[str]":
    paths = []
    for path in os.listdir(dir):
        if path.endswith(".txt"):
            paths.append(os.path.join(dir, path))
    return paths

def GetOutputPath(path: str, outdir: str):
    return f"{os.path.join(outdir, os.path.splitext(os.path.basename(path))[0])}_{USER_NAME}.txt"

def CharNumber(char) -> bool:
    if char in NUMBERS: return True
    else: return False

def CharPunct(char) -> bool:
    if char in PUNCTUATION: return True
    else: return False

def LintString(inData: str) -> Tuple[str, Tuple[int, int, int]]:
    output = ""
    caps = 0
    nums = 0
    punct = 0
    # The following is a workaround entirely to correctly identify "ellipses". I hate everything. this could just be a "for char in inData:" why do you do this to me
    # and yes i know i could loop through once first to remove ellipses but 2 passes over the whole string is horrible and i hate it aaaa
    i = 0
    while i < len(inData):
        if CharNumber(inData[i]): 
            nums += 1
        elif CharPunct(inData[i]):
            if inData[i] == ".":
                try: # cba to do this properly have a try catch instead
                    if inData[i+1] == "." and inData[i+2] == ".":
                        i += 2
                except:
                    print("lol")
            punct += 1
        elif inData[i] != inData[i].lower():
            caps += 1
            output += inData[i].lower()
        else: 
            output += inData[i]
        i += 1
    return output, (caps, punct, nums)

def WordsFromString(input: str) -> str:
    return [x for x in input.split(" ") if x and x != "\n"] # extremely funny workaround which i now realise i should just do at the linting stage but Oh Well!
def NumOfWords(inData: str) -> int:
    word = WordsFromString(inData)
    return len(WordsFromString(inData))
def NumFalseWords(inData: str, dict: List[str]) -> int:
    false = 0
    for word in WordsFromString(inData):
        if word not in dict: false += 1
    return false
def NumGoodWords(inData: str, dict: List[str]) -> int:
    correct = 0
    for word in WordsFromString(inData):
        if word in dict: correct += 1
    return correct

def GenerateOutput(linterTuple, spellTuple):
    return f"""{USER_NAME}
Formatting ###################
Number of upper case letters changed: {linterTuple[0]}
Number of punctuations removed: {linterTuple[1]}
Number of numbers removed: {linterTuple[2]}
Spellchecking ###################
Number of words: {spellTuple[0]}
Number of correct words: {spellTuple[1]}
Number of incorrect words: {spellTuple[2]}"""

def Main(wordsPath, inPath, outPath):
    words = ReadFileWithoutJoin(wordsPath)
    for file in GetAllFilesAtPath(inPath):
        text = ReadFileWithJoin(file)
        linterOut = LintString(text)
        linted = linterOut[0]
        spellResults = (NumOfWords(linted), NumGoodWords(linted, words), NumFalseWords(linted, words))
        WriteToFile(GetOutputPath(file, outPath), GenerateOutput(linterOut[1], spellResults))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("EnglishWords")
    parser.add_argument("Input")
    parser.add_argument("Output")
    args = parser.parse_args()
    Main(args.EnglishWords, args.Input, args.Output)
