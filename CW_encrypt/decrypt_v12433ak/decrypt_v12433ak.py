import sys
import os
import os.path
fn= sys.argv[1]
fo=sys.argv[2]
j=1
for filename in os.listdir(fn):
    if filename.endswith(".txt"):
        f1=os.path.join(fn,filename)
        file=open(f1,'rt')
        f4=filename.index('.txt')
        f4=filename[0:f4]
        file1 =open(fo+"/"+f4+"_v12433ak.txt","w")
        j=j+1
        s = file.read()
        l=len(s)
        l=l+1
        c =  s[0]
        s2=""
        if(c=="H"):
            s1=s[4:l]
            for i in range(len(s1)):
                if(s1[i]==" "):
                    continue
                else:
                    d=bytes.fromhex(s1)
                    d=d.decode("ascii")
            s2=s2+d  

        if(c=="M"):
            Morse_dict={'a':'.-','b':'-...',
                        'c':'-.-.', 'd':'-..', 'e':'.',
                        'f':'..-.', 'g':'--.', 'h':'....',
                        'i':'..', 'j':'.---', 'k':'-.-',
                        'l':'.-..', 'm':'--', 'n':'-.',
                        'o':'---', 'p':'.--.', 'q':'--.-',
                        'r':'.-.', 's':'...', 't':'-',
                        'u':'..-', 'v':'...-', 'w':'.--',
                        'x':'-..-', 'y':'-.--', 'z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ', ':'--..--', '.':'.-.-.-',
                        '?':'..--..', '/':'-..-.', '-':'-....-',
                        '(':'-.--.', ')':'-.--.-'}     
            s1=s[11:l]
            s1=s1+' '
            d=""
            c1=""
            s2=""
            for i in range(len(s1)):
                if(s1[i]=="/"):
                    continue
                else:
                    s2=s2+s1[i]

            for i in s2:
                if(i!=" " and i!="/"):
                    j=0;
                    c1+=i
                else:
                    j+=1
                    if(j==2):
                        d+=" "
                    else:
                        d+=list(Morse_dict.keys())[list(Morse_dict.values()).index(c1)]
                        c1=""
            s2=d

        if (c=="C"):
                s1=s[18:l]   
                s1=s1+" "
                w=""
                w1=""
                for i in range(len(s1)):
                    if(s1[i]!=" "):
                        w=w+s1[i]
                    else:
                        for j in range(len(w)):
                            d=(ord(w[j]))-3
                            if(d<97):
                                d=(d-3+96)%97+26
                            w1=w1+chr(d)
                        w=""
                        s2=s2+w1+" "
                        w1="" 

        file1.write(s2)
