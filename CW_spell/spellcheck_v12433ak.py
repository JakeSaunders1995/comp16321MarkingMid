import os
import sys
import os.path
fn= sys.argv[2]
fo=sys.argv[3]
word1=sys.argv[1]
for filename in os.listdir(fn):
    if filename.endswith(".txt"):
        f1=os.path.join(fn,filename)
        file=open(f1,'rt')
        f4=filename.index('.txt')
        f4=filename[0:f4]
        file1 =open(fo+"/"+f4+"_v12433ak.txt","w")
    s = file.read()
    s=s+" "
    num = "0123456789"
    punc = '''!()-[]{};:~"\,<>./?@#$%^&*_~'''
    c1=c2=c3=c4=c5=c6=k=0
    s1=""
    w=""
    ss=""
    file1.write("v12433ak\n")
    file1.write("Formatting ###################"+"\n")
    for i in range(len(s)-3):
        if(s[i]=='.' and s[i+1]=='.' and s[i+2]=='.'):
            i=i+2
            continue
        else:
            ss=ss+s[i]
    for ch in ss:
        if(ord(ch)>=65 and ord(ch)<=90):
            c1=c1+1
            ch=ch.lower()
            s1=s1+str(ch)
        elif(ch in punc):
            s1=s1+""
            c2=c2+1
        elif(ch in num):
            s1=s1+""
            c3=c3+1
        else:
            s1=s1+ch
    s2=""
    for i in range(len(s1)-1):
        if(s1[i]==" " and s1[i+1]==" "):
            continue
        else:
            s2=s2+s1[i]
    s2=s2+" "
    file1.write("Number of upper case letters changed: " +str(c1)+"\n")
    file1.write("Number of punctuation's removed " +str(c2)+"\n")
    file1.write("Number of numbers removed: "+ str(c3)+"\n")
    file1.write("Spellchecking ###################"+"\n")
    w=""
    for i in s2:
        if(i!=" "):
            w=w+i
        else:
            c4=c4+1
            words=open(word1,"r")
            lines=words.read()
            if w in lines:
                c5=c5+1
            else:
                c6=c6+1
            w=""
    file1.write("Number of words: "+str(c4)+"\n")
    file1.write("Number of correct words: "+str(c5)+"\n")
    file1.write("Number of incorrect word: "+str(c6)+"\n")



