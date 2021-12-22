punctuation = [
    '.', '?', '!', ',', ':', ';', '--','-',         #1-8
    '[', ']', '{', '}', '(', ')', "'", '"', '…'   #9-17
]
import argparse, os, os.path, re
parser = argparse.ArgumentParser()
parser.add_argument("inputwordsfile")
parser.add_argument("inputfolder")
parser.add_argument("outputfolder")
args = parser.parse_args()

wordsfile = args.inputwordsfile
f2 = open(wordsfile, 'r')
str2 = f2.read()
infile = args.inputfolder
pathlist = os.listdir(infile)
for file in pathlist:
    filepath = os.path.join(infile, file)
    f=open(filepath, 'r')    
    str1 = f.read()
    uppercase = re.findall(r'[A-Z]', str1)
    numofuppercase = len(uppercase)       #number of upper case word changed
    number = re.findall(r'\d', str1)
    numofnumber = len(number)             #number of number changed
    numofpunctuation = 0                  #Number of punctuations removed
    for c in range(0,len(str1)):
        for w in range(0,len(punctuation)):
            if str1[c] == punctuation[w]:
                numofpunctuation += 1
    lowword = str1.lower()
    word = re.findall(r'[a-z]| ', lowword)
    words=""
    position = 0
    while position < len(word):
        if word[position] == ' ':
            if word[position-1] == ' ':
                position += 1
                continue
            elif position ==len(word) - 1 and word[position]== ' ':
                break
            else:
                words += ' '
                position += 1
        else:
            words += word[position]
            position += 1
    wordslist = re.split(r' ', words)
    numofwords = len(wordslist)              #Number of words
    numofcorrect = 0
    for n in wordslist:
        if n in str2:
            numofcorrect += 1
    numofincorrect = numofwords - numofcorrect
    writelist = []
    line1 = "p56781ng"
    writelist.append(line1)
    line2 = "Formatting ###################"
    writelist.append(line2)
    line3 = "Number of upper case words changed: " + str(numofuppercase)
    writelist.append(line3)
    line4 = "Number of punctuations removed: " + str(numofpunctuation)
    writelist.append(line4)
    line5 = "Number of numbers removed: " + str(numofnumber)
    writelist.append(line5)
    line6 = "Spellchecking ###################"
    writelist.append(line6)
    line7 = "Number of words :" + str(numofwords)
    writelist.append(line7)
    line8 = "Number of correct words: " + str(numofcorrect)
    writelist.append(line8)
    line9 = "Number of incorrect words: " + str(numofincorrect)
    writelist.append(line9)
    f.close()
    name, ext = os.path.splitext(file)
    name += "_p56781ng" + ext
    output = os.path.join(args.outputfolder, name)
    for i in writelist:
        spellcheck = open(output, 'a')
        spellcheck.write(i + '\n')
        spellcheck.close()
f2.close()
