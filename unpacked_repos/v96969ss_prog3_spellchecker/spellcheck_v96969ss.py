import sys
import os 

inpo=sys.argv[1]
inp=sys.argv[2]
out=sys.argv[3]

for filetest in os.listdir(inp):
    settings=open(inp+'/'+filetest,'r')


    txt=''


    for i in settings.read():
        txt=txt+i



    alphabet='abcdefghijklmnopqrstuvwxyz '
    Alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    correct=''
    p=['.',',','?',':','!',';','[',']','(',')','-',"'",'{','}','"']
    p1=['0','1','2','3','4','5','6','7','8','9']
    c=0
    t=0
    k=0
    L=[]
    correct_words=0
    incorrect_words=0
    settingso=open(inpo)

    for i in txt:
        if i in alphabet:
            correct+=i        
        elif i in Alphabet:
            correct=correct+alphabet[Alphabet.index(i)]
            c+=1
        elif i in p:
            txt.replace(i,'')
            t+=1
        elif i in p1:
            txt.replace(i,'')
            k+=1    
        else:
            correct+=i

            
            
    x=correct.split(' ')
    for i in x:
        if i=='':
            x.remove(i)

    for z in settingso:
        L.append(z.rstrip('\n'))

    for j in x:
        if j in L:
            correct_words+=1
        else:
            incorrect_words+=1
    
    outputfile=out+'/'+filetest[:-4]+'v96969ss.txt'
    outputfile1=open(outputfile,'w')
    

    outputfile1.write('v96969ss'+'\n')
    outputfile1.write('Formatting'+'###################'+'\n')
    outputfile1.write('Number of upper case letters changed:'+ str(c)+'\n')
    outputfile1.write('Number of punctuations removed:'+ str(t)+'\n')
    outputfile1.write('Number of numbers removed:'+ str(k)+'\n')
    outputfile1.write('Spellchecking'+'###################'+'\n')
    outputfile1.write('Number of words:'+ str(len(x))+'\n')
    outputfile1.write('Number of correct words:'+ str(correct_words)+'\n')
    outputfile1.write('Number of incorrect words:'+ str(incorrect_words)+'\n')
        
    settings.close()
    settingso.close()
    outputfile1.close()
