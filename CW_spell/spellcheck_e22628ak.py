import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('english', type=str)
parser.add_argument('inputf', type=str)
parser.add_argument('outputf', type=str)
args = parser.parse_args()
inputfiles = os.listdir(args.inputf)
dict = open(args.english,'r')
dictwords = dict.readlines()
for i,word in enumerate(dictwords):
    dictwords[i] = word.strip()
for file in inputfiles:
    fileloc = fr'{args.inputf}/{file}'
    outloc = fr'{args.outputf}/{file[: -4]}_e22628ak.txt'
    fin = open(fileloc,'r')
    txt = fin.readlines()
    fin.close()
    upperc = 0
    punctc = 0
    numc = 0
    correctword = 0
    wrongword = 0
    wordlist = []
    for line in txt:
        newline = line.strip()
        newline = newline.split()
        for word in newline:
            newword = ''
            if word == '...':
                punctc += 1
                continue
            for letter in word:
                if letter.isupper() == True:
                    upperc += 1
                    newword = newword + letter.lower()
                elif (letter.isalpha() != True) and (letter.isdigit() != True):
                    punctc += 1
                elif letter.isdigit() == True:
                    numc += 1
                else:
                    newword = newword + letter
            if newword != '':
                wordlist.append(newword)
    wordc = len(wordlist)
    for word in wordlist:
        if word in dictwords:
            correctword += 1
        else:
            wrongword += 1
    out = open(outloc,'w')
    out.write('e22628ak\n')
    out.write('Formatting ###################\n')
    out.write(f'Number of upper case letters changed: {upperc}\n')
    out.write(f'Number of punctuations removed: {punctc}\n')
    out.write(f'Number of numbers removed: {numc}\n')
    out.write('Spellchecking ###################\n')
    out.write(f'Number of words {wordc}\n')
    out.write(f'Number of correct words: {correctword}\n')
    out.write(f'Number of incorrect words: {wrongword}')
    out.close()
dict.close()