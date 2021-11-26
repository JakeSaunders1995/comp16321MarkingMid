import os
import sys
import string
import re

def listdir_nohidden(path): 
    for f in os.listdir(path): 
        if not f.startswith('.'): 
            yield f   

def main():
    EnglishWords=sys.argv[1]
    inputPath=sys.argv[2]
    outputPath=sys.argv[3]
    filesPath=listdir_nohidden(inputPath)
    ff=open(EnglishWords)
    EnglishWords=ff.readlines()
    words=[]
    for i in EnglishWords:
        words.append(i[0:-1])
    for i in filesPath:
        file_object = open(inputPath+'/'+i)
        line = file_object.readlines()
        x=i[:-4]
        tempString =line[0]
        newstring = ''.join([i for i in tempString if not i.isdigit()])
        a=len(tempString)-len(newstring)
        newstring2 = re.sub('[%s]' % re.escape(string.punctuation), '', newstring)
        b=len(newstring)-len(newstring2)
        newstring3=newstring2.lower()
        d=0
        for j in newstring2:
            if j.isupper():
                d+=1
        word=newstring3.split(" ")
        letters=[]
        for y in range(len(word)):
            if word[y] =='':
                y+=1
                continue
            elif word[y] =='\n':
                y+=1
                continue
            else:
                letters.append(word[y])
                y+=1
        e=0
        for mm in letters:
            for kk in words:
                if mm==kk:
                    e+=1
        c=len(letters)-e
        output_object=open(outputPath+'/'+x+'_g58440zy.txt','w+')
        output_object.write(f"g58440zy\nFormatting ###################\nNumber of upper case letters changed:{d}\nNumber of punctuations removed:{b}\nNumber of numbers removed:{a}\nSpellchecking ###################\nNumber of words:{len(letters)}\nNumber of correct words:{e}\nNumber of incorrect words:{c}")
if __name__ == '__main__':
    main()















