import sys, os
f=sys.argv[1]
a=sys.argv[2]
b=os.listdir(a)
word=""
number="1234567890"
punctuations=".?!,:;-–—()[]{}''""..."
for c in b:
    x=0
    y=0
    uppercase=0
    numberremove=0
    punctuation=0
    wrongwords=0
    numberofwords=0
    i=0
    d=a+"/"+c
    dictionary=open(f,'r')
    dictionary1=dictionary.readlines()
    while i <len(dictionary1):
        dictionary1[i]=dictionary1[i].replace("\n",'')
        i+=1
    with open(d, 'r') as files:
        files=files.read()
        while x<len(files):
            if ord(files[x]) in range(65,91):
                uppercase+=1
                x+=1
            elif ord(files[x]) in range(33,35):
                punctuation+=1
                x+=1
            elif ord(files[x]) in range(39,42):
                punctuation+=1
                x+=1
            elif ord(files[x]) in range(44,47):
                punctuation+=1
                x+=1
            elif ord(files[x]) in range(58,60):
                punctuation+=1
                x+=1
            elif ord(files[x]) == 63:
                punctuation+=1
                x+=1
            elif ord(files[x]) == 91:
                punctuation+=1
                x+=1
            elif ord(files[x]) == 93:
                punctuation+=1
                x+=1
            elif ord(files[x]) == 123:
                punctuation+=1
                x+=1
            elif ord(files[x]) in range(125,127):
                punctuation+=1
                x+=1
            elif ord(files[x]) in range(48,58):
                numberremove+=1
                x+=1
            else:
                x+=1
        files=files.lower()
        x=0
        while x<len(files):
            if files[x] in punctuations:
                files=files.replace(files[x],'')
                x=0
            elif files[x] in number:
                files=files.replace(files[x],'')
                x=0
            else:
                x+=1
        while y<len(files):
            if files[y]==" ":
                if word in " ":
                    word=""
                    y+=1
                elif word in chr(10):
                    word=""
                    y+=1
                else:
                    if word not in dictionary1:
                        numberofwords+=1
                        wrongwords+=1
                        word=""
                        y+=1
                    else:
                        numberofwords+=1
                        word=""
                        y+=1
            else:
                word+=files[y]
                y+=1
        if word in " ":
            word=""
        else:
            if word not in dictionary1:
                numberofwords+=1
                wrongwords+=1
                word=""
            else:
                numberofwords+=1
                word=""
    out="n37169dk\nFormatting ################### \nNumber of upper case letters changed: "+str(uppercase)+"\nNumber of punctuations removed: "+str(punctuation)+"\nNumber of numbers removed: "+str(numberremove)+"\nSpellchecking ################### \nNumber of words: "+str(numberofwords)+"\nNumber of correct words: "+str(numberofwords-wrongwords)+"\nNumber of incorrect words: "+str(wrongwords)
    e=c.replace('.txt','')
    w=sys.argv[3]+'/'+e+"_n37169dk"+".txt"
    x=open(w,'w')
    x.write(out)
