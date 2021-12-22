import os, sys

os.chdir('..')
os.chdir(sys.argv[1])
EngWords = open('EnglishWords.txt', "r")
EngList = []
for line in EngWords:
    line = line.rstrip()
    EngList.append(line)
for file in os.listdir(sys.argv[2]):
    os.chdir('..')
    os.chdir(sys.argv[2])
    text = open(file, "r")
    testfile = text.read()
    username = "y55928xn"+'\n'
    format = "Formatting ###################"+'\n'
    spell = "Spellchecking ###################"+'\n'
    time = 0
    numbers = 0
    punc = 0
    words = ""

    part = testfile.split(' ')
    numword = 0
    while numword < len(part):
        word = part[numword]
        position = 0
        numword += 1
        ellipsisdetermine = 0
        while position < len(word):
            char = word[position]
            position += 1
            if char.isupper():
                words = words + char.lower()
                time += 1
            elif char.isnumeric():
                numbers += 1
            elif char.islower():
                words = words + char
            else:
                punc += 1
        if any(c.isupper() or c.islower() for c in word):
            words = words + ' '
        for i in range(0, len(word)-2):
            if word[i]  == '.':
                if word[i+1] == '.' and word[i+2] == '.':
                    punc = punc - 3
                    i += 3
            

    UpCstn = 'Number of upper case words transformed: ' + str(time)+'\n'
    puncstn = 'Number of punctuations removed: ' + str(punc)+'\n'
    numstn = 'Number of numbers removed: ' + str(numbers)+'\n'

    newwords = words.rstrip().split(' ')
    length = len(newwords)
    NoW = 'Number of words in file: '+str(length)+'\n'
    wordno = 0
    right = 0
    wrong = 0
    while wordno < length:
        if newwords[wordno] in EngList:
            right += 1
        else:
            wrong += 1
        wordno += 1
    Rtstn = 'Number of correct words in file: ' + str(right)+'\n'
    Wrstn = 'Number of incorrect words in file: ' + str(wrong)+'\n'
    os.chdir('..')
    os.chdir(sys.argv[3])
    name = os.path.basename(file).split('.')[0]
    output = open(name+'_y55928xn.txt', 'x')
    seq = [username, format, UpCstn, puncstn, numstn, spell, NoW, Rtstn, Wrstn]
    output.writelines(seq)

