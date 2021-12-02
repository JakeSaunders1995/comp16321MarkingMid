import argparse
import os
import string

parser = argparse.ArgumentParser(description='Get locations')
parser.add_argument('wordpool', type=str)
parser.add_argument('inputlocation', type=str)
parser.add_argument('outputlocation', type=str)
args = parser.parse_args()


def getwords(location):
    global wordlist
    with open(location) as f:
        wordlist = f.read().splitlines()


def getinput(location):
    f = open(location, 'r')
    text = f.read()
    f.close()
    return text


def remCap(strin):
    count = 0
    for i in range(len(strin)):
        if strin[i].lower() != strin[i]:
            count += 1
            strin = list(strin)
            strin[i] = strin[i].lower()
            strin = "".join(strin)
    return strin, count


def remNum(strin):
    count = 0
    for i in range(len(strin)):
        if strin[i].isdigit():
            count += 1
    for i in range(0,10):
        strin = strin.replace(str(i), '')
    return strin, count


def remPun(strin):
    count = 0
    punctlist = string.punctuation
    punctlist = list(punctlist)
    punctlist.append('–')
    j = 0
    while j < len(strin):
        if strin[j] in punctlist and strin[j] != '@' and strin[j] != '#':
            if j <= len(strin)-3 and strin[j+1] == '.' and strin[j+2] == '.':
                j += 2
            count += 1
        j+=1
    for i in punctlist:
        if i != '@' and i != '#':
            strin = strin.replace(i, '')
    return strin, count


def checkCorrect(strin):
    correct = 0
    incorrect = 0
    strin = strin.split()
    for x in strin:
        if x in wordlist:
            correct += 1
        else:
            incorrect += 1
    return correct, incorrect


def writeFile(letcase, puncrem, numrem, worcor, worinc, location):
    f = open(location, 'a')
    f.write("t74769sm")
    f.write("\n")
    f.write("Formatting ###################")
    f.write("\n")
    f.write("Number of upper case letters changed: ")
    f.write(str(letcase))
    f.write("\n")
    f.write("Number of punctuations removed: ")
    f.write(str(puncrem))
    f.write("\n")
    f.write("Number of numbers removed: ")
    f.write(str(numrem))
    f.write("\n")
    f.write("Spellchecking ###################")
    f.write("\n")
    f.write("Number of words: ")
    f.write(str(worcor+worinc))
    f.write("\n")
    f.write("Number of correct words: ")
    f.write(str(worcor))
    f.write("\n")
    f.write("Number of incorrect words: ")
    f.write(str(worinc))
    f.close()


wordsLocation = args.wordpool
fileLocation = args.inputlocation
outputFileLocation = args.outputlocation
getwords(wordsLocation)
filelist = os.listdir(fileLocation)

for file in filelist:
    newloc = fileLocation + "/" + file
    Case = getinput(newloc)
    Case, uppercase = remCap(Case)
    Case, number = remNum(Case)
    Case, punct = remPun(Case)
    rightwords, wrongwords = checkCorrect(Case)
    newout = outputFileLocation+"/"+file
    newout = newout.replace(".txt", "_t74769sm.txt")
    writeFile(uppercase, punct, number, rightwords, wrongwords, newout)

