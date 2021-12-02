import sys
import os

inp=sys.argv[1]
out=sys.argv[2]

for filetest in os.listdir(inp):
    settings=open(inp+'/'+filetest,'r')


    x='abcdefghijklmnopqrstuvwxyz'
    y='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    morse={".-" : "a", "-..." : "b", "-.-." : "c", "-.." : "d", "." : "e", "..-." : "f", "--." : "g", "...." : "h", ".." : "i", ".---" : "j", "-.-" : "k", ".-.." : "l", 
        "--" : "m", "-." : "n", "---" : "o", ".--." : "p", "--.-" : "q", ".-." : "r", "..." : "s", "-" : "t", "..-" : "u", "...-" : "v", ".--" : "w", "-..-" : "x", 
        "-.--" : "y", "--.." : "z", ".----" : "1", "..---" : "2", "...--" : "3", "....-" : "4", "....." : "5", "-...." : "6", "--..." : "7", "---.." : "8", 
        "----." : "9", "-----" : "0", ".-.-.-" : ".", "..--.." : "?", "-.-.--" : "!", "--..--" : ",", "---..." : ":", "-.-.-." : ";", "-....-" : "-", "-.--." : "(", "-.--.-" : ")", 
        ".----." : "'", ".-..-." : "''", "/" : " "}


    s=''

    for i in settings.read():
        s=s+i   


    txt=''


      
    # HEXADECIMAL     
    if s[0:3]=='Hex':
        hexstring = s[4:]
        txt = bytes.fromhex(hexstring)
        txt = txt. decode("ascii")


    # CAESAR + 3
    if s[0:3]=='Cae':
        caestring=s[18:]
        for j in caestring:
            if j in x:
                txt=txt+(x[x.index(j)-3])
            else:
                txt=txt+j       

    # Morse code
    if s[0:3]=='Mor':
        morstring=s[11:]
        p=morstring.split(' ')
        for i in p:
            txt+=morse[i]

    settings.close()
    

    outputfile=out+'/'+filetest[:-4]+'v96969ss.txt'
    outputfile1=open(outputfile,'w')
    outputfile1.write(txt)

    outputfile1.close()        
            
