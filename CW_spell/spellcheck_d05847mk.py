import os
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("eng")
parser.add_argument("inp")
parser.add_argument("otp")
args=parser.parse_args()
engwords=args.eng
inputpath=args.inp
outputpath=args.otp
punctuations=[".","?","!",",",":",";","_","-","[","]","{","}","(",")","'","…",'"']
numbers="1234567890"

def getengwords():
    words=""
    file=open(engwords,"r")
    for line in file:
        words+=line
    words=words.split()
    return words

words=getengwords()

def spellchecker():
    up=pn=num=wc=cwc=iwc=0
    f=open(inpfile,"r")
    txt=f.read()
    for i in txt:
        if i.isupper():
            j=i.lower()
            txt=txt.replace(i,j)
            up+=1
        elif i in punctuations:
            txt=txt.replace(i,"")
            pn+=1
        elif i in numbers:
            txt=txt.replace(i,"")
            num+=1
    lst=txt.split()
    for a in lst:
        wc+=1
        if a in words:
            cwc+=1
        else:
            iwc+=1
    return up, pn, num, wc, cwc, iwc

def output():
    opfilename=inpfile.replace(".txt","")+"_d05847mk.txt"
    up, pn, num, wc, cwc, iwc=spellchecker()
    opcon="username"
    opcon2="formatting"
    os.chdir(outputpath)
    with open(opfilename,"w") as f:
        f.write("d05847mk")
        f.write("\n")
        f.write("Formatting ###################")
        f.write("\n")
        f.write("Number of upper case letters changed: "+str(up))
        f.write("\n")
        f.write("Number of punctuations removed: "+str(pn))
        f.write("\n")
        f.write("Number of numbers removed: "+str(num))
        f.write("\n")
        f.write("Spellchecking ###################")
        f.write("\n")
        f.write("Number of words: "+str(wc))
        f.write("\n")
        f.write("Number of correct words: "+str(cwc))
        f.write("\n")
        f.write("Number of incorrect words: "+str(iwc))
    os.chdir(inputpath)


os.chdir(inputpath)
arr=os.listdir()
for inpfile in arr:
    if inpfile.endswith(".txt"):
        output()
