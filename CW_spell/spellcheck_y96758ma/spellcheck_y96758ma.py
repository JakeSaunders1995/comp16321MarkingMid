import os
import sys
import re

filename = sys.argv[-3]
folder=sys.argv[-2]
folderlist = os.listdir(folder)
folderlist.sort()
folder2=sys.argv[-1]
folderlist2 = os.listdir(folder2)
english = open(filename, 'r')
englishh=english.read()
englishh=englishh.splitlines()
for folders in folderlist:
    i_file = open(os.path.join(folder, folders))
    lineshh = str(i_file.read()).strip()
    lineshh = lineshh.splitlines()
    lineshh+=" "
    folderstring=folders.replace(".txt","_y96758ma.txt")
    print()
    newstring=""
    punctuation, number, char, words, yes, no, newline, x, upper=0, 0, 0, 0, 0, 0, 0, 0, 0
    list=[]
    word=""
    oldcharacter=""
    for lin in lineshh:
        count=0
        for character in lin:
            if newline>0:
                newstring+=" "
                words+=1
                list+=[word]
                word=""
                newline=0
                x=1
            if character.isupper():
                upper+=1
            if character.isalpha():
                newstring+=character.lower()
                word+=character.lower()
            elif character.isnumeric():
                number+=1
            elif character == " " and x!=1:
                newstring+=" "
                list+=[word]
                word=""
            else:
                punctuation+=1
        newline+=1
        count+=1
    newstring = re.sub('\s{2,}',' ', newstring)
    print(newstring)
    lineshhh = newstring.split()
    words = len(lineshhh)
    for l in list:
        if l in englishh:
            yes+=1
    no = words - yes
    o_file = open(os.path.join(folder2, folderstring), 'w')
    o_file.writelines(("y96758ma\n") +("Formatting ###################\n") +("Number of upper case words changed: " +str(upper) +"\n") +("Number of punctuations removed: " + str(punctuation-(count))+"\n") +("Number of numbers removed: " + str(number)+"\n") +("Spellchecking ###################\n") +("Number of words: " + str(words)+"\n") +("Number of correct words: " + str(yes)+"\n") +("Number of incorrect words: " + str(no)))
