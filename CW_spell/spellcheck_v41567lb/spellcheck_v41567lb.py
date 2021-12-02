import argparse
import os
parser=argparse.ArgumentParser()
parser.add_argument("wordpath",type=str)
parser.add_argument("inp", type=str)
parser.add_argument("out", type=str)
args=parser.parse_args()


wordfile=getattr(args, "wordpath")
dir1=getattr(args, "inp")
dir2=getattr(args, "out")

for infile in os.listdir(dir1):
    file=open(dir1+"/"+infile, "r")
    text=file.read()
    file.close()
    numcount=0
    punccount=0
    uppercount=0
    formattext=""
    num=["1","2","3","4","5","6","7","8","9","0"]
    punc=[",",".","!","?",":",";","[","]","(",")","{","}","@","#",'"',"'","-"]
    text=list(text)
    for i in range (0, len(text)):
        if ord(text[i])>=65 and ord(text[i])<=90:
            uppercount+=1
        if text[i] in num:
            numcount+=1
            continue
        elif text[i] in punc:
            punccount+=1
            continue
        else:
            formattext=formattext+str(text[i])
    formattext=formattext.lower()
    formattext=formattext.split()
    file3=open(wordfile, "r")
    words=file3.read()
    file3.close()
    words=words.split()
    wordnum=len(formattext)
    correctword=0
    wrongword=0
    for i in range (0, len(formattext)):
        if formattext[i] in words:
            correctword+=1
        else:
            wrongword+=1
    outname=infile.replace(".txt","_v41567lb.txt")
    outfile=open(dir2+"/"+outname, "w")
    outputstr=str("v41567lb\nFormatting ###################\nNumber of upper case words changed: "+str(uppercount)+"\nNumber of punctuations removed: "+str(punccount)+"\nNumber of numbers removed: "+str(numcount)+"\nSpellchecking ###################\nNumber of words: "+str(wordnum)+"\nNumber of correct words: "+str(correctword)+"\nNumber of incorrect words: "+str(wrongword))
    outfile.write(outputstr)
    outfile.close()
