import argparse
import os
parse = argparse.ArgumentParser(description='input test file path and output file path')
parse.add_argument('paths', type=str, nargs='+', help='file paths')
args = parse.parse_args()

inputfilelist= []
outputfilelist = []

for outfpath,outdirname,outfilename in os.walk(args.paths[2]):
    continue

for fpath,dirname,fname in os.walk(args.paths[1]):
    for i in fname:
        inputfilelist.append(fpath + '/' + i)
        outputfilelist.append(outfpath + '/' + i[:-4] + '_c74752hz.txt')

for file in range(len(inputfilelist)):
    Numofupper = 0
    Numofpunctuation = 0
    Numofnumbers = 0
    Numofwords = 0
    Numofcorrectword = 0
    Numofincorrectword = 0

    with open(args.paths[0],mode='r') as f1:
        englishwordlist = []
        for line in f1:
            line = line.strip('\n')
            englishwordlist.append(line)

    with open(inputfilelist[file],mode='r') as f2:
        text = f2.read().strip('\n')
        text = text.replace('. . .', '.')
        originlist = text.split(' ')
        newlist = []
        for i in originlist:
            i = i.replace('...', '.')
            i = i.replace('…', '.')
            i = i.replace(r'\n', '')

            string = ''
            for j in i:
                if ord(j) >= 65 and ord(j) <= 90:
                    Numofupper += 1
                    string += chr(ord(j) + 32)
                elif ord(j) >= 97 and ord(j) <= 122:
                    string += j
                elif ord(j) >= 48 and ord(j) <= 57:
                    Numofnumbers += 1
                else:
                    if ord(j) == 35 or ord(j) == 64:
                        Numofpunctuation -= 1
                    Numofpunctuation += 1

            if string != '':
                newlist.append(string)

    Numofwords = len(newlist)
    for i in newlist:
        if i in englishwordlist:
            Numofcorrectword += 1
        else:
            Numofincorrectword += 1
    with open(outputfilelist[file],mode = 'w') as f3:
        f3.write('c74752hz\n')

    with open(outputfilelist[file],mode='a') as f3:
        f3.write('Formatting ###################\n')
        f3.write('Number of upper case letters changed: %d\nNumber of punctuations removed: %d\nNumber of numbers removed: %d\n'%(Numofupper,Numofpunctuation,Numofnumbers))
        f3.write('Spellchecking ###################\n')
        f3.write('Number of words: %d\nNumber of correct words: %d\nNumber of incorrect words: %d'%(Numofwords,Numofcorrectword,Numofincorrectword))

# print(Numofupper)
# print(Numofpunctuation)
# print(Numofnumbers)
# print(Numofwords)
# print(Numofcorrectword)
# print(Numofincorrectword)