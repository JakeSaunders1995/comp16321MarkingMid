import sys
import os
file = open(rf"{sys.argv[1]}","r")
englishwords = []
for line in file:
    line = line.rstrip()
    englishwords.append(line)
inpath = rf"{sys.argv[2]}"
outpath = rf"{sys.argv[3]}"
for file in os.listdir(inpath):
    if ".txt" in file:
        f = open(rf"{str(inpath)}/{file}","r")
        text = ""
        for line in f:
            line = line.rstrip()
            text += " "+line
        if text[0] == " ":
            text = text[1:]
        uppercount = 0
        punctuationcount = 0
        numbercount = 0
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "@#abcdefghijklmnopqrstuvwxyz "
        num = "1234567890"
        punc = '.?—,:();!-[]}{"'+"'"
        text1 = ""
        for i in range(len(text)):
            if text[i] in upper:
                uppercount += 1
        text = text.lower()
        pos = 0
        while pos != len(text):
            if text[pos] in lower:
                text1 += text[pos]
                pos += 1
            elif text[pos] in num:
                numbercount += 1
                pos += 1
            elif text[pos] in punc:
                if text[pos:pos+3] == "...":
                    punctuationcount += 1
                    pos += 3
                    print("t")
                else:
                    punctuationcount += 1
                    pos += 1
        position = 0
        textlist = []
        for i in range(len(text1)):
            if text1[i] == " ":
                textlist.append(text1[position:i])
                position = i+1
            elif i == len(text1)-1:
                textlist.append(text1[position:i+1])
        position = 0
        while position < len(textlist):
            if textlist[position] == '':
                textlist.remove(textlist[position])
            else:
                position += 1
        total = len(textlist)
        correct = 0
        incorrect = 0
        for i in range(len(textlist)):
            if textlist[i] in englishwords:
                correct += 1
            else:
                incorrect += 1
        g = open(rf"{str(outpath)}/{file[:-4]}_y36340hc.txt","w")
        g.write(f"y36340hc\nFormatting ###################\nNumber of upper case letters changed: {uppercount}\nNumber of punctuations removed: {punctuationcount}\nNumber of numbers removed: {numbercount}\nSpellchecking ###################\nNumber of words: {total}\nNumber of correct words: {correct}\nNumber of incorrect words: {incorrect}")
