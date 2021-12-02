import re
import argparse
import string
import codecs
import os
if __name__=="__main__":
    f=argparse.ArgumentParser()
    f.add_argument('english')
    f.add_argument('input')
    f.add_argument('output')
    args = f.parse_args()
    e=str(args.english)
    sl=str(args.input)
    outs= str(args.output)
    tfile= os.listdir(sl)
    tfile.sort()
    for path in tfile:
        fname = os.path.join(sl,path)
        tpos = path.find(".txt")
        outputf=path[0:tpos]
        with codecs.open(fname, 'r', encoding='utf-8',errors='ignore') as infile :
            s=str(infile.read())
            i=0
            j=0
            c1=0
            c2=0
            c3=0
            c=0
            nw=0
            cw=0
            tc=0
            n = r'[0-9]'
            p = r"[!.$%&()*+,-/:;<=>?[\]^_`{|}~]"
            pun = "!.$%&()*+,-/:;<=>?[\]^_`{|}~"
            while i < len(s):
                if s[i].isdigit()== True :
                    c1=c1+1
                while j < len(pun):
                    if s[i] == pun[j]:
                        c2=c2+1
                    j=j+1
                j=0
                if s[i].isupper() == True:
                    c3=c3+1
                i=i+1
            s=re.sub(n,'',s)
            s=re.sub(p,'',s)
            s=s.lower()
            slist=s.split()
            f=open(e,'r')
            fi=f.read()
            dic=fi.split()
            for a in slist :
                nw=nw+1
                if a not in dic:
                    tc=tc+1
                if a in dic:
                    cw=cw+1
            with open(os.path.join(outs,f'{outputf}_t50885aa.txt'),"w") as w:
                w.write("t50885aa")
                w.write("\nFormatting ###################")
                w.write("\nNumber of upper case letters changed: "+str(c3))
                w.write("\nNumber of punctuations removed: "+str(c2))
                w.write("\nNumber of numbers removed: "+str(c1))
                w.write("\nSpellchecking ###################")
                w.write("\nNumber of words: "+str(nw))
                w.write("\nNumber of correct words: "+str(cw))
                w.write("\nNumber of incorrect words: "+str(tc))
