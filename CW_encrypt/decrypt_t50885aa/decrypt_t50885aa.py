import argparse
import string
import sys
import codecs
import os
def encryption(s):
    i=0
    if s[0] == 'H' or s[0]=='h' :
        while i < len(s) :
            if s[i] == ':' :
                new_s=s[i+1:]
            i=i+1
        encrypted = bytes.fromhex(new_s).decode('utf-8')
    if s[0] == 'C' or s[0]=='c' :
        while i < len(s) :
            if s[i] == ':' :
                new_s = s[i+1:]
            i=i+1
        encrypted=""
        x=0
        while x<len(new_s):
            if new_s[x]==" " or new_s[x] == "." :
                x=x+1
                encrypted = encrypted + " "
                continue
            new_s_ch=new_s[x]
            asv= ord(new_s_ch)
            asv=asv-3
            if new_s_ch == 'a' or new_s_ch == 'b' or new_s_ch == 'c' :
                asv=asv+26
            cv=chr(asv)
            encrypted=encrypted+ cv
            x=x+1
    if s[0] == 'M' or s[0]== 'm' :
        while i < len(s) :
            if s[i] == ':' :
                break
            i=i+1
        new_s = s[i+1:]
        Morse={'.-':'A', '-...':'B','-.-.':'C', '-..':'D', '.':'E','..-.':'F', '--.':'G','....':'H','..':'I', '.---':'J','-.-':'K','.-..':'L','--':'M', '-.':'N','---':'O', '.--.':'P', '--.-':'Q','.-.':'R', '...':'S', '-':'T','..-':'U', '...-':'V', '.--':'W','-..-':'X', '-.--':'Y', '--..':'Z','.----':'1', '..---':'2', '...--':'3','....-':'4', '.....':'5', '-....':'6','--...':'7', '---..':'8', '----.':'9','-----':'0'}
        me=""
        encrypted=""
        new_s=new_s +" "
        for a in new_s :
            if (a != " "):
                if(a!="/") :
                  me=me+a
                  continue
            if a == "/" :
                space=" "
                encrypted=encrypted+space
                me=""
                continue
            if me!="":
                wordchanged=Morse[me]
                encrypted=encrypted+wordchanged
                me=""
                continue
    return (encrypted)
if __name__=="__main__":
    f=argparse.ArgumentParser()
    f.add_argument('input')
    f.add_argument('output')
    args = f.parse_args()
    s=str(args.input)
    outs=str(args.output)
    tfile=os.listdir(s)
    tfile.sort()
    for path in tfile:
        fname= os.path.join(s,path)
        tpos=path.find(".txt")
        outputf=path[0:tpos]
        with codecs.open(fname, 'r', encoding='utf-8',errors='ignore') as infile:
          s_in=str(infile.read())
          output=encryption(s_in)
          with open(os.path.join(outs,f'{outputf}_t50885aa.txt'),"w") as w:
               print(outs)
               w.write(output)
