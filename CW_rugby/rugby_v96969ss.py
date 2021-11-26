import sys
import os

inp=sys.argv[1]
out=sys.argv[2]

for filetest in os.listdir(inp):
    settings=open(inp+'/'+filetest,'r')

#Scoring types and quantity
    t=5
    c=2
    p=3
    d=3

    # s contains the content of the text and s is a str
    s=''
    c=0 

    # initial score of the teams one and two
    one=0
    two=0
      

    # s contains the text file 
    for i in(settings.read()):
        s=s+i
      
    for i in range (len(s)):
        c+=1
        if s[i]=='t':
            if s[c-2]=='1':
                one=one+t
            else:
                two=two+t
            
        if s[i]=='c':
            if s[c-2]=='1':
                one=one+c
            else:
                two=two+c
                
        if s[i]=='p':
            if s[c-2]=='1':
                one=one+p
            else:
                two=two+p
                
        if s[i]=='d':
            if s[c-2]=='1':
                one=one+d
            else:
                two=two+d
            
    settings.close()

    outputfile=out+'/'+filetest[:-4]+'v96969ss.txt'
    outputfile1=open(outputfile,'w')
    outputfile1.write(str(one)+':'+str(two))

    outputfile1.close()
